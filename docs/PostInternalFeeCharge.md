# PostInternalFeeCharge

Request body for fee_charge creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The environment for the configuration. | 
**type** | **str** | The order type. | defaults to "platform_assignment"
**exchange_order_guid** | **str, none_type** | The exchange order guid to generate a fee charge for Required when type is platform_assignment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


