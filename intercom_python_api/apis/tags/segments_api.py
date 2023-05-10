# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.segments.get import ListSegments
from intercom_python_api.paths.contacts_contact_id_segments.get import ListSegmentsForAContact
from intercom_python_api.paths.segments_id.get import RetrieveSegment


class SegmentsApi(
    ListSegments,
    ListSegmentsForAContact,
    RetrieveSegment,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
