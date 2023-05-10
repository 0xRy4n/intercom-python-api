# intercom_python_api.model.newsfeed.Newsfeed

A newsfeed is a collection of news items, targeted to a specific audience.  Newsfeeds currently cannot be edited through the API, please refer to [this article](https://www.intercom.com/help/en/articles/6362267-getting-started-with-news) to set up your newsfeeds in Intercom. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A newsfeed is a collection of news items, targeted to a specific audience.  Newsfeeds currently cannot be edited through the API, please refer to [this article](https://www.intercom.com/help/en/articles/6362267-getting-started-with-news) to set up your newsfeeds in Intercom.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier for the newsfeed which is given by Intercom. | [optional] 
**type** | str,  | str,  | The type of object. | [optional] must be one of ["newsfeed", ] 
**name** | str,  | str,  | The name of the newsfeed. This name will never be visible to your users. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp for when the newsfeed was created. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp for when the newsfeed was last updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

