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


class Admin(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Admins are teammate accounts that have access to a workspace.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
            email = schemas.StrSchema
            job_title = schemas.StrSchema
            away_mode_enabled = schemas.BoolSchema
            away_mode_reassign = schemas.BoolSchema
            has_inbox_seat = schemas.BoolSchema
            
            
            class team_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'team_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class avatar(
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
                ) -> 'avatar':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def team_priority_level() -> typing.Type['TeamPriorityLevel']:
                return TeamPriorityLevel
            __annotations__ = {
                "type": type,
                "id": id,
                "name": name,
                "email": email,
                "job_title": job_title,
                "away_mode_enabled": away_mode_enabled,
                "away_mode_reassign": away_mode_reassign,
                "has_inbox_seat": has_inbox_seat,
                "team_ids": team_ids,
                "avatar": avatar,
                "team_priority_level": team_priority_level,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["away_mode_enabled"]) -> MetaOapg.properties.away_mode_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["away_mode_reassign"]) -> MetaOapg.properties.away_mode_reassign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_inbox_seat"]) -> MetaOapg.properties.has_inbox_seat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_ids"]) -> MetaOapg.properties.team_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_priority_level"]) -> 'TeamPriorityLevel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", "email", "job_title", "away_mode_enabled", "away_mode_reassign", "has_inbox_seat", "team_ids", "avatar", "team_priority_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title"]) -> typing.Union[MetaOapg.properties.job_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["away_mode_enabled"]) -> typing.Union[MetaOapg.properties.away_mode_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["away_mode_reassign"]) -> typing.Union[MetaOapg.properties.away_mode_reassign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_inbox_seat"]) -> typing.Union[MetaOapg.properties.has_inbox_seat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_ids"]) -> typing.Union[MetaOapg.properties.team_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> typing.Union[MetaOapg.properties.avatar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_priority_level"]) -> typing.Union['TeamPriorityLevel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", "email", "job_title", "away_mode_enabled", "away_mode_reassign", "has_inbox_seat", "team_ids", "avatar", "team_priority_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        job_title: typing.Union[MetaOapg.properties.job_title, str, schemas.Unset] = schemas.unset,
        away_mode_enabled: typing.Union[MetaOapg.properties.away_mode_enabled, bool, schemas.Unset] = schemas.unset,
        away_mode_reassign: typing.Union[MetaOapg.properties.away_mode_reassign, bool, schemas.Unset] = schemas.unset,
        has_inbox_seat: typing.Union[MetaOapg.properties.has_inbox_seat, bool, schemas.Unset] = schemas.unset,
        team_ids: typing.Union[MetaOapg.properties.team_ids, list, tuple, schemas.Unset] = schemas.unset,
        avatar: typing.Union[MetaOapg.properties.avatar, None, str, schemas.Unset] = schemas.unset,
        team_priority_level: typing.Union['TeamPriorityLevel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Admin':
        return super().__new__(
            cls,
            *_args,
            type=type,
            id=id,
            name=name,
            email=email,
            job_title=job_title,
            away_mode_enabled=away_mode_enabled,
            away_mode_reassign=away_mode_reassign,
            has_inbox_seat=has_inbox_seat,
            team_ids=team_ids,
            avatar=avatar,
            team_priority_level=team_priority_level,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.team_priority_level import TeamPriorityLevel
