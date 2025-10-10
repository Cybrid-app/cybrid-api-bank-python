# PostInternalStage

Request body for stage creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of stage. | 
**plan_guid** | **str** | The unique identifier for the  plan. | 
**accounts** | [**[PostInternalAccountAssociation]**](PostInternalAccountAssociation.md) | The accounts associated with the stage. | 
**fees** | [**[PostInternalFeeAssociation]**](PostInternalFeeAssociation.md) | The custom fees associated with the stage | 
**stage_index** | **int** | The index of the stage within the plan, starting from 0. | 
**failure_code** | **str, none_type** | The failure code for the stage, if applicable. | [optional] 
**failed_at** | **datetime, none_type** | The timestamp when the stage failed, if applicable. | [optional] 
**planned_at** | **datetime, none_type** | The timestamp when the stage is planned, if applicable. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


