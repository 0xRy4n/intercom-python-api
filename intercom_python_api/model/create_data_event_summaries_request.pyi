# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: Unstable
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


class CreateDataEventSummariesRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can send a list of event summaries for a user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense "verb-noun" combination, to improve readability, for example `updated-plan`.
    """


    class MetaOapg:
        
        class properties:
            user_id = schemas.StrSchema
            
            
            class event_summaries(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        event_name = schemas.StrSchema
                        count = schemas.IntSchema
                        first = schemas.IntSchema
                        last = schemas.IntSchema
                        __annotations__ = {
                            "event_name": event_name,
                            "count": count,
                            "first": first,
                            "last": last,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["event_name"]) -> MetaOapg.properties.event_name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_name", "count", "first", "last", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["event_name"]) -> typing.Union[MetaOapg.properties.event_name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union[MetaOapg.properties.first, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union[MetaOapg.properties.last, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_name", "count", "first", "last", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    event_name: typing.Union[MetaOapg.properties.event_name, str, schemas.Unset] = schemas.unset,
                    count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    first: typing.Union[MetaOapg.properties.first, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    last: typing.Union[MetaOapg.properties.last, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'event_summaries':
                    return super().__new__(
                        cls,
                        *_args,
                        event_name=event_name,
                        count=count,
                        first=first,
                        last=last,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "user_id": user_id,
                "event_summaries": event_summaries,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_summaries"]) -> MetaOapg.properties.event_summaries: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_id", "event_summaries", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_summaries"]) -> typing.Union[MetaOapg.properties.event_summaries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_id", "event_summaries", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, schemas.Unset] = schemas.unset,
        event_summaries: typing.Union[MetaOapg.properties.event_summaries, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDataEventSummariesRequest':
        return super().__new__(
            cls,
            *_args,
            user_id=user_id,
            event_summaries=event_summaries,
            _configuration=_configuration,
            **kwargs,
        )
