# intercom_python_api.model.update_ticket_type_request.UpdateTicketTypeRequest

The request payload for updating a ticket type. You can copy the `icon` property for your ticket type from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/) 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The request payload for updating a ticket type. You can copy the &#x60;icon&#x60; property for your ticket type from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the ticket type. | [optional] 
**description** | str,  | str,  | The description of the ticket type. | [optional] 
**icon** | str,  | str,  | The icon of the ticket type. | [optional] if omitted the server will use the default value of "🎟️"
**archived** | bool,  | BoolClass,  | The archived status of the ticket type. | [optional] 
**is_internal** | bool,  | BoolClass,  | Whether the tickets associated with this ticket type are intended for internal use only or will be shared with customers. This is currently a limited attribute. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

