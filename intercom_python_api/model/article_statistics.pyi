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


class ArticleStatistics(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The statistics of an article.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ARTICLE_STATISTICS(cls):
                    return cls("article_statistics")
            views = schemas.IntSchema
            conversions = schemas.IntSchema
            reactions = schemas.IntSchema
            happy_reaction_precentage = schemas.IntSchema
            netural_reaction_precentage = schemas.IntSchema
            sad_reaction_precentage = schemas.IntSchema
            __annotations__ = {
                "type": type,
                "views": views,
                "conversions": conversions,
                "reactions": reactions,
                "happy_reaction_precentage": happy_reaction_precentage,
                "netural_reaction_precentage": netural_reaction_precentage,
                "sad_reaction_precentage": sad_reaction_precentage,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["views"]) -> MetaOapg.properties.views: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversions"]) -> MetaOapg.properties.conversions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactions"]) -> MetaOapg.properties.reactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["happy_reaction_precentage"]) -> MetaOapg.properties.happy_reaction_precentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netural_reaction_precentage"]) -> MetaOapg.properties.netural_reaction_precentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sad_reaction_precentage"]) -> MetaOapg.properties.sad_reaction_precentage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "views", "conversions", "reactions", "happy_reaction_precentage", "netural_reaction_precentage", "sad_reaction_precentage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["views"]) -> typing.Union[MetaOapg.properties.views, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversions"]) -> typing.Union[MetaOapg.properties.conversions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactions"]) -> typing.Union[MetaOapg.properties.reactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["happy_reaction_precentage"]) -> typing.Union[MetaOapg.properties.happy_reaction_precentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netural_reaction_precentage"]) -> typing.Union[MetaOapg.properties.netural_reaction_precentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sad_reaction_precentage"]) -> typing.Union[MetaOapg.properties.sad_reaction_precentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "views", "conversions", "reactions", "happy_reaction_precentage", "netural_reaction_precentage", "sad_reaction_precentage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        views: typing.Union[MetaOapg.properties.views, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        conversions: typing.Union[MetaOapg.properties.conversions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reactions: typing.Union[MetaOapg.properties.reactions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        happy_reaction_precentage: typing.Union[MetaOapg.properties.happy_reaction_precentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        netural_reaction_precentage: typing.Union[MetaOapg.properties.netural_reaction_precentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sad_reaction_precentage: typing.Union[MetaOapg.properties.sad_reaction_precentage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArticleStatistics':
        return super().__new__(
            cls,
            *_args,
            type=type,
            views=views,
            conversions=conversions,
            reactions=reactions,
            happy_reaction_precentage=happy_reaction_precentage,
            netural_reaction_precentage=netural_reaction_precentage,
            sad_reaction_precentage=sad_reaction_precentage,
            _configuration=_configuration,
            **kwargs,
        )
