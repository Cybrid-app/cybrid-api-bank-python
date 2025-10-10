# PostInternalFeeAssociation

Request body for fee association creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of fee. | 
**asset** | **str** | The asset code associated with the stage. | 
**step_identifier** | **str** | The unique identifier for the step. | 
**quoted_amount** | **int, none_type** | The estimated fee amount in base units of the currency. | [optional] 
**executed_amount** | **int, none_type** | The executed fee amount in base units of the currency. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


