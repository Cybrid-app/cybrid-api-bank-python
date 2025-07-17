# IdentityVerificationWithDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**type** | **str** | The identity verification type; one of kyc, bank_account, or counterparty. | [optional] 
**method** | **str** | The identity verification method; one of attested, document_submission, enhanced_due_diligence, id_and_selfie, tax_id_and_selfie, business_registration, attested_id_and_selfie, attested_business_registration, watchlists, attested_ownership, or account_ownership. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**customer_guid** | **str, none_type** | The identity verification&#39;s identifier. | [optional] 
**counterparty_guid** | **str, none_type** | The identity verification&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str, none_type** | The identity verification&#39;s identifier. | [optional] 
**state** | **str** | The identity verification state; one of storing, waiting, pending, reviewing, expired, or completed. | [optional] 
**outcome** | **str, none_type** | The identity verification outcome; one of passed or failed. | [optional] 
**failure_codes** | **[str], none_type** | The reason codes explaining the outcome. | [optional] 
**compliance_checks** | [**[ComplianceCheck]**](ComplianceCheck.md) | The compliance checks associated with the identity verification. | [optional] 
**compliance_decisions** | [**[ComplianceDecision]**](ComplianceDecision.md) | The compliance decisions associated with the identity verification. | [optional] 
**persona_inquiry_id** | **str, none_type** | The Persona identifier of the backing inquiry. | [optional] 
**persona_state** | **str, none_type** | The Persona state of the backing inquiry; one of waiting, pending, reviewing, processing, expired, completed, or unknown. | [optional] 
**business_associates** | [**[IdentityVerificationBusinessAssociate]**](IdentityVerificationBusinessAssociate.md) | List of associates declared for the business customer. | [optional] 
**pii** | [**IdentityVerificationWithDetailsPii**](IdentityVerificationWithDetailsPii.md) |  | [optional] 
**documents** | [**[IdentityVerificationDocument], none_type**](IdentityVerificationDocument.md) | The documents associated with the identity verification. | [optional] 
**supporting_files** | [**[IdentityVerificationDocument]**](IdentityVerificationDocument.md) | The supporting documents associated with the attested identity verification. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


