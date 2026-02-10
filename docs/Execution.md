# Execution



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the quote. | 
**type** | **str** | The type of product the plan is for; one of remittance. | 
**plan_guid** | **str** | The unique identifier for the plan. | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | 
**state** | **str** | The state of the execution; one of storing, executing, completed, or failed. | 
**source_account** | [**AccountAssociation**](AccountAssociation.md) |  | 
**destination_account** | [**AccountAssociation**](AccountAssociation.md) |  | 
**stages** | [**[Stage]**](Stage.md) | The stages of the execution. | 
**fees** | [**[FeeAssociation]**](FeeAssociation.md) | The fees associated with the execution. | 
**travel_rule_info** | [**ExecutionTravelRuleInfo**](ExecutionTravelRuleInfo.md) |  | 
**bank_guid** | **str, none_type** | The unique identifier for the bank. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed executions. | [optional] 
**purpose_of_transaction** | **str, none_type** | The purpose of transaction for the execution. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


