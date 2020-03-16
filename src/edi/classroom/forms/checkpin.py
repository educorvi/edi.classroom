# -*- coding: utf-8 -*-
from zope import schema
from z3c.form import button, form, field
from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm

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
        import pdb;pdb.set_trace()
        # do something

    @button.buttonAndHandler(u'Abbrechen')
    def handleCancel(self, action):
        data, errors = self.extractData()
        import pdb;pdb.set_trace()
        # do something
