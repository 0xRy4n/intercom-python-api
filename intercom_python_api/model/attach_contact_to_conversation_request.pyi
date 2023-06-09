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


class AttachContactToConversationRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Payload of the request to assign a conversation
    """


    class MetaOapg:
        
        class properties:
            admin_id = schemas.StrSchema
            
            
            class customer(
                schemas.ComposedBase,
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "intercom_user_id",
                            }
                            
                            class properties:
                            
                                @staticmethod
                                def customer() -> typing.Type['CustomerRequest']:
                                    return CustomerRequest
                                intercom_user_id = schemas.StrSchema
                                __annotations__ = {
                                    "customer": customer,
                                    "intercom_user_id": intercom_user_id,
                                }
                    
                        
                        intercom_user_id: MetaOapg.properties.intercom_user_id
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'CustomerRequest': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["intercom_user_id"]) -> MetaOapg.properties.intercom_user_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer", "intercom_user_id", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['CustomerRequest', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["intercom_user_id"]) -> MetaOapg.properties.intercom_user_id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer", "intercom_user_id", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            intercom_user_id: typing.Union[MetaOapg.properties.intercom_user_id, str, ],
                            customer: typing.Union['CustomerRequest', schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                *_args,
                                intercom_user_id=intercom_user_id,
                                customer=customer,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class one_of_1(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "user_id",
                            }
                            
                            class properties:
                            
                                @staticmethod
                                def customer() -> typing.Type['CustomerRequest']:
                                    return CustomerRequest
                                user_id = schemas.StrSchema
                                __annotations__ = {
                                    "customer": customer,
                                    "user_id": user_id,
                                }
                    
                        
                        user_id: MetaOapg.properties.user_id
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'CustomerRequest': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer", "user_id", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['CustomerRequest', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer", "user_id", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            user_id: typing.Union[MetaOapg.properties.user_id, str, ],
                            customer: typing.Union['CustomerRequest', schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'one_of_1':
                            return super().__new__(
                                cls,
                                *_args,
                                user_id=user_id,
                                customer=customer,
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
                            
                                @staticmethod
                                def customer() -> typing.Type['CustomerRequest']:
                                    return CustomerRequest
                                email = schemas.StrSchema
                                __annotations__ = {
                                    "customer": customer,
                                    "email": email,
                                }
                    
                        
                        email: MetaOapg.properties.email
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'CustomerRequest': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer", "email", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['CustomerRequest', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer", "email", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            email: typing.Union[MetaOapg.properties.email, str, ],
                            customer: typing.Union['CustomerRequest', schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'one_of_2':
                            return super().__new__(
                                cls,
                                *_args,
                                email=email,
                                customer=customer,
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
                ) -> 'customer':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "admin_id": admin_id,
                "customer": customer,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> MetaOapg.properties.customer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["admin_id", "customer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_id"]) -> typing.Union[MetaOapg.properties.admin_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union[MetaOapg.properties.customer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["admin_id", "customer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        admin_id: typing.Union[MetaOapg.properties.admin_id, str, schemas.Unset] = schemas.unset,
        customer: typing.Union[MetaOapg.properties.customer, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttachContactToConversationRequest':
        return super().__new__(
            cls,
            *_args,
            admin_id=admin_id,
            customer=customer,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.customer_request import CustomerRequest
