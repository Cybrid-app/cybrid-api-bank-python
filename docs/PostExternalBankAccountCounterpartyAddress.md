# PostExternalBankAccountCounterpartyAddress

The counterparty's address on their checking account. Required when account_kind is raw_routing_details and counterparty_guid is not present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str, none_type** | The first line of the address. Required when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**street2** | **str, none_type** | The optional second line of the address. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**city** | **str, none_type** | The city of the address. Required when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**subdivision** | **str, none_type** | The ISO 3166-2 subdivision code of the address. Applicable only for countries that use subnational states, provinces, lands, oblasts or regions. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**postal_code** | **str, none_type** | The postal, zip or post code of the address. Applicable only for countries that use postal, zip or post codes. Optional when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country code of the address. Required when account_kind is raw_routing_details and counterparty_guid is not present. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


