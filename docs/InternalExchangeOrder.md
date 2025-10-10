# InternalExchangeOrder

Response body for exchange_orders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The platform environment. | 
**guid** | **str** | Auto-generated unique identifier for the entity. | 
**created_at** | **datetime** | ISO8601 datetime the entity was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the entity was last updated at. | 
**exchange_guid** | **str** | The exchange identifier. | 
**trade_guids** | **[str]** | The set of included trade guids. | 
**symbol** | **str** | The symbol code representing the trading pair. | 
**side** | **str** | The direction for order. | 
**deliver_asset** | **str** | The deliver amount asset code. | 
**receive_asset** | **str** | The receive amount asset code. | 
**requested_deliver_amount** | **int** | The requested deliver amount in cents. | 
**requested_receive_amount** | **int** | The requested receive amount in cents. | 
**source_payable_account_guid** | **str** | The source payable account identifier. | 
**destination_payable_account_guid** | **str** | The destination payable account identifier. | 
**source_receivable_account_guid** | **str** | The source receivable account identifier. | 
**destination_receivable_account_guid** | **str** | The destination receivable account identifier. | 
**state** | **str** | The state of the entity. | 
**type** | **str** | The type of the entity. | defaults to "fixed"
**executed_deliver_amount** | **int, none_type** | The executed deliver amount in cents. | [optional] 
**executed_receive_amount** | **int, none_type** | The executed receive amount in cents. | [optional] 
**unassigned_deliver_amount** | **int, none_type** | The unassigned deliver amount in cents. | [optional] 
**unassigned_receive_amount** | **int, none_type** | The unassigned receive amount in cents. | [optional] 
**failure_code** | **str, none_type** | The failure code if the entity is in a failed state. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


