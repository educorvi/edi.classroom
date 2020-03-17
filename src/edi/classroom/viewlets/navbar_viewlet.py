# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class NavbarViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'My message'

    def render(self):
        return super(NavbarViewlet, self).render()
