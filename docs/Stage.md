# Stage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The unique identifier for the stage. | 
**type** | **str** | The type of stage; one of payout. | 
**state** | **str** | The state of the stage; one of storing, planning, planned, executing, holding, completed, or failed. | 
**identifiers** | [**[StageIdentifier]**](StageIdentifier.md) | Provider-issued identifiers associated with this stage. Always present, possibly empty. | 
**links** | [**[StageLink]**](StageLink.md) | Provider-issued links associated with this stage. Always present, possibly empty. | 
**created_at** | **datetime** | The ISO8601 datetime the stage was created at. | 
**updated_at** | **datetime** | The ISO8601 datetime the stage was last updated at. | 
**source_account** | [**AccountAssociation**](AccountAssociation.md) |  | 
**destination_account** | [**AccountAssociation**](AccountAssociation.md) |  | 
**fees** | [**[FeeAssociation]**](FeeAssociation.md) | The fees associated with the stage. | 
**failure_code** | **str, none_type** | The failure code for failed stages. | [optional] 
**hold_started_at** | **datetime, none_type** | The ISO8601 datetime when the stage entered the hold state, if applicable. | [optional] 
**hold_duration** | **int, none_type** | The approximate time (in seconds) that the stage will be held for, if applicable. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


