"""Setup tests for this package."""
from kitconcept import api
from kitconcept.mediarepository.testing import MEDIAREPOSITORY_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.mediarepository is properly installed."""

    layer = MEDIAREPOSITORY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.types = self.portal.portal_types

    def test_product_installed(self):
        """Test if kitconcept.mediarepository is installed."""
        self.assertIn(
            "kitconcept.mediarepository", api.addon.get_addons_ids("installed")
        )

    def test_browserlayer(self):
        """Test that IMediaRepositoryLayer is registered."""  # noqa
        from kitconcept.mediarepository.interfaces import IMediaRepositoryLayer
        from plone.browserlayer import utils

        self.assertIn(IMediaRepositoryLayer, utils.registered_layers())  # noqa


class TestUninstall(unittest.TestCase):

    layer = MEDIAREPOSITORY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        api.addon.uninstall("kitconcept.mediarepository")

    def test_product_uninstalled(self):
        """Test if kitconcept.mediarepository is cleanly uninstalled."""
        self.assertNotIn(
            "kitconcept.mediarepository", api.addon.get_addons_ids("installed")
        )

    def test_browserlayer_removed(self):
        """Test that IMediaRepositoryLayer is removed."""
        from kitconcept.mediarepository.interfaces import IMediaRepositoryLayer
        from plone.browserlayer import utils

        self.assertNotIn(IMediaRepositoryLayer, utils.registered_layers())
