# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api

class OrderViewlet(ViewletBase):

    def update(self):
        self.portal_url = self.portal_url()
        self.is_anon = self.is_anon()

    def portal_url(self):
        return api.portal.get().absolute_url()

    def is_anon(self):
        if api.user.is_anonymous():
            return True
        return False

    def render(self):
        objid = u"handy-stative-fuer-die-produktion-von-medien-fuer-das-online-lernen"
        if self.context.portal_type == "Folder" and self.context.getId() == objid:
            return super(OrderViewlet, self).render()
        return ''
