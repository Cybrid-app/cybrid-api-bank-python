# PostInternalExpectedPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_kind** | **str** | The kind of expected payment. | 
**nonce** | **int** | The sequence number of the expected payment | 
**payment_amount** | **int** | The amount expected to be received as part of this payment. | 
**internal_account_guid** | **str** | The identifier of the internal account that is expected to originate the payment. | 
**internal_account_type** | **str** | The type of the internal account that is expected to originate the payment. | 
**exchange_settlement_guid** | **str, none_type** | The identifier of the exchange settlement that this payment is associated with. | [optional] 
**exchange_settlement_obligation_guid** | **str, none_type** | The identifier of the exchange settlement obligation that this payment is associated with. | [optional] 
**environment** | **str, none_type** | The environment the payment is expeged in. | [optional] 
**credit_account_guid** | **str, none_type** | The identifier of the credit platform account the payment should be credited to. | [optional] 
**settlement_account_guid** | **str, none_type** | The identifier of the settlement cybrid account the funds should be made available in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


