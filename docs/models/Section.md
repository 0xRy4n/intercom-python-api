# intercom_python_api.model.section.Section

Sections are subdivisions of a collection, with a collection potentially having multiple sections.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Sections are subdivisions of a collection, with a collection potentially having multiple sections. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the section was created. For multilingual sections, this will be the timestamp of creation of the default language&#x27;s content. | [optional] value must conform to RFC-3339 date-time
**default_locale** | str,  | str,  | The default locale of the help center. This field is only returned for multilingual help centers. | [optional] 
**icon** | None, str,  | NoneClass, str,  | The icon of the section. | [optional] 
**id** | str,  | str,  | The unique identifier for the section which is given by Intercom. | [optional] 
**name** | str,  | str,  | The name of the section. For multilingual sections, this will be the name of the default language&#x27;s content. | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  | The order of the section in relation to others sections within a collection. Values go from &#x60;0&#x60;&#x60; upwards. &#x60;0&#x60;&#x60; is the default if there&#x27;s no order. | [optional] 
**[parent_id](#parent_id)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The id of the parent section. | [optional] 
**translated_content** | [**GroupTranslatedContent**](GroupTranslatedContent.md) | [**GroupTranslatedContent**](GroupTranslatedContent.md) |  | [optional] 
**type** | str,  | str,  | The type of object - &#x60;section&#x60;. | [optional] must be one of ["section", ] if omitted the server will use the default value of "section"
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the section was last updated. For multilingual sections, this will be the timestamp of last update of the default language&#x27;s content. | [optional] value must conform to RFC-3339 date-time
**url** | None, str,  | NoneClass, str,  | The URL of the section. For multilingual help centers, this will be the URL of the section for the default language. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace which the section belongs to. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parent_id

The id of the parent section.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The id of the parent section. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | decimal.Decimal, int,  | decimal.Decimal,  |  | 
[one_of_1](#one_of_1) | str,  | str,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

