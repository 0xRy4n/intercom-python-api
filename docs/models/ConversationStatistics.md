# intercom_python_api.model.conversation_statistics.ConversationStatistics

A Statistics object containing all information required for reporting, with timestamps and calculated metrics.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | A Statistics object containing all information required for reporting, with timestamps and calculated metrics. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] 
**time_to_assignment** | decimal.Decimal, int,  | decimal.Decimal,  | Duration until last assignment before first admin reply. In seconds. | [optional] 
**time_to_admin_reply** | decimal.Decimal, int,  | decimal.Decimal,  | Duration until first admin reply. Subtracts out of business hours. In seconds. | [optional] 
**time_to_first_close** | decimal.Decimal, int,  | decimal.Decimal,  | Duration until conversation was closed first time. Subtracts out of business hours. In seconds. | [optional] 
**time_to_last_close** | decimal.Decimal, int,  | decimal.Decimal,  | Duration until conversation was closed last time. Subtracts out of business hours. In seconds. | [optional] 
**median_time_to_reply** | decimal.Decimal, int,  | decimal.Decimal,  | Median based on all admin replies after a contact reply. Subtracts out of business hours. In seconds. | [optional] 
**first_contact_reply_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of first text conversation part from a contact. | [optional] value must conform to RFC-3339 date-time
**first_assignment_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of first assignment after first_contact_reply_at. | [optional] value must conform to RFC-3339 date-time
**first_admin_reply_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of first admin reply after first_contact_reply_at. | [optional] value must conform to RFC-3339 date-time
**first_close_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of first close after first_contact_reply_at. | [optional] value must conform to RFC-3339 date-time
**last_assignment_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of last assignment after first_contact_reply_at. | [optional] value must conform to RFC-3339 date-time
**last_assignment_admin_reply_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of first admin reply since most recent assignment. | [optional] value must conform to RFC-3339 date-time
**last_contact_reply_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the last conversation part from a contact. | [optional] value must conform to RFC-3339 date-time
**last_admin_reply_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the last conversation part from an admin. | [optional] value must conform to RFC-3339 date-time
**last_close_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the last conversation close. | [optional] value must conform to RFC-3339 date-time
**last_closed_by_id** | str,  | str,  | The last admin who closed the conversation. Returns a reference to an Admin object. | [optional] 
**count_reopens** | decimal.Decimal, int,  | decimal.Decimal,  | Number of reopens after first_contact_reply_at. | [optional] 
**count_assignments** | decimal.Decimal, int,  | decimal.Decimal,  | Number of assignments after first_contact_reply_at. | [optional] 
**count_conversation_parts** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of conversation parts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

