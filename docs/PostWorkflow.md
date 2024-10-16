# PostWorkflow

Request body for workflow creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The workflow type. | defaults to "plaid"
**kind** | **str, none_type** | The Plaid workflow kind. Required when type is plaid. | [optional] 
**customer_guid** | **str, none_type** | The customer identifier associated with the workflow. Optional when type is plaid and kind is link_token_create. | [optional] 
**external_bank_account_guid** | **str, none_type** | The external bank account identifier associated with the workflow. Required when type is plaid and kind is link_token_update. | [optional] 
**language** | **str, none_type** | The language to initialize Plaid link. Required when type is plaid. | [optional] 
**link_customization_name** | **str, none_type** | The customization name for Plaid link. Currently only supports the value \&quot;default\&quot;. Required when type is plaid. | [optional] 
**redirect_uri** | **str, none_type** | The redirect URI for Plaid link. Optional when type is plaid. | [optional] 
**android_package_name** | **str, none_type** | The Android package name for Plaid link. Optional when type is plaid. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


