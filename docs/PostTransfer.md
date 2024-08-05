# PostTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_guid** | **str** | The associated quote&#39;s identifier. | 
**transfer_type** | **str** | The type of transfer. | 
**customer_guid** | **str** | The customer&#39;s identifier. | [optional] 
**fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the transfer. Required if the customer or bank has multiple fiat accounts. Only valid for funding transfers. | [optional] 
**customer_fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the transfer. Required if the customer has multiple fiat accounts. Only valid for instant funding and lightning transfers. | [optional] 
**bank_fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the transfer. Required if the bank has multiple fiat accounts. Only valid for instant funding and lightning transfers. | [optional] 
**source_account_guid** | **str** | The source account&#39;s identifier. Required for book transfers. | [optional] 
**source_participants** | [**[PostTransferParticipant], none_type**](PostTransferParticipant.md) | The source participants for the transfer. | [optional] 
**destination_account_guid** | **str** | The destination account&#39;s identifier. Required for book transfers. | [optional] 
**destination_participants** | [**[PostTransferParticipant], none_type**](PostTransferParticipant.md) | The destination participants for the transfer. | [optional] 
**external_wallet_guid** | **str** | The customer&#39;s external wallet&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str** | The customer&#39;s &#39;plaid&#39; or &#39;plaid_processor_token&#39; external bank account&#39;s identifier. | [optional] 
**network_fee_account_guid** | **str** | The network fee account&#39;s identifier. Required for network fee transfers. Must be the identifier for the customer&#39;s or bank&#39;s fiat account. For customer&#39;s to pay the network fees, include the customer&#39;s fiat account guid. For bank&#39;s to pay the network fees, include the bank&#39;s fiat account guid. | [optional] 
**payment_rail** | **str** | The desired payment rail to initiate the transfer for. Valid values are: ach, eft, wire. Valid for funding transfers only. | [optional] 
**beneficiary_memo** | **str, none_type** | The memo to send to the counterparty. | [optional] 
**send_as_deposit_bank_account_guid** | **str** | The deposit bank account&#39;s identifier. Optional for funding transfers. Only valid for withdrawals. The deposit bank account must be owned by the customer or bank initiating the transfer. | [optional] 
**labels** | **[str], none_type** | The labels associated with the transfer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


