# PostInternalExternalBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account. | 
**account_kind** | **str** | The account type | 
**asset** | **str** | The asset code. | 
**provider_id** | **str, none_type** | The id of the account at the third-party provider. | [optional] 
**beneficiary_memo** | **str, none_type** | The memo to send to the counterparty. | [optional] 
**exchange_guid** | **str** | The exchange identifier. | [optional] 
**bank_guid** | **str** | The bank identifier. | [optional] 
**customer_guid** | **str** | The customer identifier. | [optional] 
**plaid_public_token** | **str, none_type** | The public token for the account. | [optional] 
**plaid_account_id** | **str, none_type** | The account identifier in plaid. | [optional] 
**counterparty_bank_account** | [**PostInternalExternalBankAccountCounterpartyBankAccount**](PostInternalExternalBankAccountCounterpartyBankAccount.md) |  | [optional] 
**counterparty_name** | [**PostInternalExternalBankAccountCounterpartyName**](PostInternalExternalBankAccountCounterpartyName.md) |  | [optional] 
**counterparty_address** | [**PostInternalExternalBankAccountCounterpartyAddress**](PostInternalExternalBankAccountCounterpartyAddress.md) |  | [optional] 
**counterparty_email_address** | **str, none_type** | The counterparty&#39;s email address on the account (internal). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


