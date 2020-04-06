# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from plone.namedfile.field import NamedBlobImage
from zope import schema
from zope.interface import implementer
from collective.beaker.interfaces import ISession
from zope.interface import Invalid
from plone.indexer import indexer
from plone import api as ploneapi
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import provider, Invalid
from zope.interface import invariant

from edi.classroom import _

@provider(IContextSourceBinder)
def possibleClasslists(context):
    pm = ploneapi.portal.get_tool(name='portal_membership')
    homefolder = pm.getHomeFolder()
    classlists = ploneapi.content.find(context=homefolder, portal_type="Klassenliste")
    terms = []
    if classlists:
        for i in classlists:
            terms.append(SimpleVocabulary.createTerm(i.UID, i.id, i.Title))
    return SimpleVocabulary(terms)


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

    classlist = schema.Choice(title=u"Klassenliste für diesen Klassenraum",
                         description=u'Sie können für diesen Klassenraum eine Klassenliste auswählen wenn Sie diese vorher in "Mein Ordner"\
                                 angelegt haben. Sie benötigen eine Klassenliste, wenn Sie für Ihren Klassenraum einen sicheren Chatroom\
                                 einrichten wollen.',
                         source=possibleClasslists,
                         required=False)

    chatroom = schema.Bool(title="Chatroom aktivieren",
                           description="Die Aktivierung des Chatrooms setzt die Auswahl einer Klassenliste voraus.",
                           required=False)

    @invariant
    def chat_invariant(data):
        if data.chatroom and not data.classlist:
            raise Invalid(u'Für die Aktivierung eines Chatrooms für diesen Klassenraum muss eine Klassenliste ausgewählt werden.')


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

    def chatmember(self, checkpin):
        chatmember = {}
        if self.classlist:
            classlist = ploneapi.content.get(UID=self.classlist).traineelist
            for i in classlist:
                if checkpin == i.get('pin'):
                    return chatmember
        return chatmember 

    def checkchat(self, request):
        check = False
        uid = self.UID()
        chatid = 'chat_%s' %uid
        session = ISession(request)
        if chatid in session:
            checkpin = session[checkid]
            chatmember = self.chatmember(checkpin)
            if chatmember:
                check = True
        return check

    def get_classlist(self):
        classlist = ploneapi.content.get(UID=self.classlist).traineelist
        return classlist

    def get_backurl(self):
        return self.absolute_url()

    def get_homelink(self):
        return self.absolute_url()


@indexer(IKlassenraum)
def nameIndexer(obj):
    current = ploneapi.user.get_current()
    userroles = ploneapi.user.get_roles(user=current)
    if 'Manager' in userroles or 'Site Administrator' in userroles:
        creator = ploneapi.user.get(username=obj.Creator())
        return creator.getProperty('fullname')
    return current.getProperty('fullname')

@indexer(IKlassenraum)
def mailIndexer(obj):
    current = ploneapi.user.get_current()
    userroles = ploneapi.user.get_roles(user=current)
    if 'Manager' in userroles or 'Site Administrator' in userroles:
        creator = ploneapi.user.get(username=obj.Creator())
        return creator.getProperty('email')
    return current.getProperty('email')
