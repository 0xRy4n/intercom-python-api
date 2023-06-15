# intercom_python_api.model.admin.Admin

Admins are teammate accounts that have access to a workspace.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Admins are teammate accounts that have access to a workspace. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**avatar** | None, str,  | NoneClass, str,  | Image for the associated team or teammate | [optional] 
**away_mode_enabled** | bool,  | BoolClass,  | Identifies if this admin is currently set in away mode. | [optional] 
**away_mode_reassign** | bool,  | BoolClass,  | Identifies if this admin is set to automatically reassign new conversations to the apps default inbox. | [optional] 
**email** | str,  | str,  | The email of the admin. | [optional] 
**has_inbox_seat** | bool,  | BoolClass,  | Identifies if this admin has a paid inbox seat to restrict/allow features that require them. | [optional] 
**id** | str,  | str,  | The id representing the admin. | [optional] 
**job_title** | str,  | str,  | The job title of the admin. | [optional] 
**name** | str,  | str,  | The name of the admin. | [optional] 
**[team_ids](#team_ids)** | list, tuple,  | tuple,  | This object represents the avatar associated with the admin. | [optional] 
**team_priority_level** | [**TeamPriorityLevel**](TeamPriorityLevel.md) | [**TeamPriorityLevel**](TeamPriorityLevel.md) |  | [optional] 
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;admin&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# team_ids

This object represents the avatar associated with the admin.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This object represents the avatar associated with the admin. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

