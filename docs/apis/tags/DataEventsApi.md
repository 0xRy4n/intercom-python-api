<a name="__pageTop"></a>
# intercom_python_api.apis.tags.data_events_api.DataEventsApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_event**](#create_data_event) | **post** /events | Submit a data event
[**data_event_summaries**](#data_event_summaries) | **post** /events/summaries | Create event summaries
[**lis_data_events**](#lis_data_events) | **get** /events | List all data events

# **create_data_event**
<a name="create_data_event"></a>
> create_data_event()

Submit a data event

 You will need an Access Token that has write permissions to send Events. Once you have a key you can submit events via POST to the Events resource, which is located at https://api.intercom.io/events, or you can send events using one of the client libraries. When working with the HTTP API directly a client should send the event with a `Content-Type` of `application/json`.  When using the JavaScript API, [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app) makes the Events API available. Once added, you can submit an event using the `trackEvent` method. This will associate the event with the Lead or currently logged-in user or logged-out visitor/lead and send it to Intercom. The final parameter is a map that can be used to send optional metadata about the event.  With the Ruby client you pass a hash describing the event to `Intercom::Event.create`, or call the `track_user` method directly on the current user object (e.g. `user.track_event`).  | Type            | Description                                                                                                                                                                                                     | Example                                                                           | | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- | | String          | The value is a JSON String                                                                                                                                                                                      | `\"source\":\"desktop\"`                                                              | | Number          | The value is a JSON Number                                                                                                                                                                                      | `\"load\": 3.67`                                                                    | | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `\"contact_date\": 1392036272`                                                      | | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `\"article\": \"https://example.org/ab1de.html\"`                                     | | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `\"article\": {\"url\": \"https://example.org/ab1de.html\", \"value\":\"the dude abides\"}` | | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `\"price\": {\"amount\": 34999, \"currency\": \"eur\"}`                                   |  **NB: For the JSON object types, please note that we do not currently support nested JSON structure.**  > 🚧 Lead Events > > When submitting events for Leads, you will need to specify the Lead's `id`.  > 📘 Metadata behaviour > > - We currently limit the number of tracked metadata keys to 10 per event. Once the quota is reached, we ignore any further keys we receive. The first 10 metadata keys are determined by the order in which they are sent in with the event. > - It is not possible to change the metadata keys once the event has been sent. A new event will need to be created with the new keys and you can archive the old one. > - There might be up to 24 hrs delay when you send a new metadata for an existing event.  > 📘 Event de-duplication > > The API may detect and ignore duplicate events. Each event is uniquely identified as a combination of the following data - the Workspace identifier, the Contact external identifier, the Data Event name and the Data Event created time. As a result, it is **strongly recommended** to send a second granularity Unix timestamp in the `created_at` field. > > Duplicated events are responded to using the normal `202 Accepted` code - an error is not thrown, however repeat requests will be counted against any rate limit that is in place.  ### HTTP API Responses  - Successful responses to submitted events return `202 Accepted` with an empty body. - Unauthorised access will be rejected with a `401 Unauthorized` or `403 Forbidden` response code. - Events sent about users that cannot be found will return a `404 Not Found`. - Event lists containing duplicate events will have those duplicates ignored. - Server errors will return a `500` response code and may contain an error message in the body.  

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api import Intercom
from intercom_python_api.apis.tags import data_events_api
from intercom_python_api.model.create_data_event_request import CreateDataEventRequest
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
    body = CreateDataEventRequest()
    try:
        # Submit a data event
        api_response = intercom.DataEventsApi.create_data_event(
            header_params=header_params,
            body=body,
        )
    except intercom_python_api.ApiException as e:
        print("Exception when calling DataEventsApi->create_data_event: %s\n" % e)

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
[**CreateDataEventRequest**](../../models/CreateDataEventRequest.md) |  | 


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
202 | [ApiResponseFor202](#create_data_event.ApiResponseFor202) | successful
401 | [ApiResponseFor401](#create_data_event.ApiResponseFor401) | Unauthorized

#### create_data_event.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_data_event.ApiResponseFor401
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

# **data_event_summaries**
<a name="data_event_summaries"></a>
> data_event_summaries()

Create event summaries

Create event summaries for a user. Event summaries are used to track the number of times an event has occurred, the first time it occurred and the last time it occurred.  

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api import Intercom
from intercom_python_api.apis.tags import data_events_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.create_data_event_summaries_request import CreateDataEventSummariesRequest
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    body = CreateDataEventSummariesRequest(
        user_id="314159",
        event_summaries=dict(
            event_name="invited-friend",
            count=1,
            first=1671028894,
            last=1671028894,
        ),
    )
    try:
        # Create event summaries
        api_response = intercom.DataEventsApi.data_event_summaries(
            header_params=header_params,
            body=body,
        )
    except intercom_python_api.ApiException as e:
        print("Exception when calling DataEventsApi->data_event_summaries: %s\n" % e)

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
[**CreateDataEventSummariesRequest**](../../models/CreateDataEventSummariesRequest.md) |  | 


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
200 | [ApiResponseFor200](#data_event_summaries.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#data_event_summaries.ApiResponseFor401) | Unauthorized

#### data_event_summaries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### data_event_summaries.ApiResponseFor401
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

# **lis_data_events**
<a name="lis_data_events"></a>
> DataEventSummary lis_data_events(filtertype)

List all data events

 > 🚧 > > Please note that you can only 'list' events that are less than 90 days old. Event counts and summaries will still include your events older than 90 days but you cannot 'list' these events individually if they are older than 90 days  The events belonging to a customer can be listed by sending a GET request to `https://api.intercom.io/events` with a user or lead identifier along with a `type` parameter. The identifier parameter can be one of `user_id`, `email` or `intercom_user_id`. The `type` parameter value must be `user`.  - `https://api.intercom.io/events?type=user&user_id={user_id}` - `https://api.intercom.io/events?type=user&email={email}` - `https://api.intercom.io/events?type=user&intercom_user_id={id}` (this call can be used to list leads)  The `email` parameter value should be [url encoded](http://en.wikipedia.org/wiki/Percent-encoding) when sending.  You can optionally define the result page size as well with the `per_page` parameter. 

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api import Intercom
from intercom_python_api.apis.tags import data_events_api
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.data_event_summary import DataEventSummary
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
    query_params = {
        'filter': dict(),
        'type': "type_example",
    }
    header_params = {
    }
    try:
        # List all data events
        api_response = intercom.DataEventsApi.lis_data_events(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling DataEventsApi->lis_data_events: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
    query_params = {
        'filter': dict(),
        'type': "type_example",
        'summary': True,
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List all data events
        api_response = intercom.DataEventsApi.lis_data_events(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling DataEventsApi->lis_data_events: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | 
type | TypeSchema | | 
summary | SummarySchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_2](#one_of_2) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_id** | str,  | str,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**intercom_user_id** | str,  | str,  |  | 

# one_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SummarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

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
200 | [ApiResponseFor200](#lis_data_events.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#lis_data_events.ApiResponseFor401) | Unauthorized

#### lis_data_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataEventSummary**](../../models/DataEventSummary.md) |  | 


#### lis_data_events.ApiResponseFor401
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

