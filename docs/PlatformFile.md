# PlatformFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The unique identifier for the file. | [optional] 
**file_type** | **str** | The file type; one of drivers_license_front, drivers_license_back, passport, identification_card, residence_card, selfie, selfie_left, selfie_right, utility_bill, bank_statement, property_tax, tax_document, ein_letter, or incorporation_certificate. | [optional] 
**content_type** | **str** | The media type; one of image/jpeg, image/png, or application/pdf. | [optional] 
**completed_at** | **datetime** | The ISO8601 datetime the file was completed at. | [optional] 
**failed_at** | **datetime** | The ISO8601 datetime the file failed at. | [optional] 
**state** | **str** | The state of the file. One of storing, completed, or failed. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed files. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


