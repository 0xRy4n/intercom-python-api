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


class Ticket(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Tickets are how you track requests from your users.
    """


    class MetaOapg:
        
        class properties:
            admin_assignee_id = schemas.StrSchema
        
            @staticmethod
            def contacts() -> typing.Type['TicketContacts']:
                return TicketContacts
            created_at = schemas.IntSchema
            id = schemas.StrSchema
            team_assignee_id = schemas.StrSchema
        
            @staticmethod
            def ticket_attributes() -> typing.Type['TicketCustomAttributes']:
                return TicketCustomAttributes
        
            @staticmethod
            def ticket_parts() -> typing.Type['TicketParts']:
                return TicketParts
            
            
            class ticket_state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "submitted": "SUBMITTED",
                        "in_progress": "IN_PROGRESS",
                        "waiting_on_customer": "WAITING_ON_CUSTOMER",
                        "resolved": "RESOLVED",
                    }
                
                @schemas.classproperty
                def SUBMITTED(cls):
                    return cls("submitted")
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("in_progress")
                
                @schemas.classproperty
                def WAITING_ON_CUSTOMER(cls):
                    return cls("waiting_on_customer")
                
                @schemas.classproperty
                def RESOLVED(cls):
                    return cls("resolved")
        
            @staticmethod
            def ticket_type() -> typing.Type['TicketType']:
                return TicketType
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ticket": "TICKET",
                    }
                
                @schemas.classproperty
                def TICKET(cls):
                    return cls("ticket")
            updated_at = schemas.IntSchema
            __annotations__ = {
                "admin_assignee_id": admin_assignee_id,
                "contacts": contacts,
                "created_at": created_at,
                "id": id,
                "team_assignee_id": team_assignee_id,
                "ticket_attributes": ticket_attributes,
                "ticket_parts": ticket_parts,
                "ticket_state": ticket_state,
                "ticket_type": ticket_type,
                "type": type,
                "updated_at": updated_at,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_assignee_id"]) -> MetaOapg.properties.admin_assignee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contacts"]) -> 'TicketContacts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_assignee_id"]) -> MetaOapg.properties.team_assignee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_attributes"]) -> 'TicketCustomAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_parts"]) -> 'TicketParts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_state"]) -> MetaOapg.properties.ticket_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_type"]) -> 'TicketType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["admin_assignee_id", "contacts", "created_at", "id", "team_assignee_id", "ticket_attributes", "ticket_parts", "ticket_state", "ticket_type", "type", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_assignee_id"]) -> typing.Union[MetaOapg.properties.admin_assignee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contacts"]) -> typing.Union['TicketContacts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_assignee_id"]) -> typing.Union[MetaOapg.properties.team_assignee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_attributes"]) -> typing.Union['TicketCustomAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_parts"]) -> typing.Union['TicketParts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_state"]) -> typing.Union[MetaOapg.properties.ticket_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_type"]) -> typing.Union['TicketType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["admin_assignee_id", "contacts", "created_at", "id", "team_assignee_id", "ticket_attributes", "ticket_parts", "ticket_state", "ticket_type", "type", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        admin_assignee_id: typing.Union[MetaOapg.properties.admin_assignee_id, str, schemas.Unset] = schemas.unset,
        contacts: typing.Union['TicketContacts', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        team_assignee_id: typing.Union[MetaOapg.properties.team_assignee_id, str, schemas.Unset] = schemas.unset,
        ticket_attributes: typing.Union['TicketCustomAttributes', schemas.Unset] = schemas.unset,
        ticket_parts: typing.Union['TicketParts', schemas.Unset] = schemas.unset,
        ticket_state: typing.Union[MetaOapg.properties.ticket_state, str, schemas.Unset] = schemas.unset,
        ticket_type: typing.Union['TicketType', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Ticket':
        return super().__new__(
            cls,
            *_args,
            admin_assignee_id=admin_assignee_id,
            contacts=contacts,
            created_at=created_at,
            id=id,
            team_assignee_id=team_assignee_id,
            ticket_attributes=ticket_attributes,
            ticket_parts=ticket_parts,
            ticket_state=ticket_state,
            ticket_type=ticket_type,
            type=type,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.ticket_contacts import TicketContacts
from intercom_python_api.model.ticket_custom_attributes import TicketCustomAttributes
from intercom_python_api.model.ticket_parts import TicketParts
from intercom_python_api.model.ticket_type import TicketType
