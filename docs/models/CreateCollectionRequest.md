# intercom_python_api.model.create_collection_request.CreateCollectionRequest

You can create a collection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | You can create a collection | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the collection. For multilingual collections, this will be the name of the default language&#x27;s content. | 
**description** | str,  | str,  | The description of the collection. For multilingual collections, this will be the description of the default language&#x27;s content. | [optional] 
**translated_content** | [**GroupTranslatedContent**](GroupTranslatedContent.md) | [**GroupTranslatedContent**](GroupTranslatedContent.md) |  | [optional] 
**parent_id** | None, str,  | NoneClass, str,  | The id of the parent collection. If &#x60;null&#x60; then it will be created as the first level collection. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

