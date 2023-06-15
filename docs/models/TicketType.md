# intercom_python_api.model.ticket_type.TicketType

A ticket type, used to define the data fields to be captured in a ticket.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A ticket type, used to define the data fields to be captured in a ticket. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**archived** | bool,  | BoolClass,  | Whether the ticket type is archived or not. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The date and time the ticket type was created. | [optional] 
**description** | str,  | str,  | The description of the ticket type | [optional] 
**icon** | str,  | str,  | The icon of the ticket type | [optional] 
**id** | str,  | str,  | The id representing the ticket type. | [optional] 
**name** | str,  | str,  | The name of the ticket type | [optional] 
**ticket_type_attributes** | [**TicketTypeAttributeList**](TicketTypeAttributeList.md) | [**TicketTypeAttributeList**](TicketTypeAttributeList.md) |  | [optional] 
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;ticket_type&#x60;. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The date and time the ticket type was last updated. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace that the ticket type belongs to. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

