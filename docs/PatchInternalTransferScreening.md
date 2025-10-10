# PatchInternalTransferScreening


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **datetime** | ISO8601 datetime the transfer screening was started at. | [optional] 
**reviewing_at** | **datetime** | ISO8601 datetime the transfer screening was reviewing at. | [optional] 
**completed_at** | **datetime** | ISO8601 datetime the transfer screening was completed at. | [optional] 
**outcome** | **str** | The outcome of the transfer screening. | [optional] 
**failure_code** | **str** | The failure code for failed screenings. | [optional]  if omitted the server will use the default value of "invalid_operation"
**hold_requested** | **str** | The hold type requested for the transfer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


