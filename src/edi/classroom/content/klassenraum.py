# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.namedfile.field import NamedBlobImage
from zope import schema
from zope.interface import implementer


from edi.classroom import _

class IKlassenraum(model.Schema):
    """ Marker interface and Dexterity Python Schema for Klassenraum
    """

    pin = schema.TextLine(title=u"Zugangscode",
                          description=u"Geben Sie hier einen 6-stelligen Zugangscode ein, den die Schüler eingeben\
                                        müssen um den virtuellen Klassenraum zu betreten."

    banner = NamedBlobImage(title=u"Titelbild des Klassenraums", required=False)
    text = RichText(title=u"Beschreibung des Klassenraums", required=False)                                     


@implementer(IKlassenraum)
class Klassenraum(Container):
    """
    """

    def compare_pin(self, checkpin):
        if self.pin == checkpin:
            return True
        return False
