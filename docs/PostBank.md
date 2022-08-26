# PostBank


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The bank&#39;s name. | 
**type** | **str** | The bank&#39;s type. At present, only **sandbox** is supported. | 
**supported_trading_symbols** | **[str]** | The bank&#39;s list of supported trading symbols. | 
**features** | **[str]** | The bank&#39;s enabled features. At present, both **attestation_identity_records** and **backstopped_funding_source** must be set. | 
**supported_savings_configuration** | **{str: ([str],)}** | The bank&#39;s list of supported savings asset by provider. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


