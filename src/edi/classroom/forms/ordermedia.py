# -*- coding: utf-8 -*-
from zope import schema
from z3c.form import button, form, field
from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from collective.beaker.interfaces import ISession
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile as FiveViewPageTemplateFile
from plone import api as ploneapi
from edi.classroom.forms.mailconfig import create_edibody, create_userbody
import z3c.form

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
        user_body = create_userbody(data)

        ploneapi.portal.send_email(
            recipient=u"info@educorvi.de",
            sender="educorvi@web.de",
            subject="Bestellung eines Handy-Stativs",
            body=edi_body,
            )

        ploneapi.portal.send_email(
            recipient=data.get('email'),
            sender="educorvi@web.de",
            subject="Ihre Bestellung eines Handy-Stativs auf kraeks.de",
            body=user_body,
            )

        self.output = dict(country="foobar")
        self.status = _(u"Report complete")

            #if data.get('checkpin') != self.context.pin:
            #    errormsg = u"Der eingegebene PIN ist leider nicht gültig"
            #    ploneapi.portal.show_message(message=errormsg, request=self.request, type='error')
            #    url = self.context.absolute_url() + '/check-pin'
            #    return self.request.response.redirect(url)
            #else:
            #    session = ISession(self.request)
            #    uid = self.context.UID()
            #    session[uid] = data.get('checkpin')
            #    session.save()
            #    url = self.context.absolute_url()
            #    return self.request.response.redirect(url)


    #@button.buttonAndHandler(u'Abbrechen')
    #def handleCancel(self, action):
    #    data, errors = self.extractData()
    #    import pdb;pdb.set_trace()
    #    # do something

order_form_frame = plone.z3cform.layout.wrap_form(SendOrder, index=FiveViewPageTemplateFile("order.pt"))    
