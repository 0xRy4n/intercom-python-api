# intercom_python_api.model.collection_list.CollectionList

This will return a list of Collections for the App.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This will return a list of Collections for the App. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object - &#x60;list&#x60;. | [optional] must be one of ["list", ] 
**pages** | [**CursorPages**](CursorPages.md) | [**CursorPages**](CursorPages.md) |  | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | A count of the total number of collections. | [optional] 
**[data](#data)** | list, tuple,  | tuple,  | An array of collection objects | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

An array of collection objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of collection objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Collection**](Collection.md) | [**Collection**](Collection.md) | [**Collection**](Collection.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

