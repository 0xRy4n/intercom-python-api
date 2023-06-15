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


class Conversation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Conversations are how you can communicate with users in Intercom. They are created when a contact replies to an outbound message, or when one admin directly sends a message to a single contact.
    """


    class MetaOapg:
        
        class properties:
            
            
            class admin_assignee_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'admin_assignee_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def contacts() -> typing.Type['ConversationContacts']:
                return ConversationContacts
        
            @staticmethod
            def conversation_parts() -> typing.Type['ConversationParts']:
                return ConversationParts
        
            @staticmethod
            def conversation_rating() -> typing.Type['ConversationRating']:
                return ConversationRating
            created_at = schemas.IntSchema
        
            @staticmethod
            def custom_attributes() -> typing.Type['CustomAttributes']:
                return CustomAttributes
        
            @staticmethod
            def first_contact_reply() -> typing.Type['ConversationFirstContactReply']:
                return ConversationFirstContactReply
            id = schemas.StrSchema
            open = schemas.BoolSchema
            
            
            class priority(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PRIORITY(cls):
                    return cls("priority")
                
                @schemas.classproperty
                def NOT_PRIORITY(cls):
                    return cls("not_priority")
            read = schemas.BoolSchema
        
            @staticmethod
            def sla_applied() -> typing.Type['SlaApplied']:
                return SlaApplied
            
            
            class snoozed_until(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'snoozed_until':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def source() -> typing.Type['ConversationSource']:
                return ConversationSource
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("closed")
                
                @schemas.classproperty
                def SNOOZED(cls):
                    return cls("snoozed")
        
            @staticmethod
            def statistics() -> typing.Type['ConversationStatistics']:
                return ConversationStatistics
        
            @staticmethod
            def tags() -> typing.Type['Tags']:
                return Tags
            
            
            class team_assignee_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'team_assignee_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def teammates() -> typing.Type['ConversationTeammates']:
                return ConversationTeammates
            
            
            class title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'title':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            type = schemas.StrSchema
            updated_at = schemas.IntSchema
            
            
            class waiting_since(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'waiting_since':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "admin_assignee_id": admin_assignee_id,
                "contacts": contacts,
                "conversation_parts": conversation_parts,
                "conversation_rating": conversation_rating,
                "created_at": created_at,
                "custom_attributes": custom_attributes,
                "first_contact_reply": first_contact_reply,
                "id": id,
                "open": open,
                "priority": priority,
                "read": read,
                "sla_applied": sla_applied,
                "snoozed_until": snoozed_until,
                "source": source,
                "state": state,
                "statistics": statistics,
                "tags": tags,
                "team_assignee_id": team_assignee_id,
                "teammates": teammates,
                "title": title,
                "type": type,
                "updated_at": updated_at,
                "waiting_since": waiting_since,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_assignee_id"]) -> MetaOapg.properties.admin_assignee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contacts"]) -> 'ConversationContacts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_parts"]) -> 'ConversationParts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_rating"]) -> 'ConversationRating': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_attributes"]) -> 'CustomAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_contact_reply"]) -> 'ConversationFirstContactReply': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["open"]) -> MetaOapg.properties.open: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read"]) -> MetaOapg.properties.read: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sla_applied"]) -> 'SlaApplied': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snoozed_until"]) -> MetaOapg.properties.snoozed_until: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'ConversationSource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statistics"]) -> 'ConversationStatistics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'Tags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_assignee_id"]) -> MetaOapg.properties.team_assignee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teammates"]) -> 'ConversationTeammates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waiting_since"]) -> MetaOapg.properties.waiting_since: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["admin_assignee_id", "contacts", "conversation_parts", "conversation_rating", "created_at", "custom_attributes", "first_contact_reply", "id", "open", "priority", "read", "sla_applied", "snoozed_until", "source", "state", "statistics", "tags", "team_assignee_id", "teammates", "title", "type", "updated_at", "waiting_since", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_assignee_id"]) -> typing.Union[MetaOapg.properties.admin_assignee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contacts"]) -> typing.Union['ConversationContacts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_parts"]) -> typing.Union['ConversationParts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_rating"]) -> typing.Union['ConversationRating', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_attributes"]) -> typing.Union['CustomAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_contact_reply"]) -> typing.Union['ConversationFirstContactReply', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["open"]) -> typing.Union[MetaOapg.properties.open, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read"]) -> typing.Union[MetaOapg.properties.read, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sla_applied"]) -> typing.Union['SlaApplied', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snoozed_until"]) -> typing.Union[MetaOapg.properties.snoozed_until, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union['ConversationSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statistics"]) -> typing.Union['ConversationStatistics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['Tags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_assignee_id"]) -> typing.Union[MetaOapg.properties.team_assignee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teammates"]) -> typing.Union['ConversationTeammates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waiting_since"]) -> typing.Union[MetaOapg.properties.waiting_since, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["admin_assignee_id", "contacts", "conversation_parts", "conversation_rating", "created_at", "custom_attributes", "first_contact_reply", "id", "open", "priority", "read", "sla_applied", "snoozed_until", "source", "state", "statistics", "tags", "team_assignee_id", "teammates", "title", "type", "updated_at", "waiting_since", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        admin_assignee_id: typing.Union[MetaOapg.properties.admin_assignee_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contacts: typing.Union['ConversationContacts', schemas.Unset] = schemas.unset,
        conversation_parts: typing.Union['ConversationParts', schemas.Unset] = schemas.unset,
        conversation_rating: typing.Union['ConversationRating', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        custom_attributes: typing.Union['CustomAttributes', schemas.Unset] = schemas.unset,
        first_contact_reply: typing.Union['ConversationFirstContactReply', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        open: typing.Union[MetaOapg.properties.open, bool, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, str, schemas.Unset] = schemas.unset,
        read: typing.Union[MetaOapg.properties.read, bool, schemas.Unset] = schemas.unset,
        sla_applied: typing.Union['SlaApplied', schemas.Unset] = schemas.unset,
        snoozed_until: typing.Union[MetaOapg.properties.snoozed_until, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        source: typing.Union['ConversationSource', schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        statistics: typing.Union['ConversationStatistics', schemas.Unset] = schemas.unset,
        tags: typing.Union['Tags', schemas.Unset] = schemas.unset,
        team_assignee_id: typing.Union[MetaOapg.properties.team_assignee_id, None, str, schemas.Unset] = schemas.unset,
        teammates: typing.Union['ConversationTeammates', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, None, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        waiting_since: typing.Union[MetaOapg.properties.waiting_since, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Conversation':
        return super().__new__(
            cls,
            *_args,
            admin_assignee_id=admin_assignee_id,
            contacts=contacts,
            conversation_parts=conversation_parts,
            conversation_rating=conversation_rating,
            created_at=created_at,
            custom_attributes=custom_attributes,
            first_contact_reply=first_contact_reply,
            id=id,
            open=open,
            priority=priority,
            read=read,
            sla_applied=sla_applied,
            snoozed_until=snoozed_until,
            source=source,
            state=state,
            statistics=statistics,
            tags=tags,
            team_assignee_id=team_assignee_id,
            teammates=teammates,
            title=title,
            type=type,
            updated_at=updated_at,
            waiting_since=waiting_since,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.conversation_contacts import ConversationContacts
from intercom_python_api.model.conversation_first_contact_reply import ConversationFirstContactReply
from intercom_python_api.model.conversation_parts import ConversationParts
from intercom_python_api.model.conversation_rating import ConversationRating
from intercom_python_api.model.conversation_source import ConversationSource
from intercom_python_api.model.conversation_statistics import ConversationStatistics
from intercom_python_api.model.conversation_teammates import ConversationTeammates
from intercom_python_api.model.custom_attributes import CustomAttributes
from intercom_python_api.model.sla_applied import SlaApplied
from intercom_python_api.model.tags import Tags
