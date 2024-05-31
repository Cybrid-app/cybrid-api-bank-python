# IdentityVerificationWithDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**customer_guid** | **str** | The identity verification&#39;s identifier. | [optional] 
**type** | **str** | The identity verification type; one of kyc or bank_account. | [optional] 
**method** | **str** | The identity verification method; one of business_registration, id_and_selfie, tax_id_and_selfie, attested, attested_ownership, account_ownership, plaid_identity_match, or document_submission. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**state** | **str** | The identity verification state; one of storing, waiting, expired, or completed. | [optional] 
**outcome** | **str, none_type** | The identity verification outcome; one of passed or failed. | [optional] 
**failure_codes** | **[str], none_type** | The reason codes explaining the outcome. | [optional] 
**compliance_checks** | [**[ComplianceCheck]**](ComplianceCheck.md) | The compliance checks associated with the identity verification. | [optional] 
**compliance_decisions** | [**[ComplianceDecision]**](ComplianceDecision.md) | The compliance decisions associated with the identity verification. | [optional] 
**verification_checks** | [**[ComplianceDecision]**](ComplianceDecision.md) | Deprecated; use compliance_decisions instead. | [optional] 
**persona_inquiry_id** | **str, none_type** | The Persona identifier of the backing inquiry. | [optional] 
**persona_state** | **str, none_type** | The Persona state of the backing inquiry; one of waiting, pending, reviewing, processing, expired, completed, or unknown. | [optional] 
**external_bank_account_guid** | **str, none_type** | The external bank account&#39;s identifier. | [optional] 
**pii** | [**IdentityVerificationWithDetailsPii**](IdentityVerificationWithDetailsPii.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


