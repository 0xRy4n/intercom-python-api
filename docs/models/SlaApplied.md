# intercom_python_api.model.sla_applied.SlaApplied

The SLA Applied object contains the details for which SLA has been applied to this conversation. Important: if there are any canceled sla_events for the conversation - meaning an SLA has been manually removed from a conversation, the sla_status will always be returned as null. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The SLA Applied object contains the details for which SLA has been applied to this conversation. Important: if there are any canceled sla_events for the conversation - meaning an SLA has been manually removed from a conversation, the sla_status will always be returned as null.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sla_name** | str,  | str,  | The name of the SLA as given by the teammate when it was created. | [optional] 
**sla_status** | str,  | str,  | SLA statuses:             - &#x60;hit&#x60;: If there’s at least one hit event in the underlying sla_events table, and no “missed” or “canceled” events for the conversation.             - &#x60;missed&#x60;: If there are any missed sla_events for the conversation and no canceled events. If there’s even a single missed sla event, the status will always be missed. A missed status is not applied when the SLA expires, only the next time a teammate replies.             - &#x60;active&#x60;: An SLA has been applied to a conversation, but has not yet been fulfilled. SLA status is active only if there are no “hit, “missed”, or “canceled” events. | [optional] must be one of ["hit", "missed", "cancelled", "active", ] 
**type** | str,  | str,  | object type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

