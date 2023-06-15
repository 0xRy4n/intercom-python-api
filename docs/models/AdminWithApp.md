# intercom_python_api.model.admin_with_app.AdminWithApp

Admins are the teammate accounts that have access to a workspace

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Admins are the teammate accounts that have access to a workspace | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app** | [**App**](App.md) | [**App**](App.md) |  | [optional] 
**[avatar](#avatar)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | This object represents the avatar associated with the admin. | [optional] 
**away_mode_enabled** | bool,  | BoolClass,  | Identifies if this admin is currently set in away mode. | [optional] 
**away_mode_reassign** | bool,  | BoolClass,  | Identifies if this admin is set to automatically reassign new conversations to the apps default inbox. | [optional] 
**email** | str,  | str,  | The email of the admin. | [optional] 
**email_verified** | None, bool,  | NoneClass, BoolClass,  | Identifies if this admin&#x27;s email is verified. | [optional] 
**has_inbox_seat** | bool,  | BoolClass,  | Identifies if this admin has a paid inbox seat to restrict/allow features that require them. | [optional] 
**id** | str,  | str,  | The id representing the admin. | [optional] 
**job_title** | str,  | str,  | The job title of the admin. | [optional] 
**name** | str,  | str,  | The name of the admin. | [optional] 
**[team_ids](#team_ids)** | list, tuple,  | tuple,  | This is a list of ids of the teams that this admin is part of. | [optional] 
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;admin&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# avatar

This object represents the avatar associated with the admin.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This object represents the avatar associated with the admin. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**image_url** | None, str,  | NoneClass, str,  | This object represents the avatar associated with the admin. | [optional] 
**type** | str,  | str,  | This is a string that identifies the type of the object. It will always have the value &#x60;avatar&#x60;. | [optional] if omitted the server will use the default value of "avatar"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# team_ids

This is a list of ids of the teams that this admin is part of.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This is a list of ids of the teams that this admin is part of. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

