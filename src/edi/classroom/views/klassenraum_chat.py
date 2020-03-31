# -*- coding: utf-8 -*-
from edi.classroom import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi
import jsonlib

class ChatData(BrowserView):

    def __call__(self):
        data = {}
        matches = []
        if not  ploneapi.user.is_anonymous():
            authuser = ploneapi.user.get_current()
            userroles = ploneapi.user.get_roles(user=authuser, obj=self.context, inherit=True)
            editorroles = ['Owner', 'Manager', 'Editor']
            matches = [x for x in editorroles if x in userroles]
        if not matches:    
            if not self.context.checkpin(self.request):
                data = {'error':'no valid pin for entering classroom'}
                payload = jsonlib.write(data)
                return payload
        if matches:
            data['user'] = {'name':authuser.getProperty('fullname'), 'pin':'', 'role':'teacher'}
        else:
            data['user'] = {'name':'julian', 'pin':'0815', 'role':'trainee'}
        data['teacher_folder_uid'] = self.context.aq_parent.UID()
        data['classroom_uid'] = self.context.UID()
        data['dbuser'] = 'admin'
        data['dbpassword'] = '!krks.d3print/edi_sicherinvestieren!'
        data['classlist'] = [{'name':'john', 'pin':'1234'}, {'name':'julian', 'pin':'0815'}, {'name':'lars', 'pin':'4711'}]
        print(data)
        payload = jsonlib.write(data)
        return payload
