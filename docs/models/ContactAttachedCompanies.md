# intercom_python_api.model.contact_attached_companies.ContactAttachedCompanies

A list of Company Objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A list of Company Objects | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[companies](#companies)** | list, tuple,  | tuple,  | An array containing Company Objects | [optional] 
**pages** | [**PagesLink**](PagesLink.md) | [**PagesLink**](PagesLink.md) |  | [optional] 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of companies associated to this contact | [optional] 
**type** | str,  | str,  | The type of object | [optional] must be one of ["list", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# companies

An array containing Company Objects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array containing Company Objects | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Company**](Company.md) | [**Company**](Company.md) | [**Company**](Company.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

