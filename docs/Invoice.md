# Invoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the payment instruction. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**account_guid** | **str** | The account payment will ultimately be received into. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**invoice_type** | **str** | The type of invoice; one of lightning. | [optional] 
**asset** | **str** | The asset code the customer will receive the funds in. | [optional] 
**receive_amount** | **int, none_type** | The amount to be received in base units of the asset, i.e., the amount the customer will receive after fees. ONLY one of receive_amount or deliver_amount is required. | [optional] 
**deliver_amount** | **int, none_type** | The amount to be delivered in base units of the asset, i.e., the amount the customer will receive before fees. ONLY one of receive_amount or deliver_amount is required. | [optional] 
**fee** | **int, none_type** | The fee associated with this invoice in base units of the asset. | [optional] 
**state** | **str** | The state of the invoice; one of storing, unpaid, cancelling, cancelled, settling, or paid. | [optional] 
**labels** | **[str], none_type** | The labels associated with the invoice. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


