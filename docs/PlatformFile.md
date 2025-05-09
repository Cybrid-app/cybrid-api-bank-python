# PlatformFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The unique identifier for the file. | [optional] 
**type** | **str** | The file type; one of drivers_license_front, drivers_license_back, passport, passport_card, visa, identification_card, residence_card, selfie, selfie_video, selfie_left, selfie_right, utility_bill, proof_of_address, bank_statement, property_tax, tax_document, ein_letter, incorporation_certificate, persona_inquiry_report, or persona_inquiry_export. | [optional] 
**content_type** | **str** | The media type; one of image/jpeg, image/png, application/pdf, application/json, or video/mp4. | [optional] 
**filename** | **str** | The name of the file. | [optional] 
**completed_at** | **datetime** | The ISO8601 datetime the file was completed at. | [optional] 
**failed_at** | **datetime** | The ISO8601 datetime the file failed at. | [optional] 
**state** | **str** | The state of the file. One of storing, completed, or failed. | [optional] 
**failure_code** | **str, none_type** | The failure code for failed files. | [optional] 
**upload_url** | **str, none_type** | The URL to upload the file to. | [optional] 
**upload_expires_at** | **datetime, none_type** | The ISO8601 datetime the upload URL expires at. | [optional] 
**download_url** | **str, none_type** | The URL to download the file from. | [optional] 
**download_expires_at** | **datetime, none_type** | The ISO8601 datetime the download URL expires at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


