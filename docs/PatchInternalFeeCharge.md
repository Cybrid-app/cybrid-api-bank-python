# PatchInternalFeeCharge

Request body for fee_charge modification.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str, none_type** | The state of the resource. | [optional] 
**pending_at** | **datetime, none_type** | The timestamp when the order was set to pending. | [optional] 
**failed_at** | **datetime, none_type** | The timestamp when the order was set to failed. | [optional] 
**completed_at** | **datetime, none_type** | The timestamp when the order was set to completed. | [optional] 
**failure_code** | **str, none_type** | The error message in case of failure. | [optional]  if omitted the server will use the default value of "non_sufficient_funds"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


