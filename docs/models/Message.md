# intercom_python_api.model.message.Message

Message are how you reach out to contacts in Intercom. They are created when an admin sends an outbound message to a contact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Message are how you reach out to contacts in Intercom. They are created when an admin sends an outbound message to a contact. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the conversation was created. | value must conform to RFC-3339 date-time
**message_type** | str,  | str,  | The type of message that was sent. Can be email, inapp, facebook or twitter. | must be one of ["email", "inapp", "facebook", "twitter", ] 
**id** | str,  | str,  | The id representing the message. | 
**body** | str,  | str,  | The message body, which may contain HTML. | 
**type** | str,  | str,  | The type of the message | 
**conversation_id** | str,  | str,  | The associated conversation_id | [optional] 
**subject** | str,  | str,  | The subject of the message. Only present if message_type: email. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

