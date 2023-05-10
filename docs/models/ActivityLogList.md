# intercom_python_api.model.activity_log_list.ActivityLogList

A paginated list of activity logs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A paginated list of activity logs. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;activity_log.list&#x60;. | [optional] 
**pages** | [**CursorPages**](CursorPages.md) | [**CursorPages**](CursorPages.md) |  | [optional] 
**[activity_logs](#activity_logs)** | list, tuple,  | tuple,  | An array of activity logs | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# activity_logs

An array of activity logs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of activity logs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ActivityLog**](ActivityLog.md) | [**ActivityLog**](ActivityLog.md) | [**ActivityLog**](ActivityLog.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

