# intercom_python_api.model.article.Article

The Articles API is a central place to gather all information and take actions on your articles. Articles can live within collections and sections, or alternatively they can stand alone.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Articles API is a central place to gather all information and take actions on your articles. Articles can live within collections and sections, or alternatively they can stand alone. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of object - &#x60;article&#x60;. | [optional] must be one of ["article", ] if omitted the server will use the default value of "article"
**id** | str,  | str,  | The unique identifier for the article which is given by Intercom. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace which the article belongs to. | [optional] 
**title** | str,  | str,  | The title of the article. For multilingual articles, this will be the title of the default language&#x27;s content. | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the article. For multilingual articles, this will be the description of the default language&#x27;s content. | [optional] 
**body** | None, str,  | NoneClass, str,  | The body of the article in HTML. For multilingual articles, this will be the body of the default language&#x27;s content. | [optional] 
**author_id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the author of the article. For multilingual articles, this will be the id of the author of the default language&#x27;s content. Must be a teammate on the help center&#x27;s workspace. | [optional] 
**state** | str,  | str,  | Whether the article is &#x60;published&#x60; or is a &#x60;draft&#x60;. For multilingual articles, this will be the state of the default language&#x27;s content. | [optional] must be one of ["published", "draft", ] if omitted the server will use the default value of "draft"
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the article was created. For multilingual articles, this will be the timestamp of creation of the default language&#x27;s content. | [optional] value must conform to RFC-3339 date-time
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time when the article was last updated. For multilingual articles, this will be the timestamp of last update of the default language&#x27;s content. | [optional] value must conform to RFC-3339 date-time
**url** | None, str,  | NoneClass, str,  | The URL of the article. For multilingual articles, this will be the URL of the default language&#x27;s content. | [optional] 
**parent_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the article&#x27;s parent collection or section. An article without this field stands alone. | [optional] 
**parent_type** | None, str,  | NoneClass, str,  | The type of parent, which can either be a &#x60;collection&#x60; or &#x60;section&#x60;. | [optional] 
**default_locale** | str,  | str,  | The default locale of the help center. This field is only returned for multilingual help centers. | [optional] 
**translated_content** | [**ArticleTranslatedContent**](ArticleTranslatedContent.md) | [**ArticleTranslatedContent**](ArticleTranslatedContent.md) |  | [optional] 
**statistics** | [**ArticleStatistics**](ArticleStatistics.md) | [**ArticleStatistics**](ArticleStatistics.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

