# intercom_python_api.model.data_export.DataExport

The data export api is used to view all message sent & viewed in a given timeframe.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data export api is used to view all message sent &amp; viewed in a given timeframe. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**download_expires_at** | str,  | str,  | The time after which you will not be able to access the data. | [optional] 
**download_url** | str,  | str,  | The location where you can download your data. | [optional] 
**job_identfier** | str,  | str,  | The identifier for your job. | [optional] 
**status** | str,  | str,  | The current state of your job. | [optional] must be one of ["pending", "in_progress", "failed", "completed", "no_data", "canceled", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

