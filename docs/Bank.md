# Bank


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the bank. | 
**organization_guid** | **str** | The organization&#39;s identifier. | 
**name** | **str** | The bank&#39;s name. | 
**type** | **str** | The bank type; one of sandbox or production. | 
**features** | **[str]** | The bank&#39;s enabled features. | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**supported_trading_symbols** | **[str]** | The bank&#39;s list of supported trading symbols. | [optional] 
**supported_fiat_account_assets** | **[str]** | The bank&#39;s list of supported fiat symbols. | [optional] 
**supported_country_codes** | **[str]** | The bank&#39;s list of supported country codes. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


