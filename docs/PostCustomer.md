# PostCustomer

Request body for customer creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of customer. | 
**name** | [**PostCustomerName**](PostCustomerName.md) |  | [optional] 
**address** | [**PostCustomerAddress**](PostCustomerAddress.md) |  | [optional] 
**date_of_birth** | **date, none_type** | The customer&#39;s date of birth. Optional when type is individual. | [optional] 
**phone_number** | **str, none_type** | The customer&#39;s phone number. Optional when type is individual. | [optional] 
**email_address** | **str, none_type** | The customer&#39;s email address. Optional when type is individual. | [optional] 
**identification_numbers** | [**[PostIdentificationNumber], none_type**](PostIdentificationNumber.md) | The customer&#39;s identification numbers. Optional when type is individual. | [optional] 
**labels** | **[str], none_type** | The labels associated with the customer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


