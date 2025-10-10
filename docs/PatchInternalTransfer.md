# PatchInternalTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the transfer. | [optional] 
**failure_code** | **str** | The failure code for failed transfers. | [optional] 
**amount** | **int** | The actual amount in base units of asset. | [optional] 
**txn_hash** | **str** | The hash of the blockchain transaction | [optional] 
**network_fee** | **int** | The actual network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount** | **int** | The equivalent fiat network fee in base units of network_fee_liability_amount_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount_asset** | **str** | The fiat asset the network_fee_liability_amount is denominated in. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**return_code** | **str** | The code for the transfer return. | [optional] 
**returned_at** | **str** | The ISO8601 datetime when the transfer was returned. | [optional] 
**hold_started_at** | **str** | The ISO8601 datetime when the transfer entered the hold state. | [optional] 
**hold_duration** | **int** | The approximate time (in seconds) that the transfer will be held for. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


