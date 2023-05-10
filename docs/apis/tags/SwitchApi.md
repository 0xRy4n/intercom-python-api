<a name="__pageTop"></a>
# intercom_python_api.apis.tags.switch_api.SwitchApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phone_switch**](#create_phone_switch) | **post** /phone_call_redirects | Create a phone Switch

# **create_phone_switch**
<a name="create_phone_switch"></a>
> PhoneSwitch create_phone_switch()

Create a phone Switch

You can use the API to deflect phone calls to the Intercom Messenger. Calling this endpoint will send an SMS with a link to the Messenger to the phone number specified.  If custom attributes are specified, they will be added to the user or lead's custom data attributes. 

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import switch_api
from intercom_python_api.model.phone_switch import PhoneSwitch
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.create_phone_switch_request import CreatePhoneSwitchRequest
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
    api_instance = switch_api.SwitchApi(api_client)

    # example passing only optional values
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    body = CreatePhoneSwitchRequest(
        phone="+1 1234567890",
        custom_attributes=CustomAttributes(
            key=None,
        ),
    )
    try:
        # Create a phone Switch
        api_response = api_instance.create_phone_switch(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling SwitchApi->create_phone_switch: %s\n" % e)
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
[**CreatePhoneSwitchRequest**](../../models/CreatePhoneSwitchRequest.md) |  | 


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
200 | [ApiResponseFor200](#create_phone_switch.ApiResponseFor200) | successful
400 | [ApiResponseFor400](#create_phone_switch.ApiResponseFor400) | bad request - invalid number
422 | [ApiResponseFor422](#create_phone_switch.ApiResponseFor422) | unprocessable entity
401 | [ApiResponseFor401](#create_phone_switch.ApiResponseFor401) | Unauthorized

#### create_phone_switch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PhoneSwitch**](../../models/PhoneSwitch.md) |  | 


#### create_phone_switch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### create_phone_switch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### create_phone_switch.ApiResponseFor401
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

