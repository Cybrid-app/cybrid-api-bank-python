# PostDepositBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | The fiat account guid. | 
**type** | **str** | The account type. To generate deposit bank accounts with their own unique account number set this to \&quot;main\&quot;. To generate deposit bank accounts with the same account number as the parent deposit bank account set this to \&quot;sub_account\&quot;. This setting will only generate a unique identifier for the deposit bank and will not result in a unique account number being generated. \&quot;sub_account\&quot; is only  available for customer-level deposit bank accounts. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**parent_deposit_bank_account_guid** | **str, none_type** | The unique identifier for the bank-level deposit bank account. This is only required for sub-accounts. | [optional] 
**labels** | **[str], none_type** | The labels associated with the address. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


