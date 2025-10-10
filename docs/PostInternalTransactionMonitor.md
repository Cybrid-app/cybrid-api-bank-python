# PostInternalTransactionMonitor

Request body for transaction_monitor creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of transaction_monitor to create. | defaults to "account"
**account_guid** | **str, none_type** | The account identifier. Required when type is account. | [optional] 
**direction** | **str, none_type** | The direction to monitor for transactions Optional when type is account. | [optional] 
**polling_interval** | **int, none_type** | The interval in seconds to poll for transactions. Required when type is account. | [optional] 
**start_date** | **date, none_type** | The date to start monitoring transactions. Required when type is account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


