# PostInternalComplianceDecision


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The compliance decision&#39;s type | 
**decided_at** | **datetime** | ISO8601 datetime the compliance decision was rendered. | 
**outcome** | **str** | The outcome of the verification process. | 
**expired_at** | **datetime** | ISO8601 datetime the compliance decision is expired. | [optional] 
**customer_guid** | **str** | The identifier of the customer that corresponds to this decision. | [optional] 
**identity_verification_guid** | **str** | The identifier of the identity verification that corresponds to this decision. | [optional] 
**reference_id** | **str, none_type** | A link to where the manual compliance decision can be found. | [optional] 
**comment** | **str, none_type** | The comment associated with the manual compliance decision. | [optional] 
**failure_codes** | **[str]** | The reason codes explaining the outcome. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


