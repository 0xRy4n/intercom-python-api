<a name="__pageTop"></a>
# intercom_python_api.apis.tags.subscription_types_api.SubscriptionTypesApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_subscription_type_to_contact**](#attach_subscription_type_to_contact) | **post** /contacts/{contact_id}/subscriptions | Add subscription to a contact
[**detach_subscription_type_to_contact**](#detach_subscription_type_to_contact) | **delete** /contacts/{contact_id}/subscriptions/{id} | Remove subscription from a contact
[**list_subscription_types**](#list_subscription_types) | **get** /subscription_types | List subscription types
[**list_subscriptions_for_a_contact**](#list_subscriptions_for_a_contact) | **get** /contacts/{contact_id}/subscriptions | List subscriptions for a contact

# **attach_subscription_type_to_contact**
<a name="attach_subscription_type_to_contact"></a>
> SubscriptionType attach_subscription_type_to_contact(contact_id)

Add subscription to a contact

You can add a specific subscription to a contact. In Intercom, we have two different subscription types based on user consent - opt-out and opt-in:    1.Attaching a contact to an opt-out subscription type will opt that user out from receiving messages related to that subscription type.    2.Attaching a contact to an opt-in subscription type will opt that user in to receiving messages related to that subscription type.  This will return a subscription type model for the subscription type that was added to the contact. 

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import subscription_types_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error
from intercom_python_api.model.subscription_type import SubscriptionType
from pprint import pprint
# Defining the host is optional and defaults to https://api.intercom.io
# See configuration.py for a list of all supported configuration parameters.
configuration = intercom_python_api.Configuration(
    host = "https://api.intercom.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = intercom_python_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with intercom_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = subscription_types_api.SubscriptionTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contact_id': "63a07ddf05a32042dffac965",
    }
    header_params = {
    }
    try:
        # Add subscription to a contact
        api_response = api_instance.attach_subscription_type_to_contact(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->attach_subscription_type_to_contact: %s\n" % e)

    # example passing only optional values
    path_params = {
        'contact_id': "63a07ddf05a32042dffac965",
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    body = dict(
        id="37846",
        consent_type="opt_in",
    )
    try:
        # Add subscription to a contact
        api_response = api_instance.attach_subscription_type_to_contact(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->attach_subscription_type_to_contact: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier for the subscription which is given by Intercom | 
**consent_type** | str,  | str,  | The consent_type of a subscription, opt_out or opt_in. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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
contact_id | ContactIdSchema | | 

# ContactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#attach_subscription_type_to_contact.ApiResponseFor200) | Successful
404 | [ApiResponseFor404](#attach_subscription_type_to_contact.ApiResponseFor404) | Resource not found
401 | [ApiResponseFor401](#attach_subscription_type_to_contact.ApiResponseFor401) | Unauthorized

#### attach_subscription_type_to_contact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubscriptionType**](../../models/SubscriptionType.md) |  | 


#### attach_subscription_type_to_contact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### attach_subscription_type_to_contact.ApiResponseFor401
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

# **detach_subscription_type_to_contact**
<a name="detach_subscription_type_to_contact"></a>
> SubscriptionType detach_subscription_type_to_contact(contact_idid)

Remove subscription from a contact

You can remove a specific subscription from a contact. This will return a subscription type model for the subscription type that was removed from the contact.

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import subscription_types_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error
from intercom_python_api.model.subscription_type import SubscriptionType
from pprint import pprint
# Defining the host is optional and defaults to https://api.intercom.io
# See configuration.py for a list of all supported configuration parameters.
configuration = intercom_python_api.Configuration(
    host = "https://api.intercom.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = intercom_python_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with intercom_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = subscription_types_api.SubscriptionTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contact_id': "63a07ddf05a32042dffac965",
        'id': "37846",
    }
    header_params = {
    }
    try:
        # Remove subscription from a contact
        api_response = api_instance.detach_subscription_type_to_contact(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->detach_subscription_type_to_contact: %s\n" % e)

    # example passing only optional values
    path_params = {
        'contact_id': "63a07ddf05a32042dffac965",
        'id': "37846",
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # Remove subscription from a contact
        api_response = api_instance.detach_subscription_type_to_contact(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->detach_subscription_type_to_contact: %s\n" % e)
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
contact_id | ContactIdSchema | | 
id | IdSchema | | 

# ContactIdSchema

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
200 | [ApiResponseFor200](#detach_subscription_type_to_contact.ApiResponseFor200) | Successful
404 | [ApiResponseFor404](#detach_subscription_type_to_contact.ApiResponseFor404) | Resource not found
401 | [ApiResponseFor401](#detach_subscription_type_to_contact.ApiResponseFor401) | Unauthorized

#### detach_subscription_type_to_contact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubscriptionType**](../../models/SubscriptionType.md) |  | 


#### detach_subscription_type_to_contact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### detach_subscription_type_to_contact.ApiResponseFor401
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

# **list_subscription_types**
<a name="list_subscription_types"></a>
> SubscriptionTypeList list_subscription_types()

List subscription types

You can list all subscription types. A list of subscription type objects will be returned.

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import subscription_types_api
from intercom_python_api.model.subscription_type_list import SubscriptionTypeList
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.intercom.io
# See configuration.py for a list of all supported configuration parameters.
configuration = intercom_python_api.Configuration(
    host = "https://api.intercom.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = intercom_python_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with intercom_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = subscription_types_api.SubscriptionTypesApi(api_client)

    # example passing only optional values
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List subscription types
        api_response = api_instance.list_subscription_types(
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->list_subscription_types: %s\n" % e)
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
200 | [ApiResponseFor200](#list_subscription_types.ApiResponseFor200) | Successful
401 | [ApiResponseFor401](#list_subscription_types.ApiResponseFor401) | Unauthorized

#### list_subscription_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubscriptionTypeList**](../../models/SubscriptionTypeList.md) |  | 


#### list_subscription_types.ApiResponseFor401
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

# **list_subscriptions_for_a_contact**
<a name="list_subscriptions_for_a_contact"></a>
> SubscriptionTypeList list_subscriptions_for_a_contact(contact_id)

List subscriptions for a contact

You can fetch a list of subscription types that are attached to a contact. These can be subscriptions that a user has 'opted-in' to or has 'opted-out' from, depending on the subscription type. This will return a list of Subscription Type objects that the contact is associated with.  The data property will show a combined list of:    1.Opt-out subscription types that the user has opted-out from.   2.Opt-in subscription types that the user has opted-in to receiving. 

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import subscription_types_api
from intercom_python_api.model.subscription_type_list import SubscriptionTypeList
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.intercom.io
# See configuration.py for a list of all supported configuration parameters.
configuration = intercom_python_api.Configuration(
    host = "https://api.intercom.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = intercom_python_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with intercom_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = subscription_types_api.SubscriptionTypesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contact_id': "63a07ddf05a32042dffac965",
    }
    header_params = {
    }
    try:
        # List subscriptions for a contact
        api_response = api_instance.list_subscriptions_for_a_contact(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->list_subscriptions_for_a_contact: %s\n" % e)

    # example passing only optional values
    path_params = {
        'contact_id': "63a07ddf05a32042dffac965",
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List subscriptions for a contact
        api_response = api_instance.list_subscriptions_for_a_contact(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SubscriptionTypesApi->list_subscriptions_for_a_contact: %s\n" % e)
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
contact_id | ContactIdSchema | | 

# ContactIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_subscriptions_for_a_contact.ApiResponseFor200) | Successful
404 | [ApiResponseFor404](#list_subscriptions_for_a_contact.ApiResponseFor404) | Contact not found
401 | [ApiResponseFor401](#list_subscriptions_for_a_contact.ApiResponseFor401) | Unauthorized

#### list_subscriptions_for_a_contact.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SubscriptionTypeList**](../../models/SubscriptionTypeList.md) |  | 


#### list_subscriptions_for_a_contact.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### list_subscriptions_for_a_contact.ApiResponseFor401
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

