# PostPlanDestinationAccount

Destination account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The destination account&#39;s identifier. | 
**amount** | **int, none_type** | The amount to be delivered in base units of the source account currency | [optional] 
**payment_rail** | **str, none_type** | The desired payment rail to use to initiate a fiat transfer to the destination account. | [optional] 
**security_question** | **str, none_type** | The security question for an Interac e-Transfer withdrawal or conversion. Only accepted for an e-transfer rail destination; must be paired with security_answer. | [optional] 
**security_answer** | **str, none_type** | The security answer the recipient must provide to claim an Interac e-Transfer. Only accepted for an e-transfer rail destination; must be paired with security_question. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


