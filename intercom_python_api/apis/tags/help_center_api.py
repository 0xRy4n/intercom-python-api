# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.help_center_collections.post import CreateCollection
from intercom_python_api.paths.help_center_sections.post import CreateSection
from intercom_python_api.paths.help_center_collections_id.delete import DeleteCollection
from intercom_python_api.paths.help_center_sections_id.delete import DeleteSection
from intercom_python_api.paths.help_center_collections.get import ListAllCollections
from intercom_python_api.paths.help_center_sections.get import ListAllSections
from intercom_python_api.paths.help_center_collections_id.get import RetrieveCollection
from intercom_python_api.paths.help_center_sections_id.get import RetrieveSection
from intercom_python_api.paths.help_center_collections_id.put import UpdateCollection
from intercom_python_api.paths.help_center_sections_id.put import UpdateSection


class HelpCenterApi(
    CreateCollection,
    CreateSection,
    DeleteCollection,
    DeleteSection,
    ListAllCollections,
    ListAllSections,
    RetrieveCollection,
    RetrieveSection,
    UpdateCollection,
    UpdateSection,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass