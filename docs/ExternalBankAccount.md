# ExternalBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the account. | [optional] 
**name** | **str** | The name of the account. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**account_kind** | **str** | The type of account; one of plaid, plaid_processor_token, or raw_routing_details. | [optional] 
**environment** | **str** | The environment that the external bank account is operating in; one of sandbox or production. | [optional] 
**bank_guid** | **str** | The bank identifier. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**counterparty_guid** | **str, none_type** | The counterparty identifier. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**plaid_institution_id** | **str, none_type** | The Plaid institution ID for the account. | [optional] 
**plaid_account_mask** | **str, none_type** | The account number mask for the account. | [optional] 
**plaid_account_name** | **str, none_type** | The name for the account. | [optional] 
**state** | **str** | The state of the external bank account; one of storing, completed, failed, refresh_required, unverified, deleting, or deleted. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed transfers. | [optional] 
**balance_updated_at** | **datetime, none_type** | The timestamp that the balance information was last updated at. | [optional] 
**balances** | [**ExternalBankAccountBalances**](ExternalBankAccountBalances.md) |  | [optional] 
**pii** | [**[ExternalBankAccountPiiInner], none_type**](ExternalBankAccountPiiInner.md) | The account holder information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


