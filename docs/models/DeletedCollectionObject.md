# intercom_python_api.model.deleted_collection_object.DeletedCollectionObject

Response returned when an object is deleted

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response returned when an object is deleted | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deleted** | bool,  | BoolClass,  | Whether the collection was deleted successfully or not. | [optional] 
**id** | str,  | str,  | The unique identifier for the collection which you provided in the URL. | [optional] 
**object** | str,  | str,  | The type of object which was deleted. - &#x60;collection&#x60; | [optional] must be one of ["collection", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

