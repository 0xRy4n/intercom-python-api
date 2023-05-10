# intercom_python_api.model.assign_conversation_request.AssignConversationRequest

Payload of the request to assign a conversation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to assign a conversation | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**admin_id** | str,  | str,  | The id of the admin who is performing the action. | 
**message_type** | str,  | str,  |  | must be one of ["assignment", ] 
**type** | str,  | str,  |  | must be one of ["admin", "team", ] 
**assignee_id** | str,  | str,  | The &#x60;id&#x60;&#x60; of the &#x60;admin&#x60; or &#x60;team&#x60; which will be assigned the conversation.\\nA conversation can be assigned both an admin and a team.\\nSet &#x60;0&#x60; if you want this assign to no admin or team (ie. Unassigned). | 
**body** | str,  | str,  | Optionally you can leave a note in the conversation for additional context to other teammates. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

