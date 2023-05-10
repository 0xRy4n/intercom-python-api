# intercom_python_api.model.news_item_request.NewsItemRequest

A News Item is a content type in Intercom enabling you to announce product updates, company news, promotions, events and more with your customers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A News Item is a content type in Intercom enabling you to announce product updates, company news, promotions, events and more with your customers. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | The title of the news item. | 
**sender_id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the sender of the news item. Must be a teammate on the workspace. | 
**body** | str,  | str,  | The news item body, which may contain HTML. | [optional] 
**state** | str,  | str,  | News items will not be visible to your users in the assigned newsfeeds until they are set live. | [optional] must be one of ["draft", "live", ] 
**deliver_silently** | bool,  | BoolClass,  | When set to &#x60;true&#x60;, the news item will appear in the messenger newsfeed without showing a notification badge. | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  | Label names displayed to users to categorize the news item. | [optional] 
**[reactions](#reactions)** | list, tuple,  | tuple,  | Ordered list of emoji reactions to the news item. When empty, reactions are disabled. | [optional] 
**[newsfeed_assignments](#newsfeed_assignments)** | list, tuple,  | tuple,  | A list of newsfeed_assignments to assign to the specified newsfeed. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# labels

Label names displayed to users to categorize the news item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Label names displayed to users to categorize the news item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reactions

Ordered list of emoji reactions to the news item. When empty, reactions are disabled.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ordered list of emoji reactions to the news item. When empty, reactions are disabled. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

