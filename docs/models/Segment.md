# intercom_python_api.model.segment.Segment

A segment is a group of your contacts defined by the rules that you set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A segment is a group of your contacts defined by the rules that you set. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of items in the user segment. It&#x27;s returned when &#x60;include_count&#x3D;true&#x60; is included in the request. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the segment was created. | [optional] 
**id** | str,  | str,  | The unique identifier representing the segment. | [optional] 
**name** | str,  | str,  | The name of the segment. | [optional] 
**person_type** | str,  | str,  | Type of the contact: contact (lead) or user. | [optional] must be one of ["contact", "user", ] 
**type** | str,  | str,  | The type of object. | [optional] must be one of ["segment", ] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the segment was updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

