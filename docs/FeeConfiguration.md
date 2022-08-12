# FeeConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the exchange. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier. | [optional] 
**product_type** | **str** | The type of product being configured. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the bank was created at. | [optional] 
**product_provider** | **str, none_type** | The provider for the product being configured. | [optional]  if omitted the server will use the default value of "compound"
**fees** | [**[Fee]**](Fee.md) | The fees associated with the configuration | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


