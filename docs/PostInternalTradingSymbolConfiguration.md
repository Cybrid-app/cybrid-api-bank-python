# PostInternalTradingSymbolConfiguration

Request body for trading symbol configuration updates.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the configuration. | 
**enabled** | **bool** | Flag indicating if the symbol is enabled | 
**symbol** | **str** | The trading symbol being configured | 
**environment** | **str, none_type** | The environment for the configuration. Required when type is platform. | [optional] 
**execution_mode** | **str, none_type** | The execution mode for the configuration Required when type is platform. Optional when type is bank. | [optional] 
**bank_guid** | **str, none_type** | The bank_guid for the configuration. Required when type is bank. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


