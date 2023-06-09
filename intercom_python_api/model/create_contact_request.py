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


class CreateContactRequest(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Payload to create a contact
    """


    class MetaOapg:
        
        class properties:
            
            
            class avatar(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'avatar':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class custom_attributes(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'custom_attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            email = schemas.StrSchema
            external_id = schemas.StrSchema
            
            
            class last_seen_at(
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
                ) -> 'last_seen_at':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class owner_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'owner_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class phone(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phone':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            role = schemas.StrSchema
            
            
            class signed_up_at(
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
                ) -> 'signed_up_at':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class unsubscribed_from_emails(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unsubscribed_from_emails':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "avatar": avatar,
                "custom_attributes": custom_attributes,
                "email": email,
                "external_id": external_id,
                "last_seen_at": last_seen_at,
                "name": name,
                "owner_id": owner_id,
                "phone": phone,
                "role": role,
                "signed_up_at": signed_up_at,
                "unsubscribed_from_emails": unsubscribed_from_emails,
            }
        
        
        class any_of_0(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "email",
                }
        
            
            email: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "external_id",
                }
        
            
            external_id: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_2(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "role",
                }
        
            
            role: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_2':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def any_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.any_of_0,
                cls.any_of_1,
                cls.any_of_2,
            ]

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_attributes"]) -> MetaOapg.properties.custom_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signed_up_at"]) -> MetaOapg.properties.signed_up_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribed_from_emails"]) -> MetaOapg.properties.unsubscribed_from_emails: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["avatar", "custom_attributes", "email", "external_id", "last_seen_at", "name", "owner_id", "phone", "role", "signed_up_at", "unsubscribed_from_emails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> typing.Union[MetaOapg.properties.avatar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_attributes"]) -> typing.Union[MetaOapg.properties.custom_attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_seen_at"]) -> typing.Union[MetaOapg.properties.last_seen_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_id"]) -> typing.Union[MetaOapg.properties.owner_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signed_up_at"]) -> typing.Union[MetaOapg.properties.signed_up_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribed_from_emails"]) -> typing.Union[MetaOapg.properties.unsubscribed_from_emails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avatar", "custom_attributes", "email", "external_id", "last_seen_at", "name", "owner_id", "phone", "role", "signed_up_at", "unsubscribed_from_emails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        avatar: typing.Union[MetaOapg.properties.avatar, None, str, schemas.Unset] = schemas.unset,
        custom_attributes: typing.Union[MetaOapg.properties.custom_attributes, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, str, schemas.Unset] = schemas.unset,
        last_seen_at: typing.Union[MetaOapg.properties.last_seen_at, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        owner_id: typing.Union[MetaOapg.properties.owner_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        signed_up_at: typing.Union[MetaOapg.properties.signed_up_at, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        unsubscribed_from_emails: typing.Union[MetaOapg.properties.unsubscribed_from_emails, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateContactRequest':
        return super().__new__(
            cls,
            *_args,
            avatar=avatar,
            custom_attributes=custom_attributes,
            email=email,
            external_id=external_id,
            last_seen_at=last_seen_at,
            name=name,
            owner_id=owner_id,
            phone=phone,
            role=role,
            signed_up_at=signed_up_at,
            unsubscribed_from_emails=unsubscribed_from_emails,
            _configuration=_configuration,
            **kwargs,
        )
