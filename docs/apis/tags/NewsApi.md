<a name="__pageTop"></a>
# intercom_python_api.apis.tags.news_api.NewsApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_news_item**](#create_news_item) | **post** /news/news_items | Create a news item
[**delete_news_item**](#delete_news_item) | **delete** /news/news_items/{id} | Delete a news item
[**list_live_newsfeed_items**](#list_live_newsfeed_items) | **get** /news/newsfeeds/{id}/items | List all live newsfeed items
[**list_news_items**](#list_news_items) | **get** /news/news_items | List all news items
[**list_newsfeeds**](#list_newsfeeds) | **get** /news/newsfeeds | List all newsfeeds
[**retrieve_news_item**](#retrieve_news_item) | **get** /news/news_items/{id} | Retrieve a news item
[**retrieve_newsfeed**](#retrieve_newsfeed) | **get** /news/newsfeeds/{id} | Retrieve a newsfeed
[**update_news_item**](#update_news_item) | **put** /news/news_items/{id} | Update a news item

# **create_news_item**
<a name="create_news_item"></a>
> NewsItem create_news_item()

Create a news item

You can create a news item

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.news_item_request import NewsItemRequest
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.news_item import NewsItem
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only optional values
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    body = NewsItemRequest(
        title="Halloween is here!",
        body="<p>New costumes in store for this spooky season</p>",
        sender_id=123,
        state="live",
        deliver_silently=True,
        labels=["Product","Update","New"],
        reactions=["😆","😅"],
        newsfeed_assignments=[
            NewsfeedAssignment(
                newsfeed_id=198313,
                published_at=1674917488,
            )
        ],
    )
    try:
        # Create a news item
        api_response = api_instance.create_news_item(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->create_news_item: %s\n" % e)
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
[**NewsItemRequest**](../../models/NewsItemRequest.md) |  | 


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
200 | [ApiResponseFor200](#create_news_item.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#create_news_item.ApiResponseFor401) | Unauthorized

#### create_news_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NewsItem**](../../models/NewsItem.md) |  | 


#### create_news_item.ApiResponseFor401
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

# **delete_news_item**
<a name="delete_news_item"></a>
> DeletedObject delete_news_item(id)

Delete a news item

You can delete a single news item.

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.deleted_object import DeletedObject
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 123,
    }
    header_params = {
    }
    try:
        # Delete a news item
        api_response = api_instance.delete_news_item(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->delete_news_item: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 123,
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # Delete a news item
        api_response = api_instance.delete_news_item(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->delete_news_item: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_news_item.ApiResponseFor200) | successful
404 | [ApiResponseFor404](#delete_news_item.ApiResponseFor404) | News Item Not Found
401 | [ApiResponseFor401](#delete_news_item.ApiResponseFor401) | Unauthorized

#### delete_news_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeletedObject**](../../models/DeletedObject.md) |  | 


#### delete_news_item.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### delete_news_item.ApiResponseFor401
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

# **list_live_newsfeed_items**
<a name="list_live_newsfeed_items"></a>
> PaginatedResponse list_live_newsfeed_items(id)

List all live newsfeed items

You can fetch a list of all news items that are live on a given newsfeed

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.paginated_response import PaginatedResponse
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # List all live newsfeed items
        api_response = api_instance.list_live_newsfeed_items(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->list_live_newsfeed_items: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List all live newsfeed items
        api_response = api_instance.list_live_newsfeed_items(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->list_live_newsfeed_items: %s\n" % e)
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
200 | [ApiResponseFor200](#list_live_newsfeed_items.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#list_live_newsfeed_items.ApiResponseFor401) | Unauthorized

#### list_live_newsfeed_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedResponse**](../../models/PaginatedResponse.md) |  | 


#### list_live_newsfeed_items.ApiResponseFor401
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

# **list_news_items**
<a name="list_news_items"></a>
> PaginatedResponse list_news_items()

List all news items

You can fetch a list of all news items

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.paginated_response import PaginatedResponse
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only optional values
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List all news items
        api_response = api_instance.list_news_items(
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->list_news_items: %s\n" % e)
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
200 | [ApiResponseFor200](#list_news_items.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#list_news_items.ApiResponseFor401) | Unauthorized

#### list_news_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedResponse**](../../models/PaginatedResponse.md) |  | 


#### list_news_items.ApiResponseFor401
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

# **list_newsfeeds**
<a name="list_newsfeeds"></a>
> PaginatedResponse list_newsfeeds()

List all newsfeeds

You can fetch a list of all newsfeeds

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.paginated_response import PaginatedResponse
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only optional values
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List all newsfeeds
        api_response = api_instance.list_newsfeeds(
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->list_newsfeeds: %s\n" % e)
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
200 | [ApiResponseFor200](#list_newsfeeds.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#list_newsfeeds.ApiResponseFor401) | Unauthorized

#### list_newsfeeds.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedResponse**](../../models/PaginatedResponse.md) |  | 


#### list_newsfeeds.ApiResponseFor401
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

# **retrieve_news_item**
<a name="retrieve_news_item"></a>
> NewsItem retrieve_news_item(id)

Retrieve a news item

You can fetch the details of a single news item.

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.news_item import NewsItem
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 123,
    }
    header_params = {
    }
    try:
        # Retrieve a news item
        api_response = api_instance.retrieve_news_item(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->retrieve_news_item: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 123,
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # Retrieve a news item
        api_response = api_instance.retrieve_news_item(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->retrieve_news_item: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_news_item.ApiResponseFor200) | successful
404 | [ApiResponseFor404](#retrieve_news_item.ApiResponseFor404) | News Item Not Found
401 | [ApiResponseFor401](#retrieve_news_item.ApiResponseFor401) | Unauthorized

#### retrieve_news_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NewsItem**](../../models/NewsItem.md) |  | 


#### retrieve_news_item.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### retrieve_news_item.ApiResponseFor401
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

# **retrieve_newsfeed**
<a name="retrieve_newsfeed"></a>
> Newsfeed retrieve_newsfeed(id)

Retrieve a newsfeed

You can fetch the details of a single newsfeed

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.newsfeed import Newsfeed
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # Retrieve a newsfeed
        api_response = api_instance.retrieve_newsfeed(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->retrieve_newsfeed: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # Retrieve a newsfeed
        api_response = api_instance.retrieve_newsfeed(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->retrieve_newsfeed: %s\n" % e)
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
200 | [ApiResponseFor200](#retrieve_newsfeed.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#retrieve_newsfeed.ApiResponseFor401) | Unauthorized

#### retrieve_newsfeed.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Newsfeed**](../../models/Newsfeed.md) |  | 


#### retrieve_newsfeed.ApiResponseFor401
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

# **update_news_item**
<a name="update_news_item"></a>
> NewsItem update_news_item(id)

Update a news item

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import news_api
from intercom_python_api.model.news_item_request import NewsItemRequest
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.news_item import NewsItem
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
    api_instance = news_api.NewsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 123,
    }
    header_params = {
    }
    try:
        # Update a news item
        api_response = api_instance.update_news_item(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->update_news_item: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 123,
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    body = NewsItemRequest(
        title="Halloween is here!",
        body="<p>New costumes in store for this spooky season</p>",
        sender_id=123,
        state="live",
        deliver_silently=True,
        labels=["Product","Update","New"],
        reactions=["😆","😅"],
        newsfeed_assignments=[
            NewsfeedAssignment(
                newsfeed_id=198313,
                published_at=1674917488,
            )
        ],
    )
    try:
        # Update a news item
        api_response = api_instance.update_news_item(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling NewsApi->update_news_item: %s\n" % e)
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
[**NewsItemRequest**](../../models/NewsItemRequest.md) |  | 


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
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_news_item.ApiResponseFor200) | successful
404 | [ApiResponseFor404](#update_news_item.ApiResponseFor404) | News Item Not Found
401 | [ApiResponseFor401](#update_news_item.ApiResponseFor401) | Unauthorized

#### update_news_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NewsItem**](../../models/NewsItem.md) |  | 


#### update_news_item.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_news_item.ApiResponseFor401
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

