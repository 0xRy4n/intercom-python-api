# intercom_python_api.model.update_ticket_type_attribute_request.UpdateTicketTypeAttributeRequest

You can update a Ticket Type Attribute

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | You can update a Ticket Type Attribute | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the ticket type attribute | [optional] 
**description** | str,  | str,  | The description of the attribute presented to the teammate or contact | [optional] 
**required_to_create** | bool,  | BoolClass,  | Whether the attribute is required to be filled in when teammates are creating the ticket in Inbox. | [optional] if omitted the server will use the default value of False
**required_to_create_for_contacts** | bool,  | BoolClass,  | Whether the attribute is required to be filled in when contacts are creating the ticket in Messenger. | [optional] if omitted the server will use the default value of False
**visible_on_create** | bool,  | BoolClass,  | Whether the attribute is visible to teammates when creating a ticket in Inbox. | [optional] if omitted the server will use the default value of True
**visible_to_contacts** | bool,  | BoolClass,  | Whether the attribute is visible to contacts when creating a ticket in Messenger. | [optional] if omitted the server will use the default value of True
**multiline** | bool,  | BoolClass,  | Whether the attribute allows multiple lines of text (only applicable to string attributes) | [optional] 
**list_items** | str,  | str,  | A comma delimited list of items for the attribute value (only applicable to list attributes) | [optional] 
**allow_multiple_values** | bool,  | BoolClass,  | Whether the attribute allows multiple files to be attached to it (only applicable to file attributes) | [optional] 
**archived** | bool,  | BoolClass,  | Whether the attribute should be archived and not shown during creation of the ticket (it will still be present on previously created tickets) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

