<a name="__pageTop"></a>
# intercom_python_api.apis.tags.ticket_type_attributes_api.TicketTypeAttributesApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ticket_type_attribute**](#create_ticket_type_attribute) | **post** /ticket_types/{ticket_type_id}/attributes | Create a new attribute for a ticket type
[**update_ticket_type_attribute**](#update_ticket_type_attribute) | **put** /ticket_types/{ticket_type_id}/attributes/{id} | Update an existing attribute for a ticket type

# **create_ticket_type_attribute**
<a name="create_ticket_type_attribute"></a>
> TicketTypeAttribute create_ticket_type_attribute(ticket_type_id)

Create a new attribute for a ticket type

You can create a new attribute for a ticket type.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.ticket_type_attribute import TicketTypeAttribute
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.create_ticket_type_attribute_request import CreateTicketTypeAttributeRequest
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'ticket_type_id': "ticket_type_id_example",
}
header_params = {
}
try:
    # Create a new attribute for a ticket type
    api_response = intercom.TicketTypeAttributesApi.create_ticket_type_attribute(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypeAttributesApi->create_ticket_type_attribute: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'ticket_type_id': "ticket_type_id_example",
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = CreateTicketTypeAttributeRequest(
        name="Bug Priority",
        description="Priority level of the bug",
        data_type="string",
        required_to_create=False,
        required_to_create_for_contacts=False,
        visible_on_create=True,
        visible_to_contacts=True,
        multiline=False,
        list_items="Low Priority,Medium Priority,High Priority",
        allow_multiple_values=False,
    )
try:
    # Create a new attribute for a ticket type
    api_response = intercom.TicketTypeAttributesApi.create_ticket_type_attribute(
        path_params=path_params,
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypeAttributesApi->create_ticket_type_attribute: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTicketTypeAttributeRequest**](../../models/CreateTicketTypeAttributeRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Intercom-Version | IntercomVersionSchema | | optional

# IntercomVersionSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**IntercomVersion**](../../models/IntercomVersion.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ticket_type_id | TicketTypeIdSchema | | 

# TicketTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_ticket_type_attribute.ApiResponseFor200) | Ticket Type Attribute created
401 | [ApiResponseFor401](#create_ticket_type_attribute.ApiResponseFor401) | Unauthorized

#### create_ticket_type_attribute.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketTypeAttribute**](../../models/TicketTypeAttribute.md) |  | 


#### create_ticket_type_attribute.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_ticket_type_attribute**
<a name="update_ticket_type_attribute"></a>
> TicketTypeAttribute update_ticket_type_attribute(ticket_type_idid)

Update an existing attribute for a ticket type

You can update an existing attribute for a ticket type.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.update_ticket_type_attribute_request import UpdateTicketTypeAttributeRequest
from intercom_python_api.model.ticket_type_attribute import TicketTypeAttribute
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'ticket_type_id': "ticket_type_id_example",
    'id': "id_example",
}
header_params = {
}
try:
    # Update an existing attribute for a ticket type
    api_response = intercom.TicketTypeAttributesApi.update_ticket_type_attribute(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypeAttributesApi->update_ticket_type_attribute: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'ticket_type_id': "ticket_type_id_example",
    'id': "id_example",
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = UpdateTicketTypeAttributeRequest(
        name="Bug Priority",
        description="Priority level of the bug",
        required_to_create=False,
        required_to_create_for_contacts=False,
        visible_on_create=True,
        visible_to_contacts=True,
        multiline=False,
        list_items="Low Priority,Medium Priority,High Priority",
        allow_multiple_values=False,
        archived=False,
    )
try:
    # Update an existing attribute for a ticket type
    api_response = intercom.TicketTypeAttributesApi.update_ticket_type_attribute(
        path_params=path_params,
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypeAttributesApi->update_ticket_type_attribute: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateTicketTypeAttributeRequest**](../../models/UpdateTicketTypeAttributeRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Intercom-Version | IntercomVersionSchema | | optional

# IntercomVersionSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**IntercomVersion**](../../models/IntercomVersion.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ticket_type_id | TicketTypeIdSchema | | 
id | IdSchema | | 

# TicketTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_ticket_type_attribute.ApiResponseFor200) | Ticket Type Attribute updated
401 | [ApiResponseFor401](#update_ticket_type_attribute.ApiResponseFor401) | Unauthorized

#### update_ticket_type_attribute.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketTypeAttribute**](../../models/TicketTypeAttribute.md) |  | 


#### update_ticket_type_attribute.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

