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


class UpdateTicketRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can update a Ticket
    """


    class MetaOapg:
        
        class properties:
            
            
            class assignment(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        admin_id = schemas.StrSchema
                        assignee_id = schemas.StrSchema
                        __annotations__ = {
                            "admin_id": admin_id,
                            "assignee_id": assignee_id,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["assignee_id"]) -> MetaOapg.properties.assignee_id: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["admin_id", "assignee_id", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["admin_id"]) -> typing.Union[MetaOapg.properties.admin_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["assignee_id"]) -> typing.Union[MetaOapg.properties.assignee_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["admin_id", "assignee_id", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    admin_id: typing.Union[MetaOapg.properties.admin_id, str, schemas.Unset] = schemas.unset,
                    assignee_id: typing.Union[MetaOapg.properties.assignee_id, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'assignment':
                    return super().__new__(
                        cls,
                        *_args,
                        admin_id=admin_id,
                        assignee_id=assignee_id,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "in_progress": "IN_PROGRESS",
                        "waiting_on_customer": "WAITING_ON_CUSTOMER",
                        "resolved": "RESOLVED",
                    }
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("in_progress")
                
                @schemas.classproperty
                def WAITING_ON_CUSTOMER(cls):
                    return cls("waiting_on_customer")
                
                @schemas.classproperty
                def RESOLVED(cls):
                    return cls("resolved")
            ticket_attributes = schemas.DictSchema
            __annotations__ = {
                "assignment": assignment,
                "state": state,
                "ticket_attributes": ticket_attributes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignment"]) -> MetaOapg.properties.assignment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_attributes"]) -> MetaOapg.properties.ticket_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assignment", "state", "ticket_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignment"]) -> typing.Union[MetaOapg.properties.assignment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_attributes"]) -> typing.Union[MetaOapg.properties.ticket_attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assignment", "state", "ticket_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assignment: typing.Union[MetaOapg.properties.assignment, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        ticket_attributes: typing.Union[MetaOapg.properties.ticket_attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateTicketRequest':
        return super().__new__(
            cls,
            *_args,
            assignment=assignment,
            state=state,
            ticket_attributes=ticket_attributes,
            _configuration=_configuration,
            **kwargs,
        )
