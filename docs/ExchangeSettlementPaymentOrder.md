# ExchangeSettlementPaymentOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the exchange settlement payment order. | [optional] 
**exchange_settlement_obligation_guid** | **str** | The identifier of the exchange settlement obligation that this payment is associated with. | [optional] 
**sequence_number** | **int** | The sequence number of the payment order | [optional] 
**payment_amount** | **int** | The amount expected to be received as part of this payment. | [optional] 
**internal_account_guid** | **str** | The identifier of the internal account that is expected to originate the payment. | [optional] 
**internal_account_type** | **str** | The type of the internal account that is expected to originate the payment. | [optional] 
**external_account_guid** | **str** | The identifier of the external account that is expected to receive the payment. | [optional] 
**external_account_type** | **str** | The type of the external account that is expected to receive the payment. | [optional] 
**state** | **str** | The exchange settlement payment order&#39;s state | [optional] 
**created_at** | **datetime** | ISO8601 datetime the exchange settlement payment order was created at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


