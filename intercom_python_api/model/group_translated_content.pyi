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


class GroupTranslatedContent(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The Translated Content of an Group. The keys are the locale codes and the values are the translated content of the Group.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def ar() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def bg() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def bs() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def ca() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def cs() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def da() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def de() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def el() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def en() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def es() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def et() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def fi() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def fr() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def he() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def hr() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def hu() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def id() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def it() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def ja() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def ko() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def lt() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def lv() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def mn() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def nb() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def nl() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def pl() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def pt() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def pt_br() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def ro() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def ru() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def sl() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def sr() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def sv() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def tr() -> typing.Type['GroupContent']:
                return GroupContent
            
            
            class type(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        schemas.NoneClass.NONE: "NONE",
                        "group_translated_content": "GROUP_TRANSLATED_CONTENT",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
                
                @schemas.classproperty
                def GROUP_TRANSLATED_CONTENT(cls):
                    return cls("group_translated_content")
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def vi() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def zh_cn() -> typing.Type['GroupContent']:
                return GroupContent
        
            @staticmethod
            def zh_tw() -> typing.Type['GroupContent']:
                return GroupContent
            __annotations__ = {
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
                "pt-BR": pt_br,
                "ro": ro,
                "ru": ru,
                "sl": sl,
                "sr": sr,
                "sv": sv,
                "tr": tr,
                "type": type,
                "vi": vi,
                "zh-CN": zh_cn,
                "zh-TW": zh_tw,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ar"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bg"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bs"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ca"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cs"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["da"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["de"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["el"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["en"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["et"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fi"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fr"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["he"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hr"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hu"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["it"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ja"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ko"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lt"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lv"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mn"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nb"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nl"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pl"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pt"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pt-BR"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ro"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ru"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sl"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sr"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sv"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tr"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vi"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zh-CN"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zh-TW"]) -> 'GroupContent': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ar", "bg", "bs", "ca", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "he", "hr", "hu", "id", "it", "ja", "ko", "lt", "lv", "mn", "nb", "nl", "pl", "pt", "pt-BR", "ro", "ru", "sl", "sr", "sv", "tr", "type", "vi", "zh-CN", "zh-TW", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ar"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bg"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bs"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ca"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cs"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["da"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["de"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["el"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["en"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["et"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fi"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fr"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["he"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hr"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hu"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["it"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ja"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ko"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lt"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lv"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mn"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nb"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nl"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pl"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pt"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pt-BR"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ro"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ru"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sl"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sr"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sv"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tr"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vi"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zh-CN"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zh-TW"]) -> typing.Union['GroupContent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ar", "bg", "bs", "ca", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "he", "hr", "hu", "id", "it", "ja", "ko", "lt", "lv", "mn", "nb", "nl", "pl", "pt", "pt-BR", "ro", "ru", "sl", "sr", "sv", "tr", "type", "vi", "zh-CN", "zh-TW", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        ar: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        bg: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        bs: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        ca: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        cs: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        da: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        de: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        el: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        en: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        es: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        et: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        fi: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        fr: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        he: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        hr: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        hu: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        id: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        it: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        ja: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        ko: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        lt: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        lv: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        mn: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        nb: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        nl: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        pl: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        pt: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        ro: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        ru: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        sl: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        sr: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        sv: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        tr: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, None, str, schemas.Unset] = schemas.unset,
        vi: typing.Union['GroupContent', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupTranslatedContent':
        return super().__new__(
            cls,
            *_args,
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
            type=type,
            vi=vi,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.group_content import GroupContent
