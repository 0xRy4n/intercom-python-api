# intercom_python_api.model.conversation.Conversation

Conversations are how you can communicate with users in Intercom. They are created when a contact replies to an outbound message, or when one admin directly sends a message to a single contact.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Conversations are how you can communicate with users in Intercom. They are created when a contact replies to an outbound message, or when one admin directly sends a message to a single contact. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**admin_assignee_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The id of the admin assigned to the conversation. If it&#x27;s not assigned to an admin it will return null. | [optional] 
**contacts** | [**ConversationContacts**](ConversationContacts.md) | [**ConversationContacts**](ConversationContacts.md) |  | [optional] 
**conversation_parts** | [**ConversationParts**](ConversationParts.md) | [**ConversationParts**](ConversationParts.md) |  | [optional] 
**conversation_rating** | [**ConversationRating**](ConversationRating.md) | [**ConversationRating**](ConversationRating.md) |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the conversation was created. | [optional] value must conform to RFC-3339 date-time
**custom_attributes** | [**CustomAttributes**](CustomAttributes.md) | [**CustomAttributes**](CustomAttributes.md) |  | [optional] 
**first_contact_reply** | [**ConversationFirstContactReply**](ConversationFirstContactReply.md) | [**ConversationFirstContactReply**](ConversationFirstContactReply.md) |  | [optional] 
**id** | str,  | str,  | The id representing the conversation. | [optional] 
**open** | bool,  | BoolClass,  | Indicates whether a conversation is open (true) or closed (false). | [optional] 
**priority** | str,  | str,  | If marked as priority, it will return priority or else not_priority. | [optional] must be one of ["priority", "not_priority", ] 
**read** | bool,  | BoolClass,  | Indicates whether a conversation has been read. | [optional] 
**sla_applied** | [**SlaApplied**](SlaApplied.md) | [**SlaApplied**](SlaApplied.md) |  | [optional] 
**snoozed_until** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | If set this is the time in the future when this conversation will be marked as open. i.e. it will be in a snoozed state until this time. i.e. it will be in a snoozed state until this time. | [optional] value must conform to RFC-3339 date-time
**source** | [**ConversationSource**](ConversationSource.md) | [**ConversationSource**](ConversationSource.md) |  | [optional] 
**state** | str,  | str,  | Can be set to \&quot;open\&quot;, \&quot;closed\&quot; or \&quot;snoozed\&quot;. | [optional] must be one of ["open", "closed", "snoozed", ] 
**statistics** | [**ConversationStatistics**](ConversationStatistics.md) | [**ConversationStatistics**](ConversationStatistics.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) | [**Tags**](Tags.md) |  | [optional] 
**team_assignee_id** | None, str,  | NoneClass, str,  | The id of the team assigned to the conversation. If it&#x27;s not assigned to a team it will return null. | [optional] 
**teammates** | [**ConversationTeammates**](ConversationTeammates.md) | [**ConversationTeammates**](ConversationTeammates.md) |  | [optional] 
**title** | None, str,  | NoneClass, str,  | The title given to the conversation. | [optional] 
**type** | str,  | str,  | Always conversation. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the conversation was updated. | [optional] value must conform to RFC-3339 date-time
**waiting_since** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The last time a Contact responded to an Admin. In other words, the time a customer started waiting for a response. Set to null if last reply is from an Admin. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

