from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import mediarepository.core


class MEDIAREPOSITORYCORELayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=mediarepository.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "mediarepository.core:default")


MEDIAREPOSITORY_CORE_FIXTURE = MEDIAREPOSITORYCORELayer()


MEDIAREPOSITORY_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIAREPOSITORY_CORE_FIXTURE,),
    name="MEDIAREPOSITORYCORELayer:IntegrationTesting",
)


MEDIAREPOSITORY_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIAREPOSITORY_CORE_FIXTURE, WSGI_SERVER_FIXTURE),
    name="MEDIAREPOSITORYCORELayer:FunctionalTesting",
)


MEDIAREPOSITORY_COREACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIAREPOSITORY_CORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="MEDIAREPOSITORYCORELayer:AcceptanceTesting",
)
