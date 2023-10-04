# PostExternalBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account. | 
**account_kind** | **str** | The account type | 
**asset** | **str, none_type** | The asset code. If not set will try and default to the Bank&#39;s configured fiat asset. | 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**plaid_public_token** | **str, none_type** | The public token for the account. Required for &#39;plaid&#39; accounts. | [optional] 
**plaid_account_id** | **str, none_type** | The account identifier in plaid. Required for &#39;plaid&#39; accounts. | [optional] 
**plaid_processor_token** | **str, none_type** | The Plaid processor token used to access the account. Required for &#39;plaid_processor_token&#39; accounts. | [optional] 
**plaid_institution_id** | **str, none_type** | Plaid&#39;s institution ID for the account&#39;s institution. Required for &#39;plaid_processor_token&#39; accounts. | [optional] 
**plaid_account_mask** | **str, none_type** | The account mask for the account. Required for &#39;plaid_processor_token&#39; accounts. | [optional] 
**plaid_account_name** | **str, none_type** | The name of the account. Required for &#39;plaid_processor_token&#39; accounts. | [optional] 
**counterparty_bank_account** | [**PostExternalBankAccountCounterpartyBankAccount**](PostExternalBankAccountCounterpartyBankAccount.md) |  | [optional] 
**counterparty_name** | [**PostExternalBankAccountCounterpartyName**](PostExternalBankAccountCounterpartyName.md) |  | [optional] 
**counterparty_address** | [**PostExternalBankAccountCounterpartyAddress**](PostExternalBankAccountCounterpartyAddress.md) |  | [optional] 
**counterparty_email_address** | **str, none_type** | The counterparty&#39;s email address on the account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


