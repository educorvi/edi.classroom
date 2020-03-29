from plone import api as ploneapi

def PublishClassroom(Klassenraum, event):

    ploneapi.content.rename(obj=Klassenraum, new_id=Klassenraum.UID())
