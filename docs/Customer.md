# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the customer. | [optional] 
**bank_guid** | **str** | Auto-generated unique identifier for the customer&#39;s bank. | [optional] 
**type** | **str** | The customer type; one of business or individual. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**state** | **str** | The customer state; one of storing, unverified, verified, rejected, or frozen. | [optional] 
**name** | [**CustomerName**](CustomerName.md) |  | [optional] 
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**aliases** | [**[CustomerAliasesInner], none_type**](CustomerAliasesInner.md) | The customer&#39;s aliases. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**website** | **str, none_type** | The customer&#39;s website. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**date_of_birth** | **date, none_type** | The customer&#39;s DOB. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**phone_number** | **str, none_type** | The customer&#39;s phone number. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**email_address** | **str, none_type** | The customer&#39;s email address. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**labels** | **[str], none_type** | The labels associated with the customer. | [optional] 
**compliance_decisions** | [**[ComplianceDecision]**](ComplianceDecision.md) | The compliance decisions associated with the customer. | [optional] 
**identification_numbers** | [**[IdentificationNumber], none_type**](IdentificationNumber.md) | The customer&#39;s identification numbers. Only available for GET operations when &#39;include_pii&#39; is set and bank has access. | [optional] 
**activity_limits** | [**[ActivityLimit]**](ActivityLimit.md) | The asset limits associated with the customer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


