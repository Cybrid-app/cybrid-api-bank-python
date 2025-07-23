# DepositAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**bank_guid** | **str** | The address&#39; bank identifier. | [optional] 
**customer_guid** | **str, none_type** | The address&#39; customer identifier. | [optional] 
**account_guid** | **str** | The address&#39; account identifier. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**asset** | **str** | The asset the transfer is related to, e.g., USD. | [optional] 
**state** | **str** | The state of the address; one of storing, created, or failed. | [optional] 
**address** | **str** | The blockchain address. | [optional] 
**format** | **str** | The blockchain address format; one of standard or legacy. | [optional] 
**tag** | **str** | The blockchain address tag. | [optional] 
**labels** | **[str], none_type** | The labels associated with the address. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


