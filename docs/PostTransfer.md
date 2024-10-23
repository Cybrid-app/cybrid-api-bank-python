# PostTransfer

Request body for transfer creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_guid** | **str** | The associated quote&#39;s identifier. | 
**transfer_type** | **str** | The type of transfer. | 
**external_bank_account_guid** | **str, none_type** | The customer&#39;s &#39;plaid&#39; or &#39;plaid_processor_token&#39; external bank account&#39;s identifier. Required when transfer_type is funding or transfer_type is instant_funding. | [optional] 
**fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the transfer. Required if the customer or bank has multiple fiat accounts. Optional when transfer_type is funding. | [optional] 
**send_as_deposit_bank_account_guid** | **str, none_type** | The deposit bank account&#39;s identifier. Only valid for withdrawals. The deposit bank account must be owned by the customer or bank initiating the transfer. Optional when transfer_type is funding. | [optional] 
**payment_rail** | **str, none_type** | The desired payment rail to initiate the transfer for. Optional when transfer_type is funding. | [optional] 
**beneficiary_memo** | **str, none_type** | The memo to send to the counterparty. Optional when transfer_type is funding. | [optional] 
**source_participants** | [**[PostTransferParticipant], none_type**](PostTransferParticipant.md) | The source participants for the transfer. Optional when transfer_type is funding, transfer_type is instant_funding, transfer_type is book, transfer_type is crypto, or transfer_type is lightning. | [optional] 
**destination_participants** | [**[PostTransferParticipant], none_type**](PostTransferParticipant.md) | The destination participants for the transfer. Optional when transfer_type is funding, transfer_type is instant_funding, transfer_type is book, transfer_type is crypto, or transfer_type is lightning. | [optional] 
**bank_fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the transfer. Required if the bank has multiple fiat accounts. Optional when transfer_type is instant_funding or transfer_type is lightning. | [optional] 
**customer_fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the transfer. Required if the customer has multiple fiat accounts. Optional when transfer_type is instant_funding or transfer_type is lightning. | [optional] 
**source_account_guid** | **str, none_type** | The source account&#39;s identifier. Required when transfer_type is book or transfer_type is inter_account. | [optional] 
**destination_account_guid** | **str, none_type** | The destination account&#39;s identifier. Required when transfer_type is book or transfer_type is inter_account. | [optional] 
**external_wallet_guid** | **str, none_type** | The customer&#39;s external wallet&#39;s identifier. Optional when transfer_type is crypto. | [optional] 
**customer_guid** | **str, none_type** | The customer&#39;s identifier. Required when transfer_type is lightning. | [optional] 
**network_fee_account_guid** | **str, none_type** | The network fee account&#39;s identifier. Required for network fee transfers. Must be the identifier for the customer&#39;s or bank&#39;s fiat or trading account. For customer&#39;s to pay the network fees, include the customer&#39;s fiat or trading account guid. For bank&#39;s to pay the network fees, include the bank&#39;s fiat or trading account guid. Required when transfer_type is lightning. | [optional] 
**expected_behaviours** | **[str], none_type** | The optional expected behaviour to simulate. Only applicable for transfers under sandbox banks. The force_review behaviour will force the transfer to be reviewed for funding and instant_funding transfers. | [optional] 
**labels** | **[str], none_type** | The labels associated with the transfer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


