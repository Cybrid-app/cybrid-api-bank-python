# PostExternalBankAccount

Request body for external bank account creation. The owner (the counterparty, or the customer when there is no counterparty) must already have a verified identity -- KYC for an individual, KYB for a business -- before an external bank account can be onboarded for them; the create is refused otherwise. Banks that verify individuals non-documentarily are the exception: an individual customer whose attested personal details have passed may onboard an account before verification completes, because the account is what authenticates them. 'plaid_processor_token' is not supported for this onboarding version.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the account. | 
**account_kind** | **str** | The account type | 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**asset** | **str, none_type** | The asset code. If not set will try and default to the Bank&#39;s configured fiat asset. | [optional] 
**plaid_public_token** | **str, none_type** | The public token for the account. Required for &#39;plaid&#39; accounts. Required when account_kind is plaid. | [optional] 
**plaid_account_id** | **str, none_type** | The account identifier in plaid. Required for &#39;plaid&#39; accounts. Required when account_kind is plaid. | [optional] 
**plaid_processor_token** | **str, none_type** | The Plaid processor token used to access the account. Required when account_kind is plaid_processor_token. | [optional] 
**plaid_institution_id** | **str, none_type** | Plaid&#39;s institution ID for the account&#39;s institution. Required when account_kind is plaid_processor_token. | [optional] 
**plaid_account_mask** | **str, none_type** | The account mask for the account. Required when account_kind is plaid_processor_token. | [optional] 
**plaid_account_name** | **str, none_type** | The name of the account. Required when account_kind is plaid_processor_token. | [optional] 
**expected_behaviours** | **[str], none_type** | Sandbox only: deterministically simulate the holder-name-match outcome instead of aligning the owner&#39;s KYC/KYB data with the linked account. Ignored for account kinds whose plan runs no holder-name match. | [optional] 
**counterparty_guid** | **str, none_type** | The counterparty identifier. Optional when account_kind is raw_routing_details. | [optional] 
**counterparty_bank_account_details** | [**[PostBankAccountDetails], none_type**](PostBankAccountDetails.md) | The counterparty&#39;s checking bank account information. Required when account_kind is raw_routing_details. | [optional] 
**counterparty_name** | [**PostExternalBankAccountCounterpartyName**](PostExternalBankAccountCounterpartyName.md) |  | [optional] 
**counterparty_address** | [**PostExternalBankAccountCounterpartyAddress**](PostExternalBankAccountCounterpartyAddress.md) |  | [optional] 
**counterparty_email_address** | **str, none_type** | The account holder&#39;s email address. Optional when account_kind is raw_routing_details. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


