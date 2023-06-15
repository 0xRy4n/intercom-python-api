# intercom_python_api.model.admin_reply_conversation_request.AdminReplyConversationRequest

Payload of the request to reply on behalf of an admin

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of an admin | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**admin_id** | str,  | str,  | The id of the admin who is authoring the comment. | 
**message_type** | str,  | str,  |  | must be one of ["comment", "note", ] 
**type** | str,  | str,  |  | must be one of ["admin", ] 
**[attachment_urls](#attachment_urls)** | list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | [optional] 
**body** | str,  | str,  | The text body of the reply.\\nNotes accept some HTML formatting.\\nMust be present for comment and note message types. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachment_urls

A list of image URLs that will be added as attachments. You can include up to 5 URLs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

