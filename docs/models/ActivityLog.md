# intercom_python_api.model.activity_log.ActivityLog

Activities performed by admins.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Activities performed by admins. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**activity_description** | str,  | str,  | A sentence or two describing the activity. | [optional] 
**activity_type** | str,  | str,  |  | [optional] must be one of ["admin_assignment_limit_change", "admin_away_mode_change", "admin_deletion", "admin_deprovisioned", "admin_impersonation_end", "admin_impersonation_start", "admin_invite_change", "admin_invite_creation", "admin_invite_deletion", "admin_login_failure", "admin_login_success", "admin_logout", "admin_password_reset_request", "admin_password_reset_success", "admin_permission_change", "admin_provisioned", "admin_two_factor_auth_change", "admin_unauthorized_sign_in_method", "app_admin_join", "app_authentication_method_change", "app_data_deletion", "app_data_export", "app_google_sso_domain_change", "app_identity_verification_change", "app_name_change", "app_outbound_address_change", "app_package_installation", "app_package_token_regeneration", "app_package_uninstallation", "app_team_creation", "app_team_deletion", "app_team_membership_modification", "app_timezone_change", "app_webhook_creation", "app_webhook_deletion", "articles_in_messenger_enabled_change", "bulk_delete", "bulk_export", "campaign_deletion", "campaign_state_change", "conversation_part_deletion", "conversation_topic_change", "conversation_topic_creation", "conversation_topic_deletion", "help_center_settings_change", "inbound_conversations_change", "inbox_access_change", "message_deletion", "message_state_change", "messenger_look_and_feel_change", "messenger_search_required_change", "messenger_spaces_change", "office_hours_change", "role_change", "role_creation", "role_deletion", "ruleset_activation_title_preview", "ruleset_creation", "ruleset_deletion", "search_browse_enabled_change", "search_browse_required_change", "seat_change", "seat_revoke", "security_settings_change", "temporary_expectation_change", "upfront_email_collection_change", "welcome_message_change", ] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the activity was created. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | The id representing the activity. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[performed_by](#performed_by)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the admin who performed the activity. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# performed_by

An object representing the admin who performed the activity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object representing the admin who performed the activity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  | The email of the admin. | [optional] 
**id** | str,  | str,  | The id representing the admin. | [optional] 
**ip** | str,  | str,  | The IP address of the admin. | [optional] 
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;admin&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

