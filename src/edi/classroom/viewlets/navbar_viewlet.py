# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api as ploneapi


class NavbarViewlet(ViewletBase):

    def get_homelink(self):
        if self.context.portal_type in [u'Klassenraum', u'Thema']:
            return self.context.get_homelink()
        else:
            return self.context.aq_inner.aq_parent.get_homelink()

    def get_skills(self):
        skills = ploneapi.content.find(context=self.context, depth=1, portal_type='Skill')
        return skills

    def get_themen(self):
        themen = ploneapi.content.find(context=self.context, depth=1, portal_type='Thema')
        return themen

    def render(self):
        if not self.context.portal_type in [u'Klassenraum', u'Thema', u'Skill']:
            return u''
        if self.context.portal_type == 'Skill':
            if not self.context.aq_parent.portal_type in [u'Klassenraum', u'Thema']:
                return u''
        return super(NavbarViewlet, self).render()
