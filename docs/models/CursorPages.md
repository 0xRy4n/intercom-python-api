# intercom_python_api.model.cursor_pages.CursorPages

Cursor-based pagination is a technique used in the Intercom API to navigate through large amounts of data. A \"cursor\" or pointer is used to keep track of the current position in the result set, allowing the API to return the data in small chunks or \"pages\" as needed. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Cursor-based pagination is a technique used in the Intercom API to navigate through large amounts of data. A \&quot;cursor\&quot; or pointer is used to keep track of the current position in the result set, allowing the API to return the data in small chunks or \&quot;pages\&quot; as needed.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | [**StartingAfterPaging**](StartingAfterPaging.md) | [**StartingAfterPaging**](StartingAfterPaging.md) |  | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The current page | [optional] 
**per_page** | decimal.Decimal, int,  | decimal.Decimal,  | Number of results per page | [optional] 
**total_pages** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of pages | [optional] 
**type** | str,  | str,  | the type of object &#x60;pages&#x60;. | [optional] must be one of ["pages", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

