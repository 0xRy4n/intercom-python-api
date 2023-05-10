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


class Message(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Message are how you reach out to contacts in Intercom. They are created when an admin sends an outbound message to a contact.
    """


    class MetaOapg:
        required = {
            "created_at",
            "message_type",
            "id",
            "body",
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
            id = schemas.StrSchema
            created_at = schemas.IntSchema
            body = schemas.StrSchema
            
            
            class message_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("email")
                
                @schemas.classproperty
                def INAPP(cls):
                    return cls("inapp")
                
                @schemas.classproperty
                def FACEBOOK(cls):
                    return cls("facebook")
                
                @schemas.classproperty
                def TWITTER(cls):
                    return cls("twitter")
            subject = schemas.StrSchema
            conversation_id = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "id": id,
                "created_at": created_at,
                "body": body,
                "message_type": message_type,
                "subject": subject,
                "conversation_id": conversation_id,
            }
    
    created_at: MetaOapg.properties.created_at
    message_type: MetaOapg.properties.message_type
    id: MetaOapg.properties.id
    body: MetaOapg.properties.body
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_id"]) -> MetaOapg.properties.conversation_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "created_at", "body", "message_type", "subject", "conversation_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_id"]) -> typing.Union[MetaOapg.properties.conversation_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "created_at", "body", "message_type", "subject", "conversation_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, ],
        message_type: typing.Union[MetaOapg.properties.message_type, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        body: typing.Union[MetaOapg.properties.body, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        conversation_id: typing.Union[MetaOapg.properties.conversation_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Message':
        return super().__new__(
            cls,
            *_args,
            created_at=created_at,
            message_type=message_type,
            id=id,
            body=body,
            type=type,
            subject=subject,
            conversation_id=conversation_id,
            _configuration=_configuration,
            **kwargs,
        )