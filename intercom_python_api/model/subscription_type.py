# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.7
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


class SubscriptionType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A subscription type lets customers easily opt out of non-essential communications without missing what's important to them.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "live": "LIVE",
                        "draft": "DRAFT",
                        "archived": "ARCHIVED",
                    }
                
                @schemas.classproperty
                def LIVE(cls):
                    return cls("live")
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
                
                @schemas.classproperty
                def ARCHIVED(cls):
                    return cls("archived")
        
            @staticmethod
            def default_translation() -> typing.Type['Translation']:
                return Translation
            
            
            class translations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Translation']:
                        return Translation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Translation'], typing.List['Translation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'translations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Translation':
                    return super().__getitem__(i)
            
            
            class consent_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "opt_out": "OUT",
                        "opt_in": "IN",
                    }
                
                @schemas.classproperty
                def OUT(cls):
                    return cls("opt_out")
                
                @schemas.classproperty
                def IN(cls):
                    return cls("opt_in")
            
            
            class content_types(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "email": "EMAIL",
                                "sms_message": "SMS_MESSAGE",
                            }
                        
                        @schemas.classproperty
                        def EMAIL(cls):
                            return cls("email")
                        
                        @schemas.classproperty
                        def SMS_MESSAGE(cls):
                            return cls("sms_message")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'content_types':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "type": type,
                "id": id,
                "state": state,
                "default_translation": default_translation,
                "translations": translations,
                "consent_type": consent_type,
                "content_types": content_types,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_translation"]) -> 'Translation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translations"]) -> MetaOapg.properties.translations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consent_type"]) -> MetaOapg.properties.consent_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_types"]) -> MetaOapg.properties.content_types: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "state", "default_translation", "translations", "consent_type", "content_types", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_translation"]) -> typing.Union['Translation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translations"]) -> typing.Union[MetaOapg.properties.translations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consent_type"]) -> typing.Union[MetaOapg.properties.consent_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_types"]) -> typing.Union[MetaOapg.properties.content_types, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "state", "default_translation", "translations", "consent_type", "content_types", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        default_translation: typing.Union['Translation', schemas.Unset] = schemas.unset,
        translations: typing.Union[MetaOapg.properties.translations, list, tuple, schemas.Unset] = schemas.unset,
        consent_type: typing.Union[MetaOapg.properties.consent_type, str, schemas.Unset] = schemas.unset,
        content_types: typing.Union[MetaOapg.properties.content_types, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubscriptionType':
        return super().__new__(
            cls,
            *_args,
            type=type,
            id=id,
            state=state,
            default_translation=default_translation,
            translations=translations,
            consent_type=consent_type,
            content_types=content_types,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.translation import Translation
