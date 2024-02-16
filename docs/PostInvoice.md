# PostInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | The asset code the customer will receive the funds in. | 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**receive_amount** | **int, none_type** | The amount to be received in base units of the asset, i.e., the amount the customer will receive after fees. ONLY one of receive_amount or deliver_amount is required. | [optional] 
**deliver_amount** | **int, none_type** | The amount to be delivered in base units of the asset, i.e., the amount the customer will receive before fees. ONLY one of receive_amount or deliver_amount is required. | [optional] 
**labels** | **[str], none_type** | The labels associated with the customer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


