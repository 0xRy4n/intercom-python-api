# intercom_python_api.model.create_ticket_reply_request.CreateTicketReplyRequest

You can create a reply on a ticket.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | You can create a reply on a ticket. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**admin_id** | str,  | str,  | The id of the admin who is making the note. | 
**body** | str,  | str,  | The message body of the note, which may contain HTML. | [optional] 
**message_type** | str,  | str,  | The type of the reply. Only &#x60;note&#x60; is supported at the moment. | [optional] if omitted the server will use the default value of "note"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

