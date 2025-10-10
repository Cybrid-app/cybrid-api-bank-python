# PostInternalCryptoAssetConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of crypto asset configuration: bank or platform. | 
**deposits_enabled** | **bool** | Flag indicating if the asset is enabled for deposit addresses on the platform. | 
**asset** | **str** | The asset code. | 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**invoices_enabled** | **bool** | Flag indicating if the asset is enabled for invoices on the platform. | [optional] 
**storage_enabled** | **bool** | Flag indicating if the asset is enabled for storage on the platform. | [optional] 
**maximum_number_of_addresses** | **int, none_type** | The maximum number of deposit addresses allowed for the asset on the platform. Must be omitted or set to nil if deposits_enabled is False. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


