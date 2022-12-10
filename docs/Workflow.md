# Workflow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the workflow. | [optional] 
**customer_guid** | **str** | The associated customer&#39;s identifier. | [optional] 
**type** | **str** | The type of workflow. | [optional]  if omitted the server will use the default value of "plaid"
**state** | **str** | The state of the workflow. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed workflows. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the bank was created at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


