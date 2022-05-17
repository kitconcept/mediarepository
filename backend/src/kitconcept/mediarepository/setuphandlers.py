"""Setup helpers."""
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import logging


logger = logging.getLogger("kitconcept.mediarepository.setuphandlers")


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation."""
        return ["kitconcept.mediarepository:uninstall"]


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
