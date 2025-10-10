# InternalExchangeSettlement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the exchange settlement. | 
**environment** | **str** | The environment that the settlement is for. | 
**exchange_guid** | **str** | The identifier of the exchange that corresponds to this settlement. | 
**name** | **str** | The name of the exchange settlement. | 
**trade_guids** | **[str]** | The exchange settlement&#39;s set of included trade guids. | 
**trade_amounts** | [**[InternalExchangeSettlementTradeAmountsInner]**](InternalExchangeSettlementTradeAmountsInner.md) | The exchange settlement&#39;s set of trade amounts. | 
**order_guids** | **[str]** | The exchange settlement&#39;s set of included order guids. | 
**order_amounts** | [**[InternalExchangeSettlementOrderAmountsInner]**](InternalExchangeSettlementOrderAmountsInner.md) | The exchange settlement&#39;s set of order amounts. | 
**state** | **str** | The exchange settlement&#39;s state | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | 
**exchange_settlement_obligation_guids** | **[str], none_type** | The exchange settlement&#39;s set of obligation guids. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


