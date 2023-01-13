# PostExternalBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account. | 
**asset** | **str, none_type** | The asset code. If not set will try and default to the Bank&#39;s configured fiat asset. | 
**account_kind** | **str** | The account type | defaults to "plaid"
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**plaid_public_token** | **str, none_type** | The public token for the account. | [optional] 
**plaid_account_id** | **str, none_type** | The account identifier in plaid. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


