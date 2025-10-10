# PostInternalActivityLimitConfiguration

Request body for activity limit configuration creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the configuration. | 
**limits** | [**[ParamInternalActivityLimit]**](ParamInternalActivityLimit.md) | The limits for the configuration. | 
**activity** | **str, none_type** | The activity type of the configuration. | [optional] 
**side** | **str, none_type** | The side of the activity. | [optional] 
**environment** | **str, none_type** | The environment for the configuration. Required when type is platform. | [optional] 
**audience** | **str, none_type** | The audience for the configuration. Required when type is platform or type is bank. | [optional] 
**country_code** | **str, none_type** | The country code for the configuration. Required when type is platform. | [optional] 
**bank_guid** | **str, none_type** | The bank GUID for the configuration. Required when type is bank. | [optional] 
**customer_guid** | **str, none_type** | The customer GUID for the configuration. Required when type is customer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


