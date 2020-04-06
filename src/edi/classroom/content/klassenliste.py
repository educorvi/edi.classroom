# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from edi.classroom import _

def chatpin_constraint(value):
    """Prueft die PIN-Laenge auf 4 Zeichen
    """
    if not len(value) == 4:
        raise Invalid(u"Die Schüler-PIN muss 4 Zeichen lang sein.")
    if u' ' in value:
        raise Invalid(u"Die Schüler-PIN darf keine Leerzeichen enthalten.")
    return True


class ITrainee(model.Schema):
    name = schema.TextLine(title=u"Schülername",
                              required=True)

    pin = schema.TextLine(title=u"Schüler-PIN",
                              constraint = chatpin_constraint,
                              required=True)

class IKlassenliste(model.Schema):
    """ Marker interface and Dexterity Python Schema for Klassenliste
    """

    directives.widget(traineelist = DataGridFieldFactory)
    traineelist = schema.List(title=u"Ihre Klassenliste. Bitte vergeben Sie jedem Schüler einen Namen oder Nickname und einen PIN für den Zutritt\
                            zum Chatroom",
                            required=True,
                            value_type=DictRow(title=u"Schüler/Schülerin", schema=ITrainee))

@implementer(IKlassenliste)
class Klassenliste(Item):
    """
    """
