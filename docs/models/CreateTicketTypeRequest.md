# intercom_python_api.model.create_ticket_type_request.CreateTicketTypeRequest

The request payload for creating a ticket type.   The `name` property is required.   The `icon` property can be copied easy from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/). 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The request payload for creating a ticket type.   The &#x60;name&#x60; property is required.   The &#x60;icon&#x60; property can be copied easy from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/).  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the ticket type. | 
**description** | str,  | str,  | The description of the ticket type. | [optional] 
**icon** | str,  | str,  | The icon of the ticket type. | [optional] if omitted the server will use the default value of "🎟️"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

