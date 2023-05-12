<a name="__pageTop"></a>
# intercom_python_api.apis.tags.tickets_api.TicketsApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tickets_id_get**](#tickets_id_get) | **get** /tickets/{id} | Retrieve a ticket
[**tickets_id_put**](#tickets_id_put) | **put** /tickets/{id} | Update a ticket
[**tickets_post**](#tickets_post) | **post** /tickets | Create a ticket
[**tickets_ticket_id_reply_post**](#tickets_ticket_id_reply_post) | **post** /tickets/{ticket_id}/reply | Create a ticket reply

# **tickets_id_get**
<a name="tickets_id_get"></a>
> Ticket tickets_id_get(id)

Retrieve a ticket

You can fetch the details of a single ticket.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.ticket import Ticket
from intercom_python_api.model.intercom_version import IntercomVersion
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
    # Retrieve a ticket
    api_response = intercom.TicketsApi.tickets_id_get(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_id_get: %s\n" % e)

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
    # Retrieve a ticket
    api_response = intercom.TicketsApi.tickets_id_get(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_id_get: %s\n" % e)

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
200 | [ApiResponseFor200](#tickets_id_get.ApiResponseFor200) | Ticket found
401 | [ApiResponseFor401](#tickets_id_get.ApiResponseFor401) | Unauthorized

#### tickets_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Ticket**](../../models/Ticket.md) |  | 


#### tickets_id_get.ApiResponseFor401
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

# **tickets_id_put**
<a name="tickets_id_put"></a>
> Ticket tickets_id_put(id)

Update a ticket

You can update a ticket.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.ticket import Ticket
from intercom_python_api.model.update_ticket_request import UpdateTicketRequest
from intercom_python_api.model.intercom_version import IntercomVersion
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
    # Update a ticket
    api_response = intercom.TicketsApi.tickets_id_put(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_id_put: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'id': "id_example",
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = UpdateTicketRequest(
        ticket_attributes=dict(),
        state="submitted",
        assignment=dict(
            admin_id="123",
            assignee_id="123",
        ),
    )
try:
    # Update a ticket
    api_response = intercom.TicketsApi.tickets_id_put(
        path_params=path_params,
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_id_put: %s\n" % e)

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
[**UpdateTicketRequest**](../../models/UpdateTicketRequest.md) |  | 


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
200 | [ApiResponseFor200](#tickets_id_put.ApiResponseFor200) | Successful response
404 | [ApiResponseFor404](#tickets_id_put.ApiResponseFor404) | Assignee not found
401 | [ApiResponseFor401](#tickets_id_put.ApiResponseFor401) | Unauthorized

#### tickets_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Ticket**](../../models/Ticket.md) |  | 


#### tickets_id_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### tickets_id_put.ApiResponseFor401
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

# **tickets_post**
<a name="tickets_post"></a>
> Ticket tickets_post()

Create a ticket

You can create a new ticket.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.ticket import Ticket
from intercom_python_api.model.create_ticket_request import CreateTicketRequest
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = CreateTicketRequest(
        ticket_type_id="1234",
        contacts=[{"id":"1234"}],
        ticket_attributes=TicketRequestCustomAttributes(
            key=None,
        ),
    )
try:
    # Create a ticket
    api_response = intercom.TicketsApi.tickets_post(
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_post: %s\n" % e)

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
[**CreateTicketRequest**](../../models/CreateTicketRequest.md) |  | 


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
200 | [ApiResponseFor200](#tickets_post.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#tickets_post.ApiResponseFor401) | Unauthorized

#### tickets_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Ticket**](../../models/Ticket.md) |  | 


#### tickets_post.ApiResponseFor401
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

# **tickets_ticket_id_reply_post**
<a name="tickets_ticket_id_reply_post"></a>
> TicketNote tickets_ticket_id_reply_post(ticket_id)

Create a ticket reply

You can create a new ticket reply. Only note is supported as a ticket reply type at the moment. > 📘 Creating ticket notes. > > All tickets have the same internal notes functionality as conversations so teammates can discuss and resolve the customer request internally. 

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.ticket_note import TicketNote
from intercom_python_api.model.create_ticket_note_request import CreateTicketNoteRequest
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'ticket_id': "ticket_id_example",
}
header_params = {
}
try:
    # Create a ticket reply
    api_response = intercom.TicketsApi.tickets_ticket_id_reply_post(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_ticket_id_reply_post: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'ticket_id': "ticket_id_example",
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = CreateTicketNoteRequest(None)
try:
    # Create a ticket reply
    api_response = intercom.TicketsApi.tickets_ticket_id_reply_post(
        path_params=path_params,
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling TicketsApi->tickets_ticket_id_reply_post: %s\n" % e)

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
[**CreateTicketNoteRequest**](../../models/CreateTicketNoteRequest.md) |  | 


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
ticket_id | TicketIdSchema | | 

# TicketIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tickets_ticket_id_reply_post.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#tickets_ticket_id_reply_post.ApiResponseFor401) | Unauthorized

#### tickets_ticket_id_reply_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TicketNote**](../../models/TicketNote.md) |  | 


#### tickets_ticket_id_reply_post.ApiResponseFor401
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

