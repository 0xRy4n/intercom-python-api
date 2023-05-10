# intercom_python_api.model.create_data_exports_request.CreateDataExportsRequest

Request for creating a data export

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request for creating a data export | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at_before** | decimal.Decimal, int,  | decimal.Decimal,  | The end date that you request data for. It must be formatted as a unix timestamp. | 
**created_at_after** | decimal.Decimal, int,  | decimal.Decimal,  | The start date that you request data for. It must be formatted as a unix timestamp. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

