# intercom_python_api.model.conversation_source.ConversationSource

The Conversation Part that originated this conversation, which can be Contact, Admin, Campaign, Automated or Operator initiated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Conversation Part that originated this conversation, which can be Contact, Admin, Campaign, Automated or Operator initiated. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attachments](#attachments)** | list, tuple,  | tuple,  | A list of attachments for the part. | [optional] 
**author** | [**ConversationPartAuthor**](ConversationPartAuthor.md) | [**ConversationPartAuthor**](ConversationPartAuthor.md) |  | [optional] 
**body** | str,  | str,  | The message body, which may contain HTML. For Twitter, this will show a generic message regarding why the body is obscured. | [optional] 
**delivered_as** | str,  | str,  | The conversation&#x27;s initiation type. Possible values are customer_initiated, campaigns_initiated (legacy campaigns), operator_initiated (Custom bot), automated (Series and other outbounds with dynamic audience message) and admin_initiated (fixed audience message, ticket initiated by an admin, group email). | [optional] 
**id** | str,  | str,  | The id representing the message. | [optional] 
**redacted** | bool,  | BoolClass,  | Whether or not the source message has been redacted. Only applicable for contact initiated messages. | [optional] 
**subject** | str,  | str,  | Optional. The message subject. For Twitter, this will show a generic message regarding why the subject is obscured. | [optional] 
**type** | str,  | str,  | This includes conversation, push, facebook, twitter and email. | [optional] 
**url** | None, str,  | NoneClass, str,  | The URL where the conversation was started. For Twitter, Email, and Bots, this will be blank. | [optional] 
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

