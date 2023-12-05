# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the customer. | [optional] 
**bank_guid** | **str** | Auto-generated unique identifier for the customer&#39;s bank. | [optional] 
**type** | **str** | The customer&#39;s type. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**state** | **str** | The customer&#39;s state. | [optional] 
**name** | [**CustomerName**](CustomerName.md) |  | [optional] 
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**date_of_birth** | **date, none_type** | The customer&#39;s DOB. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**phone_number** | **str, none_type** | The customer&#39;s phone number. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**email_address** | **str, none_type** | The customer&#39;s email address. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**labels** | **[str], none_type** | The labels associated with the customer. | [optional] 
**verification_checks** | [**[VerificationCheck]**](VerificationCheck.md) | The verification checks associated with the customer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


