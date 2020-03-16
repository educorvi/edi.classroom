# -*- coding: utf-8 -*-
from edi.classroom.content.thema import IThema  # NOQA E501
from edi.classroom.testing import EDI_CLASSROOM_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ThemaIntegrationTest(unittest.TestCase):

    layer = EDI_CLASSROOM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Klassenraum',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_thema_schema(self):
        fti = queryUtility(IDexterityFTI, name='Thema')
        schema = fti.lookupSchema()
        self.assertEqual(IThema, schema)

    def test_ct_thema_fti(self):
        fti = queryUtility(IDexterityFTI, name='Thema')
        self.assertTrue(fti)

    def test_ct_thema_factory(self):
        fti = queryUtility(IDexterityFTI, name='Thema')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IThema.providedBy(obj),
            u'IThema not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_thema_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Thema',
            id='thema',
        )

        self.assertTrue(
            IThema.providedBy(obj),
            u'IThema not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('thema', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('thema', parent.objectIds())

    def test_ct_thema_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Thema')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_thema_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Thema')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'thema_id',
            title='Thema container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
