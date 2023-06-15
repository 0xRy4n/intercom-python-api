# intercom_python_api.model.conversation_contacts.ConversationContacts

The list of contacts (users or leads) involved in this conversation. This will only contain one customer unless more were added via the group conversation feature.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of contacts (users or leads) involved in this conversation. This will only contain one customer unless more were added via the group conversation feature. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[contacts](#contacts)** | list, tuple,  | tuple,  | The list of contacts (users or leads) involved in this conversation. This will only contain one customer unless more were added via the group conversation feature. | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["contact.list", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contacts

The list of contacts (users or leads) involved in this conversation. This will only contain one customer unless more were added via the group conversation feature.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of contacts (users or leads) involved in this conversation. This will only contain one customer unless more were added via the group conversation feature. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Reference**](Reference.md) | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

