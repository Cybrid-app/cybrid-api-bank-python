# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The account type; one of trading, fee, fiat, gas, or reserve. | [optional] 
**guid** | **str** | Auto-generated unique identifier for the account. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**name** | **str** | The name of the account. | [optional] 
**bank_guid** | **str** | The bank identifier associated with the account. | [optional] 
**customer_guid** | **str** | The customer identifier associated with the account. | [optional] 
**platform_balance** | **int** | The amount of funds that are in the account, in base units of the asset. | [optional] 
**platform_available** | **int** | The amount of funds that are in the account, in base units of the asset, that are available for use on the platform. | [optional] 
**state** | **str** | The state of the account; one of storing or created. | [optional] 
**labels** | **[str], none_type** | The labels associated with the account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


