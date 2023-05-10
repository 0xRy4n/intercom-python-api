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


class CreateDataExportsRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request for creating a data export
    """


    class MetaOapg:
        required = {
            "created_at_before",
            "created_at_after",
        }
        
        class properties:
            created_at_after = schemas.IntSchema
            created_at_before = schemas.IntSchema
            __annotations__ = {
                "created_at_after": created_at_after,
                "created_at_before": created_at_before,
            }
    
    created_at_before: MetaOapg.properties.created_at_before
    created_at_after: MetaOapg.properties.created_at_after
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at_after"]) -> MetaOapg.properties.created_at_after: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at_before"]) -> MetaOapg.properties.created_at_before: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at_after", "created_at_before", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at_after"]) -> MetaOapg.properties.created_at_after: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at_before"]) -> MetaOapg.properties.created_at_before: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at_after", "created_at_before", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        created_at_before: typing.Union[MetaOapg.properties.created_at_before, decimal.Decimal, int, ],
        created_at_after: typing.Union[MetaOapg.properties.created_at_after, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDataExportsRequest':
        return super().__new__(
            cls,
            *_args,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            _configuration=_configuration,
            **kwargs,
        )
