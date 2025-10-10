# InternalPayoutSymbolConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the configuration. | [optional] 
**type** | **str** | The type of symbol configuration: bank or platform. | [optional] 
**environment** | **str, none_type** | The environment the configuration is associated with. | [optional] 
**bank_guid** | **str, none_type** | The bank identifier that the configuration is associated with. | [optional] 
**enabled** | **bool** | Flag indicating if the symbol is enabled for payout on the platform. | [optional] 
**symbol** | **str** | The symbol code of the configuration. | [optional] 
**country_code** | **str** | The ISO 3166 2-Alpha country code. | [optional] 
**participants_type** | **str** | The type of participants the symbol is enabled for. | [optional] 
**route** | **str** | The route the symbol is enabled for. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


