# InternalTransactionMonitor

Response body for transaction_monitors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the monitor. | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | 
**account_guid** | **str** | The account guid to monitor. | 
**directions** | **[str]** | The directions to monitor. | 
**polling_interval** | **int** | The polling interval in seconds. | 
**start_date** | **date** | The start date to monitor from. | 
**type** | **str** | The type of monitor. | defaults to "account"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


