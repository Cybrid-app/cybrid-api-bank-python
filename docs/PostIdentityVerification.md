# PostIdentityVerification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of identity verification. | defaults to "kyc"
**method** | **str** | The identity verification method. | defaults to "id_and_selfie"
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country the customer is being verified in. If not present, will default to the Bank&#39;s configured country code. | [optional] 
**customer_guid** | **str** | The customer&#39;s identifier. | [optional] 
**expected_behaviours** | **[str]** | The optional expected behaviour to simulate. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


