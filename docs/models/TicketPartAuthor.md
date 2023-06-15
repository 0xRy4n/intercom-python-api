# intercom_python_api.model.ticket_part_author.TicketPartAuthor

The author that wrote or triggered the part. Can be a bot or an admin.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The author that wrote or triggered the part. Can be a bot or an admin. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  | The email of the author | [optional] 
**id** | str,  | str,  | The id of the author | [optional] 
**name** | str,  | str,  | The name of the author | [optional] 
**type** | str,  | str,  | The type of the author | [optional] must be one of ["admin", "bot", "team", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

