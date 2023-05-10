# intercom_python_api.model.data_event.DataEvent

Data events are used to notify Intercom of changes to your data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data events are used to notify Intercom of changes to your data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the event occurred as a UTC Unix timestamp | value must conform to RFC-3339 date-time
**event_name** | str,  | str,  | The name of the event that occurred. This is presented to your App&#x27;s admins when filtering and creating segments - a good event name is typically a past tense &#x27;verb-noun&#x27; combination, to improve readability, for example &#x60;updated-plan&#x60;. | 
**type** | str,  | str,  | The type of the object | [optional] must be one of ["event", ] 
**user_id** | str,  | str,  | Your identifier for the user. | [optional] 
**id** | str,  | str,  | Your identifier for a lead or a user. | [optional] 
**intercom_user_id** | str,  | str,  | The Intercom identifier for the user. | [optional] 
**email** | str,  | str,  | An email address for your user. An email should only be used where your application uses email to uniquely identify users. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional metadata about the event. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Optional metadata about the event.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional metadata about the event. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

