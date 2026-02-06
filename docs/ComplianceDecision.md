# ComplianceDecision


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of verification check; one of business_watchlists, business_verification, business_tax_id_verification, business_attested, person_attested, person_tax_id_attested, person_watchlists, person_verification, person_authentication, person_gov_id_verification, person_tax_id_verification, business_associate_gov_id_attested, business_associate_authentication_attested, business_associate_attested, business_associate_tax_id_attested, business_associate_watchlists_attested, external_bank_account_verification, or external_bank_account_attested. | 
**state** | **str** | The state of the verification check; one of passed, failed, expired, or invalidated. | 
**failure_codes** | **[str], none_type** | The reason codes explaining the outcome. | [optional] 
**expired_at** | **datetime, none_type** | ISO8601 datetime the compliance decision is expired. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


