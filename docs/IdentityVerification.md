# IdentityVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**customer_guid** | **str** | The identity verification&#39;s identifier. | [optional] 
**type** | **str** | The identity verification type; one of kyc or bank_account. | [optional] 
**method** | **str** | The identity verification method; one of business_registration, id_and_selfie, tax_id_and_selfie, attested, plaid_identity_match, or document_submission. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**state** | **str** | The identity verification state; one of storing, waiting, expired, or completed. | [optional] 
**outcome** | **str, none_type** | The identity verification outcome; one of passed or failed. | [optional] 
**failure_codes** | **[str], none_type** | The reason codes explaining the outcome. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


