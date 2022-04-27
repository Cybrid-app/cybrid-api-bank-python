# SymbolPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The trade symbol the pricing is related to. Format is asset-counter_asset, e.g., BTC-USD. | [optional] 
**buy_price** | **int, none_type** | The purchase price (in base units) for the asset denominated in the counter asset currency. | [optional] 
**sell_price** | **int, none_type** | The sale price (in base units) for the asset denominated in the counter asset currency. | [optional] 
**buy_price_last_updated_at** | **datetime, none_type** | ISO8601 datetime the purchase price was generated at. | [optional] 
**sell_price_last_updated_at** | **datetime, none_type** | ISO8601 datetime the sale price was generated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


