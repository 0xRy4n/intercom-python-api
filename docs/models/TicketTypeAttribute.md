# intercom_python_api.model.ticket_type_attribute.TicketTypeAttribute

Ticket type attribute, used to define each data field to be captured in a ticket.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Ticket type attribute, used to define each data field to be captured in a ticket. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;ticket_type_attribute&#x60;. | [optional] 
**id** | str,  | str,  | The id representing the ticket type attribute. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace that the ticket type attribute belongs to. | [optional] 
**name** | str,  | str,  | The name of the ticket type attribute | [optional] 
**description** | str,  | str,  | The description of the ticket type attribute | [optional] 
**data_type** | str,  | str,  | The type of the data attribute (allowed values: \&quot;string list integer decimal boolean datetime files\&quot;) | [optional] 
**[input_options](#input_options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Input options for the attribute | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  | The order of the attribute against other attributes | [optional] 
**required_to_create** | bool,  | BoolClass,  | Whether the attribute is required or not for teammates. | [optional] if omitted the server will use the default value of False
**required_to_create_for_contacts** | bool,  | BoolClass,  | Whether the attribute is required or not for contacts. | [optional] if omitted the server will use the default value of False
**visible_on_create** | bool,  | BoolClass,  | Whether the attribute is visible or not to teammates. | [optional] if omitted the server will use the default value of True
**visible_to_contacts** | bool,  | BoolClass,  | Whether the attribute is visible or not to contacts. | [optional] if omitted the server will use the default value of True
**default** | bool,  | BoolClass,  | Whether the attribute is built in or not. | [optional] 
**ticket_type_id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the ticket type that the attribute belongs to. | [optional] 
**archived** | bool,  | BoolClass,  | Whether the ticket type attribute is archived or not. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The date and time the ticket type attribute was created. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The date and time the ticket type attribute was last updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# input_options

Input options for the attribute

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Input options for the attribute | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

