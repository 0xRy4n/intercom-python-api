# intercom_python_api.model.visitor.Visitor

Visitors are useful for representing anonymous people that have not yet been identified. They usually represent website visitors. Visitors are not visible in Intercom platform. The Visitors resource provides methods to fetch, update, convert and delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Visitors are useful for representing anonymous people that have not yet been identified. They usually represent website visitors. Visitors are not visible in Intercom platform. The Visitors resource provides methods to fetch, update, convert and delete. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Value is &#x27;visitor&#x27; | [optional] if omitted the server will use the default value of "visitor"
**id** | str,  | str,  | The Intercom defined id representing the Visitor. | [optional] 
**user_id** | str,  | str,  | Automatically generated identifier for the Visitor. | [optional] 
**anonymous** | bool,  | BoolClass,  | Identifies if this visitor is anonymous. | [optional] 
**email** | str,  | str,  | The email of the visitor. | [optional] 
**phone** | None, str,  | NoneClass, str,  | The phone number of the visitor. | [optional] 
**name** | None, str,  | NoneClass, str,  | The name of the visitor. | [optional] 
**pseudonym** | None, str,  | NoneClass, str,  | The pseudonym of the visitor. | [optional] 
**[avatar](#avatar)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**app_id** | str,  | str,  | The id of the app the visitor is associated with. | [optional] 
**[companies](#companies)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[location_data](#location_data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**las_request_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the Lead last recorded making a request. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the Visitor was added to Intercom. | [optional] 
**remote_created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the Visitor was added to Intercom. | [optional] 
**signed_up_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the Visitor signed up for your product. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the Visitor was updated. | [optional] 
**session_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of sessions the Visitor has had. | [optional] 
**[social_profiles](#social_profiles)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**owner_id** | None, str,  | NoneClass, str,  | The id of the admin that owns the Visitor. | [optional] 
**unsubscribed_from_emails** | bool,  | BoolClass,  | Whether the Visitor is unsubscribed from emails. | [optional] 
**marked_email_as_spam** | bool,  | BoolClass,  | Identifies if this visitor has marked an email as spam. | [optional] 
**has_hard_bounced** | bool,  | BoolClass,  | Identifies if this visitor has had a hard bounce. | [optional] 
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[segments](#segments)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[custom_attributes](#custom_attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes you have set on the Visitor. | [optional] 
**referrer** | None, str,  | NoneClass, str,  | The referer of the visitor. | [optional] 
**utm_campaign** | None, str,  | NoneClass, str,  | The utm_campaign of the visitor. | [optional] 
**utm_content** | None, str,  | NoneClass, str,  | The utm_content of the visitor. | [optional] 
**utm_medium** | None, str,  | NoneClass, str,  | The utm_medium of the visitor. | [optional] 
**utm_source** | None, str,  | NoneClass, str,  | The utm_source of the visitor. | [optional] 
**utm_term** | None, str,  | NoneClass, str,  | The utm_term of the visitor. | [optional] 
**do_not_track** | None, bool,  | NoneClass, BoolClass,  | Identifies if this visitor has do not track enabled. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# avatar

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] if omitted the server will use the default value of "avatar"
**image_url** | None, str,  | NoneClass, str,  | This object represents the avatar associated with the visitor. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# companies

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object | [optional] must be one of ["company.list", ] 
**[companies](#companies)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# companies

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Company**](Company.md) | [**Company**](Company.md) | [**Company**](Company.md) |  | 

# location_data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] if omitted the server will use the default value of "location_data"
**city_name** | str,  | str,  | The city name of the visitor. | [optional] 
**continent_code** | str,  | str,  | The continent code of the visitor. | [optional] 
**country_code** | str,  | str,  | The country code of the visitor. | [optional] 
**country_name** | str,  | str,  | The country name of the visitor. | [optional] 
**postal_code** | str,  | str,  | The postal code of the visitor. | [optional] 
**region_name** | str,  | str,  | The region name of the visitor. | [optional] 
**timezone** | str,  | str,  | The timezone of the visitor. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# social_profiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object | [optional] must be one of ["social_profile.list", ] 
**[social_profiles](#social_profiles)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# social_profiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object | [optional] must be one of ["tag.list", ] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object | [optional] must be one of ["segment.list", ] 
**[segments](#segments)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# custom_attributes

The custom attributes you have set on the Visitor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes you have set on the Visitor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

