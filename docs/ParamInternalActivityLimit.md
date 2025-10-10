# ParamInternalActivityLimit

Request body for activity limit creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the limit. | 
**limit_type** | **str** | The type of the limit. | 
**limit_asset** | **str** | The asset of the limit. | 
**limit_amount** | **int** | The amount of the limit. | 
**limit_interval** | **int, none_type** | The interval of the limit. Required when limit_type is rolling. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


