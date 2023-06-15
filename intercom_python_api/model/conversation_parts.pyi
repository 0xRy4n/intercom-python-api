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


class ConversationParts(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A list of Conversation Part objects for each part message in the conversation. This is only returned when Retrieving a Conversation, and ignored when Listing all Conversations. There is a limit of 500 parts.
    """


    class MetaOapg:
        
        class properties:
            
            
            class conversation_parts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ConversationPart']:
                        return ConversationPart
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ConversationPart'], typing.List['ConversationPart']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conversation_parts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ConversationPart':
                    return super().__getitem__(i)
            total_count = schemas.IntSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONVERSATION_PART_LIST(cls):
                    return cls("conversation_part.list")
            __annotations__ = {
                "conversation_parts": conversation_parts,
                "total_count": total_count,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_parts"]) -> MetaOapg.properties.conversation_parts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conversation_parts", "total_count", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_parts"]) -> typing.Union[MetaOapg.properties.conversation_parts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> typing.Union[MetaOapg.properties.total_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conversation_parts", "total_count", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        conversation_parts: typing.Union[MetaOapg.properties.conversation_parts, list, tuple, schemas.Unset] = schemas.unset,
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConversationParts':
        return super().__new__(
            cls,
            *_args,
            conversation_parts=conversation_parts,
            total_count=total_count,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.conversation_part import ConversationPart
