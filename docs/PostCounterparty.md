# PostCounterparty

Request body for counterparty creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The counterparty&#39;s type. | 
**address** | [**PostCounterpartyAddress**](PostCounterpartyAddress.md) |  | 
**customer_guid** | **str, none_type** | The owning customer&#39;s identifier. | [optional] 
**name** | [**PostCounterpartyName**](PostCounterpartyName.md) |  | [optional] 
**aliases** | [**[PostCounterpartyAliasesInner], none_type**](PostCounterpartyAliasesInner.md) | The aliases of the counterparty. Optional when type is business. | [optional] 
**date_of_birth** | **date, none_type** | The counterparty&#39;s date of birth. Optional when type is individual. | [optional] 
**email_address** | **str, none_type** | The counterparty&#39;s email address. | [optional] 
**identification_numbers** | [**[PostIdentificationNumber], none_type**](PostIdentificationNumber.md) | The counterparty&#39;s identification numbers. | [optional] 
**labels** | **[str], none_type** | The labels associated with the counterparty. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


