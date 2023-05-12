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


class NewsItem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A News Item is a content type in Intercom enabling you to announce product updates, company news, promotions, events and more with your customers.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NEWSITEM(cls):
                    return cls("news-item")
            id = schemas.StrSchema
            workspace_id = schemas.StrSchema
            title = schemas.StrSchema
            body = schemas.StrSchema
            sender_id = schemas.IntSchema
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
                
                @schemas.classproperty
                def LIVE(cls):
                    return cls("live")
            
            
            class newsfeed_assignments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NewsfeedAssignment']:
                        return NewsfeedAssignment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NewsfeedAssignment'], typing.List['NewsfeedAssignment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'newsfeed_assignments':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NewsfeedAssignment':
                    return super().__getitem__(i)
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, None, str, ]], typing.List[typing.Union[MetaOapg.items, None, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class cover_image_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cover_image_url':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class reactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, None, str, ]], typing.List[typing.Union[MetaOapg.items, None, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            deliver_silently = schemas.BoolSchema
            created_at = schemas.IntSchema
            updated_at = schemas.IntSchema
            __annotations__ = {
                "type": type,
                "id": id,
                "workspace_id": workspace_id,
                "title": title,
                "body": body,
                "sender_id": sender_id,
                "state": state,
                "newsfeed_assignments": newsfeed_assignments,
                "labels": labels,
                "cover_image_url": cover_image_url,
                "reactions": reactions,
                "deliver_silently": deliver_silently,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_id"]) -> MetaOapg.properties.workspace_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_id"]) -> MetaOapg.properties.sender_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newsfeed_assignments"]) -> MetaOapg.properties.newsfeed_assignments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_image_url"]) -> MetaOapg.properties.cover_image_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactions"]) -> MetaOapg.properties.reactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver_silently"]) -> MetaOapg.properties.deliver_silently: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "workspace_id", "title", "body", "sender_id", "state", "newsfeed_assignments", "labels", "cover_image_url", "reactions", "deliver_silently", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_id"]) -> typing.Union[MetaOapg.properties.workspace_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_id"]) -> typing.Union[MetaOapg.properties.sender_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newsfeed_assignments"]) -> typing.Union[MetaOapg.properties.newsfeed_assignments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_image_url"]) -> typing.Union[MetaOapg.properties.cover_image_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactions"]) -> typing.Union[MetaOapg.properties.reactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver_silently"]) -> typing.Union[MetaOapg.properties.deliver_silently, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "workspace_id", "title", "body", "sender_id", "state", "newsfeed_assignments", "labels", "cover_image_url", "reactions", "deliver_silently", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        workspace_id: typing.Union[MetaOapg.properties.workspace_id, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        sender_id: typing.Union[MetaOapg.properties.sender_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        newsfeed_assignments: typing.Union[MetaOapg.properties.newsfeed_assignments, list, tuple, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        cover_image_url: typing.Union[MetaOapg.properties.cover_image_url, None, str, schemas.Unset] = schemas.unset,
        reactions: typing.Union[MetaOapg.properties.reactions, list, tuple, schemas.Unset] = schemas.unset,
        deliver_silently: typing.Union[MetaOapg.properties.deliver_silently, bool, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewsItem':
        return super().__new__(
            cls,
            *_args,
            type=type,
            id=id,
            workspace_id=workspace_id,
            title=title,
            body=body,
            sender_id=sender_id,
            state=state,
            newsfeed_assignments=newsfeed_assignments,
            labels=labels,
            cover_image_url=cover_image_url,
            reactions=reactions,
            deliver_silently=deliver_silently,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.newsfeed_assignment import NewsfeedAssignment
