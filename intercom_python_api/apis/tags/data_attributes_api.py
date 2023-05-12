# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: Unstable
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.data_attributes.post import CreateDataAttribute
from intercom_python_api.paths.data_attributes.get import LisDataAttributes
from intercom_python_api.paths.data_attributes_id.put import UpdateDataAttribute


class DataAttributesApi(
    CreateDataAttribute,
    LisDataAttributes,
    UpdateDataAttribute,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
