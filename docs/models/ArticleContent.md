# intercom_python_api.model.article_content.ArticleContent

The Content of an Article.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The Content of an Article. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of object - &#x60;article_content&#x60; . | [optional] must be one of [None, "article_content", ] 
**title** | str,  | str,  | The title of the article. | [optional] 
**description** | str,  | str,  | The description of the article. | [optional] 
**body** | str,  | str,  | The body of the article. | [optional] 
**author_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the author of the article. | [optional] 
**state** | str,  | str,  | Whether the article is &#x60;published&#x60; or is a &#x60;draft&#x60; . | [optional] must be one of ["published", "draft", ] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the article was created. | [optional] value must conform to RFC-3339 date-time
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the article was last updated. | [optional] value must conform to RFC-3339 date-time
**url** | str,  | str,  | The URL of the article. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

