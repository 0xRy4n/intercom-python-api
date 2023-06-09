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


class CreateDataAttributeRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "data_type",
            "name",
            "model",
        }
        
        class properties:
            
            
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
                def DATETIME(cls):
                    return cls("datetime")
                
                @schemas.classproperty
                def DATE(cls):
                    return cls("date")
            
            
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
            description = schemas.StrSchema
            
            
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
            __annotations__ = {
                "data_type": data_type,
                "model": model,
                "name": name,
                "description": description,
                "options": options,
            }
    
    data_type: MetaOapg.properties.data_type
    name: MetaOapg.properties.name
    model: MetaOapg.properties.model
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data_type", "model", "name", "description", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_type"]) -> MetaOapg.properties.data_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data_type", "model", "name", "description", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        data_type: typing.Union[MetaOapg.properties.data_type, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDataAttributeRequest':
        return super().__new__(
            cls,
            *_args,
            data_type=data_type,
            name=name,
            model=model,
            description=description,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )
