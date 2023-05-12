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


class SnoozeConversationRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Payload of the request to snooze a conversation
    """


    class MetaOapg:
        required = {
            "admin_id",
            "message_type",
            "snoozed_until",
        }
        
        class properties:
            
            
            class message_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SNOOZED(cls):
                    return cls("snoozed")
            admin_id = schemas.StrSchema
            snoozed_until = schemas.IntSchema
            __annotations__ = {
                "message_type": message_type,
                "admin_id": admin_id,
                "snoozed_until": snoozed_until,
            }
    
    admin_id: MetaOapg.properties.admin_id
    message_type: MetaOapg.properties.message_type
    snoozed_until: MetaOapg.properties.snoozed_until
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snoozed_until"]) -> MetaOapg.properties.snoozed_until: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message_type", "admin_id", "snoozed_until", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snoozed_until"]) -> MetaOapg.properties.snoozed_until: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message_type", "admin_id", "snoozed_until", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        admin_id: typing.Union[MetaOapg.properties.admin_id, str, ],
        message_type: typing.Union[MetaOapg.properties.message_type, str, ],
        snoozed_until: typing.Union[MetaOapg.properties.snoozed_until, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SnoozeConversationRequest':
        return super().__new__(
            cls,
            *_args,
            admin_id=admin_id,
            message_type=message_type,
            snoozed_until=snoozed_until,
            _configuration=_configuration,
            **kwargs,
        )
