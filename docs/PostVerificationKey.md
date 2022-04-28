# PostVerificationKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | DER encoded public key in Base64 format. | 
**nonce** | **str** | Value signed in the **signature** field. | 
**signature** | **str** | Signature on **nonce** using PKCS1v15 padding and the SHA512 hashing algorithm in Base64 format. | 
**type** | **str** | The verification key&#39;s type. | defaults to "attestation"
**algorithm** | **str** | The verification key&#39;s algorithm. | defaults to "RS512"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


