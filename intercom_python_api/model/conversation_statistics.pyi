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


class ConversationStatistics(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A Statistics object containing all information required for reporting, with timestamps and calculated metrics.
    """


    class MetaOapg:
        
        class properties:
            count_assignments = schemas.IntSchema
            count_conversation_parts = schemas.IntSchema
            count_reopens = schemas.IntSchema
            first_admin_reply_at = schemas.IntSchema
            first_assignment_at = schemas.IntSchema
            first_close_at = schemas.IntSchema
            first_contact_reply_at = schemas.IntSchema
            last_admin_reply_at = schemas.IntSchema
            last_assignment_admin_reply_at = schemas.IntSchema
            last_assignment_at = schemas.IntSchema
            last_close_at = schemas.IntSchema
            last_closed_by_id = schemas.StrSchema
            last_contact_reply_at = schemas.IntSchema
            median_time_to_reply = schemas.IntSchema
            time_to_admin_reply = schemas.IntSchema
            time_to_assignment = schemas.IntSchema
            time_to_first_close = schemas.IntSchema
            time_to_last_close = schemas.IntSchema
            type = schemas.StrSchema
            __annotations__ = {
                "count_assignments": count_assignments,
                "count_conversation_parts": count_conversation_parts,
                "count_reopens": count_reopens,
                "first_admin_reply_at": first_admin_reply_at,
                "first_assignment_at": first_assignment_at,
                "first_close_at": first_close_at,
                "first_contact_reply_at": first_contact_reply_at,
                "last_admin_reply_at": last_admin_reply_at,
                "last_assignment_admin_reply_at": last_assignment_admin_reply_at,
                "last_assignment_at": last_assignment_at,
                "last_close_at": last_close_at,
                "last_closed_by_id": last_closed_by_id,
                "last_contact_reply_at": last_contact_reply_at,
                "median_time_to_reply": median_time_to_reply,
                "time_to_admin_reply": time_to_admin_reply,
                "time_to_assignment": time_to_assignment,
                "time_to_first_close": time_to_first_close,
                "time_to_last_close": time_to_last_close,
                "type": type,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count_assignments"]) -> MetaOapg.properties.count_assignments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count_conversation_parts"]) -> MetaOapg.properties.count_conversation_parts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count_reopens"]) -> MetaOapg.properties.count_reopens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_admin_reply_at"]) -> MetaOapg.properties.first_admin_reply_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_assignment_at"]) -> MetaOapg.properties.first_assignment_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_close_at"]) -> MetaOapg.properties.first_close_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_contact_reply_at"]) -> MetaOapg.properties.first_contact_reply_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_admin_reply_at"]) -> MetaOapg.properties.last_admin_reply_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_assignment_admin_reply_at"]) -> MetaOapg.properties.last_assignment_admin_reply_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_assignment_at"]) -> MetaOapg.properties.last_assignment_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_close_at"]) -> MetaOapg.properties.last_close_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_closed_by_id"]) -> MetaOapg.properties.last_closed_by_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_contact_reply_at"]) -> MetaOapg.properties.last_contact_reply_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["median_time_to_reply"]) -> MetaOapg.properties.median_time_to_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_to_admin_reply"]) -> MetaOapg.properties.time_to_admin_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_to_assignment"]) -> MetaOapg.properties.time_to_assignment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_to_first_close"]) -> MetaOapg.properties.time_to_first_close: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_to_last_close"]) -> MetaOapg.properties.time_to_last_close: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["count_assignments", "count_conversation_parts", "count_reopens", "first_admin_reply_at", "first_assignment_at", "first_close_at", "first_contact_reply_at", "last_admin_reply_at", "last_assignment_admin_reply_at", "last_assignment_at", "last_close_at", "last_closed_by_id", "last_contact_reply_at", "median_time_to_reply", "time_to_admin_reply", "time_to_assignment", "time_to_first_close", "time_to_last_close", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count_assignments"]) -> typing.Union[MetaOapg.properties.count_assignments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count_conversation_parts"]) -> typing.Union[MetaOapg.properties.count_conversation_parts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count_reopens"]) -> typing.Union[MetaOapg.properties.count_reopens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_admin_reply_at"]) -> typing.Union[MetaOapg.properties.first_admin_reply_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_assignment_at"]) -> typing.Union[MetaOapg.properties.first_assignment_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_close_at"]) -> typing.Union[MetaOapg.properties.first_close_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_contact_reply_at"]) -> typing.Union[MetaOapg.properties.first_contact_reply_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_admin_reply_at"]) -> typing.Union[MetaOapg.properties.last_admin_reply_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_assignment_admin_reply_at"]) -> typing.Union[MetaOapg.properties.last_assignment_admin_reply_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_assignment_at"]) -> typing.Union[MetaOapg.properties.last_assignment_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_close_at"]) -> typing.Union[MetaOapg.properties.last_close_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_closed_by_id"]) -> typing.Union[MetaOapg.properties.last_closed_by_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_contact_reply_at"]) -> typing.Union[MetaOapg.properties.last_contact_reply_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["median_time_to_reply"]) -> typing.Union[MetaOapg.properties.median_time_to_reply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_to_admin_reply"]) -> typing.Union[MetaOapg.properties.time_to_admin_reply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_to_assignment"]) -> typing.Union[MetaOapg.properties.time_to_assignment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_to_first_close"]) -> typing.Union[MetaOapg.properties.time_to_first_close, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_to_last_close"]) -> typing.Union[MetaOapg.properties.time_to_last_close, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count_assignments", "count_conversation_parts", "count_reopens", "first_admin_reply_at", "first_assignment_at", "first_close_at", "first_contact_reply_at", "last_admin_reply_at", "last_assignment_admin_reply_at", "last_assignment_at", "last_close_at", "last_closed_by_id", "last_contact_reply_at", "median_time_to_reply", "time_to_admin_reply", "time_to_assignment", "time_to_first_close", "time_to_last_close", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        count_assignments: typing.Union[MetaOapg.properties.count_assignments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        count_conversation_parts: typing.Union[MetaOapg.properties.count_conversation_parts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        count_reopens: typing.Union[MetaOapg.properties.count_reopens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        first_admin_reply_at: typing.Union[MetaOapg.properties.first_admin_reply_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        first_assignment_at: typing.Union[MetaOapg.properties.first_assignment_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        first_close_at: typing.Union[MetaOapg.properties.first_close_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        first_contact_reply_at: typing.Union[MetaOapg.properties.first_contact_reply_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_admin_reply_at: typing.Union[MetaOapg.properties.last_admin_reply_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_assignment_admin_reply_at: typing.Union[MetaOapg.properties.last_assignment_admin_reply_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_assignment_at: typing.Union[MetaOapg.properties.last_assignment_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_close_at: typing.Union[MetaOapg.properties.last_close_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_closed_by_id: typing.Union[MetaOapg.properties.last_closed_by_id, str, schemas.Unset] = schemas.unset,
        last_contact_reply_at: typing.Union[MetaOapg.properties.last_contact_reply_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        median_time_to_reply: typing.Union[MetaOapg.properties.median_time_to_reply, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        time_to_admin_reply: typing.Union[MetaOapg.properties.time_to_admin_reply, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        time_to_assignment: typing.Union[MetaOapg.properties.time_to_assignment, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        time_to_first_close: typing.Union[MetaOapg.properties.time_to_first_close, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        time_to_last_close: typing.Union[MetaOapg.properties.time_to_last_close, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConversationStatistics':
        return super().__new__(
            cls,
            *_args,
            count_assignments=count_assignments,
            count_conversation_parts=count_conversation_parts,
            count_reopens=count_reopens,
            first_admin_reply_at=first_admin_reply_at,
            first_assignment_at=first_assignment_at,
            first_close_at=first_close_at,
            first_contact_reply_at=first_contact_reply_at,
            last_admin_reply_at=last_admin_reply_at,
            last_assignment_admin_reply_at=last_assignment_admin_reply_at,
            last_assignment_at=last_assignment_at,
            last_close_at=last_close_at,
            last_closed_by_id=last_closed_by_id,
            last_contact_reply_at=last_contact_reply_at,
            median_time_to_reply=median_time_to_reply,
            time_to_admin_reply=time_to_admin_reply,
            time_to_assignment=time_to_assignment,
            time_to_first_close=time_to_first_close,
            time_to_last_close=time_to_last_close,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
