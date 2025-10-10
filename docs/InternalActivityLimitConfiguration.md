# InternalActivityLimitConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the configuration. | [optional] 
**type** | **str** | The type of configuration; one of platform, bank, or customer. | [optional] 
**activity** | **str, none_type** | The (optional) activity the configuration is associated with; one of trading, funding, book_transfer, or crypto_transfer. | [optional] 
**side** | **str, none_type** | The (optional) side the configuration is associated with; one of deposit or withdrawal. | [optional] 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier that the configuration is associated with. | [optional] 
**audience** | **str, none_type** | The payment rail. | [optional] 
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country code the configuration. | [optional] 
**limits** | [**[InternalActivityLimit]**](InternalActivityLimit.md) | The limits for the configuration. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


