from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from zope.interface import implementer


class IMediaRepository(Schema):
    """Media Repository content type interface"""


@implementer(IMediaRepository)
class MediaRepository(Container):
    """Media Repository content type"""
