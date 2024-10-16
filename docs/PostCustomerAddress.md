# PostCustomerAddress

The customer's address. Optional when type is individual.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str, none_type** | The first line of the address. Required when type is individual. | [optional] 
**street2** | **str, none_type** | The optional second line of the address. Optional when type is individual. | [optional] 
**city** | **str, none_type** | The city of the address. Required when type is individual. | [optional] 
**subdivision** | **str, none_type** | The ISO 3166-2 subdivision code of the address; not used by all countries. Optional when type is individual. | [optional] 
**postal_code** | **str, none_type** | The postal/post/zip code of the address; not used by all countries. Optional when type is individual. | [optional] 
**country_code** | **str, none_type** | The ISO 3166 country 2-Alpha country code of the address. Required when type is individual. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


