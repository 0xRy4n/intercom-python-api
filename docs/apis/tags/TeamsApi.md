<a name="__pageTop"></a>
# intercom_python_api.apis.tags.teams_api.TeamsApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_teams**](#list_teams) | **get** /teams | List all teams
[**retrieve_team**](#retrieve_team) | **get** /teams/{id} | Retrieve a team

# **list_teams**
<a name="list_teams"></a>
> TeamList list_teams()

List all teams

This will return a list of team objects for the App.

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import teams_api
from intercom_python_api.model.team_list import TeamList
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
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only optional values
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # List all teams
        api_response = api_instance.list_teams(
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling TeamsApi->list_teams: %s\n" % e)
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
200 | [ApiResponseFor200](#list_teams.ApiResponseFor200) | successful
401 | [ApiResponseFor401](#list_teams.ApiResponseFor401) | Unauthorized

#### list_teams.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TeamList**](../../models/TeamList.md) |  | 


#### list_teams.ApiResponseFor401
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

# **retrieve_team**
<a name="retrieve_team"></a>
> Team retrieve_team(id)

Retrieve a team

You can fetch the details of a single team, containing an array of admins that belong to this team.

### Example

* Bearer Authentication (bearerAuth):
```python
import intercom_python_api
from intercom_python_api.apis.tags import teams_api
from intercom_python_api.model.team import Team
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
    api_instance = teams_api.TeamsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "123",
    }
    header_params = {
    }
    try:
        # Retrieve a team
        api_response = api_instance.retrieve_team(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling TeamsApi->retrieve_team: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "123",
    }
    header_params = {
        'Intercom-Version': IntercomVersion("Unstable"),
    }
    try:
        # Retrieve a team
        api_response = api_instance.retrieve_team(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except intercom_python_api.ApiException as e:
        print("Exception when calling TeamsApi->retrieve_team: %s\n" % e)
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
200 | [ApiResponseFor200](#retrieve_team.ApiResponseFor200) | successful
404 | [ApiResponseFor404](#retrieve_team.ApiResponseFor404) | Team not found
401 | [ApiResponseFor401](#retrieve_team.ApiResponseFor401) | Unauthorized

#### retrieve_team.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Team**](../../models/Team.md) |  | 


#### retrieve_team.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### retrieve_team.ApiResponseFor401
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

