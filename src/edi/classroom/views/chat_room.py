# -*- coding: utf-8 -*-

from edi.classroom import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ChatRoom(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('chat_room.pt')

    def __call__(self):
        # Implement your own actions:

        portal = ploneapi.portal.get().absolute_url()
        self.statics= portal + '/++resource++edi.classroom'
        return self.index()
