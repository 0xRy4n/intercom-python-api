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


class CreateArticleRequest(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can create an Article
    """


    class MetaOapg:
        required = {
            "author_id",
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            author_id = schemas.IntSchema
            description = schemas.StrSchema
            body = schemas.StrSchema
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PUBLISHED(cls):
                    return cls("published")
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
            parent_id = schemas.IntSchema
            parent_type = schemas.StrSchema
        
            @staticmethod
            def translated_content() -> typing.Type['ArticleTranslatedContent']:
                return ArticleTranslatedContent
            __annotations__ = {
                "title": title,
                "author_id": author_id,
                "description": description,
                "body": body,
                "state": state,
                "parent_id": parent_id,
                "parent_type": parent_type,
                "translated_content": translated_content,
            }

    
    author_id: MetaOapg.properties.author_id
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_type"]) -> MetaOapg.properties.parent_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translated_content"]) -> 'ArticleTranslatedContent': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "author_id", "description", "body", "state", "parent_id", "parent_type", "translated_content", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> typing.Union[MetaOapg.properties.parent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_type"]) -> typing.Union[MetaOapg.properties.parent_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translated_content"]) -> typing.Union['ArticleTranslatedContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "author_id", "description", "body", "state", "parent_id", "parent_type", "translated_content", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        parent_id: typing.Union[MetaOapg.properties.parent_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        parent_type: typing.Union[MetaOapg.properties.parent_type, str, schemas.Unset] = schemas.unset,
        translated_content: typing.Union['ArticleTranslatedContent', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateArticleRequest':
        return super().__new__(
            cls,
            *_args,
            description=description,
            body=body,
            state=state,
            parent_id=parent_id,
            parent_type=parent_type,
            translated_content=translated_content,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.article_translated_content import ArticleTranslatedContent
