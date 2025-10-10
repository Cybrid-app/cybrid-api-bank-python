# PatchInternalPaymentInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stored_at** | **datetime** | ISO8601 datetime the payment instruction was stored at. | [optional] 
**expired_at** | **datetime** | ISO8601 datetime the payment instruction was expired at. | [optional] 
**failed_at** | **datetime** | ISO8601 datetime the payment instruction failed to be created at. | [optional] 
**network_address** | **str, none_type** | The network address to pay the invoice to. | [optional] 
**expected_payment_asset** | **str, none_type** | The asset the payor must pay the invoice in, e.g., BTC. | [optional] 
**expected_payment_amount** | **int, none_type** | The amount to be paid in base units of expected_payment_asset. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed payment instructions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


