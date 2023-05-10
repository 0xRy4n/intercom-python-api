# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from intercom_python_api import schemas  # noqa: F401


class IntercomVersion(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Intercom API version.</br>By default, it's equal to the version set in the app package.
    """


    class MetaOapg:
        enum_value_to_name = {
            "1.0": "POSITIVE_1_PT_0",
            "1.1": "POSITIVE_1_PT_1",
            "1.2": "POSITIVE_1_PT_2",
            "1.3": "POSITIVE_1_PT_3",
            "1.4": "POSITIVE_1_PT_4",
            "2.0": "POSITIVE_2_PT_0",
            "2.1": "POSITIVE_2_PT_1",
            "2.2": "POSITIVE_2_PT_2",
            "2.3": "POSITIVE_2_PT_3",
            "2.4": "POSITIVE_2_PT_4",
            "2.5": "POSITIVE_2_PT_5",
            "2.6": "POSITIVE_2_PT_6",
            "2.7": "POSITIVE_2_PT_7",
            "2.8": "POSITIVE_2_PT_8",
            "Unstable": "UNSTABLE",
        }
    
    @schemas.classproperty
    def POSITIVE_1_PT_0(cls):
        return cls("1.0")
    
    @schemas.classproperty
    def POSITIVE_1_PT_1(cls):
        return cls("1.1")
    
    @schemas.classproperty
    def POSITIVE_1_PT_2(cls):
        return cls("1.2")
    
    @schemas.classproperty
    def POSITIVE_1_PT_3(cls):
        return cls("1.3")
    
    @schemas.classproperty
    def POSITIVE_1_PT_4(cls):
        return cls("1.4")
    
    @schemas.classproperty
    def POSITIVE_2_PT_0(cls):
        return cls("2.0")
    
    @schemas.classproperty
    def POSITIVE_2_PT_1(cls):
        return cls("2.1")
    
    @schemas.classproperty
    def POSITIVE_2_PT_2(cls):
        return cls("2.2")
    
    @schemas.classproperty
    def POSITIVE_2_PT_3(cls):
        return cls("2.3")
    
    @schemas.classproperty
    def POSITIVE_2_PT_4(cls):
        return cls("2.4")
    
    @schemas.classproperty
    def POSITIVE_2_PT_5(cls):
        return cls("2.5")
    
    @schemas.classproperty
    def POSITIVE_2_PT_6(cls):
        return cls("2.6")
    
    @schemas.classproperty
    def POSITIVE_2_PT_7(cls):
        return cls("2.7")
    
    @schemas.classproperty
    def POSITIVE_2_PT_8(cls):
        return cls("2.8")
    
    @schemas.classproperty
    def UNSTABLE(cls):
        return cls("Unstable")
