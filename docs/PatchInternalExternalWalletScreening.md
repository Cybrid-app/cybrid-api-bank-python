# PatchInternalExternalWalletScreening


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **datetime** | ISO8601 datetime the external wallet screening was started at. | [optional] 
**decided_at** | **datetime** | ISO8601 datetime the external wallet screening was decided at. | [optional] 
**outcome** | **str** | The outcome of the external wallet screening. | [optional] 
**comment** | **str** | The comment to justify the outcome. | [optional] 
**reference_id** | **str** | An internal reference to look up the case. | [optional] 
**failure_code** | **str** | The failure code for failed screenings. | [optional]  if omitted the server will use the default value of "invalid_address"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


