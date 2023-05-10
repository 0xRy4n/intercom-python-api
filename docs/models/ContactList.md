# intercom_python_api.model.contact_list.ContactList

Contacts are your users in Intercom.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contacts are your users in Intercom. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Always list | [optional] must be one of ["list", ] 
**[data](#data)** | list, tuple,  | tuple,  | The list of contact objects | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | A count of the total number of objects. | [optional] 
**pages** | [**CursorPages**](CursorPages.md) | [**CursorPages**](CursorPages.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

The list of contact objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of contact objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Contact**](Contact.md) | [**Contact**](Contact.md) | [**Contact**](Contact.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

