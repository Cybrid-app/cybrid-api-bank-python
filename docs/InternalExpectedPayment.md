# InternalExpectedPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the exchange settlement expected payment. | [optional] 
**payment_kind** | **str** | The kind of expected payment. | [optional] 
**environment** | **str** | The environment that the payment is expected in. | [optional] 
**exchange_settlement_obligation_guid** | **str, none_type** | The identifier of the exchange settlement obligation that this payment is associated with. | [optional] 
**credit_account_guid** | **str, none_type** | The identifier of the platform account that this payment is associated with. | [optional] 
**settlement_account_guid** | **str, none_type** | The identifier of the settlement account that this payment is made available in. | [optional] 
**nonce** | **int** | The nonce of the expected payment | [optional] 
**payment_amount** | **int** | The amount expected to be received as part of this payment. | [optional] 
**internal_account_guid** | **str** | The identifier of the internal account that is expected to originate the payment. | [optional] 
**internal_account_type** | **str** | The type of the internal account that is expected to originate the payment. | [optional] 
**state** | **str** | The exchange settlement expected payment&#39;s state | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


