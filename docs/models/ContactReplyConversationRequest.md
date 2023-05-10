# intercom_python_api.model.contact_reply_conversation_request.ContactReplyConversationRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of a contact using their &#x60;intercom_user_id&#x60; | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of a contact using their &#x60;user_id&#x60; | 
[one_of_2](#one_of_2) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of a contact using their &#x60;email&#x60; | 

# one_of_0

Payload of the request to reply on behalf of a contact using their `intercom_user_id`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of a contact using their &#x60;intercom_user_id&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**intercom_user_id** | str,  | str,  | The identifier for the contact as given by Intercom. | 
**message_type** | str,  | str,  |  | must be one of ["comment", ] 
**body** | str,  | str,  | The text body of the comment. | 
**type** | str,  | str,  |  | must be one of ["user", ] 
**[attachment_urls](#attachment_urls)** | list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachment_urls

A list of image URLs that will be added as attachments. You can include up to 5 URLs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# one_of_1

Payload of the request to reply on behalf of a contact using their `user_id`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of a contact using their &#x60;user_id&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_id** | str,  | str,  | The external_id you have defined for the contact. | 
**message_type** | str,  | str,  |  | must be one of ["comment", ] 
**body** | str,  | str,  | The text body of the comment. | 
**type** | str,  | str,  |  | must be one of ["user", ] 
**[attachment_urls](#attachment_urls)** | list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachment_urls

A list of image URLs that will be added as attachments. You can include up to 5 URLs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# one_of_2

Payload of the request to reply on behalf of a contact using their `email`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload of the request to reply on behalf of a contact using their &#x60;email&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message_type** | str,  | str,  |  | must be one of ["comment", ] 
**body** | str,  | str,  | The text body of the comment. | 
**type** | str,  | str,  |  | must be one of ["user", ] 
**email** | str,  | str,  | The email you have defined for the user. | 
**[attachment_urls](#attachment_urls)** | list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachment_urls

A list of image URLs that will be added as attachments. You can include up to 5 URLs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of image URLs that will be added as attachments. You can include up to 5 URLs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

