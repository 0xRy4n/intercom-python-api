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


class TeamList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This will return a list of team objects for the App.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "team.list": "TEAM_LIST",
                    }
                
                @schemas.classproperty
                def TEAM_LIST(cls):
                    return cls("team.list")
            
            
            class teams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Team']:
                        return Team
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Team'], typing.List['Team']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'teams':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Team':
                    return super().__getitem__(i)
            __annotations__ = {
                "type": type,
                "teams": teams,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teams"]) -> MetaOapg.properties.teams: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "teams", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teams"]) -> typing.Union[MetaOapg.properties.teams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "teams", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        teams: typing.Union[MetaOapg.properties.teams, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TeamList':
        return super().__new__(
            cls,
            *_args,
            type=type,
            teams=teams,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.team import Team
