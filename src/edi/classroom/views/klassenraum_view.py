# -*- coding: utf-8 -*-

from edi.classroom import _
from Products.Five.browser import BrowserView
from collective.beaker.interfaces import ISession

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class KlassenraumView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('klassenraum_view.pt')


    def __call__(self):
        # Implement your own actions:
        if not self.checkpin():
            url = self.context.absolute_url() + '/check-pin'
            return self.request.response.redirect(url)
        self.msg = _(u'A small message')
        return self.index()

    def checkpin(self):
        check = False
        uid = self.context.UID()
        session = ISession(self.request)
        if uid in session:
            checkpin = session[uid]
            check = self.context.compare_pin(checkpin)
        return check

