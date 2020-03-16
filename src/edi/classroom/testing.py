# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.classroom


class EdiClassroomLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.classroom)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.classroom:default')


EDI_CLASSROOM_FIXTURE = EdiClassroomLayer()


EDI_CLASSROOM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_CLASSROOM_FIXTURE,),
    name='EdiClassroomLayer:IntegrationTesting',
)


EDI_CLASSROOM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_CLASSROOM_FIXTURE,),
    name='EdiClassroomLayer:FunctionalTesting',
)


EDI_CLASSROOM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_CLASSROOM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiClassroomLayer:AcceptanceTesting',
)
