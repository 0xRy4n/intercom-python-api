# intercom_python_api.model.close_conversation_request.CloseConversationRequest

Payload of the request to close a conversation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to close a conversation | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**admin_id** | str,  | str,  | The id of the admin who is performing the action. | 
**message_type** | str,  | str,  |  | must be one of ["close", ] 
**type** | str,  | str,  |  | must be one of ["admin", ] 
**body** | str,  | str,  | Optionally you can leave a message in the conversation to provide additional context to the user and other teammates. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

