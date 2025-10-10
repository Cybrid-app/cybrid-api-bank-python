# InternalExchangeMonitor

Response body for exchange_monitors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the monitor. | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | 
**exchange_guid** | **str** | The exchange identifier. | 
**cron_schedule** | **str** | The cron schedule to run the monitor at. | 
**denied_symbols** | **[str], none_type** | Array of trading symbol codes to deny; empty if all symbols are allowed. | [optional] 
**allowed_symbols** | **[str], none_type** | Array of trading symbol codes to allow; empty if all symbols should be allowed. | [optional] 
**workday_countries** | **[str], none_type** | Array of ISO 3166 country 2-Alpha country codes to use for workday calculations. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


