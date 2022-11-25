# ExternalBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the account. | [optional] 
**name** | **str** | The name of the account. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**account_kind** | **str** | The type of account. | [optional]  if omitted the server will use the default value of "plaid"
**environment** | **str** | The environment that the external bank account is operating in. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the exchange was created at. | [optional] 
**plaid_access_token** | **str, none_type** | The Plaid access token for the account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


