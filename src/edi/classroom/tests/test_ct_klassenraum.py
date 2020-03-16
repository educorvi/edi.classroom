# -*- coding: utf-8 -*-
from edi.classroom.content.klassenraum import IKlassenraum  # NOQA E501
from edi.classroom.testing import EDI_CLASSROOM_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class KlassenraumIntegrationTest(unittest.TestCase):

    layer = EDI_CLASSROOM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_klassenraum_schema(self):
        fti = queryUtility(IDexterityFTI, name='Klassenraum')
        schema = fti.lookupSchema()
        self.assertEqual(IKlassenraum, schema)

    def test_ct_klassenraum_fti(self):
        fti = queryUtility(IDexterityFTI, name='Klassenraum')
        self.assertTrue(fti)

    def test_ct_klassenraum_factory(self):
        fti = queryUtility(IDexterityFTI, name='Klassenraum')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IKlassenraum.providedBy(obj),
            u'IKlassenraum not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_klassenraum_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Klassenraum',
            id='klassenraum',
        )

        self.assertTrue(
            IKlassenraum.providedBy(obj),
            u'IKlassenraum not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('klassenraum', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('klassenraum', parent.objectIds())

    def test_ct_klassenraum_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Klassenraum')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_klassenraum_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Klassenraum')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'klassenraum_id',
            title='Klassenraum container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
