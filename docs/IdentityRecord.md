# IdentityRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity record. | [optional] 
**customer_guid** | **str** | The customer&#39;s identifier. | [optional] 
**type** | **str** | The identity record&#39;s type. | [optional]  if omitted the server will use the default value of "attestation"
**attestation_details** | [**AttestationDetails**](AttestationDetails.md) |  | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**expired_at** | **datetime, none_type** | ISO8601 datetime the record is expired at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


