# intercom_python_api.model.app.App

App is a workspace on Intercom

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | App is a workspace on Intercom | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] if omitted the server will use the default value of "app"
**id_code** | str,  | str,  | The id of the app. | [optional] 
**name** | str,  | str,  | The name of the app. | [optional] 
**region** | str,  | str,  | The Intercom region the app is located in. | [optional] 
**timezone** | str,  | str,  | The timezone of the region where the app is located. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | When the app was created. | [optional] 
**identity_verification** | bool,  | BoolClass,  | Whether or not the app uses identity verification. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

