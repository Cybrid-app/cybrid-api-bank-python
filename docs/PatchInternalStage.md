# PatchInternalStage

Request body for stage creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the stage. | 
**failure_code** | **str, none_type** | The failure code for the stage, if applicable. | [optional] 
**completed_at** | **datetime, none_type** | The timestamp when the stage failed, if applicable. | [optional] 
**failed_at** | **datetime, none_type** | The timestamp when the stage failed, if applicable. | [optional] 
**accounts** | [**[PatchInternalAccountAssociation], none_type**](PatchInternalAccountAssociation.md) | The accounts associated with the stage. | [optional] 
**fees** | [**[PatchInternalFeeAssociation], none_type**](PatchInternalFeeAssociation.md) | The custom fees associated with the stage | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


