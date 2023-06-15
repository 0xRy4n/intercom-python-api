# intercom_python_api.model.segment_list.SegmentList

This will return a list of Segment Objects. The result may also have a pages object if the response is paginated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This will return a list of Segment Objects. The result may also have a pages object if the response is paginated. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[pages](#pages)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A pagination object, which may be empty, indicating no further pages to fetch. | [optional] 
**[segments](#segments)** | list, tuple,  | tuple,  | A list of Segment objects | [optional] 
**type** | str,  | str,  | The type of the object | [optional] must be one of ["segment.list", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pages

A pagination object, which may be empty, indicating no further pages to fetch.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A pagination object, which may be empty, indicating no further pages to fetch. | 

# segments

A list of Segment objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of Segment objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Segment**](Segment.md) | [**Segment**](Segment.md) | [**Segment**](Segment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

