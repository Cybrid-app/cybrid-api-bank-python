# PostInternalInternalWalletConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of configuration: bank or platform. | 
**transfer_wallet_guid** | **str** | The identifier of the internal wallet to use for transfers. | 
**asset** | **str** | The asset code. | 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**invoice_wallet_guid** | **str, none_type** | The identifier of the internal wallet to use for invoices. This must be a Strike internal wallet. | [optional] 
**storage_wallet_guid** | **str, none_type** | The identifier of the internal wallet to use for storage. This must be a BitGo internal wallet. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


