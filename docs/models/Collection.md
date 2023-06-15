# intercom_python_api.model.collection.Collection

Collections are top level containers for Articles within the Help Center.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collections are top level containers for Articles within the Help Center. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the article was created. For multilingual articles, this will be the timestamp of creation of the default language&#x27;s content. | [optional] value must conform to RFC-3339 date-time
**default_locale** | str,  | str,  | The default locale of the help center. This field is only returned for multilingual help centers. | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the collection. For multilingual help centers, this will be the description of the collection for the default language. | [optional] 
**icon** | None, str,  | NoneClass, str,  | The icon of the collection. | [optional] 
**id** | str,  | str,  | The unique identifier for the collection which is given by Intercom. | [optional] 
**name** | str,  | str,  | The name of the collection. For multilingual collections, this will be the name of the default language&#x27;s content. | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  | The order of the section in relation to others sections within a collection. Values go from &#x60;0&#x60;&#x60; upwards. &#x60;0&#x60;&#x60; is the default if there&#x27;s no order. | [optional] 
**translated_content** | [**GroupTranslatedContent**](GroupTranslatedContent.md) | [**GroupTranslatedContent**](GroupTranslatedContent.md) |  | [optional] 
**type** | str,  | str,  | The type of object - &#x60;collection&#x60;. | [optional] must be one of ["collection", ] if omitted the server will use the default value of "collection"
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the article was last updated. For multilingual articles, this will be the timestamp of last update of the default language&#x27;s content. | [optional] value must conform to RFC-3339 date-time
**url** | None, str,  | NoneClass, str,  | The URL of the collection. For multilingual help centers, this will be the URL of the collection for the default language. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace which the collection belongs to. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

