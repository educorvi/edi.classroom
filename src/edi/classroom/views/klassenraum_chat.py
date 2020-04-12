# -*- coding: utf-8 -*-
import requests
from edi.classroom import _
from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from collective.beaker.interfaces import ISession
from plone import api as ploneapi
import jsonlib


class ChatData(BrowserView):

    def get_credentials(self):
        registry = getUtility(IRegistry)
        adminuser = registry['edi.classroom.browser.settings.ISettings.adminuser']
        adminpassword = registry['edi.classroom.browser.settings.ISettings.adminpassword']
        return (adminuser, adminpassword)

    def get_databases(self):
        myheaders ={'Accept': 'application/json'}
        myauth = self.get_credentials()
        response = requests.get('https://couch.kraeks.de/_all_dbs', headers=myheaders, auth=myauth)
        databases = response.json()
        compare = "classroomchat_%s" %self.context.UID()
        if compare in databases:
            return True
        return False

    def create_database(self):
        token = self.context.UID()
        myheaders ={'Accept': 'application/json', 'Content-Type': 'application/json'}
        myauth = self.get_credentials()

        database_url = 'https://couch.kraeks.de/classroomchat_%s' %token
        new_database = requests.put(database_url, headers=myheaders, auth=myauth)

        newuser_url = 'https://couch.kraeks.de/_users/org.couchdb.user:%s' %token
        data = {"name": token, "password": token, "roles": [], "type": "user"}
        newuser = requests.put(newuser_url, headers=myheaders, auth=myauth, json=data)

        security_url = 'https://couch.kraeks.de/classroomchat_%s/_security' %token
        data = {"admins":{"names":[], "roles":[]}, "members":{"names":[token], "roles":[]}}
        security = requests.put(security_url, headers=myheaders, auth=myauth, json=data)

        if new_database.status_code == 200 and newuser.status_code == 200 and security.status_code == 200:
            return True
        return False

    def __call__(self):
        data = {}
        if not  ploneapi.user.is_anonymous():
            authuser = ploneapi.user.get_current()
            data['user'] = {'name':authuser.getProperty('fullname'), 'pin':authuser.getProperty('email'), 'role':'teacher'}
        else:
            session = ISession(self.request)
            chatid = 'chat_%s' % self.context.UID()
            userdata = session.get(chatid)
            userdata['role'] = 'trainee'
            data['user'] = userdata
        database = True
        if not self.get_databases():
            database = self.create_database()
        data['database'] = database
        data['teacher_folder_uid'] = self.context.aq_parent.UID()
        data['classroom_uid'] = self.context.UID()
        myauth = self.get_credentials()
        data['dbuser'] = myauth[0]
        data['dbpassword'] = myauth[1]
        classlist = self.context.get_classlist()
        data['classlist'] = classlist
        payload = jsonlib.write(data)
        return payload
