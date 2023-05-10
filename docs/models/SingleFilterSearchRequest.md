# intercom_python_api.model.single_filter_search_request.SingleFilterSearchRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**field** | str,  | str,  | The Intercom defined id representing the company. | [optional] 
**operator** | str,  | str,  | The Intercom defined id representing the company. | [optional] must be one of ["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$", ] 
**value** | str,  | str,  | The Intercom defined id representing the company. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

