# PostFeeConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **str** | The type of product being configured. | 
**asset** | **str** | The asset code. | 
**fees** | [**[PostFee]**](PostFee.md) | The fees associated with the configuration | 
**product_provider** | **str, none_type** | The provider for the product being configured. | [optional]  if omitted the server will use the default value of "compound"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


