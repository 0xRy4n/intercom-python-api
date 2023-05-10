# intercom_python_api.model.contact_companies.ContactCompanies

An object containing companies meta data about the companies that a contact has.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing companies meta data about the companies that a contact has. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | Url to get more company resources for this contact | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | Int representing the total number of companyies attached to this contact | [optional] 
**has_more** | bool,  | BoolClass,  | Whether there&#x27;s more Addressable Objects to be viewed. If true, use the url to view all | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

