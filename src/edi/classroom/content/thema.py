# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from collective.beaker.interfaces import ISession

from edi.classroom import _

class IThema(model.Schema):
    """ Marker interface and Dexterity Python Schema for Thema
    """

    image = NamedBlobImage(title=u"Titelbild des Themas", required=False)
    text = RichText(title=u"Beschreibung des Themas", required=False)


@implementer(IThema)
class Thema(Container):
    """
    """

    def compare_pin(self, checkpin):
        if self.aq_parent.pin == checkpin:
            return True
        return False

    def checkpin(self, request):
        check = False
        uid = self.aq_parent.UID()
        session = ISession(request)
        if uid in session:
            checkpin = session[uid]
            check = self.compare_pin(checkpin)
        return check

    def get_backurl(self):
        return self.absolute_url()

    def get_homelink(self):
        return self.aq_parent.absolute_url()
