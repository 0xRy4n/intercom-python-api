# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
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


class DataAttribute(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Data Attributes are metadata used to describe your contact, company and conversation models. These include standard and custom attributes. By using the data attributes endpoint, you can get the global list of attributes for your workspace, as well as create and archive custom attributes.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DATA_ATTRIBUTE(cls):
                    return cls("data_attribute")
            id = schemas.IntSchema
            
            
            class model(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONTACT(cls):
                    return cls("contact")
                
                @schemas.classproperty
                def COMPANY(cls):
                    return cls("company")
                
                @schemas.classproperty
                def CONVERSATION(cls):
                    return cls("conversation")
            name = schemas.StrSchema
            full_name = schemas.StrSchema
            label = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class data_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STRING(cls):
                    return cls("string")
                
                @schemas.classproperty
                def INTEGER(cls):
                    return cls("integer")
                
                @schemas.classproperty
                def FLOAT(cls):
                    return cls("float")
                
                @schemas.classproperty
                def BOOLEAN(cls):
                    return cls("boolean")
                
                @schemas.classproperty
                def DATE(cls):
                    return cls("date")
            
            
            class options(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'options':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            api_writable = schemas.BoolSchema
            ui_writable = schemas.BoolSchema
            custom = schemas.BoolSchema
            archived = schemas.BoolSchema
            created_at = schemas.IntSchema
            updated_at = schemas.IntSchema
            admin_id = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "id": id,
                "model": model,
                "name": name,
                "full_name": full_name,
                "label": label,
                "description": description,
                "data_type": data_type,
                "options": options,
                "api_writable": api_writable,
                "ui_writable": ui_writable,
                "custom": custom,
                "archived": archived,
                "created_at": created_at,
                "updated_at": updated_at,
                "admin_id": admin_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_writable"]) -> MetaOapg.properties.api_writable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ui_writable"]) -> MetaOapg.properties.ui_writable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> MetaOapg.properties.custom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["admin_id"]) -> MetaOapg.properties.admin_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "model", "name", "full_name", "label", "description", "data_type", "options", "api_writable", "ui_writable", "custom", "archived", "created_at", "updated_at", "admin_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> typing.Union[MetaOapg.properties.model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_name"]) -> typing.Union[MetaOapg.properties.full_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_type"]) -> typing.Union[MetaOapg.properties.data_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_writable"]) -> typing.Union[MetaOapg.properties.api_writable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ui_writable"]) -> typing.Union[MetaOapg.properties.ui_writable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union[MetaOapg.properties.custom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["admin_id"]) -> typing.Union[MetaOapg.properties.admin_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "model", "name", "full_name", "label", "description", "data_type", "options", "api_writable", "ui_writable", "custom", "archived", "created_at", "updated_at", "admin_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        model: typing.Union[MetaOapg.properties.model, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        full_name: typing.Union[MetaOapg.properties.full_name, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        data_type: typing.Union[MetaOapg.properties.data_type, str, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, list, tuple, schemas.Unset] = schemas.unset,
        api_writable: typing.Union[MetaOapg.properties.api_writable, bool, schemas.Unset] = schemas.unset,
        ui_writable: typing.Union[MetaOapg.properties.ui_writable, bool, schemas.Unset] = schemas.unset,
        custom: typing.Union[MetaOapg.properties.custom, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        admin_id: typing.Union[MetaOapg.properties.admin_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataAttribute':
        return super().__new__(
            cls,
            *_args,
            type=type,
            id=id,
            model=model,
            name=name,
            full_name=full_name,
            label=label,
            description=description,
            data_type=data_type,
            options=options,
            api_writable=api_writable,
            ui_writable=ui_writable,
            custom=custom,
            archived=archived,
            created_at=created_at,
            updated_at=updated_at,
            admin_id=admin_id,
            _configuration=_configuration,
            **kwargs,
        )
