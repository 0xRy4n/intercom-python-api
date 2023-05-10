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


class ConvertVisitorRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    You can merge a Visitor to a Contact of role type lead or user.
    """


    class MetaOapg:
        required = {
            "type",
            "visitor",
            "user",
        }
        
        class properties:
            type = schemas.StrSchema
            
            
            class user(
                schemas.ComposedBase,
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        id = schemas.StrSchema
                        user_id = schemas.StrSchema
                        email = schemas.StrSchema
                        __annotations__ = {
                            "id": id,
                            "user_id": user_id,
                            "email": email,
                        }
                    
                    
                    class any_of_0(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "id",
                            }
                    
                        
                        id: schemas.AnyTypeSchema
                    
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
                                "user_id",
                            }
                    
                        
                        user_id: schemas.AnyTypeSchema
                    
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
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "email", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "email", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                    user_id: typing.Union[MetaOapg.properties.user_id, str, schemas.Unset] = schemas.unset,
                    email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'user':
                    return super().__new__(
                        cls,
                        *_args,
                        id=id,
                        user_id=user_id,
                        email=email,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class visitor(
                schemas.ComposedBase,
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        id = schemas.StrSchema
                        user_id = schemas.StrSchema
                        email = schemas.StrSchema
                        __annotations__ = {
                            "id": id,
                            "user_id": user_id,
                            "email": email,
                        }
                    
                    
                    class any_of_0(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "id",
                            }
                    
                        
                        id: schemas.AnyTypeSchema
                    
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
                                "user_id",
                            }
                    
                        
                        user_id: schemas.AnyTypeSchema
                    
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
                    
                    
                    class any_of_2(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "email",
                            }
                    
                        
                        email: schemas.AnyTypeSchema
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'any_of_2':
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
                            cls.any_of_2,
                        ]
            
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "email", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "email", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                    user_id: typing.Union[MetaOapg.properties.user_id, str, schemas.Unset] = schemas.unset,
                    email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'visitor':
                    return super().__new__(
                        cls,
                        *_args,
                        id=id,
                        user_id=user_id,
                        email=email,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "user": user,
                "visitor": visitor,
            }
    
    type: MetaOapg.properties.type
    visitor: MetaOapg.properties.visitor
    user: MetaOapg.properties.user
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visitor"]) -> MetaOapg.properties.visitor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "user", "visitor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visitor"]) -> MetaOapg.properties.visitor: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "user", "visitor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        visitor: typing.Union[MetaOapg.properties.visitor, dict, frozendict.frozendict, ],
        user: typing.Union[MetaOapg.properties.user, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConvertVisitorRequest':
        return super().__new__(
            cls,
            *_args,
            type=type,
            visitor=visitor,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )