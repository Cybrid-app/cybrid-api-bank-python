# PostInternalTrade


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_type** | **str** | The type of trade. | 
**quote_guid** | **str** | The associated quote&#39;s identifier. | 
**environment** | **str** | The environment the quote is for. | 
**fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the trade. Required if the customer or bank has multiple fiat accounts. | [optional] 
**source_account_guid** | **str, none_type** | The identifier for the source account to use for the trade. Required if there are multiple cybrid accounts. | [optional] 
**destination_account_guid** | **str, none_type** | The identifier for the destination account to use for the trade. Required if there are multiple cybrid accounts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


