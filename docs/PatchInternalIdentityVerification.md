# PatchInternalIdentityVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **datetime** | ISO8601 datetime the identity verification was started at. | [optional] 
**external_bank_account_check_guid** | **str, none_type** | The GUID of the external bank account check backing the verification. | [optional] 
**attested_check_guid** | **str, none_type** | The GUID of the attested check backing the verification. | [optional] 
**identity_workflow_guid** | **str, none_type** | The GUID of the identity workflow backing the verification. | [optional] 
**pending_at** | **datetime** | ISO8601 datetime the identity verification was started by the user at. | [optional] 
**reviewing_at** | **datetime** | ISO8601 datetime the identity verification was marked for review at. | [optional] 
**expired_at** | **datetime** | ISO8601 datetime the identity verification was expired at. | [optional] 
**completed_at** | **datetime** | ISO8601 datetime the identity verification was completed at. | [optional] 
**outcome** | **str** | The outcome of the identity verification. | [optional] 
**failure_codes** | **[str]** | The reason codes explaining the outcome. | [optional] 
**supporting_file_guids** | **[str]** | The GUIDs of the supporting files backing the verification. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


