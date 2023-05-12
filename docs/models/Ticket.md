# intercom_python_api.model.ticket.Ticket

Tickets are how you track requests from your users.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Tickets are how you track requests from your users. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Always ticket | [optional] must be one of ["ticket", ] if omitted the server will use the default value of "ticket"
**id** | str,  | str,  | The id representing the ticket. | [optional] 
**ticket_attributes** | [**TicketCustomAttributes**](TicketCustomAttributes.md) | [**TicketCustomAttributes**](TicketCustomAttributes.md) |  | [optional] 
**ticket_state** | str,  | str,  | The state the ticket is currenly in | [optional] must be one of ["submitted", "in_progress", "waiting_on_customer", "resolved", ] 
**ticket_type** | [**TicketType**](TicketType.md) | [**TicketType**](TicketType.md) |  | [optional] 
**contacts** | [**TicketContacts**](TicketContacts.md) | [**TicketContacts**](TicketContacts.md) |  | [optional] 
**admin_assignee_id** | str,  | str,  | The id representing the admin assigned to the ticket. | [optional] 
**team_assignee_id** | str,  | str,  | The id representing the team assigned to the ticket. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the ticket was created. | [optional] value must conform to RFC-3339 date-time
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the ticket was updated. | [optional] value must conform to RFC-3339 date-time
**ticket_parts** | [**TicketParts**](TicketParts.md) | [**TicketParts**](TicketParts.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

