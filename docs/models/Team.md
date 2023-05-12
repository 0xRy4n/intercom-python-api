# intercom_python_api.model.team.Team

Teams are groups of admins in Intercom.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Teams are groups of admins in Intercom. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Value is always \&quot;team\&quot; | [optional] 
**id** | str,  | str,  | The id of the team | [optional] 
**name** | str,  | str,  | The name of the team | [optional] 
**[admin_ids](#admin_ids)** | list, tuple,  | tuple,  | The list of admin IDs that are a part of the team. | [optional] 
**admin_priority_level** | [**AdminPriorityLevel**](AdminPriorityLevel.md) | [**AdminPriorityLevel**](AdminPriorityLevel.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# admin_ids

The list of admin IDs that are a part of the team.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of admin IDs that are a part of the team. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

