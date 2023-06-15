# intercom_python_api.model.file_attribute.FileAttribute

The value describing a file upload set for a custom attribute

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The value describing a file upload set for a custom attribute | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**content_type** | str,  | str,  | The type of file | [optional] 
**filesize** | decimal.Decimal, int,  | decimal.Decimal,  | The size of the file in bytes | [optional] 
**height** | decimal.Decimal, int,  | decimal.Decimal,  | The height of the file in pixels, if applicable | [optional] 
**name** | str,  | str,  | The name of the file | [optional] 
**type** | str,  | str,  |  | [optional] 
**url** | str,  | str,  | The url of the file. This is a temporary URL and will expire after 30 minutes. | [optional] 
**width** | decimal.Decimal, int,  | decimal.Decimal,  | The width of the file in pixels, if applicable | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

