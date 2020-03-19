=============
edi.classroom
=============

Dieses Add-On stellt einen virtuellen Klassenraum für das Content-Management-System Plone zur Verfügung. Für die volle Funktionsweise 
von edi.classroom werden weitere Packages benötigt:

- nva.kurzfassung (https://github.com/novareto/nva.kurzfassung.git)
- nva.folderbehaviors (https://github.com/novareto/nva.folderbehaviors.git)
- edi.skillpill (https://github.com/educorvi/edi.skillpill.git)

Features
--------

- Inhaltstypen Klassenraum und Thema
- Eigene Navigation für Schülerinnen und Schüler
- Short-Link für das Teilen von Inhalten mit Schülerinnen und Schülern
- Für den Zugang zum Klassenraum wird der Link und ein PIN benötigt  


Examples
--------

Dieses Add-On kann ist auf folgenden Seiten installiert:

- https://www.kraeks.de


Documentation
-------------

Dokumentationen des Packages stehen hier zur Verfügung:

- https://www.kraeks.de/fulldok
- https://github.com/educorvi/edi.classroom


Translations
------------

Das Add-On steht momentan nur in Deutscher Sprache zur Verfügung.

Installation
------------

Die Installation von edi.classroom durch Hinzufügen des folgenden Add-Ons zur buildout.cfg::

    [buildout]

    ...

    eggs =
        edi.classroom


dann bitte ausführen: ``bin/buildout``


Contribute
----------

- Problemmeldungen: https://github.com/collective/edi.classroom/issues
- Quellcode: https://github.com/collective/edi.classroom
- Documentation: https://www.kraeks.de/fulldok


Support
-------

Sie haben ein Problem mit edi.classroom? Bitte lassen Sie es uns wissen: info@educorvi.de


License
-------

Das Add-on ist lizensiert unter GPLv2.
