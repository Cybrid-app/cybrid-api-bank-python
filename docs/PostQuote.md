# PostQuote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_guid** | **str** | The unique identifier for the customer. | 
**side** | **str** | The direction of the quote: either &#39;buy&#39; or &#39;sell&#39; for trade quotes. | 
**product_type** | **str** | The type of product the quote is for. | [optional]  if omitted the server will use the default value of "trading"
**symbol** | **str** | Symbol the quote is being requested for. Format is \&quot;asset-counter_asset\&quot; in uppercase. See the Symbols API for a complete list of cryptocurrencies supported. | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell for trade quotes. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell for trade quotes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


