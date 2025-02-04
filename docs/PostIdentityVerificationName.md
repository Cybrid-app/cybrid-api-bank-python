# PostIdentityVerificationName

The customer's name. Required when type is kyc and method is attested, type is kyc and method is attested_business_registration, type is kyc and method is attested_id_and_selfie, or type is bank_account and method is attested_ownership.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str, none_type** | The customer&#39;s first name. Required when type is kyc and method is attested or type is kyc and method is attested_id_and_selfie. Optional when type is bank_account and method is attested_ownership. | [optional] 
**middle** | **str, none_type** | The customer&#39;s middle name. Optional when type is kyc and method is attested, type is kyc and method is attested_id_and_selfie, or type is bank_account and method is attested_ownership. | [optional] 
**last** | **str, none_type** | The customer&#39;s last name. Required when type is kyc and method is attested or type is kyc and method is attested_id_and_selfie. Optional when type is bank_account and method is attested_ownership. | [optional] 
**full** | **str, none_type** | The customer&#39;s full name. Required when type is kyc and method is attested_business_registration or type is bank_account and method is attested_ownership. Optional when type is kyc and method is attested or type is kyc and method is attested_id_and_selfie. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


