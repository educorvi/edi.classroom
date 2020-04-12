# -*- coding: utf-8 -*-
from zope import schema
from z3c.form import button, form, field
from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from collective.beaker.interfaces import ISession
from plone import api as ploneapi

from edi.classroom import _

class IChatPin(model.Schema):

    chatpin = schema.TextLine(title=u"Gib Deinen persönlichen Pin ein, um im Chatroom zu sagen wer Du bist.",
                               required=True)

class ChatPinForm(AutoExtensibleForm, form.Form):

    label = u"Anmeldung im Chatroom"
    description = u""
    ignoreContext = True
 
    schema = IChatPin

    @button.buttonAndHandler(u'Anmelden')
    def handleApply(self, action):
        data, errors = self.extractData()
        if not errors:
            checkmember = self.context.chatmember(data.get('chatpin'))
            if not checkmember:
                errormsg = u"Der eingegebene PIN ist leider nicht gültig"
                ploneapi.portal.show_message(message=errormsg, request=self.request, type='error')
                url = self.context.absolute_url() + '/chat-pin'
                return self.request.response.redirect(url)
            else:
                session = ISession(self.request)
                uid = self.context.UID()
                chatid = "chat_%s" %uid
                session[chatid] = checkmember
                session.save()
                url = self.context.absolute_url() + '/@@chatroom/'
                return self.request.response.redirect(url)

    @button.buttonAndHandler(u'Abbrechen')
    def handleCancel(self, action):
        url = self.context.absolute_url()
        return self.request.response.redirect(url)
