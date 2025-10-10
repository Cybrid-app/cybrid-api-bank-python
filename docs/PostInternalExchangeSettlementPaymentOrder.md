# PostInternalExchangeSettlementPaymentOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_settlement_guid** | **str** | The identifier of the exchange settlement that this payment is associated with. | 
**exchange_settlement_obligation_guid** | **str** | The identifier of the exchange settlement obligation that this payment is associated with. | 
**sequence_number** | **int** | The sequence number of the payment order | 
**payment_amount** | **int** | The amount expected to be received as part of this payment. | 
**internal_account_guid** | **str** | The identifier of the internal account that is expected to originate the payment. | 
**internal_account_type** | **str** | The type of the internal account that is expected to originate the payment. | 
**external_account_guid** | **str** | The identifier of the external account that is expected to receive the payment. | 
**external_account_type** | **str** | The type of the external account that is expected to receive the payment. | 
**network_fee** | **int, none_type** | The network fee for the payment. Only required for crypto payments. | [optional] 
**expected_state** | **str** | The expected state of the underlying money transfer for the payment order (sandbox only) | [optional] 
**network_fee_account_guid** | **str, none_type** | The identifier of the liability network fee account that has the network fee. | [optional] 
**internal_network_fee_wallet_guid** | **str, none_type** | The identifier of the cash network fee account that has the network fee. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


