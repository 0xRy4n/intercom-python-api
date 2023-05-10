# intercom_python_api.model.tag.Tag

A tag allows you to label your contacts, companies, and conversations and list them using that tag.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A tag allows you to label your contacts, companies, and conversations and list them using that tag. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | value is \&quot;tag\&quot; | [optional] 
**id** | str,  | str,  | The id of the tag | [optional] 
**name** | str,  | str,  | The name of the tag | [optional] 
**applied_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the tag was applied to the object | [optional] value must conform to RFC-3339 date-time
**applied_by** | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

