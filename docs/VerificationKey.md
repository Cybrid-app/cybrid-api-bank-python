# VerificationKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the verification key. | [optional] 
**bank_guid** | **str** | The banks&#39;s identifier. | [optional] 
**type** | **str** | The verification key&#39;s type. | [optional]  if omitted the server will use the default value of "attestation"
**state** | **str** | The verification key&#39;s state. | [optional] 
**failure_code** | **str, none_type** | The verification key&#39;s failure code (if any). | [optional] 
**algorithm** | **str** | The verification key&#39;s algorithm. | [optional]  if omitted the server will use the default value of "RS512"
**fingerprint** | **str** | The verification key&#39;s cryptographic fingerprint. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the verification key was created at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


