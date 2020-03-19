# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from plone import api as ploneapi

class KrksView(BrowserView):
    def __call__(self):
        wc = self.request.get('wc','noWebCode')
        brains = ploneapi.content.find(Webcode=wc)
        if brains:
            if len(brains) == 1:
                url = brains[0].getURL()
                return self.request.response.redirect(url)
        errormsg = u"Der eingegebene Link ist leider nicht gültig."    
        ploneapi.portal.show_message(message=errormsg, request=self.request, type='error')
        portal = ploneapi.portal.get().absolute_url()
        return self.request.response.redirect(portal)
