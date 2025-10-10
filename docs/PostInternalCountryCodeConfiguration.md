# PostInternalCountryCodeConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of country code configuration: bank or platform. | 
**jurisdiction_enabled** | **bool** | Flag indicating if the country code is configured for jurisdiction use. | 
**business_customers_enabled** | **bool** | Flag indicating if the country code is configured for business customers. | 
**individual_customers_enabled** | **bool** | Flag indicating if the country code is configured for individual customers. | 
**business_counterparties_enabled** | **bool** | Flag indicating if the country code is configured for business counterparties. | 
**individual_counterparties_enabled** | **bool** | Flag indicating if the country code is configured for individual counterparties. | 
**code** | **str** | The ISO 3166 2-Alpha country code. | 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


