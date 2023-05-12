# intercom_python_api.model.contact.Contact

Contact are the objects that represent your leads and users in Intercom.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact are the objects that represent your leads and users in Intercom. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of object. | [optional] 
**id** | str,  | str,  | The unique identifier for the contact which is given by Intercom. | [optional] 
**workspace_id** | str,  | str,  | The id of the workspace which the contact belongs to. | [optional] 
**role** | str,  | str,  | The role of the contact. | [optional] 
**email** | str,  | str,  | The contacts email. | [optional] 
**phone** | None, str,  | NoneClass, str,  | The contacts phone. | [optional] 
**name** | None, str,  | NoneClass, str,  | The contacts name. | [optional] 
**owner_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of an admin that has been assigned account ownership of the contact. | [optional] 
**has_hard_bounced** | bool,  | BoolClass,  | Whether the contact has had an email sent to them hard bounce. | [optional] 
**marked_email_as_spam** | bool,  | BoolClass,  | Whether the contact has marked an email sent to them as spam. | [optional] 
**unsubscribed_from_emails** | bool,  | BoolClass,  | Whether the contact is unsubscribed from emails. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | (UNIX timestamp) The time when the contact was created. | [optional] value must conform to RFC-3339 date-time
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | (UNIX timestamp) The time when the contact was last updated. | [optional] value must conform to RFC-3339 date-time
**signed_up_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time specified for when a contact signed up. | [optional] value must conform to RFC-3339 date-time
**last_seen_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time when the contact was last seen (either where the Intercom Messenger was installed or when specified manually). | [optional] value must conform to RFC-3339 date-time
**last_replied_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time when the contact last messaged in. | [optional] value must conform to RFC-3339 date-time
**last_contacted_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time when the contact was last messaged. | [optional] value must conform to RFC-3339 date-time
**last_email_opened_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time when the contact last opened an email. | [optional] value must conform to RFC-3339 date-time
**last_email_clicked_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time when the contact last clicked a link in an email. | [optional] value must conform to RFC-3339 date-time
**language_override** | None, str,  | NoneClass, str,  | A preferred language setting for the contact, used by the Intercom Messenger even if their browser settings change. | [optional] 
**browser** | None, str,  | NoneClass, str,  | The name of the browser which the contact is using. | [optional] 
**browser_version** | None, str,  | NoneClass, str,  | The version of the browser which the contact is using. | [optional] 
**browser_language** | None, str,  | NoneClass, str,  | The language set by the browser which the contact is using. | [optional] 
**os** | None, str,  | NoneClass, str,  | The operating system which the contact is using. | [optional] 
**android_app_name** | None, str,  | NoneClass, str,  | The name of the Android app which the contact is using. | [optional] 
**android_app_version** | None, str,  | NoneClass, str,  | The version of the Android app which the contact is using. | [optional] 
**android_device** | None, str,  | NoneClass, str,  | The Android device which the contact is using. | [optional] 
**android_os_version** | None, str,  | NoneClass, str,  | The version of the Android OS which the contact is using. | [optional] 
**android_sdk_version** | None, str,  | NoneClass, str,  | The version of the Android SDK which the contact is using. | [optional] 
**android_last_seen_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The time when the contact was last seen on an Android device. | [optional] value must conform to RFC-3339 date-time
**ios_app_name** | None, str,  | NoneClass, str,  | The name of the iOS app which the contact is using. | [optional] 
**ios_app_version** | None, str,  | NoneClass, str,  | The version of the iOS app which the contact is using. | [optional] 
**ios_device** | None, str,  | NoneClass, str,  | The iOS device which the contact is using. | [optional] 
**ios_os_version** | None, str,  | NoneClass, str,  | The version of iOS which the contact is using. | [optional] 
**ios_sdk_version** | None, str,  | NoneClass, str,  | The version of the iOS SDK which the contact is using. | [optional] 
**ios_last_seen_at** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | (UNIX timestamp) The last time the contact used the iOS app. | [optional] value must conform to RFC-3339 date-time
**[custom_attributes](#custom_attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes which are set for the contact. | [optional] 
**[avatar](#avatar)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**tags** | [**ContactTags**](ContactTags.md) | [**ContactTags**](ContactTags.md) |  | [optional] 
**notes** | [**ContactNotes**](ContactNotes.md) | [**ContactNotes**](ContactNotes.md) |  | [optional] 
**companies** | [**ContactCompanies**](ContactCompanies.md) | [**ContactCompanies**](ContactCompanies.md) |  | [optional] 
**location** | [**ContactLocation**](ContactLocation.md) | [**ContactLocation**](ContactLocation.md) |  | [optional] 
**social_profiles** | [**ContactSocialProfiles**](ContactSocialProfiles.md) | [**ContactSocialProfiles**](ContactSocialProfiles.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_attributes

The custom attributes which are set for the contact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes which are set for the contact. | 

# avatar

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of object | [optional] 
**image_url** | None, str,  | NoneClass, str,  | An image URL containing the avatar of a contact. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

