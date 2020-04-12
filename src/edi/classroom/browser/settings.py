# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope import schema
from Products.CMFCore.interfaces import ISiteRoot
from Products.Five.browser import BrowserView
from zope.interface import Invalid
from zope.interface import invariant
from plone.z3cform import layout
from plone.supermodel import model
from z3c.form import form
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

class ISettings(model.Schema):
    """ 
    """
    adminuser = schema.TextLine(title=u"Admin-Benutzer der Couch-DB",
                                description=u"Die Couch-DB wird für den Chatroom benötigt. Die Angabe ist optional.")
    adminpassword = schema.Password(title=u"Admin-Passwort der Couch-DB")
    adminpassword2 = schema.Password(title=u"Wiederholung des Admin-Passworts")

    @invariant
    def password_invariant(data):
        if data.adminpassword != data.adminpassword2:
            raise Invalid(u'Die eingegebenen Passwörter sind nicht gleich!')

class SettingsEditForm(RegistryEditForm):

    form.extends(RegistryEditForm)
    schema = ISettings


EdiClassroomPanelView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
EdiClassroomPanelView.label = u"Einstellungen virtueller Klassenraum"
