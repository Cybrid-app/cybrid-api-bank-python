# PostQuote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **str** | The type of product the quote is for. | [optional]  if omitted the server will use the default value of "trading"
**bank_guid** | **str, none_type** | The unique identifier for the bank. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**asset** | **str** | The asset code the quote was requested for. Populated for funding, book transfer and crypto transfer quotes. | [optional] 
**network_address** | **str, none_type** | The network address to pay the invoice to. Populated for lightning_transfer quotes. | [optional] 
**symbol** | **str** | Symbol the quote is being requested for. Format is \&quot;asset-counter_asset\&quot; in uppercase. See the Symbols API for a complete list of cryptocurrencies supported. Populated for trade quotes. | [optional] 
**side** | **str, none_type** | The direction for trade quotes: either &#39;buy&#39; or &#39;sell&#39;. The direction for funding quotes: either &#39;deposit&#39; or &#39;withdrawal&#39;. The direction for crypto transfer quotes: &#39;withdrawal&#39;. Book transfers do not require a side. They are all &#39;deposit&#39;s.  | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell for trade quotes. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell for trade quotes. | [optional] 
**fees** | [**[PostFee]**](PostFee.md) | The custom fees associated with the quote | [optional] 
**reference_trade_guid** | **str** | The guid of the related trade. Only present on &#x60;exit&#x60; trades. | [optional] 
**source_account_guid** | **str, none_type** | The source account&#39;s identifier. Required for inter-account transfers. | [optional] 
**destination_account_guid** | **str, none_type** | The destination account&#39;s identifier. Required for inter-account transfers. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


