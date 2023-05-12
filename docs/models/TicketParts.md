# intercom_python_api.model.ticket_parts.TicketParts

A list of Ticket Part objects for each note and event in the ticket. There is a limit of 500 parts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of Ticket Part objects for each note and event in the ticket. There is a limit of 500 parts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] must be one of ["ticket_part.list", ] 
**[ticket_parts](#ticket_parts)** | list, tuple,  | tuple,  | A list of Ticket Part objects for each note and even in the ticket. There is a limit of 500 parts. | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ticket_parts

A list of Ticket Part objects for each note and even in the ticket. There is a limit of 500 parts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of Ticket Part objects for each note and even in the ticket. There is a limit of 500 parts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TicketPart**](TicketPart.md) | [**TicketPart**](TicketPart.md) | [**TicketPart**](TicketPart.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

