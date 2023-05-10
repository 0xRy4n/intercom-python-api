# intercom_python_api.model.subscription_type.SubscriptionType

A subscription type lets customers easily opt out of non-essential communications without missing what's important to them.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A subscription type lets customers easily opt out of non-essential communications without missing what&#x27;s important to them. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object - subscription | [optional] 
**id** | str,  | str,  | The unique identifier representing the subscription type. | [optional] 
**state** | str,  | str,  | The state of the subscription type. | [optional] must be one of ["live", "draft", "archived", ] 
**default_translation** | [**Translation**](Translation.md) | [**Translation**](Translation.md) |  | [optional] 
**[translations](#translations)** | list, tuple,  | tuple,  | An array of translations objects with the localised version of the subscription type in each available locale within your translation settings. | [optional] 
**consent_type** | str,  | str,  | Describes the type of consent. | [optional] must be one of ["opt_out", "opt_in", ] 
**[content_types](#content_types)** | list, tuple,  | tuple,  | The message types that this subscription supports - can contain &#x60;email&#x60; or &#x60;sms_message&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# translations

An array of translations objects with the localised version of the subscription type in each available locale within your translation settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of translations objects with the localised version of the subscription type in each available locale within your translation settings. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Translation**](Translation.md) | [**Translation**](Translation.md) | [**Translation**](Translation.md) |  | 

# content_types

The message types that this subscription supports - can contain `email` or `sms_message`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The message types that this subscription supports - can contain &#x60;email&#x60; or &#x60;sms_message&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["email", "sms_message", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

