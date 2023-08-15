# Trade


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the trade. | [optional] 
**customer_guid** | **str, none_type** | The associated customer&#39;s identifier. | [optional] 
**quote_guid** | **str** | The associated quote&#39;s identifier. | [optional] 
**symbol** | **str** | The trade symbol the pricing is related to. Format is asset-counter_asset, e.g., BTC-USD. | [optional] 
**side** | **str** | The direction of the quote: either &#39;buy&#39; or &#39;sell&#39;. | [optional] 
**state** | **str** | The trade&#39;s state | [optional] 
**failure_code** | **str, none_type** | The failure code for failed trades. | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell. | [optional] 
**fee** | **int** | The fee associated with the trade. Denominated in \&quot;counter_asset\&quot; base units | [optional] 
**created_at** | **datetime** | ISO8601 datetime the trade was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the trade was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


