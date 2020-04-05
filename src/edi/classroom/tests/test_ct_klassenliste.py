# -*- coding: utf-8 -*-
from edi.classroom.content.klassenliste import IKlassenliste  # NOQA E501
from edi.classroom.testing import EDI_CLASSROOM_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class KlassenlisteIntegrationTest(unittest.TestCase):

    layer = EDI_CLASSROOM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_klassenliste_schema(self):
        fti = queryUtility(IDexterityFTI, name='Klassenliste')
        schema = fti.lookupSchema()
        self.assertEqual(IKlassenliste, schema)

    def test_ct_klassenliste_fti(self):
        fti = queryUtility(IDexterityFTI, name='Klassenliste')
        self.assertTrue(fti)

    def test_ct_klassenliste_factory(self):
        fti = queryUtility(IDexterityFTI, name='Klassenliste')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IKlassenliste.providedBy(obj),
            u'IKlassenliste not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_klassenliste_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Klassenliste',
            id='klassenliste',
        )

        self.assertTrue(
            IKlassenliste.providedBy(obj),
            u'IKlassenliste not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('klassenliste', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('klassenliste', parent.objectIds())

    def test_ct_klassenliste_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Klassenliste')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
