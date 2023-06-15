# intercom_python_api.model.update_contact_request.UpdateContactRequest

You can update a contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | You can update a contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**avatar** | None, str,  | NoneClass, str,  | An image URL containing the avatar of a contact | [optional] 
**[custom_attributes](#custom_attributes)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The custom attributes which are set for the contact | [optional] 
**email** | str,  | str,  | The contacts email | [optional] 
**external_id** | str,  | str,  | A unique identifier for the contact which is given to Intercom | [optional] 
**last_seen_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The time when the contact was last seen (either where the Intercom Messenger was installed or when specified manually) | [optional] value must conform to RFC-3339 date-time
**name** | None, str,  | NoneClass, str,  | The contacts name | [optional] 
**owner_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of an admin that has been assigned account ownership of the contact | [optional] 
**phone** | None, str,  | NoneClass, str,  | The contacts phone | [optional] 
**role** | str,  | str,  | The role of the contact. | [optional] 
**signed_up_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The time specified for when a contact signed up | [optional] value must conform to RFC-3339 date-time
**unsubscribed_from_emails** | None, bool,  | NoneClass, BoolClass,  | Whether the contact is unsubscribed from emails | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_attributes

The custom attributes which are set for the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The custom attributes which are set for the contact | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

