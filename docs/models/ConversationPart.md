# intercom_python_api.model.conversation_part.ConversationPart

A Conversation Part represents a message in the conversation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Conversation Part represents a message in the conversation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assigned_to** | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | [optional] 
**[attachments](#attachments)** | list, tuple,  | tuple,  | A list of attachments for the part. | [optional] 
**author** | [**ConversationPartAuthor**](ConversationPartAuthor.md) | [**ConversationPartAuthor**](ConversationPartAuthor.md) |  | [optional] 
**body** | None, str,  | NoneClass, str,  | The message body, which may contain HTML. For Twitter, this will show a generic message regarding why the body is obscured. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the conversation part was created. | [optional] value must conform to RFC-3339 date-time
**external_id** | None, str,  | NoneClass, str,  | The external id of the conversation part | [optional] 
**id** | str,  | str,  | The id representing the conversation part. | [optional] 
**notified_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the user was notified with the conversation part. | [optional] value must conform to RFC-3339 date-time
**part_type** | str,  | str,  | The type of conversation part. | [optional] 
**redacted** | bool,  | BoolClass,  | Whether or not the conversation part has been redacted. | [optional] 
**type** | str,  | str,  | Always conversation_part | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the conversation part was updated. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachments

A list of attachments for the part.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of attachments for the part. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PartAttachment**](PartAttachment.md) | [**PartAttachment**](PartAttachment.md) | [**PartAttachment**](PartAttachment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

