# intercom_python_api.model.note.Note

Notes allow you to annotate and comment on your contacts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes allow you to annotate and comment on your contacts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;note&#x60;. | [optional] 
**id** | str,  | str,  | The id of the note. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the note was created. | [optional] 
**[contact](#contact)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Represents the contact that the note was created about. | [optional] 
**author** | [**Admin**](Admin.md) | [**Admin**](Admin.md) |  | [optional] 
**body** | str,  | str,  | The body text of the note. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contact

Represents the contact that the note was created about.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Represents the contact that the note was created about. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | String representing the object&#x27;s type. Always has the value &#x60;contact&#x60;. | [optional] 
**id** | str,  | str,  | The id of the contact. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

