# PostIdentityVerificationAddress

The customer's address. Required when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str, none_type** | The first line of the address. Required when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership. | [optional] 
**street2** | **str, none_type** | The optional second line of the address. Optional when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership. | [optional] 
**city** | **str, none_type** | The city of the address. Required when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership. | [optional] 
**subdivision** | **str, none_type** | The ISO 3166-2 subdivision code of the address. Applicable only for countries that use subnational states, provinces, lands, oblasts or regions. Optional when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership. | [optional] 
**postal_code** | **str, none_type** | The postal, zip or post code of the address. Applicable only for countries that use postal, zip or post codes. Optional when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership. | [optional] 
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country code of the address. Required when type is kyc and method is attested, type is bank_account and method is attested, or type is bank_account and method is attested_ownership. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


