# -*- coding: utf-8 -*-
import requests
from edi.classroom import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi
import jsonlib

class ChatData(BrowserView):

    def get_databases(self):
        myheaders ={'Accept': 'application/json'}
        myauth = ('admin', '!krks.d3print/edi_sicherinvestieren!')
        response = requests.get('https://couch.kraeks.de/_all_dbs', headers=myheaders, auth=myauth)
        databases = response.json()
        compare = "classroomchat_%s" %self.context.UID()
        if compare in databases:
            return True
        return False

    def create_database(self):
        token = self.context.UID()
        myheaders ={'Accept': 'application/json', 'Content-Type': 'application/json'}
        myauth = ('admin', '!krks.d3print/edi_sicherinvestieren!')

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
            data['user'] = {'name':authuser.getProperty('fullname'), 'pin':authuser.getProperty('email'), 'role':'teacher'}
        else:
            data['user'] = {'name':'julian', 'pin':'0815', 'role':'trainee'}
        database = True
        if not self.get_databases():
            database = self.create_database()
        data['database'] = database
        data['teacher_folder_uid'] = self.context.aq_parent.UID()
        data['classroom_uid'] = self.context.UID()
        data['dbuser'] = 'admin'
        data['dbpassword'] = '!krks.d3print/edi_sicherinvestieren!'
        myclasslist = [{'name':'Lehrer Lämpel', 'pin':'walther.educorvi@gmail.com'}, 
                       {'name':'john', 'pin':'1234'}, {'name':'julian', 'pin':'0815'}, {'name':'lars', 'pin':'4711'}]
        data['classlist'] = myclasslist
        print(data)
        payload = jsonlib.write(data)
        return payload
