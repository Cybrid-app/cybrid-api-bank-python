# IdentityVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**type** | **str** | The identity verification type; one of kyc, bank_account, or counterparty. | [optional] 
**method** | **str** | The identity verification method; one of attested, document_submission, enhanced_due_diligence, id_and_selfie, tax_id_and_selfie, business_registration, attested_id_and_selfie, attested_business_registration, watchlists, attested_ownership, or account_ownership. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**customer_guid** | **str, none_type** | The customer&#39;s identifier. | [optional] 
**counterparty_guid** | **str, none_type** | The counterparty&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str, none_type** | The external bank account&#39;s identifier. | [optional] 
**state** | **str** | The identity verification state; one of storing, waiting, pending, reviewing, expired, or completed. | [optional] 
**outcome** | **str, none_type** | The identity verification outcome; one of passed or failed. | [optional] 
**failure_codes** | **[str], none_type** | The reason codes explaining the outcome. | [optional] 
**compliance_decisions** | [**[ComplianceDecision]**](ComplianceDecision.md) | The compliance decisions associated with the identity verification. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


