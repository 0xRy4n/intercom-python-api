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


class ActivityLog(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Activities performed by admins.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class performed_by(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        type = schemas.StrSchema
                        id = schemas.StrSchema
                        email = schemas.StrSchema
                        ip = schemas.StrSchema
                        __annotations__ = {
                            "type": type,
                            "id": id,
                            "email": email,
                            "ip": ip,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "email", "ip", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> typing.Union[MetaOapg.properties.ip, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "email", "ip", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                    email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
                    ip: typing.Union[MetaOapg.properties.ip, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'performed_by':
                    return super().__new__(
                        cls,
                        *_args,
                        type=type,
                        id=id,
                        email=email,
                        ip=ip,
                        _configuration=_configuration,
                        **kwargs,
                    )
            metadata = schemas.DictSchema
            created_at = schemas.IntSchema
            
            
            class activity_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "admin_assignment_limit_change": "ADMIN_ASSIGNMENT_LIMIT_CHANGE",
                        "admin_away_mode_change": "ADMIN_AWAY_MODE_CHANGE",
                        "admin_deletion": "ADMIN_DELETION",
                        "admin_deprovisioned": "ADMIN_DEPROVISIONED",
                        "admin_impersonation_end": "ADMIN_IMPERSONATION_END",
                        "admin_impersonation_start": "ADMIN_IMPERSONATION_START",
                        "admin_invite_change": "ADMIN_INVITE_CHANGE",
                        "admin_invite_creation": "ADMIN_INVITE_CREATION",
                        "admin_invite_deletion": "ADMIN_INVITE_DELETION",
                        "admin_login_failure": "ADMIN_LOGIN_FAILURE",
                        "admin_login_success": "ADMIN_LOGIN_SUCCESS",
                        "admin_logout": "ADMIN_LOGOUT",
                        "admin_password_reset_request": "ADMIN_PASSWORD_RESET_REQUEST",
                        "admin_password_reset_success": "ADMIN_PASSWORD_RESET_SUCCESS",
                        "admin_permission_change": "ADMIN_PERMISSION_CHANGE",
                        "admin_provisioned": "ADMIN_PROVISIONED",
                        "admin_two_factor_auth_change": "ADMIN_TWO_FACTOR_AUTH_CHANGE",
                        "admin_unauthorized_sign_in_method": "ADMIN_UNAUTHORIZED_SIGN_IN_METHOD",
                        "app_admin_join": "APP_ADMIN_JOIN",
                        "app_authentication_method_change": "APP_AUTHENTICATION_METHOD_CHANGE",
                        "app_data_deletion": "APP_DATA_DELETION",
                        "app_data_export": "APP_DATA_EXPORT",
                        "app_google_sso_domain_change": "APP_GOOGLE_SSO_DOMAIN_CHANGE",
                        "app_identity_verification_change": "APP_IDENTITY_VERIFICATION_CHANGE",
                        "app_name_change": "APP_NAME_CHANGE",
                        "app_outbound_address_change": "APP_OUTBOUND_ADDRESS_CHANGE",
                        "app_package_installation": "APP_PACKAGE_INSTALLATION",
                        "app_package_token_regeneration": "APP_PACKAGE_TOKEN_REGENERATION",
                        "app_package_uninstallation": "APP_PACKAGE_UNINSTALLATION",
                        "app_team_creation": "APP_TEAM_CREATION",
                        "app_team_deletion": "APP_TEAM_DELETION",
                        "app_team_membership_modification": "APP_TEAM_MEMBERSHIP_MODIFICATION",
                        "app_timezone_change": "APP_TIMEZONE_CHANGE",
                        "app_webhook_creation": "APP_WEBHOOK_CREATION",
                        "app_webhook_deletion": "APP_WEBHOOK_DELETION",
                        "articles_in_messenger_enabled_change": "ARTICLES_IN_MESSENGER_ENABLED_CHANGE",
                        "bulk_delete": "BULK_DELETE",
                        "bulk_export": "BULK_EXPORT",
                        "campaign_deletion": "CAMPAIGN_DELETION",
                        "campaign_state_change": "CAMPAIGN_STATE_CHANGE",
                        "conversation_part_deletion": "CONVERSATION_PART_DELETION",
                        "conversation_topic_change": "CONVERSATION_TOPIC_CHANGE",
                        "conversation_topic_creation": "CONVERSATION_TOPIC_CREATION",
                        "conversation_topic_deletion": "CONVERSATION_TOPIC_DELETION",
                        "help_center_settings_change": "HELP_CENTER_SETTINGS_CHANGE",
                        "inbound_conversations_change": "INBOUND_CONVERSATIONS_CHANGE",
                        "inbox_access_change": "INBOX_ACCESS_CHANGE",
                        "message_deletion": "MESSAGE_DELETION",
                        "message_state_change": "MESSAGE_STATE_CHANGE",
                        "messenger_look_and_feel_change": "MESSENGER_LOOK_AND_FEEL_CHANGE",
                        "messenger_search_required_change": "MESSENGER_SEARCH_REQUIRED_CHANGE",
                        "messenger_spaces_change": "MESSENGER_SPACES_CHANGE",
                        "office_hours_change": "OFFICE_HOURS_CHANGE",
                        "role_change": "ROLE_CHANGE",
                        "role_creation": "ROLE_CREATION",
                        "role_deletion": "ROLE_DELETION",
                        "ruleset_activation_title_preview": "RULESET_ACTIVATION_TITLE_PREVIEW",
                        "ruleset_creation": "RULESET_CREATION",
                        "ruleset_deletion": "RULESET_DELETION",
                        "search_browse_enabled_change": "SEARCH_BROWSE_ENABLED_CHANGE",
                        "search_browse_required_change": "SEARCH_BROWSE_REQUIRED_CHANGE",
                        "seat_change": "SEAT_CHANGE",
                        "seat_revoke": "SEAT_REVOKE",
                        "security_settings_change": "SECURITY_SETTINGS_CHANGE",
                        "temporary_expectation_change": "TEMPORARY_EXPECTATION_CHANGE",
                        "upfront_email_collection_change": "UPFRONT_EMAIL_COLLECTION_CHANGE",
                        "welcome_message_change": "WELCOME_MESSAGE_CHANGE",
                    }
                
                @schemas.classproperty
                def ADMIN_ASSIGNMENT_LIMIT_CHANGE(cls):
                    return cls("admin_assignment_limit_change")
                
                @schemas.classproperty
                def ADMIN_AWAY_MODE_CHANGE(cls):
                    return cls("admin_away_mode_change")
                
                @schemas.classproperty
                def ADMIN_DELETION(cls):
                    return cls("admin_deletion")
                
                @schemas.classproperty
                def ADMIN_DEPROVISIONED(cls):
                    return cls("admin_deprovisioned")
                
                @schemas.classproperty
                def ADMIN_IMPERSONATION_END(cls):
                    return cls("admin_impersonation_end")
                
                @schemas.classproperty
                def ADMIN_IMPERSONATION_START(cls):
                    return cls("admin_impersonation_start")
                
                @schemas.classproperty
                def ADMIN_INVITE_CHANGE(cls):
                    return cls("admin_invite_change")
                
                @schemas.classproperty
                def ADMIN_INVITE_CREATION(cls):
                    return cls("admin_invite_creation")
                
                @schemas.classproperty
                def ADMIN_INVITE_DELETION(cls):
                    return cls("admin_invite_deletion")
                
                @schemas.classproperty
                def ADMIN_LOGIN_FAILURE(cls):
                    return cls("admin_login_failure")
                
                @schemas.classproperty
                def ADMIN_LOGIN_SUCCESS(cls):
                    return cls("admin_login_success")
                
                @schemas.classproperty
                def ADMIN_LOGOUT(cls):
                    return cls("admin_logout")
                
                @schemas.classproperty
                def ADMIN_PASSWORD_RESET_REQUEST(cls):
                    return cls("admin_password_reset_request")
                
                @schemas.classproperty
                def ADMIN_PASSWORD_RESET_SUCCESS(cls):
                    return cls("admin_password_reset_success")
                
                @schemas.classproperty
                def ADMIN_PERMISSION_CHANGE(cls):
                    return cls("admin_permission_change")
                
                @schemas.classproperty
                def ADMIN_PROVISIONED(cls):
                    return cls("admin_provisioned")
                
                @schemas.classproperty
                def ADMIN_TWO_FACTOR_AUTH_CHANGE(cls):
                    return cls("admin_two_factor_auth_change")
                
                @schemas.classproperty
                def ADMIN_UNAUTHORIZED_SIGN_IN_METHOD(cls):
                    return cls("admin_unauthorized_sign_in_method")
                
                @schemas.classproperty
                def APP_ADMIN_JOIN(cls):
                    return cls("app_admin_join")
                
                @schemas.classproperty
                def APP_AUTHENTICATION_METHOD_CHANGE(cls):
                    return cls("app_authentication_method_change")
                
                @schemas.classproperty
                def APP_DATA_DELETION(cls):
                    return cls("app_data_deletion")
                
                @schemas.classproperty
                def APP_DATA_EXPORT(cls):
                    return cls("app_data_export")
                
                @schemas.classproperty
                def APP_GOOGLE_SSO_DOMAIN_CHANGE(cls):
                    return cls("app_google_sso_domain_change")
                
                @schemas.classproperty
                def APP_IDENTITY_VERIFICATION_CHANGE(cls):
                    return cls("app_identity_verification_change")
                
                @schemas.classproperty
                def APP_NAME_CHANGE(cls):
                    return cls("app_name_change")
                
                @schemas.classproperty
                def APP_OUTBOUND_ADDRESS_CHANGE(cls):
                    return cls("app_outbound_address_change")
                
                @schemas.classproperty
                def APP_PACKAGE_INSTALLATION(cls):
                    return cls("app_package_installation")
                
                @schemas.classproperty
                def APP_PACKAGE_TOKEN_REGENERATION(cls):
                    return cls("app_package_token_regeneration")
                
                @schemas.classproperty
                def APP_PACKAGE_UNINSTALLATION(cls):
                    return cls("app_package_uninstallation")
                
                @schemas.classproperty
                def APP_TEAM_CREATION(cls):
                    return cls("app_team_creation")
                
                @schemas.classproperty
                def APP_TEAM_DELETION(cls):
                    return cls("app_team_deletion")
                
                @schemas.classproperty
                def APP_TEAM_MEMBERSHIP_MODIFICATION(cls):
                    return cls("app_team_membership_modification")
                
                @schemas.classproperty
                def APP_TIMEZONE_CHANGE(cls):
                    return cls("app_timezone_change")
                
                @schemas.classproperty
                def APP_WEBHOOK_CREATION(cls):
                    return cls("app_webhook_creation")
                
                @schemas.classproperty
                def APP_WEBHOOK_DELETION(cls):
                    return cls("app_webhook_deletion")
                
                @schemas.classproperty
                def ARTICLES_IN_MESSENGER_ENABLED_CHANGE(cls):
                    return cls("articles_in_messenger_enabled_change")
                
                @schemas.classproperty
                def BULK_DELETE(cls):
                    return cls("bulk_delete")
                
                @schemas.classproperty
                def BULK_EXPORT(cls):
                    return cls("bulk_export")
                
                @schemas.classproperty
                def CAMPAIGN_DELETION(cls):
                    return cls("campaign_deletion")
                
                @schemas.classproperty
                def CAMPAIGN_STATE_CHANGE(cls):
                    return cls("campaign_state_change")
                
                @schemas.classproperty
                def CONVERSATION_PART_DELETION(cls):
                    return cls("conversation_part_deletion")
                
                @schemas.classproperty
                def CONVERSATION_TOPIC_CHANGE(cls):
                    return cls("conversation_topic_change")
                
                @schemas.classproperty
                def CONVERSATION_TOPIC_CREATION(cls):
                    return cls("conversation_topic_creation")
                
                @schemas.classproperty
                def CONVERSATION_TOPIC_DELETION(cls):
                    return cls("conversation_topic_deletion")
                
                @schemas.classproperty
                def HELP_CENTER_SETTINGS_CHANGE(cls):
                    return cls("help_center_settings_change")
                
                @schemas.classproperty
                def INBOUND_CONVERSATIONS_CHANGE(cls):
                    return cls("inbound_conversations_change")
                
                @schemas.classproperty
                def INBOX_ACCESS_CHANGE(cls):
                    return cls("inbox_access_change")
                
                @schemas.classproperty
                def MESSAGE_DELETION(cls):
                    return cls("message_deletion")
                
                @schemas.classproperty
                def MESSAGE_STATE_CHANGE(cls):
                    return cls("message_state_change")
                
                @schemas.classproperty
                def MESSENGER_LOOK_AND_FEEL_CHANGE(cls):
                    return cls("messenger_look_and_feel_change")
                
                @schemas.classproperty
                def MESSENGER_SEARCH_REQUIRED_CHANGE(cls):
                    return cls("messenger_search_required_change")
                
                @schemas.classproperty
                def MESSENGER_SPACES_CHANGE(cls):
                    return cls("messenger_spaces_change")
                
                @schemas.classproperty
                def OFFICE_HOURS_CHANGE(cls):
                    return cls("office_hours_change")
                
                @schemas.classproperty
                def ROLE_CHANGE(cls):
                    return cls("role_change")
                
                @schemas.classproperty
                def ROLE_CREATION(cls):
                    return cls("role_creation")
                
                @schemas.classproperty
                def ROLE_DELETION(cls):
                    return cls("role_deletion")
                
                @schemas.classproperty
                def RULESET_ACTIVATION_TITLE_PREVIEW(cls):
                    return cls("ruleset_activation_title_preview")
                
                @schemas.classproperty
                def RULESET_CREATION(cls):
                    return cls("ruleset_creation")
                
                @schemas.classproperty
                def RULESET_DELETION(cls):
                    return cls("ruleset_deletion")
                
                @schemas.classproperty
                def SEARCH_BROWSE_ENABLED_CHANGE(cls):
                    return cls("search_browse_enabled_change")
                
                @schemas.classproperty
                def SEARCH_BROWSE_REQUIRED_CHANGE(cls):
                    return cls("search_browse_required_change")
                
                @schemas.classproperty
                def SEAT_CHANGE(cls):
                    return cls("seat_change")
                
                @schemas.classproperty
                def SEAT_REVOKE(cls):
                    return cls("seat_revoke")
                
                @schemas.classproperty
                def SECURITY_SETTINGS_CHANGE(cls):
                    return cls("security_settings_change")
                
                @schemas.classproperty
                def TEMPORARY_EXPECTATION_CHANGE(cls):
                    return cls("temporary_expectation_change")
                
                @schemas.classproperty
                def UPFRONT_EMAIL_COLLECTION_CHANGE(cls):
                    return cls("upfront_email_collection_change")
                
                @schemas.classproperty
                def WELCOME_MESSAGE_CHANGE(cls):
                    return cls("welcome_message_change")
            activity_description = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "performed_by": performed_by,
                "metadata": metadata,
                "created_at": created_at,
                "activity_type": activity_type,
                "activity_description": activity_description,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["performed_by"]) -> MetaOapg.properties.performed_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activity_type"]) -> MetaOapg.properties.activity_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activity_description"]) -> MetaOapg.properties.activity_description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "performed_by", "metadata", "created_at", "activity_type", "activity_description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["performed_by"]) -> typing.Union[MetaOapg.properties.performed_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activity_type"]) -> typing.Union[MetaOapg.properties.activity_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activity_description"]) -> typing.Union[MetaOapg.properties.activity_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "performed_by", "metadata", "created_at", "activity_type", "activity_description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        performed_by: typing.Union[MetaOapg.properties.performed_by, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activity_type: typing.Union[MetaOapg.properties.activity_type, str, schemas.Unset] = schemas.unset,
        activity_description: typing.Union[MetaOapg.properties.activity_description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ActivityLog':
        return super().__new__(
            cls,
            *_args,
            id=id,
            performed_by=performed_by,
            metadata=metadata,
            created_at=created_at,
            activity_type=activity_type,
            activity_description=activity_description,
            _configuration=_configuration,
            **kwargs,
        )
