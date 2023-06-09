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


class CreateMessageRequest(
    schemas.ComposedBase,
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can create a message
    """


    class MetaOapg:
        
        class properties:
            body = schemas.StrSchema
            create_conversation_without_contact_reply = schemas.BoolSchema
            
            
            class _from(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "id",
                        "type",
                    }
                    
                    class properties:
                        id = schemas.IntSchema
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "admin": "ADMIN",
                                }
                            
                            @schemas.classproperty
                            def ADMIN(cls):
                                return cls("admin")
                        __annotations__ = {
                            "id": id,
                            "type": type,
                        }
                
                id: MetaOapg.properties.id
                type: MetaOapg.properties.type
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                    type: typing.Union[MetaOapg.properties.type, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_from':
                    return super().__new__(
                        cls,
                        *_args,
                        id=id,
                        type=type,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class message_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "in_app": "IN_APP",
                        "email": "EMAIL",
                    }
                
                @schemas.classproperty
                def IN_APP(cls):
                    return cls("in_app")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("email")
            subject = schemas.StrSchema
            template = schemas.StrSchema
            
            
            class to(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "id",
                        "type",
                    }
                    
                    class properties:
                        id = schemas.StrSchema
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "user": "USER",
                                    "lead": "LEAD",
                                }
                            
                            @schemas.classproperty
                            def USER(cls):
                                return cls("user")
                            
                            @schemas.classproperty
                            def LEAD(cls):
                                return cls("lead")
                        __annotations__ = {
                            "id": id,
                            "type": type,
                        }
                
                id: MetaOapg.properties.id
                type: MetaOapg.properties.type
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    id: typing.Union[MetaOapg.properties.id, str, ],
                    type: typing.Union[MetaOapg.properties.type, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'to':
                    return super().__new__(
                        cls,
                        *_args,
                        id=id,
                        type=type,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "body": body,
                "create_conversation_without_contact_reply": create_conversation_without_contact_reply,
                "from": _from,
                "message_type": message_type,
                "subject": subject,
                "template": template,
                "to": to,
            }
        
        
        class any_of_0(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "template",
                    "subject",
                    "from",
                    "message_type",
                    "to",
                    "body",
                }
        
            
            template: schemas.AnyTypeSchema
            subject: schemas.AnyTypeSchema
            message_type: schemas.AnyTypeSchema
            to: schemas.AnyTypeSchema
            body: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class any_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "from",
                    "message_type",
                    "to",
                    "body",
                }
        
            
            message_type: schemas.AnyTypeSchema
            to: schemas.AnyTypeSchema
            body: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'any_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def any_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.any_of_0,
                cls.any_of_1,
            ]

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_conversation_without_contact_reply"]) -> MetaOapg.properties.create_conversation_without_contact_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message_type"]) -> MetaOapg.properties.message_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["body", "create_conversation_without_contact_reply", "from", "message_type", "subject", "template", "to", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_conversation_without_contact_reply"]) -> typing.Union[MetaOapg.properties.create_conversation_without_contact_reply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message_type"]) -> typing.Union[MetaOapg.properties.message_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["body", "create_conversation_without_contact_reply", "from", "message_type", "subject", "template", "to", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        create_conversation_without_contact_reply: typing.Union[MetaOapg.properties.create_conversation_without_contact_reply, bool, schemas.Unset] = schemas.unset,
        message_type: typing.Union[MetaOapg.properties.message_type, str, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        template: typing.Union[MetaOapg.properties.template, str, schemas.Unset] = schemas.unset,
        to: typing.Union[MetaOapg.properties.to, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateMessageRequest':
        return super().__new__(
            cls,
            *_args,
            body=body,
            create_conversation_without_contact_reply=create_conversation_without_contact_reply,
            message_type=message_type,
            subject=subject,
            template=template,
            to=to,
            _configuration=_configuration,
            **kwargs,
        )
