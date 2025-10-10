# InternalPostDepositBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | The trading account guid. | 
**type** | **str** | The account type. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**parent_deposit_bank_account_guid** | **str, none_type** | The unique identifier for the bank-level deposit bank account. This is only required for sub-accounts. | [optional] 
**provider_id** | **str, none_type** | Optional provider_id to use for the account.  Can only be set in Sandbox mode. It is automatically set in Production. Strictly for testing purposes. | [optional] 
**unique_memo_id** | **str, none_type** | Optional unique_memo_id to use for the account.  Can only be set in Sandbox mode. It is automatically set in Production. Strictly for testing purposes. | [optional] 
**labels** | **[str], none_type** | The labels associated with the address. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


