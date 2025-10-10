# InternalTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the transfer. | [optional] 
**transfer_type** | **str** | The type of transfer. | [optional] 
**bank_guid** | **str, none_type** | The associated bank&#39;s identifier. | [optional] 
**customer_guid** | **str, none_type** | The associated customer&#39;s identifier. | [optional] 
**quote_guid** | **str** | The associated quote&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str, none_type** | The associated external bank account&#39;s identifier. | [optional] 
**asset** | **str** | The asset the transfer is related to, e.g., USD. | [optional] 
**side** | **str** | The direction of the quote: &#39;deposit&#39; or &#39;withdrawal&#39;. | [optional] 
**state** | **str** | The transfer&#39;s state | [optional] 
**failure_code** | **str, none_type** | The failure code for failed transfers. | [optional] 
**return_code** | **str, none_type** | The return code for reversed transfers | [optional] 
**returned_at** | **datetime, none_type** | ISO8601 datetime the transfer was returned at. | [optional] 
**reference_transfer_guid** | **str, none_type** | The guid of the related transfer. Only present on return type transfers. | [optional] 
**amount** | **int, none_type** | The actual amount in base units of the asset. | [optional] 
**estimated_amount** | **int** | The estimated amount in base units of the asset. | [optional] 
**fee** | **int** | The fee associated with the transfer. | [optional] 
**estimated_network_fee** | **int, none_type** | The estimated network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers. | [optional] 
**network_fee** | **int, none_type** | The actual network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_asset** | **str, none_type** | The asset code of the network fee. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount** | **int, none_type** | The equivalent fiat network fee in base units of network_fee_liability_amount_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount_asset** | **str, none_type** | The fiat asset the network_fee_liability_amount is denominated in. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**txn_hash** | **str, none_type** | The hash of the blockchain transaction | [optional] 
**source_account** | [**InternalTransferSourceAccount**](InternalTransferSourceAccount.md) |  | [optional] 
**source_participants** | [**[TransferParticipant], none_type**](TransferParticipant.md) | The source participants for the transfer. | [optional] 
**destination_account** | [**InternalTransferDestinationAccount**](InternalTransferDestinationAccount.md) |  | [optional] 
**destination_participants** | [**[TransferParticipant], none_type**](TransferParticipant.md) | The destination participants for the transfer. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the transfer was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the transfer was last updated at. | [optional] 
**hold_started_at** | **datetime, none_type** | ISO8601 datetime the transfer hold was started at. | [optional] 
**hold_duration** | **int, none_type** | The approximate time (in seconds) that the transfer will be held for. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


