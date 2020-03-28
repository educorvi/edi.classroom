# -*- coding: utf-8 -*-
from zope import schema
from z3c.form import button, form, field
from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from collective.beaker.interfaces import ISession
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile as FiveViewPageTemplateFile
from plone import api as ploneapi
from edi.classroom.forms.mailconfig import create_edibody
from edi.classroom.forms.receipt import create_userbody
import z3c.form
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import plone.app.z3cform
import plone.z3cform.templates


from edi.classroom import _

class IAddr(model.Schema):

    email = schema.TextLine(title=u"Ihre E-Mail-Adresse", required=True)
    name = schema.TextLine(title=u"Ihr Name", required=True)

    strhnr = schema.TextLine(title=u"Strasse und Hausnummer", required=True)
   
    plz = schema.TextLine(title=u"Postleitzahl", required=True)
    ort = schema.TextLine(title=u"Ort", required=True)


class SendOrder(AutoExtensibleForm, form.Form):

    label = u"Ihre Bestellung"
    description = u""
    ignoreContext = True
 
    schema = IAddr

    def updateWidgets(self):
        super(SendOrder, self).updateWidgets()
        if not ploneapi.user.is_anonymous():
            user = ploneapi.user.get_current()
            self.widgets["email"].value = user.getProperty('email')
            self.widgets["name"].value = user.getProperty('fullname')
            self.widgets["email"].mode = z3c.form.interfaces.DISPLAY_MODE
            self.widgets["name"].mode = z3c.form.interfaces.DISPLAY_MODE


    @button.buttonAndHandler(u'Bestellen')
    def handleApply(self, action):
        data, errors = self.extractData()
        if ploneapi.user.is_anonymous():
            url = ploneapi.portal.get().absolute_url()
            membermessage = u"Eine Bestellung ist nur als registrierter und angemeldeter Benutzer möglich."
            ploneapi.portal.show_message(message=membermessage, request=self.request, type='error') 
            return self.request.response.redirect(url)
        if errors:
            self.status = u"Bitte korrigieren Sie die angezeigten Fehler."

        user = ploneapi.user.get_current()
        data['email'] = user.getProperty('email')
        data['name'] = user.getProperty('fullname')

        edi_body = create_edibody(data)

        ploneapi.portal.send_email(
            recipient=u"info@educorvi.de",
            sender="educorvi@web.de",
            subject="Bestellung eines Handy-Stativs",
            body=edi_body,
            )

        mime_msg = MIMEMultipart('related')
        mime_msg['Subject'] = u"Ihre Bestellung eines Handy-Stativs auf kraeks.de"
        mime_msg['From'] = u"educorvi@web.de"
        mime_msg['To'] = data.get('email')
        mime_msg.preamble = 'This is a multi-part message in MIME format.'
        msgAlternative = MIMEMultipart('alternative')
        mime_msg.attach(msgAlternative)

        htmltext = create_userbody(data)
        msg_txt = MIMEText(htmltext, _subtype='html', _charset='utf-8')
        msgAlternative.attach(msg_txt)
        mail_host = ploneapi.portal.get_tool(name='MailHost')
        mail_host.send(mime_msg.as_string())

        self.output = dict(country="foobar")
        self.status = _(u"Report complete")

        thankmessage = u"Vielen Dank für Ihre Bestellung. Diese ist bei uns eingegangen. Sie erhalten in wenigen Minuten eine\
                         Bestellbestätigung per E-Mail."

        message = ploneapi.portal.show_message(message=thankmessage, request=self.request, type='info')
        url = self.context.absolute_url()
        return self.request.response.redirect(url)


    @button.buttonAndHandler(u'Abbrechen')
    def handleCancel(self, action):
        data, errors = self.extractData()
        url = self.context.absolute_url()
        return self.request.response.redirect(url)
        
        # do something

order_form_frame = plone.z3cform.layout.wrap_form(SendOrder, index=FiveViewPageTemplateFile("order.pt"))    
