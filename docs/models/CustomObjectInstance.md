# intercom_python_api.model.custom_object_instance.CustomObjectInstance

An instance of a Custom Object Type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | An instance of a Custom Object Type. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The Intercom defined id representing the custom object instance. | [optional] 
**external_id** | str,  | str,  | The id you have defined for the custom object instance. | [optional] 
**type** | str,  | str,  | The identifier of the custom object type that defines the structure of the custom object instance. | [optional] 
**[custom_attributes](#custom_attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes you have set on the custom object instance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_attributes

The custom attributes you have set on the custom object instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes you have set on the custom object instance. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

