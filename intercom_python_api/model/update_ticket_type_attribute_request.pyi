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


class UpdateTicketTypeAttributeRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can update a Ticket Type Attribute
    """


    class MetaOapg:
        
        class properties:
            allow_multiple_values = schemas.BoolSchema
            archived = schemas.BoolSchema
            description = schemas.StrSchema
            list_items = schemas.StrSchema
            multiline = schemas.BoolSchema
            name = schemas.StrSchema
            required_to_create = schemas.BoolSchema
            required_to_create_for_contacts = schemas.BoolSchema
            visible_on_create = schemas.BoolSchema
            visible_to_contacts = schemas.BoolSchema
            __annotations__ = {
                "allow_multiple_values": allow_multiple_values,
                "archived": archived,
                "description": description,
                "list_items": list_items,
                "multiline": multiline,
                "name": name,
                "required_to_create": required_to_create,
                "required_to_create_for_contacts": required_to_create_for_contacts,
                "visible_on_create": visible_on_create,
                "visible_to_contacts": visible_to_contacts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_multiple_values"]) -> MetaOapg.properties.allow_multiple_values: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_items"]) -> MetaOapg.properties.list_items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multiline"]) -> MetaOapg.properties.multiline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required_to_create"]) -> MetaOapg.properties.required_to_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required_to_create_for_contacts"]) -> MetaOapg.properties.required_to_create_for_contacts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visible_on_create"]) -> MetaOapg.properties.visible_on_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visible_to_contacts"]) -> MetaOapg.properties.visible_to_contacts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allow_multiple_values", "archived", "description", "list_items", "multiline", "name", "required_to_create", "required_to_create_for_contacts", "visible_on_create", "visible_to_contacts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_multiple_values"]) -> typing.Union[MetaOapg.properties.allow_multiple_values, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_items"]) -> typing.Union[MetaOapg.properties.list_items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multiline"]) -> typing.Union[MetaOapg.properties.multiline, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required_to_create"]) -> typing.Union[MetaOapg.properties.required_to_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required_to_create_for_contacts"]) -> typing.Union[MetaOapg.properties.required_to_create_for_contacts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visible_on_create"]) -> typing.Union[MetaOapg.properties.visible_on_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visible_to_contacts"]) -> typing.Union[MetaOapg.properties.visible_to_contacts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allow_multiple_values", "archived", "description", "list_items", "multiline", "name", "required_to_create", "required_to_create_for_contacts", "visible_on_create", "visible_to_contacts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        allow_multiple_values: typing.Union[MetaOapg.properties.allow_multiple_values, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        list_items: typing.Union[MetaOapg.properties.list_items, str, schemas.Unset] = schemas.unset,
        multiline: typing.Union[MetaOapg.properties.multiline, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        required_to_create: typing.Union[MetaOapg.properties.required_to_create, bool, schemas.Unset] = schemas.unset,
        required_to_create_for_contacts: typing.Union[MetaOapg.properties.required_to_create_for_contacts, bool, schemas.Unset] = schemas.unset,
        visible_on_create: typing.Union[MetaOapg.properties.visible_on_create, bool, schemas.Unset] = schemas.unset,
        visible_to_contacts: typing.Union[MetaOapg.properties.visible_to_contacts, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateTicketTypeAttributeRequest':
        return super().__new__(
            cls,
            *_args,
            allow_multiple_values=allow_multiple_values,
            archived=archived,
            description=description,
            list_items=list_items,
            multiline=multiline,
            name=name,
            required_to_create=required_to_create,
            required_to_create_for_contacts=required_to_create_for_contacts,
            visible_on_create=visible_on_create,
            visible_to_contacts=visible_to_contacts,
            _configuration=_configuration,
            **kwargs,
        )
