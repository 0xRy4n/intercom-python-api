# intercom_python_api.model.create_or_update_company_request.CreateOrUpdateCompanyRequest

You can create or update a Company

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | You can create or update a Company | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the Company | [optional] 
**company_id** | str,  | str,  | The company id you have defined for the company. Can&#x27;t be updated | [optional] 
**plan** | str,  | str,  | The name of the plan you have associated with the company. | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of employees in this company. | [optional] 
**website** | str,  | str,  | The URL for this company&#x27;s website. Please note that the value specified here is not validated. Accepts any string. | [optional] 
**industry** | str,  | str,  | The industry that this company operates in. | [optional] 
**[custom_attributes](#custom_attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A hash of key/value pairs containing any other data about the company you want Intercom to store. | [optional] 
**remote_created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the company was created by you. | [optional] 
**monthly_spend** | decimal.Decimal, int,  | decimal.Decimal,  | How much revenue the company generates for your business. Note that this will truncate floats. i.e. it only allow for whole integers, 155.98 will be truncated to 155. Note that this has an upper limit of 2**31-1 or 2147483647.. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_attributes

A hash of key/value pairs containing any other data about the company you want Intercom to store.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A hash of key/value pairs containing any other data about the company you want Intercom to store. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

