# intercom_python_api.model.conversation_rating.ConversationRating

The Conversation Rating object which contains information on the rating and/or remark added by a Contact and the Admin assigned to the conversation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The Conversation Rating object which contains information on the rating and/or remark added by a Contact and the Admin assigned to the conversation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**rating** | decimal.Decimal, int,  | decimal.Decimal,  | The rating, between 1 and 5, for the conversation. | [optional] 
**remark** | str,  | str,  | An optional field to add a remark to correspond to the number rating | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the rating was requested in the conversation being rated. | [optional] value must conform to RFC-3339 date-time
**contact** | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | [optional] 
**teammate** | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

