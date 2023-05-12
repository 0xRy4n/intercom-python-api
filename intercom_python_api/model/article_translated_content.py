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


class ArticleTranslatedContent(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Translated Content of an Article. The keys are the locale codes and the values are the translated content of the article.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        schemas.NoneClass.NONE: "NONE",
                        "article_translated_content": "ARTICLE_TRANSLATED_CONTENT",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
                
                @schemas.classproperty
                def ARTICLE_TRANSLATED_CONTENT(cls):
                    return cls("article_translated_content")
        
            @staticmethod
            def ar() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def bg() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def bs() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def ca() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def cs() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def da() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def de() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def el() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def en() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def es() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def et() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def fi() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def fr() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def he() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def hr() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def hu() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def id() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def it() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def ja() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def ko() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def lt() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def lv() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def mn() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def nb() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def nl() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def pl() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def pt() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def ro() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def ru() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def sl() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def sr() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def sv() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def tr() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def vi() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def pt_br() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def zh_cn() -> typing.Type['ArticleContent']:
                return ArticleContent
        
            @staticmethod
            def zh_tw() -> typing.Type['ArticleContent']:
                return ArticleContent
            __annotations__ = {
                "type": type,
                "ar": ar,
                "bg": bg,
                "bs": bs,
                "ca": ca,
                "cs": cs,
                "da": da,
                "de": de,
                "el": el,
                "en": en,
                "es": es,
                "et": et,
                "fi": fi,
                "fr": fr,
                "he": he,
                "hr": hr,
                "hu": hu,
                "id": id,
                "it": it,
                "ja": ja,
                "ko": ko,
                "lt": lt,
                "lv": lv,
                "mn": mn,
                "nb": nb,
                "nl": nl,
                "pl": pl,
                "pt": pt,
                "ro": ro,
                "ru": ru,
                "sl": sl,
                "sr": sr,
                "sv": sv,
                "tr": tr,
                "vi": vi,
                "pt-BR": pt_br,
                "zh-CN": zh_cn,
                "zh-TW": zh_tw,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ar"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bg"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bs"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ca"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cs"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["da"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["de"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["el"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["en"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["et"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fi"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fr"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["he"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hr"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hu"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["it"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ja"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ko"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lt"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lv"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mn"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nb"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nl"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pl"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pt"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ro"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ru"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sl"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sr"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sv"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tr"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vi"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pt-BR"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zh-CN"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zh-TW"]) -> 'ArticleContent': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "ar", "bg", "bs", "ca", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "he", "hr", "hu", "id", "it", "ja", "ko", "lt", "lv", "mn", "nb", "nl", "pl", "pt", "ro", "ru", "sl", "sr", "sv", "tr", "vi", "pt-BR", "zh-CN", "zh-TW", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ar"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bg"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bs"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ca"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cs"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["da"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["de"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["el"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["en"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["et"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fi"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fr"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["he"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hr"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hu"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["it"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ja"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ko"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lt"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lv"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mn"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nb"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nl"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pl"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pt"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ro"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ru"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sl"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sr"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sv"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tr"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vi"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pt-BR"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zh-CN"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zh-TW"]) -> typing.Union['ArticleContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "ar", "bg", "bs", "ca", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "he", "hr", "hu", "id", "it", "ja", "ko", "lt", "lv", "mn", "nb", "nl", "pl", "pt", "ro", "ru", "sl", "sr", "sv", "tr", "vi", "pt-BR", "zh-CN", "zh-TW", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        ar: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        bg: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        bs: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        ca: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        cs: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        da: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        de: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        el: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        en: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        es: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        et: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        fi: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        fr: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        he: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        hr: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        hu: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        id: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        it: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        ja: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        ko: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        lt: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        lv: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        mn: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        nb: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        nl: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        pl: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        pt: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        ro: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        ru: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        sl: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        sr: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        sv: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        tr: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        vi: typing.Union['ArticleContent', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArticleTranslatedContent':
        return super().__new__(
            cls,
            *_args,
            type=type,
            ar=ar,
            bg=bg,
            bs=bs,
            ca=ca,
            cs=cs,
            da=da,
            de=de,
            el=el,
            en=en,
            es=es,
            et=et,
            fi=fi,
            fr=fr,
            he=he,
            hr=hr,
            hu=hu,
            id=id,
            it=it,
            ja=ja,
            ko=ko,
            lt=lt,
            lv=lv,
            mn=mn,
            nb=nb,
            nl=nl,
            pl=pl,
            pt=pt,
            ro=ro,
            ru=ru,
            sl=sl,
            sr=sr,
            sv=sv,
            tr=tr,
            vi=vi,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.article_content import ArticleContent
