# PostPlan

Request body for plan creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account** | [**PostPlanSourceAccount**](PostPlanSourceAccount.md) |  | 
**destination_account** | [**PostPlanDestinationAccount**](PostPlanDestinationAccount.md) |  | 
**type** | **str** | The type of product the plan is for. | defaults to "remittance"
**bank_guid** | **str, none_type** | The unique identifier for the bank. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer. | [optional] 
**travel_rule_info** | [**PostPlanTravelRuleInfo**](PostPlanTravelRuleInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


