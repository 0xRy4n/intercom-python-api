# intercom_python_api.model.article_statistics.ArticleStatistics

The statistics of an article.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The statistics of an article. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**conversions** | decimal.Decimal, int,  | decimal.Decimal,  | The number of conversations started from the article. | [optional] 
**happy_reaction_precentage** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of happy reactions the article has received against other types of reaction. | [optional] 
**netural_reaction_precentage** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of neutral reactions the article has received against other types of reaction. | [optional] 
**reactions** | decimal.Decimal, int,  | decimal.Decimal,  | The number of total reactions the article has received. | [optional] 
**sad_reaction_precentage** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of sad reactions the article has received against other types of reaction. | [optional] 
**type** | str,  | str,  | The type of object - &#x60;article_statistics&#x60;. | [optional] must be one of ["article_statistics", ] if omitted the server will use the default value of "article_statistics"
**views** | decimal.Decimal, int,  | decimal.Decimal,  | The number of total views the article has received. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

