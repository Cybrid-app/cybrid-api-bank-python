# InternalExternalWalletScreening


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The identifier of the external wallet screening. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**external_wallet_guid** | **str** | The identifier of the external wallet that was screened. | [optional] 
**state** | **str** | The state of the external wallet screening. | [optional] 
**outcome** | **str, none_type** | The outcome of the external wallet screening. | [optional] 
**failure_code** | **str, none_type** | The failure code of the external wallet screening. | [optional]  if omitted the server will use the default value of "invalid_address"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


