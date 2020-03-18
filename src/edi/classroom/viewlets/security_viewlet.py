# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi


class SecurityViewlet(ViewletBase):

    def update(self):
        portalurl = ploneapi.portal.get().absolute_url()
        matches = []
        if not ploneapi.user.is_anonymous():
            authuser = ploneapi.user.get_current()
            userroles = ploneapi.user.get_roles(user=authuser, obj=self.context, inherit=True)
            adminroles = ['Owner', 'Manager', 'Site Administrator']
            matches = [x for x in adminroles if x in userroles]
        if not matches:
            if self.context.absolute_url().endswith('/Members'):
                return self.request.response.redirect(portalurl)
            if self.context.aq_inner.aq_parent.getId() == 'Members':
                return self.request.response.redirect(portalurl)
        return True


    def render(self):
        return super(SecurityViewlet, self).render()
