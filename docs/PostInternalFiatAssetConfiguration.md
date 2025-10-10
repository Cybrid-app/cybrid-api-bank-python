# PostInternalFiatAssetConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of fiat asset configuration: bank or platform. | 
**enabled** | **bool** | Flag indicating if the asset is enabled for fiat accounts on the platform. | 
**asset** | **str** | The asset code. | 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**invoices_enabled** | **bool** | Flag indicating if the asset is enabled for invoices on the platform. | [optional] 
**maximum_number_of_accounts** | **int, none_type** | The maximum number of accounts allowed for the asset on the platform. Must be omitted or set to nil if enabled is False. | [optional] 
**maximum_funding_quote_amount** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The maximum funding quote amounts by rail for the asset. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


