# InternalCryptoAssetConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the configuration. | [optional] 
**type** | **str** | The type of crypto asset configuration: bank or platform. | [optional] 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**deposits_enabled** | **bool** | Flag indicating if the asset is enabled for deposit addresses on the platform. | [optional] 
**invoices_enabled** | **bool** | Flag indicating if the asset is enabled for invoices on the platform. | [optional] 
**storage_enabled** | **bool** | Flag indicating if the asset is enabled for storage on the platform. | [optional] 
**maximum_number_of_addresses** | **int, none_type** | The maximum number of deposit addresses allowed for the asset on the platform. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


