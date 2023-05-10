# intercom_python_api.model.ticket_type_attribute_list.TicketTypeAttributeList

A list of attributes associated with a given ticket type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of attributes associated with a given ticket type. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;ticket_type_attributes.list&#x60;. | [optional] 
**[ticket_type_attributes](#ticket_type_attributes)** | list, tuple,  | tuple,  | A list of ticket type attributes associated with a given ticket. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ticket_type_attributes

A list of ticket type attributes associated with a given ticket.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of ticket type attributes associated with a given ticket. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TicketTypeAttribute**](TicketTypeAttribute.md) | [**TicketTypeAttribute**](TicketTypeAttribute.md) | [**TicketTypeAttribute**](TicketTypeAttribute.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

