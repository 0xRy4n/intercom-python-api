# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.events.post import CreateDataEvent
from intercom_python_api.paths.events_summaries.post import DataEventSummaries
from intercom_python_api.paths.events.get import LisDataEvents


class DataEventsApi(
    CreateDataEvent,
    DataEventSummaries,
    LisDataEvents,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass