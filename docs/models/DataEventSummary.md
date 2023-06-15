# intercom_python_api.model.data_event_summary.DataEventSummary

This will return a summary of data events for the App.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This will return a summary of data events for the App. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  | The email address of the user | [optional] 
**[events](#events)** | list, tuple,  | tuple,  | A summary of data events | [optional] 
**intercom_user_id** | str,  | str,  | The Intercom user ID of the user | [optional] 
**type** | str,  | str,  | The type of the object | [optional] must be one of ["event.summary", ] 
**user_id** | str,  | str,  | The user ID of the user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# events

A summary of data events

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A summary of data events | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataEventSummaryItem**](DataEventSummaryItem.md) | [**DataEventSummaryItem**](DataEventSummaryItem.md) | [**DataEventSummaryItem**](DataEventSummaryItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

