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


class TicketTypeAttributeList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A list of attributes associated with a given ticket type.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            
            
            class ticket_type_attributes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TicketTypeAttribute']:
                        return TicketTypeAttribute
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TicketTypeAttribute'], typing.List['TicketTypeAttribute']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ticket_type_attributes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TicketTypeAttribute':
                    return super().__getitem__(i)
            __annotations__ = {
                "type": type,
                "ticket_type_attributes": ticket_type_attributes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_type_attributes"]) -> MetaOapg.properties.ticket_type_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "ticket_type_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_type_attributes"]) -> typing.Union[MetaOapg.properties.ticket_type_attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "ticket_type_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        ticket_type_attributes: typing.Union[MetaOapg.properties.ticket_type_attributes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TicketTypeAttributeList':
        return super().__new__(
            cls,
            *_args,
            type=type,
            ticket_type_attributes=ticket_type_attributes,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.ticket_type_attribute import TicketTypeAttribute
