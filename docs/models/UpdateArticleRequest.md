# intercom_python_api.model.update_article_request.UpdateArticleRequest

You can Update an Article

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | You can Update an Article | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | The title of the article.For multilingual articles, this will be the title of the default language&#x27;s content. | [optional] 
**description** | str,  | str,  | The description of the article. For multilingual articles, this will be the description of the default language&#x27;s content. | [optional] 
**body** | str,  | str,  | The content of the article. For multilingual articles, this will be the body of the default language&#x27;s content. | [optional] 
**author_id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the author of the article. For multilingual articles, this will be the id of the author of the default language&#x27;s content. Must be a teammate on the help center&#x27;s workspace. | [optional] 
**state** | str,  | str,  | Whether the article will be &#x60;published&#x60; or will be a &#x60;draft&#x60;. Defaults to draft. For multilingual articles, this will be the state of the default language&#x27;s content. | [optional] must be one of ["published", "draft", ] 
**parent_id** | str,  | str,  | The id of the article&#x27;s parent collection or section. An article without this field stands alone. | [optional] 
**parent_type** | str,  | str,  | The type of parent, which can either be a &#x60;collection&#x60; or &#x60;section&#x60;. | [optional] 
**translated_content** | [**ArticleTranslatedContent**](ArticleTranslatedContent.md) | [**ArticleTranslatedContent**](ArticleTranslatedContent.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

