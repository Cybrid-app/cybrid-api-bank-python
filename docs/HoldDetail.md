# HoldDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the hold; one of active, completed, or storing | 
**started_at** | **datetime** | ISO8601 datetime the hold was started at. | 
**type** | **str, none_type** | The type of hold; one of customer_hold_duration, reserve_below_minimum, screening_administrative, or screening_non_administrative. | [optional] 
**completed_at** | **datetime, none_type** | ISO8601 datetime the hold was completed at. | [optional] 
**eta_at** | **datetime, none_type** | ISO8601 datetime the hold is expected to complete at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


