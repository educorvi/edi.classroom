# -*- coding: utf-8 -*-
from edi.classroom import _
from Products.Five.browser import BrowserView
from nva.kurzfassung.views.erweiterte_kartenansicht import ErweiterteKartenansicht
from plone import api as ploneapi


class ThemaView(ErweiterteKartenansicht):
    """ """

    def __call__(self):
        matches = []
        if not  ploneapi.user.is_anonymous():
            authuser = ploneapi.user.get_current()
            userroles = ploneapi.user.get_roles(user=authuser, obj=self.context, inherit=True)
            editorroles = ['Owner', 'Manager', 'Editor']
            matches = [x for x in editorroles if x in userroles]
        if not matches:
            if not self.context.checkpin(self.request):
                url = self.context.aq_parent.absolute_url() + '/check-pin'
                return self.request.response.redirect(url)
        return self.index()
