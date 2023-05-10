# intercom_python_api.model.company.Company

Companies allow you to represent organizations using your product. Each company will have its own description and be associated with contacts. You can fetch, create, update and list companies.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Companies allow you to represent organizations using your product. Each company will have its own description and be associated with contacts. You can fetch, create, update and list companies. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Value is &#x60;company&#x60; | [optional] must be one of ["company", ] 
**id** | str,  | str,  | The Intercom defined id representing the company. | [optional] 
**name** | str,  | str,  | The name of the company. | [optional] 
**app_id** | str,  | str,  | The Intercom defined code of the workspace the company is associated to. | [optional] 
**[plan](#plan)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**company_id** | str,  | str,  | The company id you have defined for the company. | [optional] 
**remote_created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the company was created by you. | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the company was added in Intercom. | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The last time the company was updated. | [optional] 
**last_request_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the company last recorded making a request. | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of employees in the company. | [optional] 
**website** | str,  | str,  | The URL for the company website. | [optional] 
**industry** | str,  | str,  | The industry that the company operates in. | [optional] 
**monthly_spend** | decimal.Decimal, int,  | decimal.Decimal,  | How much revenue the company generates for your business. | [optional] 
**session_count** | decimal.Decimal, int,  | decimal.Decimal,  | How many sessions the company has recorded. | [optional] 
**user_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of users in the company. | [optional] 
**[custom_attributes](#custom_attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes you have set on the company. | [optional] 
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of tags associated with the company | [optional] 
**[segments](#segments)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of segments associated with the company | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Value is always \&quot;plan\&quot; | [optional] 
**id** | str,  | str,  | The id of the plan | [optional] 
**name** | str,  | str,  | The name of the plan | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_attributes

The custom attributes you have set on the company.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The custom attributes you have set on the company. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# tags

The list of tags associated with the company

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of tags associated with the company | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object | [optional] must be one of ["tag.list", ] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](Tag.md) | [**Tag**](Tag.md) | [**Tag**](Tag.md) |  | 

# segments

The list of segments associated with the company

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of segments associated with the company | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the object | [optional] must be one of ["segment.list", ] 
**[segments](#segments)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Segment**](Segment.md) | [**Segment**](Segment.md) | [**Segment**](Segment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

