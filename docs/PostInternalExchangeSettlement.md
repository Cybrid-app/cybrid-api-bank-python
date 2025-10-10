# PostInternalExchangeSettlement

Request body for exchange_settlement creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the settlement. | 
**exchange_guid** | **str** | The exchange guid for the settlement. | 
**automatic** | **bool, none_type** | Whether the settlement should be automatic. | [optional]  if omitted the server will use the default value of False
**trade_guids** | **[str], none_type** | The trade guids to include in the settlement. | [optional] 
**trades_created_at_lt** | **datetime, none_type** | Include trades created before this timestamp (exclusive). | [optional] 
**allowed_symbols** | **[str], none_type** | The trading symbols to include in the settlement. | [optional] 
**denied_symbols** | **[str], none_type** | The trading symbols to exclude from the settlement. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


