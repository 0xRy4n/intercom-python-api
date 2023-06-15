# intercom_python_api.model.ticket_note.TicketNote

A Ticket Part representing a note on a ticket

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Ticket Part representing a note on a ticket | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attachments](#attachments)** | list, tuple,  | tuple,  | A list of attachments for the part. | [optional] 
**author** | [**TicketPartAuthor**](TicketPartAuthor.md) | [**TicketPartAuthor**](TicketPartAuthor.md) |  | [optional] 
**body** | None, str,  | NoneClass, str,  | The message body, which may contain HTML. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the note was created. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | The id representing the note. | [optional] 
**part_type** | str,  | str,  | Always note | [optional] must be one of ["note", ] 
**redacted** | bool,  | BoolClass,  | Whether or not the ticket part has been redacted. | [optional] 
**type** | str,  | str,  | Always ticket_part | [optional] must be one of ["ticket_part", ] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the note was updated. | [optional] value must conform to RFC-3339 date-time
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

