# IdentityVerificationWithDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**customer_guid** | **str** | The customer&#39;s identifier. | [optional] 
**type** | **str** | The type of identity verification. | [optional] 
**method** | **str** | The identity verification method. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the customer was created at. | [optional] 
**state** | **str** | The state of the verification process. | [optional] 
**outcome** | **str, none_type** | The outcome of the verification process. | [optional] 
**failure_codes** | **[str]** | The reason codes explaining the outcome. | [optional] 
**persona_inquiry_id** | **str, none_type** | The Persona identifier of the backing inquiry. | [optional] 
**persona_state** | **str, none_type** | The Persona state of the backing inquiry. | [optional] 
**external_bank_account_guid** | **str, none_type** | The external bank account&#39;s identifier. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


