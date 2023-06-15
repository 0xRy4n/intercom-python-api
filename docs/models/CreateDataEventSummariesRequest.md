# intercom_python_api.model.create_data_event_summaries_request.CreateDataEventSummariesRequest

You can send a list of event summaries for a user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense \"verb-noun\" combination, to improve readability, for example `updated-plan`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | You can send a list of event summaries for a user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense \&quot;verb-noun\&quot; combination, to improve readability, for example &#x60;updated-plan&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[event_summaries](#event_summaries)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of event summaries for the user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense &#x27;verb-noun&#x27; combination, to improve readability, for example &#x60;updated-plan&#x60;. | [optional] 
**user_id** | str,  | str,  | Your identifier for the user. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# event_summaries

A list of event summaries for the user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense 'verb-noun' combination, to improve readability, for example `updated-plan`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of event summaries for the user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense &#x27;verb-noun&#x27; combination, to improve readability, for example &#x60;updated-plan&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of times the event occurred. | [optional] 
**event_name** | str,  | str,  | The name of the event that occurred. A good event name is typically a past tense &#x27;verb-noun&#x27; combination, to improve readability, for example &#x60;updated-plan&#x60;. | [optional] 
**first** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the event was sent | [optional] value must conform to RFC-3339 date-time
**last** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the event was sent | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

