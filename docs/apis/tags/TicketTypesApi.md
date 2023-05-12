<a name="__pageTop"></a>
# intercom_python_api.apis.tags.ticket_types_api.TicketTypesApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_types_get**](#ticket_types_get) | **get** /ticket_types | List all ticket types
[**ticket_types_id_get**](#ticket_types_id_get) | **get** /ticket_types/{id} | Retrieve a ticket type
[**ticket_types_id_put**](#ticket_types_id_put) | **put** /ticket_types/{id} | Update a ticket type
[**ticket_types_post**](#ticket_types_post) | **post** /ticket_types | Create a ticket type

# **ticket_types_get**
<a name="ticket_types_get"></a>
> TicketTypeList ticket_types_get()

List all ticket types

You can get a list of all ticket types for a workspace.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.ticket_type_list import TicketTypeList
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
try:
    # List all ticket types
    api_response = intercom.TicketTypesApi.ticket_types_get(
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_get: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Intercom-Version | IntercomVersionSchema | | optional

# IntercomVersionSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**IntercomVersion**](../../models/IntercomVersion.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ticket_types_get.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#ticket_types_get.ApiResponseFor401) | Unauthorized

#### ticket_types_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketTypeList**](../../models/TicketTypeList.md) |  | 


#### ticket_types_get.ApiResponseFor401
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

# **ticket_types_id_get**
<a name="ticket_types_id_get"></a>
> TicketType ticket_types_id_get(id)

Retrieve a ticket type

You can fetch the details of a single ticket type.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.ticket_type import TicketType
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'id': "id_example",
}
header_params = {
}
try:
    # Retrieve a ticket type
    api_response = intercom.TicketTypesApi.ticket_types_id_get(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_id_get: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'id': "id_example",
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
try:
    # Retrieve a ticket type
    api_response = intercom.TicketTypesApi.ticket_types_id_get(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_id_get: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ticket_types_id_get.ApiResponseFor200) | Ticket type found
401 | [ApiResponseFor401](#ticket_types_id_get.ApiResponseFor401) | Unauthorized

#### ticket_types_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketType**](../../models/TicketType.md) |  | 


#### ticket_types_id_get.ApiResponseFor401
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

# **ticket_types_id_put**
<a name="ticket_types_id_put"></a>
> TicketType ticket_types_id_put(id)

Update a ticket type

 You can update a ticket type.  > 📘 Updating a ticket type. > > For the `icon` propery, use an emoji from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/) 

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.ticket_type import TicketType
from intercom_python_api.model.update_ticket_type_request import UpdateTicketTypeRequest
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'id': "id_example",
}
header_params = {
}
try:
    # Update a ticket type
    api_response = intercom.TicketTypesApi.ticket_types_id_put(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_id_put: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'id': "id_example",
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = UpdateTicketTypeRequest(
        name="Bug",
        description="A bug has been occured",
        icon="🐞",
        archived=False,
        is_internal=False,
    )
try:
    # Update a ticket type
    api_response = intercom.TicketTypesApi.ticket_types_id_put(
        path_params=path_params,
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_id_put: %s\n" % e)

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
[**UpdateTicketTypeRequest**](../../models/UpdateTicketTypeRequest.md) |  | 


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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ticket_types_id_put.ApiResponseFor200) | Ticket type updated
401 | [ApiResponseFor401](#ticket_types_id_put.ApiResponseFor401) | Unauthorized

#### ticket_types_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketType**](../../models/TicketType.md) |  | 


#### ticket_types_id_put.ApiResponseFor401
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

# **ticket_types_post**
<a name="ticket_types_post"></a>
> TicketType ticket_types_post()

Create a ticket type

You can create a new ticket type. > 📘 Creating ticket types. > > Every ticket type will be created with two default attributes: _default_title_ and _default_description_. > For the `icon` propery, use an emoji from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/) 

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.create_ticket_type_request import CreateTicketTypeRequest
from intercom_python_api.model.ticket_type import TicketType
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = CreateTicketTypeRequest(
        name="Bug",
        description="Used for tracking bugs",
        icon="🐞",
        is_internal=False,
    )
try:
    # Create a ticket type
    api_response = intercom.TicketTypesApi.ticket_types_post(
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_post: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTicketTypeRequest**](../../models/CreateTicketTypeRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Intercom-Version | IntercomVersionSchema | | optional

# IntercomVersionSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**IntercomVersion**](../../models/IntercomVersion.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ticket_types_post.ApiResponseFor200) | Ticket type created
401 | [ApiResponseFor401](#ticket_types_post.ApiResponseFor401) | Unauthorized

#### ticket_types_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketType**](../../models/TicketType.md) |  | 


#### ticket_types_post.ApiResponseFor401
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

