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


class Company(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Companies allow you to represent organizations using your product. Each company will have its own description and be associated with contacts. You can fetch, create, update and list companies.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMPANY(cls):
                    return cls("company")
            id = schemas.StrSchema
            name = schemas.StrSchema
            app_id = schemas.StrSchema
            
            
            class plan(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        type = schemas.StrSchema
                        id = schemas.StrSchema
                        name = schemas.StrSchema
                        __annotations__ = {
                            "type": type,
                            "id": id,
                            "name": name,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'plan':
                    return super().__new__(
                        cls,
                        *_args,
                        type=type,
                        id=id,
                        name=name,
                        _configuration=_configuration,
                        **kwargs,
                    )
            company_id = schemas.StrSchema
            remote_created_at = schemas.IntSchema
            created_at = schemas.IntSchema
            updated_at = schemas.IntSchema
            last_request_at = schemas.IntSchema
            size = schemas.IntSchema
            website = schemas.StrSchema
            industry = schemas.StrSchema
            monthly_spend = schemas.IntSchema
            session_count = schemas.IntSchema
            user_count = schemas.IntSchema
            
            
            class custom_attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'custom_attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class tags(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def TAG_LIST(cls):
                                return cls("tag.list")
                        
                        
                        class tags(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['Tag']:
                                            return Tag
                                
                                    def __new__(
                                        cls,
                                        _arg: typing.Union[typing.Tuple['Tag'], typing.List['Tag']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'items':
                                        return super().__new__(
                                            cls,
                                            _arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'Tag':
                                        return super().__getitem__(i)
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'tags':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "type": type,
                            "tags": tags,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "tags", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "tags", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        *_args,
                        type=type,
                        tags=tags,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class segments(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def SEGMENT_LIST(cls):
                                return cls("segment.list")
                        
                        
                        class segments(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['Segment']:
                                    return Segment
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['Segment'], typing.List['Segment']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'segments':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'Segment':
                                return super().__getitem__(i)
                        __annotations__ = {
                            "type": type,
                            "segments": segments,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["segments"]) -> MetaOapg.properties.segments: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "segments", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["segments"]) -> typing.Union[MetaOapg.properties.segments, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "segments", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    segments: typing.Union[MetaOapg.properties.segments, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'segments':
                    return super().__new__(
                        cls,
                        *_args,
                        type=type,
                        segments=segments,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "name": name,
                "app_id": app_id,
                "plan": plan,
                "company_id": company_id,
                "remote_created_at": remote_created_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_request_at": last_request_at,
                "size": size,
                "website": website,
                "industry": industry,
                "monthly_spend": monthly_spend,
                "session_count": session_count,
                "user_count": user_count,
                "custom_attributes": custom_attributes,
                "tags": tags,
                "segments": segments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_id"]) -> MetaOapg.properties.app_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan"]) -> MetaOapg.properties.plan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remote_created_at"]) -> MetaOapg.properties.remote_created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_request_at"]) -> MetaOapg.properties.last_request_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["industry"]) -> MetaOapg.properties.industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthly_spend"]) -> MetaOapg.properties.monthly_spend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_count"]) -> MetaOapg.properties.session_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_count"]) -> MetaOapg.properties.user_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_attributes"]) -> MetaOapg.properties.custom_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["segments"]) -> MetaOapg.properties.segments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", "app_id", "plan", "company_id", "remote_created_at", "created_at", "updated_at", "last_request_at", "size", "website", "industry", "monthly_spend", "session_count", "user_count", "custom_attributes", "tags", "segments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_id"]) -> typing.Union[MetaOapg.properties.app_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> typing.Union[MetaOapg.properties.plan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> typing.Union[MetaOapg.properties.company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remote_created_at"]) -> typing.Union[MetaOapg.properties.remote_created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_request_at"]) -> typing.Union[MetaOapg.properties.last_request_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["industry"]) -> typing.Union[MetaOapg.properties.industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthly_spend"]) -> typing.Union[MetaOapg.properties.monthly_spend, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_count"]) -> typing.Union[MetaOapg.properties.session_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_count"]) -> typing.Union[MetaOapg.properties.user_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_attributes"]) -> typing.Union[MetaOapg.properties.custom_attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["segments"]) -> typing.Union[MetaOapg.properties.segments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", "app_id", "plan", "company_id", "remote_created_at", "created_at", "updated_at", "last_request_at", "size", "website", "industry", "monthly_spend", "session_count", "user_count", "custom_attributes", "tags", "segments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        app_id: typing.Union[MetaOapg.properties.app_id, str, schemas.Unset] = schemas.unset,
        plan: typing.Union[MetaOapg.properties.plan, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        company_id: typing.Union[MetaOapg.properties.company_id, str, schemas.Unset] = schemas.unset,
        remote_created_at: typing.Union[MetaOapg.properties.remote_created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_request_at: typing.Union[MetaOapg.properties.last_request_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        industry: typing.Union[MetaOapg.properties.industry, str, schemas.Unset] = schemas.unset,
        monthly_spend: typing.Union[MetaOapg.properties.monthly_spend, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        session_count: typing.Union[MetaOapg.properties.session_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_count: typing.Union[MetaOapg.properties.user_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        custom_attributes: typing.Union[MetaOapg.properties.custom_attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        segments: typing.Union[MetaOapg.properties.segments, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Company':
        return super().__new__(
            cls,
            *_args,
            type=type,
            id=id,
            name=name,
            app_id=app_id,
            plan=plan,
            company_id=company_id,
            remote_created_at=remote_created_at,
            created_at=created_at,
            updated_at=updated_at,
            last_request_at=last_request_at,
            size=size,
            website=website,
            industry=industry,
            monthly_spend=monthly_spend,
            session_count=session_count,
            user_count=user_count,
            custom_attributes=custom_attributes,
            tags=tags,
            segments=segments,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.segment import Segment
from intercom_python_api.model.tag import Tag
