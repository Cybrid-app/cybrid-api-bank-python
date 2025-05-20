# Transfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the transfer. | [optional] 
**transfer_type** | **str** | The type of transfer; one of funding, book, crypto, instant_funding, funding_return, crypto_return, loss_recovery, inter_account, lightning, or instant_funding_return. | [optional] 
**bank_guid** | **str, none_type** | The associated bank&#39;s identifier. | [optional] 
**customer_guid** | **str, none_type** | The associated customer&#39;s identifier. | [optional] 
**quote_guid** | **str** | The associated quote&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str, none_type** | The associated external bank account&#39;s identifier. | [optional] 
**asset** | **str** | The asset the transfer is related to, e.g., USD. | [optional] 
**side** | **str** | The direction of the quote; one of deposit or withdrawal. | [optional] 
**state** | **str** | The state of the transfer; one of storing, pending, reviewing, completed, or failed. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed transfers; one of non_sufficient_funds, refresh_required, party_name_invalid, payment_rail_invalid, compliance_rejection, cancelled, reversed, limit_exceeded, network_fee_too_low, amount_too_low, internal_error, or invalid_address. | [optional] 
**return_code** | **str, none_type** | The return code for reversed transfers | [optional] 
**amount** | **int, none_type** | The actual amount in base units of the asset. | [optional] 
**estimated_amount** | **int** | The estimated amount in base units of the asset. | [optional] 
**fee** | **int** | The fee associated with the transfer. | [optional] 
**estimated_network_fee** | **int, none_type** | The estimated network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers. | [optional] 
**network_fee** | **int, none_type** | The actual network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_asset** | **str, none_type** | The asset code of the network fee. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount** | **int, none_type** | The equivalent fiat network fee in base units of network_fee_liability_amount_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount_asset** | **str, none_type** | The fiat asset the network_fee_liability_amount is denominated in. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**txn_hash** | **str, none_type** | The hash of the blockchain transaction | [optional] 
**reference_transfer_guid** | **str, none_type** | The guid of the related transfer. Only present on return type transfers. | [optional] 
**source_account** | [**TransferSourceAccount**](TransferSourceAccount.md) |  | [optional] 
**source_participants** | [**[TransferParticipant], none_type**](TransferParticipant.md) | The participants in the source account. | [optional] 
**destination_account** | [**TransferDestinationAccount**](TransferDestinationAccount.md) |  | [optional] 
**destination_participants** | [**[TransferParticipant], none_type**](TransferParticipant.md) | The participants in the source account. | [optional] 
**deposit_address_guid** | **str, none_type** | The guid of the deposit address. Only present on crypto deposits. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**transfer_details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The raw details on the transfer from the bank. | [optional] 
**payment_rail** | **str, none_type** | The rail the payment was done on. One of: ach, eft, wire, rtp | [optional] 
**labels** | **[str], none_type** | The labels associated with the transfer. | [optional] 
**entries** | [**[TransferEntry], none_type**](TransferEntry.md) | Transfer entries associated with the batch transfer | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


