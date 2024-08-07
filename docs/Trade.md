# Trade


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the trade. | [optional] 
**trade_type** | **str** | The type of trade; one of platform, liquidation, or exit. | [optional] 
**customer_guid** | **str, none_type** | The associated customer&#39;s identifier. | [optional] 
**quote_guid** | **str** | The associated quote&#39;s identifier. | [optional] 
**symbol** | **str** | The trade symbol the pricing is related to. Format is asset-counter_asset, e.g., BTC-USD. | [optional] 
**side** | **str** | The direction of the trade; one of buy or sell. | [optional] 
**state** | **str** | The state of the trade; one of storing, pending, cancelled, completed, settling, or failed. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed trades; one of non_sufficient_funds, unsupported, limit_exceeded, expired_quote, or market_volatility. | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell. | [optional] 
**fee** | **int** | The fee associated with the trade. Denominated in \&quot;counter_asset\&quot; base units | [optional] 
**reference_trade_guid** | **str, none_type** | The guid of the related trade. Only present on &#x60;exit&#x60; trades. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**labels** | **[str], none_type** | The labels associated with the trade. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


