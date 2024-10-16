# PostFee

Request body for fee creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The fee&#39;s type | 
**spread_fee** | **int, none_type** | The percentage amount, in basis points, to apply when charging a fee. Required when type is spread. | [optional] 
**fixed_fee** | **int, none_type** | The fixed amount to apply when charging a fee; for trades, the fiat asset is used. Required when type is fixed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


