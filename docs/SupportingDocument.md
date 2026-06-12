# SupportingDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the document. | 
**type** | **str** | The kind of supporting document; one of invoice, purchase_order, delivery_slip, contract, bill_of_lading, or others. | 
**files** | [**[SupportingDocumentFile]**](SupportingDocumentFile.md) | The files backing this document. | 
**document_reference_number** | **str, none_type** | A reference number identifying this document (e.g. an invoice number). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


