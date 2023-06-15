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


class CreateTicketRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can create a Ticket
    """


    class MetaOapg:
        required = {
            "ticket_type_id",
            "contacts",
        }
        
        class properties:
            
            
            class contacts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedBase,
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class one_of_0(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "id",
                                    }
                                    
                                    class properties:
                                        id = schemas.StrSchema
                                        __annotations__ = {
                                            "id": id,
                                        }
                            
                                
                                id: MetaOapg.properties.id
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    id: typing.Union[MetaOapg.properties.id, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'one_of_0':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        id=id,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class one_of_1(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "external_id",
                                    }
                                    
                                    class properties:
                                        external_id = schemas.StrSchema
                                        __annotations__ = {
                                            "external_id": external_id,
                                        }
                            
                                
                                external_id: MetaOapg.properties.external_id
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["external_id", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["external_id", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    external_id: typing.Union[MetaOapg.properties.external_id, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'one_of_1':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        external_id=external_id,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class one_of_2(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "email",
                                    }
                                    
                                    class properties:
                                        email = schemas.StrSchema
                                        __annotations__ = {
                                            "email": email,
                                        }
                            
                                
                                email: MetaOapg.properties.email
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    email: typing.Union[MetaOapg.properties.email, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'one_of_2':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        email=email,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            @classmethod
                            @functools.lru_cache()
                            def one_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.one_of_0,
                                    cls.one_of_1,
                                    cls.one_of_2,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contacts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            ticket_type_id = schemas.StrSchema
        
            @staticmethod
            def ticket_attributes() -> typing.Type['TicketRequestCustomAttributes']:
                return TicketRequestCustomAttributes
            __annotations__ = {
                "contacts": contacts,
                "ticket_type_id": ticket_type_id,
                "ticket_attributes": ticket_attributes,
            }
    
    ticket_type_id: MetaOapg.properties.ticket_type_id
    contacts: MetaOapg.properties.contacts
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contacts"]) -> MetaOapg.properties.contacts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_type_id"]) -> MetaOapg.properties.ticket_type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ticket_attributes"]) -> 'TicketRequestCustomAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contacts", "ticket_type_id", "ticket_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contacts"]) -> MetaOapg.properties.contacts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_type_id"]) -> MetaOapg.properties.ticket_type_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ticket_attributes"]) -> typing.Union['TicketRequestCustomAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contacts", "ticket_type_id", "ticket_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ticket_type_id: typing.Union[MetaOapg.properties.ticket_type_id, str, ],
        contacts: typing.Union[MetaOapg.properties.contacts, list, tuple, ],
        ticket_attributes: typing.Union['TicketRequestCustomAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTicketRequest':
        return super().__new__(
            cls,
            *_args,
            ticket_type_id=ticket_type_id,
            contacts=contacts,
            ticket_attributes=ticket_attributes,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.ticket_request_custom_attributes import TicketRequestCustomAttributes
