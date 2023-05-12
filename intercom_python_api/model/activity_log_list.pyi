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


class ActivityLogList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A paginated list of activity logs.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
        
            @staticmethod
            def pages() -> typing.Type['CursorPages']:
                return CursorPages
            
            
            class activity_logs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ActivityLog']:
                        return ActivityLog
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ActivityLog'], typing.List['ActivityLog']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'activity_logs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ActivityLog':
                    return super().__getitem__(i)
            __annotations__ = {
                "type": type,
                "pages": pages,
                "activity_logs": activity_logs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pages"]) -> 'CursorPages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activity_logs"]) -> MetaOapg.properties.activity_logs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "pages", "activity_logs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> typing.Union['CursorPages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activity_logs"]) -> typing.Union[MetaOapg.properties.activity_logs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "pages", "activity_logs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        pages: typing.Union['CursorPages', schemas.Unset] = schemas.unset,
        activity_logs: typing.Union[MetaOapg.properties.activity_logs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ActivityLogList':
        return super().__new__(
            cls,
            *_args,
            type=type,
            pages=pages,
            activity_logs=activity_logs,
            _configuration=_configuration,
            **kwargs,
        )

from intercom_python_api.model.activity_log import ActivityLog
from intercom_python_api.model.cursor_pages import CursorPages
