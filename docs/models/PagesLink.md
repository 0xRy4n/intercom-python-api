# intercom_python_api.model.pages_link.PagesLink

The majority of list resources in the API are paginated to allow clients to traverse data over multiple requests.  Their responses are likely to contain a pages object that hosts pagination links which a client can use to paginate through the data without having to construct a query. The link relations for the pages field are as follows. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The majority of list resources in the API are paginated to allow clients to traverse data over multiple requests.  Their responses are likely to contain a pages object that hosts pagination links which a client can use to paginate through the data without having to construct a query. The link relations for the pages field are as follows.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**next** | None, str,  | NoneClass, str,  | A link to the next page of results. A response that does not contain a next link does not have further data to fetch. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**per_page** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**total_pages** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["pages", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

