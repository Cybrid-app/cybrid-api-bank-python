# InternalFeeCharge

Response body for fee_charges.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The platform environment. | 
**guid** | **str** | Auto-generated unique identifier for the entity. | 
**created_at** | **datetime** | ISO8601 datetime the entity was created at. | 
**updated_at** | **datetime** | ISO8601 datetime the entity was last updated at. | 
**asset** | **str** | The fee amount asset code. | 
**amount** | **int** | The fee amount in cents. | 
**source_account_guid** | **str** | The source account identifier. | 
**destination_account_guid** | **str** | The destination account identifier. | 
**state** | **str** | The state of the entity. | 
**type** | **str** | The type of the entity. | defaults to "platform_assignment"
**failure_code** | **str, none_type** | The failure code if the entity is in a failed state. | [optional]  if omitted the server will use the default value of "non_sufficient_funds"
**exchange_order_guid** | **str, none_type** | The exchange order identifier. Required when type is platform_assignment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


