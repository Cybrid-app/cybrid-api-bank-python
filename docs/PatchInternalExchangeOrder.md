# PatchInternalExchangeOrder

Request body for exchange_order modification.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_order_guid** | **str, none_type** | The unique identifier for the order in the provider system. | [optional] 
**unassigned_receive_amount** | **int, none_type** | The unassigned receive amount in base units of the currency. | [optional] 
**unassigned_deliver_amount** | **int, none_type** | The unassigned deliver in base units of the currency. | [optional] 
**executed_receive_amount** | **int, none_type** | The executed receive amount in base units of the currency. | [optional] 
**executed_deliver_amount** | **int, none_type** | The executed deliver in base units of the currency. | [optional] 
**state** | **str, none_type** | The state of the resource. | [optional] 
**pending_at** | **datetime, none_type** | The timestamp when the order was set to pending. | [optional] 
**failed_at** | **datetime, none_type** | The timestamp when the order was set to failed. | [optional] 
**completed_at** | **datetime, none_type** | The timestamp when the order was set to completed. | [optional] 
**failure_code** | **str, none_type** | The error message in case of failure. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


