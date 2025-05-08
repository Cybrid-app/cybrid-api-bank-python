# IdentityVerificationDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the document. | [optional] 
**type** | **str** | The document type; one of drivers_license, passport, passport_card, residence_card, visa, social_security_number, tax_identification_number, selfie, proof_of_address, formation_document, or employer_identification_number. | [optional] 
**validated** | **bool** | Whether the document has been validated. | [optional] 
**expiration_date** | **date, none_type** | The document expiration date. | [optional] 
**files** | [**[IdentityVerificationDocumentFile]**](IdentityVerificationDocumentFile.md) | The files associated with the document. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


