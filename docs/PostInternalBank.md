# PostInternalBank

Request body for internal bank creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_guid** | **str** | The organization GUID for which to create the bank. | 
**type** | **str** | The type of bank. | 
**name** | **str** | The name of the bank. | 
**supported_trading_symbols** | **[str]** | The trading symbols supported by the bank. | 
**supported_fiat_account_assets** | **[str]** | The fiat account assets supported by the bank. | 
**supported_country_codes** | **[str]** | The country codes supported by the bank. | 
**features** | **[str]** | The features supported by the bank. | 
**supported_payout_symbols** | [**[PostSupportedPayoutSymbols], none_type**](PostSupportedPayoutSymbols.md) | The payout symbols supported by the bank. | [optional] 
**cors_allowed_origins** | **[str], none_type** | The list of allowed CORS origin URIs. | [optional] 
**persona_theme_id** | **str, none_type** | The persona theme ID for the bank. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


