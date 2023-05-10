# intercom_python_api.model.ticket_part.TicketPart

A Ticket Part represents a message in the ticket.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Ticket Part represents a message in the ticket. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Always ticket_part | [optional] 
**id** | str,  | str,  | The id representing the ticket part. | [optional] 
**part_type** | str,  | str,  | The type of ticket part. | [optional] 
**body** | None, str,  | NoneClass, str,  | The message body, which may contain HTML. | [optional] 
**previous_ticket_state** | str,  | str,  | The previous state of the ticket. | [optional] must be one of ["submitted", "in_progress", "waiting_on_customer", "resolved", ] 
**ticket_state** | str,  | str,  | The state of the ticket. | [optional] must be one of ["submitted", "in_progress", "waiting_on_customer", "resolved", ] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the ticket part was created. | [optional] value must conform to RFC-3339 date-time
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the ticket part was updated. | [optional] value must conform to RFC-3339 date-time
**assigned_to** | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | [optional] 
**author** | [**TicketPartAuthor**](TicketPartAuthor.md) | [**TicketPartAuthor**](TicketPartAuthor.md) |  | [optional] 
**[attachments](#attachments)** | list, tuple,  | tuple,  | A list of attachments for the part. | [optional] 
**external_id** | None, str,  | NoneClass, str,  | The external id of the ticket part | [optional] 
**redacted** | bool,  | BoolClass,  | Whether or not the ticket part has been redacted. | [optional] 
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

