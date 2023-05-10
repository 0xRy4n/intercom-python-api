# intercom_python_api.model.create_data_attribute_request.CreateDataAttributeRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data_type** | str,  | str,  | The type of data stored for this attribute. | must be one of ["string", "integer", "float", "boolean", "datetime", "date", ] 
**name** | str,  | str,  | The name of the data attribute. | 
**model** | str,  | str,  | The model that the data attribute belongs to. | must be one of ["contact", "company", "conversation", ] 
**description** | str,  | str,  | The readable description you see in the UI for the attribute. | [optional] 
**[options](#options)** | list, tuple,  | tuple,  | To create list attributes. Provide a set of hashes with &#x60;value&#x60; as the key of the options you want to make. &#x60;data_type&#x60; must be &#x60;string&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# options

To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | To create list attributes. Provide a set of hashes with &#x60;value&#x60; as the key of the options you want to make. &#x60;data_type&#x60; must be &#x60;string&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

