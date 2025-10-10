# InternalInternalWalletConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the configuration. | [optional] 
**type** | **str** | The type of configuration: bank or platform. | [optional] 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**transfer_wallet_guid** | **str** | The identifier of the internal wallet to use for transfers. | [optional] 
**invoice_wallet_guid** | **str, none_type** | The identifier of the internal wallet to use for creating invoices. | [optional] 
**storage_wallet_guid** | **str, none_type** | The identifier of the internal wallet to use for crypto cold storage. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


