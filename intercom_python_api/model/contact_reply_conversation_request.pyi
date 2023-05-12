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


class ContactReplyConversationRequest(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "intercom_user_id",
                    "message_type",
                    "body",
                    "type",
                }
                
                class properties:
                    
                    
                    class message_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def COMMENT(cls):
                            return cls("comment")
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def USER(cls):
                            return cls("user")
                    body = schemas.StrSchema
                    intercom_user_id = schemas.StrSchema
                    
                    
                    class attachment_urls(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'attachment_urls':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    __annotations__ = {
                        "message_type": message_type,
                        "type": type,
                        "body": body,
                        "intercom_user_id": intercom_user_id,
                        "attachment_urls": attachment_urls,
                    }
            
            intercom_user_id: MetaOapg.properties.intercom_user_id
            message_type: MetaOapg.properties.message_type
            body: MetaOapg.properties.body
            type: MetaOapg.properties.type
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["intercom_user_id"]) -> MetaOapg.properties.intercom_user_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attachment_urls"]) -> MetaOapg.properties.attachment_urls: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "body", "intercom_user_id", "attachment_urls", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["intercom_user_id"]) -> MetaOapg.properties.intercom_user_id: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attachment_urls"]) -> typing.Union[MetaOapg.properties.attachment_urls, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "body", "intercom_user_id", "attachment_urls", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                intercom_user_id: typing.Union[MetaOapg.properties.intercom_user_id, str, ],
                message_type: typing.Union[MetaOapg.properties.message_type, str, ],
                body: typing.Union[MetaOapg.properties.body, str, ],
                type: typing.Union[MetaOapg.properties.type, str, ],
                attachment_urls: typing.Union[MetaOapg.properties.attachment_urls, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    intercom_user_id=intercom_user_id,
                    message_type=message_type,
                    body=body,
                    type=type,
                    attachment_urls=attachment_urls,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "user_id",
                    "message_type",
                    "body",
                    "type",
                }
                
                class properties:
                    
                    
                    class message_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def COMMENT(cls):
                            return cls("comment")
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def USER(cls):
                            return cls("user")
                    body = schemas.StrSchema
                    user_id = schemas.StrSchema
                    
                    
                    class attachment_urls(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'attachment_urls':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    __annotations__ = {
                        "message_type": message_type,
                        "type": type,
                        "body": body,
                        "user_id": user_id,
                        "attachment_urls": attachment_urls,
                    }
            
            user_id: MetaOapg.properties.user_id
            message_type: MetaOapg.properties.message_type
            body: MetaOapg.properties.body
            type: MetaOapg.properties.type
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attachment_urls"]) -> MetaOapg.properties.attachment_urls: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "body", "user_id", "attachment_urls", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attachment_urls"]) -> typing.Union[MetaOapg.properties.attachment_urls, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "body", "user_id", "attachment_urls", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                user_id: typing.Union[MetaOapg.properties.user_id, str, ],
                message_type: typing.Union[MetaOapg.properties.message_type, str, ],
                body: typing.Union[MetaOapg.properties.body, str, ],
                type: typing.Union[MetaOapg.properties.type, str, ],
                attachment_urls: typing.Union[MetaOapg.properties.attachment_urls, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    user_id=user_id,
                    message_type=message_type,
                    body=body,
                    type=type,
                    attachment_urls=attachment_urls,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "message_type",
                    "body",
                    "type",
                    "email",
                }
                
                class properties:
                    
                    
                    class message_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def COMMENT(cls):
                            return cls("comment")
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def USER(cls):
                            return cls("user")
                    body = schemas.StrSchema
                    email = schemas.StrSchema
                    
                    
                    class attachment_urls(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'attachment_urls':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    __annotations__ = {
                        "message_type": message_type,
                        "type": type,
                        "body": body,
                        "email": email,
                        "attachment_urls": attachment_urls,
                    }
            
            message_type: MetaOapg.properties.message_type
            body: MetaOapg.properties.body
            type: MetaOapg.properties.type
            email: MetaOapg.properties.email
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attachment_urls"]) -> MetaOapg.properties.attachment_urls: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "body", "email", "attachment_urls", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attachment_urls"]) -> typing.Union[MetaOapg.properties.attachment_urls, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message_type", "type", "body", "email", "attachment_urls", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                message_type: typing.Union[MetaOapg.properties.message_type, str, ],
                body: typing.Union[MetaOapg.properties.body, str, ],
                type: typing.Union[MetaOapg.properties.type, str, ],
                email: typing.Union[MetaOapg.properties.email, str, ],
                attachment_urls: typing.Union[MetaOapg.properties.attachment_urls, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_2':
                return super().__new__(
                    cls,
                    *_args,
                    message_type=message_type,
                    body=body,
                    type=type,
                    email=email,
                    attachment_urls=attachment_urls,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
                cls.one_of_2,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactReplyConversationRequest':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
