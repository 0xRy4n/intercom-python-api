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


class CreateSectionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can create a Section
    """


    class MetaOapg:
        required = {
            "parent_id",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            parent_id = schemas.IntSchema
        
            @staticmethod
            def translated_content() -> typing.Type['GroupTranslatedContent']:
                return GroupTranslatedContent
            __annotations__ = {
                "name": name,
                "parent_id": parent_id,
                "translated_content": translated_content,
            }
    
    parent_id: MetaOapg.properties.parent_id
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translated_content"]) -> 'GroupTranslatedContent': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "parent_id", "translated_content", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translated_content"]) -> typing.Union['GroupTranslatedContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "parent_id", "translated_content", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        parent_id: typing.Union[MetaOapg.properties.parent_id, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        translated_content: typing.Union['GroupTranslatedContent', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateSectionRequest':
        return super().__new__(
            cls,
            *_args,
            parent_id=parent_id,
            name=name,
            translated_content=translated_content,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.group_translated_content import GroupTranslatedContent
