# PostQuote

Request body for quote creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **str, none_type** | The type of product the quote is for. | [optional]  if omitted the server will use the default value of "trading"
**bank_guid** | **str, none_type** | The unique identifier for the bank. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**receive_amount** | **int, none_type** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell for trade quotes. | [optional] 
**deliver_amount** | **int, none_type** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell for trade quotes. | [optional] 
**asset** | **str, none_type** | The asset code the quote was requested for. Required when product_type is lightning_transfer, product_type is book_transfer, product_type is funding, product_type is crypto_transfer, or product_type is inter_account. | [optional] 
**network_address** | **str, none_type** | The network address to pay the invoice to. Required when product_type is lightning_transfer. | [optional] 
**fees** | [**[PostFee], none_type**](PostFee.md) | The custom fees associated with the quote Optional when product_type is lightning_transfer, product_type is funding, product_type is trading, product_type is crypto_transfer, or product_type is trading_exit. | [optional] 
**side** | **str, none_type** | The direction for trade quotes: either &#39;buy&#39; or &#39;sell&#39;. The direction for funding quotes: either &#39;deposit&#39; or &#39;withdrawal&#39;. The direction for crypto transfer quotes: &#39;withdrawal&#39;. Book transfers do not require a side. They are all &#39;deposit&#39;s.  Required when product_type is funding, product_type is trading, or product_type is crypto_transfer. | [optional] 
**symbol** | **str, none_type** | Symbol the quote is being requested for. Format is \&quot;asset-counter_asset\&quot; in uppercase. See the Symbols API for a complete list of cryptocurrencies supported.  Required when product_type is trading. | [optional] 
**destination_accounts** | [**[PostQuoteEntry], none_type**](PostQuoteEntry.md) | Destination accounts for batch transactions on UTXO-based blockchains. A single destination account is required for Base blockchain assets. Optional when product_type is crypto_transfer. | [optional] 
**reference_trade_guid** | **str, none_type** | The guid of the related trade. Only present on &#x60;exit&#x60; trades. Required when product_type is trading_exit. | [optional] 
**source_account_guid** | **str, none_type** | The source account&#39;s identifier. Required when product_type is inter_account. | [optional] 
**destination_account_guid** | **str, none_type** | The destination account&#39;s identifier. Required when product_type is inter_account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


