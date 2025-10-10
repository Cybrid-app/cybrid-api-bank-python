# InternalCountryCodeConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the configuration. | [optional] 
**type** | **str** | The type of country code configuration: bank or platform. | [optional] 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**jurisdiction_enabled** | **bool** | Flag indicating if the country code is configured for jurisdiction use. | [optional] 
**business_customers_enabled** | **bool** | Flag indicating if the country code is configured for individual customers. | [optional] 
**individual_customers_enabled** | **bool** | Flag indicating if the country code is configured for individual customers. | [optional] 
**business_counterparties_enabled** | **bool** | Flag indicating if the country code is configured for business counterparties. | [optional] 
**individual_counterparties_enabled** | **bool** | Flag indicating if the country code is configured for individual counterparties. | [optional] 
**code** | **str** | The ISO 3166 country 2-Alpha country code. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


