# intercom_python_api.model.data_export_csv.DataExportCsv

A CSV output file

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A CSV output file | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_id** | str,  | str,  | The user_id of the user who was sent the message. | [optional] 
**user_external_id** | str,  | str,  | The external_user_id of the user who was sent the message | [optional] 
**company_id** | str,  | str,  | The company ID of the user in relation to the message that was sent. Will return -1 if no company is present. | [optional] 
**email** | str,  | str,  | The users email who was sent the message. | [optional] 
**name** | str,  | str,  | The full name of the user receiving the message | [optional] 
**ruleset_id** | str,  | str,  | The id of the message. | [optional] 
**content_id** | str,  | str,  | The specific content that was received. In an A/B test each version has its own Content ID. | [optional] 
**content_type** | str,  | str,  | Email, Chat, Post etc. | [optional] 
**content_title** | str,  | str,  | The title of the content you see in your Intercom workspace. | [optional] 
**ruleset_version_id** | str,  | str,  | As you edit content we record new versions. This ID can help you determine which version of a piece of content that was received. | [optional] 
**receipt_id** | str,  | str,  | ID for this receipt. Will be included with any related stats in other files to identify this specific delivery of a message. | [optional] 
**received_at** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp for when the receipt was recorded. | [optional] 
**series_id** | str,  | str,  | The id of the series that this content is part of. Will return -1 if not part of a series. | [optional] 
**series_title** | str,  | str,  | The title of the series that this content is part of. | [optional] 
**node_id** | str,  | str,  | The id of the series node that this ruleset is associated with. Each block in a series has a corresponding node_id. | [optional] 
**first_reply** | decimal.Decimal, int,  | decimal.Decimal,  | The first time a user replied to this message if the content was able to receive replies. | [optional] 
**first_completion** | decimal.Decimal, int,  | decimal.Decimal,  | The first time a user completed this message if the content was able to be completed e.g. Tours, Surveys. | [optional] 
**first_series_completion** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the series this message was a part of was completed by the user. | [optional] 
**first_series_disengagement** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the series this message was a part of was disengaged by the user. | [optional] 
**first_series_exit** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the series this message was a part of was exited by the user. | [optional] 
**first_goal_success** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the user met this messages associated goal if one exists. | [optional] 
**first_open** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the user opened this message. | [optional] 
**first_click** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the series the user clicked on a link within this message. | [optional] 
**first_dismisall** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the series the user dismissed this message. | [optional] 
**first_unsubscribe** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the user unsubscribed from this message. | [optional] 
**first_hard_bounce** | decimal.Decimal, int,  | decimal.Decimal,  | The first time this message hard bounced for this user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

