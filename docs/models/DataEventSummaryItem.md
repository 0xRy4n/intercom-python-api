# intercom_python_api.model.data_event_summary_item.DataEventSummaryItem

This will return a summary of a data event for the App.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | This will return a summary of a data event for the App. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the event | [optional] 
**first** | str,  | str,  | The first time the event was sent | [optional] 
**last** | str,  | str,  | The last time the event was sent | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of times the event was sent | [optional] 
**description** | str,  | str,  | The description of the event | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

