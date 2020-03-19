# -*- coding: utf-8 -*-
from edi.classroom import _
from Products.Five.browser import BrowserView
from nva.kurzfassung.views.erweiterte_kartenansicht import ErweiterteKartenansicht
from plone import api as ploneapi


class KlassenraumView(ErweiterteKartenansicht):
    """ """

    def __call__(self):
        matches = []
        self.teacher = False
        if not  ploneapi.user.is_anonymous():
            authuser = ploneapi.user.get_current()
            userroles = ploneapi.user.get_roles(user=authuser, obj=self.context, inherit=True)
            editorroles = ['Owner', 'Manager', 'Editor']
            matches = [x for x in editorroles if x in userroles]
        if not matches:
            if not self.context.checkpin(self.request):
                url = self.context.absolute_url() + '/check-pin'
                return self.request.response.redirect(url)
        else:    
            self.teacher = True    
        return self.index()

    def get_link_url(self):
        portalurl = ploneapi.portal.get().absolute_url()
        returl = "%s/@@krks?wc=%s" %(portalurl, self.context.webcode)
        return returl
