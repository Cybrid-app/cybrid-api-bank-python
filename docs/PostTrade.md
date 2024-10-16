# PostTrade

Request body for trade creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_guid** | **str** | The associated quote&#39;s identifier. | 
**trade_type** | **str, none_type** | The type of trade. | [optional]  if omitted the server will use the default value of "platform"
**fiat_account_guid** | **str, none_type** | The identifier for the fiat account to use for the trade. Required if the customer or bank has multiple fiat accounts. | [optional] 
**expected_error** | **str, none_type** | The optional expected error to simulate trade failure. | [optional] 
**labels** | **[str], none_type** | The labels associated with the trade. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


