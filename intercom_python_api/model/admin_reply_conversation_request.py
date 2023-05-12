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


class AdminReplyConversationRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Payload of the request to reply on behalf of an admin
    """


    class MetaOapg:
        required = {
            "admin_id",
            "message_type",
            "type",
        }
        
        class properties:
            
            
            class message_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "comment": "COMMENT",
                        "note": "NOTE",
                    }
                
                @schemas.classproperty
                def COMMENT(cls):
                    return cls("comment")
                
                @schemas.classproperty
                def NOTE(cls):
                    return cls("note")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "admin": "ADMIN",
                    }
                
                @schemas.classproperty
                def ADMIN(cls):
                    return cls("admin")
            admin_id = schemas.StrSchema
            body = schemas.StrSchema
            
            
            class attachment_urls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 5
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachment_urls':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "message_type": message_type,
                "type": type,
                "admin_id": admin_id,
                "body": body,
                "attachment_urls": attachment_urls,
            }
    
    admin_id: MetaOapg.properties.admin_id
    message_type: MetaOapg.properties.message_type
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment_urls"]) -> MetaOapg.properties.attachment_urls: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "admin_id", "body", "attachment_urls", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment_urls"]) -> typing.Union[MetaOapg.properties.attachment_urls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "admin_id", "body", "attachment_urls", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        admin_id: typing.Union[MetaOapg.properties.admin_id, str, ],
        message_type: typing.Union[MetaOapg.properties.message_type, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        attachment_urls: typing.Union[MetaOapg.properties.attachment_urls, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdminReplyConversationRequest':
        return super().__new__(
            cls,
            *_args,
            admin_id=admin_id,
            message_type=message_type,
            type=type,
            body=body,
            attachment_urls=attachment_urls,
            _configuration=_configuration,
            **kwargs,
        )
