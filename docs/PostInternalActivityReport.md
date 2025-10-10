# PostInternalActivityReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The activity report&#39;s type | 
**environment** | **str** | The environment for the customer. | 
**customer_guid** | **str** | The identifier of the customer for the report. | 
**asset** | **str** | The asset code to report on. | 
**start_time** | **datetime** | Inclusive ISO8601 datetime start time of the period to report on. | 
**end_time** | **datetime** | Inclusive ISO8601 datetime end time of the period to report on. | 
**exclude_guids** | **[str]** | The list of guids to exclude from the report. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


