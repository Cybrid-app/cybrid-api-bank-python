# PostIdentityVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The identity verification method. | 
**type** | **str** | The type of identity verification. | defaults to "kyc"
**customer_guid** | **str, none_type** | The customer&#39;s identifier. | [optional] 
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country the customer is being verified in; required when method is set to &#39;id_and_selfie&#39;. If not present, will default to the Bank&#39;s configured country code. | [optional] 
**name** | [**PostIdentityVerificationName**](PostIdentityVerificationName.md) |  | [optional] 
**address** | [**PostIdentityVerificationAddress**](PostIdentityVerificationAddress.md) |  | [optional] 
**date_of_birth** | **date, none_type** | The customer&#39;s date of birth; required when method is set to &#39;attested&#39;. | [optional] 
**identification_numbers** | [**[PostIdentificationNumber], none_type**](PostIdentificationNumber.md) | The customer&#39;s identification numbers; required when method is set to &#39;attested&#39;. | [optional] 
**expected_behaviours** | **[str]** | The optional expected behaviour to simulate. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


