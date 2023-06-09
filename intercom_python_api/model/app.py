# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.9
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


class App(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    App is a workspace on Intercom
    """


    class MetaOapg:
        
        class properties:
            created_at = schemas.IntSchema
            id_code = schemas.StrSchema
            identity_verification = schemas.BoolSchema
            name = schemas.StrSchema
            region = schemas.StrSchema
            timezone = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "created_at": created_at,
                "id_code": id_code,
                "identity_verification": identity_verification,
                "name": name,
                "region": region,
                "timezone": timezone,
                "type": type,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id_code"]) -> MetaOapg.properties.id_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identity_verification"]) -> MetaOapg.properties.identity_verification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "id_code", "identity_verification", "name", "region", "timezone", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id_code"]) -> typing.Union[MetaOapg.properties.id_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identity_verification"]) -> typing.Union[MetaOapg.properties.identity_verification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "id_code", "identity_verification", "name", "region", "timezone", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id_code: typing.Union[MetaOapg.properties.id_code, str, schemas.Unset] = schemas.unset,
        identity_verification: typing.Union[MetaOapg.properties.identity_verification, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'App':
        return super().__new__(
            cls,
            *_args,
            created_at=created_at,
            id_code=id_code,
            identity_verification=identity_verification,
            name=name,
            region=region,
            timezone=timezone,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
