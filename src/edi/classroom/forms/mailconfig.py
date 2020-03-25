# -*- coding:utf-8 -*-

def create_edibody(data):
    body = u"""\
Neue Bestellung eines Handy-Stativs:

E-Mail: %s

%s
%s
%s %s
    """ % (data.get('email'),
            data.get('name'),
            data.get('strhnr'),
            data.get('plz'),
            data.get('ort'),)
    return body.encode('utf-8')

def create_userbody(data):
    body = u"""\
Vielen Dank für Ihre Bestellung eines Handy-Stativs auf kraeks.de.

Bitte überweisen Sie nach Erhalt des Stativs einen Betrag von 9,00 Euro (incl. Mwst).

IBAN:
BIC:
Kontoinhaber: educorvi GmbH & Co. KG

Ihre E-Mail-Adresse: %s

Wir werden das Stativ an folgende Adresse senden:

%s
%s
%s %s
    """ % (data.get('email'),
            data.get('name'),
            data.get('strhnr'),
            data.get('plz'),
            data.get('ort'),)
    return body.encode('utf-8')
