# intercom_python_api.model.note_list.NoteList

A paginated list of notes associated with a contact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A paginated list of notes associated with a contact. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  | An array of notes. | [optional] 
**pages** | [**CursorPages**](CursorPages.md) | [**CursorPages**](CursorPages.md) |  | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | A count of the total number of notes. | [optional] 
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;list&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

An array of notes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of notes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Note**](Note.md) | [**Note**](Note.md) | [**Note**](Note.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

