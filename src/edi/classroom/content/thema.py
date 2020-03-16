# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from edi.classroom import _

class IThema(model.Schema):
    """ Marker interface and Dexterity Python Schema for Thema
    """

    banner = NamedBlobImage(title=u"Titelbild des Themas", required=False)
    text = RichText(title=u"Beschreibung des Themas", required=False)


@implementer(IThema)
class Thema(Container):
    """
    """
