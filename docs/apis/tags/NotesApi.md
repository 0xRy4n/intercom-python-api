<a name="__pageTop"></a>
# intercom_python_api.apis.tags.notes_api.NotesApi

All URIs are relative to *https://api.intercom.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note**](#create_note) | **post** /contacts/{id}/notes | Create a note
[**list_notes**](#list_notes) | **get** /contacts/{id}/notes | List all notes
[**retrieve_note**](#retrieve_note) | **get** /notes/{id} | Retrieve a note

# **create_note**
<a name="create_note"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_note(id)

Create a note

You can add a note to a single contact.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.note import Note
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'id': 123,
}
header_params = {
}
try:
    # Create a note
    api_response = intercom.NotesApi.create_note(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling NotesApi->create_note: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'id': 123,
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
body = dict(
        admin_id="123",
        body="New note",
        contact_id="123",
    )
try:
    # Create a note
    api_response = intercom.NotesApi.create_note(
        path_params=path_params,
        header_params=header_params,
        body=body,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling NotesApi->create_note: %s\n" % e)

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
**body** | str,  | str,  | The text of the note. | 
**admin_id** | str,  | str,  | The unique identifier of a given admin. | [optional] 
**contact_id** | str,  | str,  | The unique identifier of a given contact. | [optional] 
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
200 | [ApiResponseFor200](#create_note.ApiResponseFor200) | Successful response
404 | [ApiResponseFor404](#create_note.ApiResponseFor404) | Contact not found

#### create_note.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Note]({{complexTypePrefix}}Note.md) | [**Note**]({{complexTypePrefix}}Note.md) | [**Note**]({{complexTypePrefix}}Note.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### create_note.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Error]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_notes**
<a name="list_notes"></a>
> bool, date, datetime, dict, float, int, list, str, none_type list_notes(id)

List all notes

You can fetch a list of notes that are associated to a contact.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.note_list import NoteList
from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'id': 1,
}
header_params = {
}
try:
    # List all notes
    api_response = intercom.NotesApi.list_notes(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling NotesApi->list_notes: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'id': 1,
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
try:
    # List all notes
    api_response = intercom.NotesApi.list_notes(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling NotesApi->list_notes: %s\n" % e)

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
200 | [ApiResponseFor200](#list_notes.ApiResponseFor200) | Successful response
404 | [ApiResponseFor404](#list_notes.ApiResponseFor404) | Contact not found

#### list_notes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NoteList]({{complexTypePrefix}}NoteList.md) | [**NoteList**]({{complexTypePrefix}}NoteList.md) | [**NoteList**]({{complexTypePrefix}}NoteList.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### list_notes.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Error]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_note**
<a name="retrieve_note"></a>
> bool, date, datetime, dict, float, int, list, str, none_type retrieve_note(id)

Retrieve a note

You can fetch the details of a single note.

### Example

* Bearer Authentication (bearerAuth):

```python
import intercom_python_api import Intercom

from intercom_python_api.model.intercom_version import IntercomVersion
from intercom_python_api.model.note import Note
from intercom_python_api.model.error import Error

# Create an Intercom client context.
intercom = Intercom(api_key='<YOUR API TOKEN>')
```

An example of an API call passing only required parameters which have no default value:

```python
path_params = {
    'id': 1,
}
header_params = {
}
try:
    # Retrieve a note
    api_response = intercom.NotesApi.retrieve_note(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling NotesApi->retrieve_note: %s\n" % e)

```

An example passing **only** the optional values (like `Intercom-Version`):

```python
path_params = {
    'id': 1,
}
header_params = {
    'Intercom-Version': IntercomVersion("Unstable"),
}
try:
    # Retrieve a note
    api_response = intercom.NotesApi.retrieve_note(
        path_params=path_params,
        header_params=header_params,
    )
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling NotesApi->retrieve_note: %s\n" % e)

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
200 | [ApiResponseFor200](#retrieve_note.ApiResponseFor200) | Note found
401 | [ApiResponseFor401](#retrieve_note.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#retrieve_note.ApiResponseFor404) | Note not found

#### retrieve_note.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Note]({{complexTypePrefix}}Note.md) | [**Note**]({{complexTypePrefix}}Note.md) | [**Note**]({{complexTypePrefix}}Note.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### retrieve_note.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Error]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### retrieve_note.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Error]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

