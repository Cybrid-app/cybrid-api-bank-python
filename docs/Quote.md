# Quote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the quote. | [optional] 
**product_type** | **str** | The type of product the quote is for. | [optional] 
**customer_guid** | **str** | The unique identifier for the customer. | [optional] 
**symbol** | **str, none_type** | Symbol the quote was requested for. Format is \&quot;asset-counter_asset\&quot; in uppercase. Populated for trade quotes. | [optional] 
**side** | **str** | The direction of the quote: either &#39;buy&#39; or &#39;sell&#39; for trade quotes. | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell for trade quotes. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell for trade quotes. | [optional] 
**fee** | **int** | The fee associated with the trade. Denominated in \&quot;counter_asset\&quot; base units for trade quotes. | [optional] 
**issued_at** | **datetime** | ISO8601 datetime the quote was created at. | [optional] 
**expires_at** | **datetime, none_type** | ISO8601 datetime the quote is expiring at. Populated for trading quotes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


