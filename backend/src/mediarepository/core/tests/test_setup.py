"""Setup tests for this package."""
from kitconcept import api
from mediarepository.core.testing import MEDIAREPOSITORY_CORE_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that mediarepository.core is properly installed."""

    layer = MEDIAREPOSITORY_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.types = self.portal.portal_types

    def test_product_installed(self):
        """Test if mediarepository.core is installed."""
        self.assertIn("mediarepository.core", api.addon.get_addons_ids("installed"))

    def test_browserlayer(self):
        """Test that IMediaRepositoryLayer is registered."""  # noqa
        from mediarepository.core.interfaces import IMediaRepositoryLayer
        from plone.browserlayer import utils

        self.assertIn(IMediaRepositoryLayer, utils.registered_layers())  # noqa


class TestUninstall(unittest.TestCase):

    layer = MEDIAREPOSITORY_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        api.addon.uninstall("mediarepository.core")

    def test_product_uninstalled(self):
        """Test if mediarepository.core is cleanly uninstalled."""
        self.assertNotIn("mediarepository.core", api.addon.get_addons_ids("installed"))

    def test_browserlayer_removed(self):
        """Test that IMediaRepositoryLayer is removed."""
        from mediarepository.core.interfaces import IMediaRepositoryLayer
        from plone.browserlayer import utils

        self.assertNotIn(IMediaRepositoryLayer, utils.registered_layers())
