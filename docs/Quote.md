# Quote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the quote. | [optional] 
**product_type** | **str** | The type of product the quote is for; one of trading, funding, book_transfer, crypto_transfer, inter_account, or lightning_transfer. | [optional] 
**bank_guid** | **str** | The unique identifier for the bank. | [optional] 
**customer_guid** | **str** | The unique identifier for the customer. | [optional] 
**symbol** | **str, none_type** | Symbol the quote was requested for. Format is \&quot;asset-counter_asset\&quot; in uppercase. Populated for trade quotes. | [optional] 
**side** | **str** | The direction of the quote; one of buy, sell, deposit, or withdrawal. | [optional] 
**receive_amount** | **int** | The amount to be received in base units of the currency: currency is \&quot;asset\&quot; for buy and \&quot;counter_asset\&quot; for sell for trade quotes. | [optional] 
**deliver_amount** | **int** | The amount to be delivered in base units of the currency: currency is \&quot;counter_asset\&quot; for buy and \&quot;asset\&quot; for sell for trade quotes. | [optional] 
**fee** | **int** | The fee associated with the trade. Denominated in \&quot;counter_asset\&quot; base units for trade quotes. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**issued_at** | **datetime** | ISO8601 datetime the quote was created at. | [optional] 
**expires_at** | **datetime, none_type** | ISO8601 datetime the quote is expiring at. Populated for trading quotes. | [optional] 
**asset** | **str, none_type** | The asset code the quote was requested for. Populated for book transfer and funding quotes. | [optional] 
**network_fee** | **int, none_type** | The network fee in base units of network_fee_asset. Only present on &#x60;crypto_transfer&#x60; quotes. | [optional] 
**network_fee_asset** | **str, none_type** | The asset code of the network fee. | [optional] 
**network_address** | **str, none_type** | The network address to pay the invoice to. Populated for lightning_transfer quotes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


