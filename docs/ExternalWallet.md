# ExternalWallet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the wallet. | [optional] 
**name** | **str** | The name of the wallet. | [optional] 
**asset** | **str** | The asset code. | [optional] 
**environment** | **str** | The environment that the wallet is configured for; one of sandbox or production. | [optional] 
**bank_guid** | **str** | The bank identifier. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**counterparty_guid** | **str, none_type** | The counterparty identifier. | [optional] 
**address** | **str** | The blockchain wallet address for the wallet. | [optional] 
**tag** | **str, none_type** | The blockchain tag to use when transferring crypto to the wallet. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**state** | **str** | The state of the external wallet; one of storing, pending, failed, completed, deleting, or deleted. | [optional] 
**failure_code** | **str, none_type** | The failure code of an external wallet (if any) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


