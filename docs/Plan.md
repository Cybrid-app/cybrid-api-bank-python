# Plan



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the entity. | 
**type** | **str** | The type of product the plan is for; one of remittance. | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | 
**expires_at** | **datetime** | ISO8601 datetime the plan will expire at. | 
**state** | **str** | The state of the plan; one of storing, planning, completed, or failed. | 
**source_account** | [**AccountAssociation**](AccountAssociation.md) |  | 
**destination_account** | [**AccountAssociation**](AccountAssociation.md) |  | 
**stages** | [**[Stage]**](Stage.md) | The stages of the plan. | 
**fees** | [**[FeeAssociation]**](FeeAssociation.md) | The fees associated with the plan. | 
**travel_rule_info** | [**PlanTravelRuleInfo**](PlanTravelRuleInfo.md) |  | 
**bank_guid** | **str, none_type** | The unique identifier for the bank. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed plans. | [optional] 
**purpose_of_transaction** | **str, none_type** | The purpose of transaction for the plan. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


