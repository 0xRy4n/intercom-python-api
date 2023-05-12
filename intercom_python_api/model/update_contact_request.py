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


class UpdateContactRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can update a contact
    """


    class MetaOapg:
        
        class properties:
            role = schemas.StrSchema
            external_id = schemas.StrSchema
            email = schemas.StrSchema
            
            
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
            __annotations__ = {
                "role": role,
                "external_id": external_id,
                "email": email,
                "phone": phone,
                "name": name,
                "avatar": avatar,
                "signed_up_at": signed_up_at,
                "last_seen_at": last_seen_at,
                "owner_id": owner_id,
                "unsubscribed_from_emails": unsubscribed_from_emails,
                "custom_attributes": custom_attributes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signed_up_at"]) -> MetaOapg.properties.signed_up_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_seen_at"]) -> MetaOapg.properties.last_seen_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribed_from_emails"]) -> MetaOapg.properties.unsubscribed_from_emails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_attributes"]) -> MetaOapg.properties.custom_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["role", "external_id", "email", "phone", "name", "avatar", "signed_up_at", "last_seen_at", "owner_id", "unsubscribed_from_emails", "custom_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> typing.Union[MetaOapg.properties.avatar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signed_up_at"]) -> typing.Union[MetaOapg.properties.signed_up_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_seen_at"]) -> typing.Union[MetaOapg.properties.last_seen_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_id"]) -> typing.Union[MetaOapg.properties.owner_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribed_from_emails"]) -> typing.Union[MetaOapg.properties.unsubscribed_from_emails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_attributes"]) -> typing.Union[MetaOapg.properties.custom_attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["role", "external_id", "email", "phone", "name", "avatar", "signed_up_at", "last_seen_at", "owner_id", "unsubscribed_from_emails", "custom_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        avatar: typing.Union[MetaOapg.properties.avatar, None, str, schemas.Unset] = schemas.unset,
        signed_up_at: typing.Union[MetaOapg.properties.signed_up_at, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_seen_at: typing.Union[MetaOapg.properties.last_seen_at, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        owner_id: typing.Union[MetaOapg.properties.owner_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        unsubscribed_from_emails: typing.Union[MetaOapg.properties.unsubscribed_from_emails, None, bool, schemas.Unset] = schemas.unset,
        custom_attributes: typing.Union[MetaOapg.properties.custom_attributes, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateContactRequest':
        return super().__new__(
            cls,
            *_args,
            role=role,
            external_id=external_id,
            email=email,
            phone=phone,
            name=name,
            avatar=avatar,
            signed_up_at=signed_up_at,
            last_seen_at=last_seen_at,
            owner_id=owner_id,
            unsubscribed_from_emails=unsubscribed_from_emails,
            custom_attributes=custom_attributes,
            _configuration=_configuration,
            **kwargs,
        )
