# Counterparty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the counterparty. | [optional] 
**type** | **str** | The counterparty type; one of business or individual. | [optional] 
**bank_guid** | **str** | Auto-generated unique identifier for the counterparty&#39;s bank. | [optional] 
**customer_guid** | **str, none_type** | Auto-generated unique identifier for the counterparty&#39;s customer. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**state** | **str** | The counterparty state; one of storing, unverified, verified, or rejected. | [optional] 
**name** | [**CounterpartyName**](CounterpartyName.md) |  | [optional] 
**address** | [**CounterpartyAddress**](CounterpartyAddress.md) |  | [optional] 
**aliases** | [**[CounterpartyAliasesInner], none_type**](CounterpartyAliasesInner.md) | The counterparty&#39;s aliases. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**date_of_birth** | **date, none_type** | The counterparty&#39;s DOB. Only available for GET operations when &#39;include_pii&#39; is set. | [optional] 
**labels** | **[str], none_type** | The labels associated with the counterparty. | [optional] 
**compliance_decisions** | [**[ComplianceDecision]**](ComplianceDecision.md) | The compliance decisions associated with the counterparty. | [optional] 
**verification_checks** | [**[ComplianceDecision]**](ComplianceDecision.md) | Deprecated; use compliance_decisions instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


