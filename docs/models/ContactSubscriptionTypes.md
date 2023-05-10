# intercom_python_api.model.contact_subscription_types.ContactSubscriptionTypes

An object containing Subscription Types meta data about the SubscriptionTypes that a contact has.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing Subscription Types meta data about the SubscriptionTypes that a contact has. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  | This object represents the subscriptions attached to a contact. | [optional] 
**url** | str,  | str,  | Url to get more subscription type resources for this contact | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | Int representing the total number of subscription types attached to this contact | [optional] 
**has_more** | bool,  | BoolClass,  | Whether there&#x27;s more Addressable Objects to be viewed. If true, use the url to view all | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

This object represents the subscriptions attached to a contact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This object represents the subscriptions attached to a contact. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AddressableList**](AddressableList.md) | [**AddressableList**](AddressableList.md) | [**AddressableList**](AddressableList.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

