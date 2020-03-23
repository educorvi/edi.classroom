# -*- coding: utf-8 -*-
from zope import schema
from z3c.form import button, form, field
from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from collective.beaker.interfaces import ISession
from plone import api as ploneapi

from edi.classroom import _

class ICheckPin(model.Schema):

    checkpin = schema.TextLine(title=u"Gib einen Pin ein, um den virtuellen Klassenraum zu betreten.",
                               required=True)

class CheckPinForm(AutoExtensibleForm, form.Form):

    label = u"Eintritt in den virtuellen Klassenraum"
    description = u""
    ignoreContext = True
 
    schema = ICheckPin

    @button.buttonAndHandler(u'Eintreten')
    def handleApply(self, action):
        data, errors = self.extractData()
        if not errors:
            if data.get('checkpin') != self.context.pin:
                errormsg = u"Der eingegebene PIN ist leider nicht gültig"
                ploneapi.portal.show_message(message=errormsg, request=self.request, type='error')
                url = self.context.absolute_url() + '/check-pin'
                return self.request.response.redirect(url)
            else:
                session = ISession(self.request)
                uid = self.context.UID()
                session[uid] = data.get('checkpin')
                session.save()
                url = self.context.absolute_url()
                return self.request.response.redirect(url)


    #@button.buttonAndHandler(u'Abbrechen')
    #def handleCancel(self, action):
    #    data, errors = self.extractData()
    #    import pdb;pdb.set_trace()
    #    # do something
