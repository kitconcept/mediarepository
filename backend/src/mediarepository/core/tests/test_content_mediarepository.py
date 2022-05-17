from kitconcept import api
from mediarepository.core.content.mediarepository import IMediaRepository
from mediarepository.core.testing import MEDIAREPOSITORY_CORE_INTEGRATION_TESTING
from zope.component import createObject

import unittest


class MediaRepositoryIntegrationTest(unittest.TestCase):

    layer = MEDIAREPOSITORY_CORE_INTEGRATION_TESTING

    portal_type = "Media Repository"

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        fti = api.fti.get(self.portal_type)
        fti.global_allow = True

    def test_schema(self):
        fti = api.fti.get(self.portal_type)
        schema = fti.lookupSchema()
        self.assertEqual(IMediaRepository, schema)

    def test_fti(self):
        fti = api.fti.get(self.portal_type)
        self.assertTrue(fti)

    def test_factory(self):
        fti = api.fti.get(self.portal_type)
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IMediaRepository.providedBy(obj))

    def test_add_as_manager(self):
        with api.env.adopt_roles(
            [
                "Manager",
            ]
        ):
            obj = api.content.create(
                container=self.portal,
                type=self.portal_type,
                title=self.portal_type,
            )
        self.assertTrue(IMediaRepository.providedBy(obj))

    def test_add_as_site_administrator(self):
        with api.env.adopt_roles(
            [
                "Site Administrator",
            ]
        ):
            obj = api.content.create(
                container=self.portal,
                type=self.portal_type,
                title=self.portal_type,
            )
        self.assertTrue(IMediaRepository.providedBy(obj))

    def test_add_as_contributor(self):
        from AccessControl import Unauthorized

        with api.env.adopt_roles(
            [
                "Contributor",
            ]
        ):
            self.assertRaises(
                Unauthorized,
                api.content.create,
                **{
                    "container": self.portal,
                    "type": self.portal_type,
                    "title": self.portal_type,
                },
            )
