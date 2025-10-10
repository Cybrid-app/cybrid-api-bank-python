# PostInternalExchangeMonitor

Request body for exchange_monitor creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_guid** | **str** | The exchangee identifier. | 
**cron_schedule** | **str** | The cron schedule for polling the exchange. | 
**allowed_symbols** | **[str], none_type** | The trading symbols to allow in the settlement; omit if all symbols should be allowed. | [optional] 
**denied_symbols** | **[str], none_type** | The trading symbols to deny in the settlement; omit if no symbols should be denied. | [optional] 
**workday_countries** | **[str], none_type** | The country codes to skip settlements on non-workdays; omit if workdays should not be factored. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


