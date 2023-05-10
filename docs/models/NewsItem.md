# intercom_python_api.model.news_item.NewsItem

A News Item is a content type in Intercom enabling you to announce product updates, company news, promotions, events and more with your customers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A News Item is a content type in Intercom enabling you to announce product updates, company news, promotions, events and more with your customers. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of object. | [optional] must be one of ["news-item", ] 
**id** | str,  | str,  | The unique identifier for the news item which is given by Intercom. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace which the news item belongs to. | [optional] 
**title** | str,  | str,  | The title of the news item. | [optional] 
**body** | str,  | str,  | The news item body, which may contain HTML. | [optional] 
**sender_id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the sender of the news item. Must be a teammate on the workspace. | [optional] 
**state** | str,  | str,  | News items will not be visible to your users in the assigned newsfeeds until they are set live. | [optional] must be one of ["draft", "live", ] 
**[newsfeed_assignments](#newsfeed_assignments)** | list, tuple,  | tuple,  | A list of newsfeed_assignments to assign to the specified newsfeed. | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  | Label names displayed to users to categorize the news item. | [optional] 
**cover_image_url** | None, str,  | NoneClass, str,  | URL of the image used as cover. Must have .jpg or .png extension. | [optional] 
**[reactions](#reactions)** | list, tuple,  | tuple,  | Ordered list of emoji reactions to the news item. When empty, reactions are disabled. | [optional] 
**deliver_silently** | bool,  | BoolClass,  | When set to true, the news item will appear in the messenger newsfeed without showing a notification badge. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp for when the news item was created. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp for when the news item was last updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# newsfeed_assignments

A list of newsfeed_assignments to assign to the specified newsfeed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of newsfeed_assignments to assign to the specified newsfeed. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NewsfeedAssignment**](NewsfeedAssignment.md) | [**NewsfeedAssignment**](NewsfeedAssignment.md) | [**NewsfeedAssignment**](NewsfeedAssignment.md) |  | 

# labels

Label names displayed to users to categorize the news item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Label names displayed to users to categorize the news item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The label name. | 

# reactions

Ordered list of emoji reactions to the news item. When empty, reactions are disabled.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ordered list of emoji reactions to the news item. When empty, reactions are disabled. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The emoji reaction to the news item. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

