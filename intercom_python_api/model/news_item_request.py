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


class NewsItemRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A News Item is a content type in Intercom enabling you to announce product updates, company news, promotions, events and more with your customers.
    """


    class MetaOapg:
        required = {
            "title",
            "sender_id",
        }
        
        class properties:
            title = schemas.StrSchema
            sender_id = schemas.IntSchema
            body = schemas.StrSchema
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "draft": "DRAFT",
                        "live": "LIVE",
                    }
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
                
                @schemas.classproperty
                def LIVE(cls):
                    return cls("live")
            deliver_silently = schemas.BoolSchema
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
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
            __annotations__ = {
                "title": title,
                "sender_id": sender_id,
                "body": body,
                "state": state,
                "deliver_silently": deliver_silently,
                "labels": labels,
                "reactions": reactions,
                "newsfeed_assignments": newsfeed_assignments,
            }
    
    title: MetaOapg.properties.title
    sender_id: MetaOapg.properties.sender_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_id"]) -> MetaOapg.properties.sender_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deliver_silently"]) -> MetaOapg.properties.deliver_silently: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactions"]) -> MetaOapg.properties.reactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newsfeed_assignments"]) -> MetaOapg.properties.newsfeed_assignments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "sender_id", "body", "state", "deliver_silently", "labels", "reactions", "newsfeed_assignments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_id"]) -> MetaOapg.properties.sender_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deliver_silently"]) -> typing.Union[MetaOapg.properties.deliver_silently, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactions"]) -> typing.Union[MetaOapg.properties.reactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newsfeed_assignments"]) -> typing.Union[MetaOapg.properties.newsfeed_assignments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "sender_id", "body", "state", "deliver_silently", "labels", "reactions", "newsfeed_assignments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        sender_id: typing.Union[MetaOapg.properties.sender_id, decimal.Decimal, int, ],
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        deliver_silently: typing.Union[MetaOapg.properties.deliver_silently, bool, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        reactions: typing.Union[MetaOapg.properties.reactions, list, tuple, schemas.Unset] = schemas.unset,
        newsfeed_assignments: typing.Union[MetaOapg.properties.newsfeed_assignments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewsItemRequest':
        return super().__new__(
            cls,
            *_args,
            title=title,
            sender_id=sender_id,
            body=body,
            state=state,
            deliver_silently=deliver_silently,
            labels=labels,
            reactions=reactions,
            newsfeed_assignments=newsfeed_assignments,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.newsfeed_assignment import NewsfeedAssignment
