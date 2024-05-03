# ComplianceCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of compliance check; one of business_watchlists, business_verification, business_tax_id_verification, person_attested, person_tax_id_attested, person_watchlists, person_verification, person_authentication, person_gov_id_verification, person_tax_id_verification, external_bank_account_verification, or external_bank_account_attested. | 
**outcome** | **str** | The outcome of the compliance check; one of passed, failed, or inconclusive. | [optional] 
**failure_codes** | **[str], none_type** | The reason codes explaining the outcome. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


