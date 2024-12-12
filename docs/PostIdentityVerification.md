# PostIdentityVerification

Request body for identity verification creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of identity verification. | 
**customer_guid** | **str, none_type** | The customer&#39;s identifier. | [optional] 
**expected_behaviours** | **[str], none_type** | The optional expected behaviour to simulate. | [optional] 
**method** | **str, none_type** | The identity verification method. Required when type is counterparty, type is kyc, or type is bank_account. | [optional] 
**counterparty_guid** | **str, none_type** | The counterparty&#39;s identifier. Required when type is counterparty. | [optional] 
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country the customer is being verified in. If not present, will default to the Bank&#39;s configured country code. Optional when type is kyc and method is id_and_selfie, type is kyc and method is tax_id_and_selfie, or type is kyc and method is business_registration. | [optional] 
**name** | [**PostIdentityVerificationName**](PostIdentityVerificationName.md) |  | [optional] 
**address** | [**PostIdentityVerificationAddress**](PostIdentityVerificationAddress.md) |  | [optional] 
**date_of_birth** | **date, none_type** | The customer&#39;s date of birth. Required when type is kyc and method is attested. | [optional] 
**identification_numbers** | [**[PostIdentificationNumber], none_type**](PostIdentificationNumber.md) | The customer&#39;s identification numbers. Required when type is kyc and method is attested. | [optional] 
**external_bank_account_guid** | **str, none_type** | The external bank account&#39;s identifier. Required when type is bank_account. | [optional] 
**phone_number** | **str, none_type** | The customer&#39;s phone number. Optional when type is bank_account and method is attested_ownership. | [optional] 
**email_address** | **str, none_type** | The customer&#39;s email address. Optional when type is bank_account and method is attested_ownership. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


