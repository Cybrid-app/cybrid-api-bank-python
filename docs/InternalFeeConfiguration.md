# InternalFeeConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the configuration. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier. | [optional] 
**type** | **str** | The type of configuration. | [optional] 
**product_type** | **str** | The type of product being configured. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**counter_asset** | **str, none_type** | The counter asset code. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**fees** | [**[InternalFee]**](InternalFee.md) | The fees associated with the configuration | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


