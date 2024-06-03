# PostTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_guid** | **str** | The associated quote&#39;s identifier. | 
**transfer_type** | **str** | The type of transfer. | 
**customer_guid** | **str** | The customer&#39;s identifier. | [optional] 
**source_account_guid** | **str** | The source account&#39;s identifier. Required for book transfers. | [optional] 
**destination_account_guid** | **str** | The destination account&#39;s identifier. Required for book transfers. | [optional] 
**external_wallet_guid** | **str** | The customer&#39;s external wallet&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str** | The customer&#39;s &#39;plaid&#39; or &#39;plaid_processor_token&#39; external bank account&#39;s identifier. | [optional] 
**network_fee_account_guid** | **str** | The network fee account&#39;s identifier. Required for network fee transfers. Must be the identifier for the customer&#39;s or bank&#39;s fiat account. For customer&#39;s to pay the network fees, include the customer&#39;s fiat account guid. For bank&#39;s to pay the network fees, include the bank&#39;s fiat account guid. | [optional] 
**payment_rail** | **str** | The desired payment rail to initiate the transfer for. Valid values are: ach, eft, wire. Valid for funding transfers only. | [optional] 
**beneficiary_memo** | **str, none_type** | The memo to send to the counterparty. | [optional] 
**labels** | **[str], none_type** | The labels associated with the transfer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


