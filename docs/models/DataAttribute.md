# intercom_python_api.model.data_attribute.DataAttribute

Data Attributes are metadata used to describe your contact, company and conversation models. These include standard and custom attributes. By using the data attributes endpoint, you can get the global list of attributes for your workspace, as well as create and archive custom attributes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data Attributes are metadata used to describe your contact, company and conversation models. These include standard and custom attributes. By using the data attributes endpoint, you can get the global list of attributes for your workspace, as well as create and archive custom attributes. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**admin_id** | str,  | str,  | Teammate who created the attribute. Only applicable to CDAs | [optional] 
**api_writable** | bool,  | BoolClass,  | Can this attribute be updated through API | [optional] 
**archived** | bool,  | BoolClass,  | Is this attribute archived. (Only applicable to CDAs) | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the attribute was created as a UTC Unix timestamp | [optional] value must conform to RFC-3339 date-time
**custom** | bool,  | BoolClass,  | Set to true if this is a CDA | [optional] 
**data_type** | str,  | str,  | The data type of the attribute. | [optional] must be one of ["string", "integer", "float", "boolean", "date", ] 
**description** | str,  | str,  | Readable description of the attribute. | [optional] 
**full_name** | str,  | str,  | Full name of the attribute. Should match the name unless it&#x27;s a nested attribute. We can split full_name on &#x60;.&#x60; to access nested user object values. | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the data attribute which is given by Intercom. Only available for custom attributes. | [optional] 
**label** | str,  | str,  | Readable name of the attribute (i.e. name you see in the UI) | [optional] 
**model** | str,  | str,  | Value is &#x60;contact&#x60; for user/lead attributes, &#x60;company&#x60; for company attributes and &#x60;conversation&#x60; for conversation attributes.. | [optional] must be one of ["contact", "company", "conversation", ] 
**name** | str,  | str,  | Name of the attribute. | [optional] 
**[options](#options)** | list, tuple,  | tuple,  | List of predefined options for attribute value. | [optional] 
**type** | str,  | str,  | Value is &#x60;data_attribute&#x60;. | [optional] must be one of ["data_attribute", ] 
**ui_writable** | bool,  | BoolClass,  | Can this attribute be updated in the UI | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  | The time the attribute was last updated as a UTC Unix timestamp | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# options

List of predefined options for attribute value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of predefined options for attribute value. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

