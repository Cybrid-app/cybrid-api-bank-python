# Quote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the quote. | [optional] 
**customer_guid** | **str** | The unique identifier for the customer. | [optional] 
**symbol** | **str** | Symbol the quote is being requested for. Format is \&quot;asset-counter_asset\&quot; in uppercase. | [optional] 
**side** | **str** | The direction of the quote: either &#39;buy&#39; or &#39;sell&#39;. | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell. | [optional] 
**fee** | **int** | The fee associated with the trade. Denominated in \&quot;counter_asset\&quot; base units | [optional] 
**issued_at** | **datetime** | ISO8601 datetime the quote was created at. | [optional] 
**expires_at** | **datetime** | ISO8601 datetime the quote is expiring at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


