# PostExternalBankAccountCounterpartyName

The counterparty's name on their checking account. Required when account_kind is raw_routing_details and counterparty_guid is not present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str, none_type** | The counterparty&#39;s first name; used for individuals. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**middle** | **str, none_type** | The counterparty&#39;s middle name; used for individuals. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**last** | **str, none_type** | The counterparty&#39;s last name; used for individuals. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**full** | **str, none_type** | The counterparty&#39;s full name; used for businesses. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


