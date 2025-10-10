# PostInternalExchangeOrder

Request body for exchange_order creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The environment for the configuration. | 
**trade_guids** | **[str]** | The trade guids to generate an order for | 
**type** | **str** | The order type. | defaults to "fixed"
**side** | **str, none_type** | The side for the order. | [optional] 
**symbol** | **str, none_type** | The symbol for the order | [optional] 
**deliver_amount** | **int, none_type** | The amount to be delivered in base units of the currency | [optional] 
**receive_amount** | **int, none_type** | The amount to be received in base units of the currency | [optional] 
**source_payable_account_guid** | **str, none_type** | The source payable account guid to use for the order | [optional] 
**source_receivable_account_guid** | **str, none_type** | The source receivable account guid to use for the order | [optional] 
**fixed_amount** | **str, none_type** | The side to fix Optional when type is fixed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


