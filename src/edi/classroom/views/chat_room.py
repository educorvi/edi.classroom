# -*- coding: utf-8 -*-

from edi.classroom import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

class ChatRoom(BrowserView):

    def __call__(self):
        # Implement your own actions:
        matches = []
        self.teacher = False
        if not  ploneapi.user.is_anonymous():
            authuser = ploneapi.user.get_current()
            userroles = ploneapi.user.get_roles(user=authuser, obj=self.context, inherit=True)
            editorroles = ['Owner', 'Manager', 'Editor']
            matches = [x for x in editorroles if x in userroles]
        if not matches:
            if not self.context.checkchat(self.request):
                url = self.context.absolute_url() + '/chat-pin'
                return self.request.response.redirect(url)
        else:
            self.teacher = True

        portal = ploneapi.portal.get().absolute_url()
        self.statics= portal + '/++resource++edi.classroom'
        return self.index()
