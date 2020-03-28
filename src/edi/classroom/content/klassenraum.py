# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.namedfile.field import NamedBlobImage
from zope import schema
from zope.interface import implementer
from collective.beaker.interfaces import ISession
from zope.interface import Invalid

from edi.classroom import _


def pin_constraint(value):
    """Prueft die PIN-Laenge auf 6 Zeichen
    """
    if not len(value) == 6:
        raise Invalid(u"Die PIN muss 6 Zeichen lang sein.")
    if u' ' in value:
        raise Invalid(u"Die PIN darf keine Leerzeichen enthalten.") 
    return True


class IKlassenraum(model.Schema):
    """ Marker interface and Dexterity Python Schema for Klassenraum
    """

    pin = schema.TextLine(title=u"Zugang zum virtuellen Klassenraum",
                          constraint=pin_constraint,
                          description=u"Tragen Sie hier einen 6-stelligen alphanumerischen Zugangscode (PIN) ein, den die Schüler\
                                        eingeben müssen um den virtuellen Klassenraum zu betreten.")

    classimage = NamedBlobImage(title=u"Titelbild des Klassenraums", required=False)
    text = RichText(title=u"Beschreibung des Klassenraums", required=False)                                     


@implementer(IKlassenraum)
class Klassenraum(Container):
    """
    """

    def compare_pin(self, checkpin):
        if self.pin == checkpin:
            return True
        return False

    def checkpin(self, request):
        check = False
        uid = self.UID()
        session = ISession(request)
        if uid in session:
            checkpin = session[uid]
            check = self.compare_pin(checkpin)
        return check

    def get_backurl(self):
        return self.absolute_url()

    def get_homelink(self):
        return self.absolute_url()
