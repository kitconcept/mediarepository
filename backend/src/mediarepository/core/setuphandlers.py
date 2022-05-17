"""Setup helpers."""
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import logging


logger = logging.getLogger("mediarepository.core.setuphandlers")


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation."""
        return ["mediarepository.core:uninstall"]


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
