from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import kitconcept.mediarepository


class MEDIAREPOSITORYCORELayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=kitconcept.mediarepository)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "kitconcept.mediarepository:default")


MEDIAREPOSITORY_FIXTURE = MEDIAREPOSITORYCORELayer()


MEDIAREPOSITORY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIAREPOSITORY_FIXTURE,),
    name="MEDIAREPOSITORYCORELayer:IntegrationTesting",
)


MEDIAREPOSITORY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIAREPOSITORY_FIXTURE, WSGI_SERVER_FIXTURE),
    name="MEDIAREPOSITORYCORELayer:FunctionalTesting",
)


MEDIAREPOSITORYACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIAREPOSITORY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="MEDIAREPOSITORYCORELayer:AcceptanceTesting",
)
