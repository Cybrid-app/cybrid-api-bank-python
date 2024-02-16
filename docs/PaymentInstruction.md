# PaymentInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the payment instruction. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**invoice_guid** | **str** | The invoice identifier. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**expired_at** | **datetime, none_type** | ISO8601 datetime the instructions expired at. | [optional] 
**network_address** | **str, none_type** | The network address to pay the invoice to. | [optional] 
**expected_payment_asset** | **str, none_type** | The asset the payor must pay the invoice in, e.g., BTC. | [optional] 
**expected_payment_amount** | **int, none_type** | The amount to be paid in base units of expected_payment_asset. | [optional] 
**state** | **str** | The state of the payment instruction; one of storing, created, or expired. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


