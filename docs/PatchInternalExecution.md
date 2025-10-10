# PatchInternalExecution

Request body for execution update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the execution. | 
**source_executed_amount** | **int, none_type** | The executed amount for source account | [optional] 
**destination_executed_amount** | **int, none_type** | The executed amount for destination account | [optional] 
**started_at** | **datetime, none_type** | The timestamp when the plan started. | [optional] 
**completed_at** | **datetime, none_type** | The timestamp when the plan completed. | [optional] 
**failed_at** | **datetime, none_type** | The timestamp when the plan failed. | [optional] 
**failure_code** | **str, none_type** | The failure code for the plan, if applicable. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


