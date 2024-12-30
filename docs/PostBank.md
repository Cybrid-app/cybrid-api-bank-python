# PostBank

Request body for bank creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the bank. | 
**supported_trading_symbols** | **[str]** | The trading symbols supported by the bank. | 
**supported_fiat_account_assets** | **[str]** | The fiat account assets supported by the bank. | 
**supported_country_codes** | **[str]** | The country codes supported by the bank. | 
**features** | **[str]** | The features supported by the bank. | 
**type** | **str** | The type of bank. | defaults to "sandbox"
**supported_payout_symbols** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** | The payout symbols supported by the bank. This is not yet supported and should be nil or empty. | [optional] 
**cors_allowed_origins** | **[str], none_type** | The list of allowed CORS origin URIs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


