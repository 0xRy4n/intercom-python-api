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


class Article(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Articles API is a central place to gather all information and take actions on your articles. Articles can live within collections and sections, or alternatively they can stand alone.
    """


    class MetaOapg:
        
        class properties:
            author_id = schemas.IntSchema
            
            
            class body(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'body':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            created_at = schemas.IntSchema
            default_locale = schemas.StrSchema
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            id = schemas.StrSchema
            
            
            class parent_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'parent_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class parent_type(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'parent_type':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
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
        
            @staticmethod
            def statistics() -> typing.Type['ArticleStatistics']:
                return ArticleStatistics
            title = schemas.StrSchema
        
            @staticmethod
            def translated_content() -> typing.Type['ArticleTranslatedContent']:
                return ArticleTranslatedContent
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ARTICLE(cls):
                    return cls("article")
            updated_at = schemas.IntSchema
            
            
            class url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'url':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            workspace_id = schemas.StrSchema
            __annotations__ = {
                "author_id": author_id,
                "body": body,
                "created_at": created_at,
                "default_locale": default_locale,
                "description": description,
                "id": id,
                "parent_id": parent_id,
                "parent_type": parent_type,
                "state": state,
                "statistics": statistics,
                "title": title,
                "translated_content": translated_content,
                "type": type,
                "updated_at": updated_at,
                "url": url,
                "workspace_id": workspace_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_id"]) -> MetaOapg.properties.author_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_locale"]) -> MetaOapg.properties.default_locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_type"]) -> MetaOapg.properties.parent_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statistics"]) -> 'ArticleStatistics': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translated_content"]) -> 'ArticleTranslatedContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_id"]) -> MetaOapg.properties.workspace_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["author_id", "body", "created_at", "default_locale", "description", "id", "parent_id", "parent_type", "state", "statistics", "title", "translated_content", "type", "updated_at", "url", "workspace_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_id"]) -> typing.Union[MetaOapg.properties.author_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_locale"]) -> typing.Union[MetaOapg.properties.default_locale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> typing.Union[MetaOapg.properties.parent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_type"]) -> typing.Union[MetaOapg.properties.parent_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statistics"]) -> typing.Union['ArticleStatistics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translated_content"]) -> typing.Union['ArticleTranslatedContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_id"]) -> typing.Union[MetaOapg.properties.workspace_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["author_id", "body", "created_at", "default_locale", "description", "id", "parent_id", "parent_type", "state", "statistics", "title", "translated_content", "type", "updated_at", "url", "workspace_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        author_id: typing.Union[MetaOapg.properties.author_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, None, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        default_locale: typing.Union[MetaOapg.properties.default_locale, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        parent_id: typing.Union[MetaOapg.properties.parent_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        parent_type: typing.Union[MetaOapg.properties.parent_type, None, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        statistics: typing.Union['ArticleStatistics', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        translated_content: typing.Union['ArticleTranslatedContent', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, None, str, schemas.Unset] = schemas.unset,
        workspace_id: typing.Union[MetaOapg.properties.workspace_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Article':
        return super().__new__(
            cls,
            *_args,
            author_id=author_id,
            body=body,
            created_at=created_at,
            default_locale=default_locale,
            description=description,
            id=id,
            parent_id=parent_id,
            parent_type=parent_type,
            state=state,
            statistics=statistics,
            title=title,
            translated_content=translated_content,
            type=type,
            updated_at=updated_at,
            url=url,
            workspace_id=workspace_id,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.article_statistics import ArticleStatistics
from intercom_python_api.model.article_translated_content import ArticleTranslatedContent
