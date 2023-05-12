# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.7
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


class NewsfeedAssignment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Assigns a news item to a newsfeed.
    """


    class MetaOapg:
        
        class properties:
            newsfeed_id = schemas.IntSchema
            published_at = schemas.IntSchema
            __annotations__ = {
                "newsfeed_id": newsfeed_id,
                "published_at": published_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newsfeed_id"]) -> MetaOapg.properties.newsfeed_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_at"]) -> MetaOapg.properties.published_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["newsfeed_id", "published_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newsfeed_id"]) -> typing.Union[MetaOapg.properties.newsfeed_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_at"]) -> typing.Union[MetaOapg.properties.published_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["newsfeed_id", "published_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        newsfeed_id: typing.Union[MetaOapg.properties.newsfeed_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        published_at: typing.Union[MetaOapg.properties.published_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewsfeedAssignment':
        return super().__new__(
            cls,
            *_args,
            newsfeed_id=newsfeed_id,
            published_at=published_at,
            _configuration=_configuration,
            **kwargs,
        )
