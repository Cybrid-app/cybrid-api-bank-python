# Customer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the customer. | [optional] 
**bank_guid** | **str** | Auto-generated unique identifier for the customer&#39;s bank. | [optional] 
**type** | **str** | The customer&#39;s type. | [optional]  if omitted the server will use the default value of "individual"
**created_at** | **datetime** | ISO8601 datetime the customer was created at. | [optional] 
**state** | **str** | The customer&#39;s state. | [optional] 
**name** | [**CustomerName**](CustomerName.md) |  | [optional] 
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**date_of_birth** | **date, none_type** | The customer&#39;s date of birth. | [optional] 
**phone_number** | **str, none_type** | The customer&#39;s phone number. | [optional] 
**email_address** | **str, none_type** | The customer&#39;s phone number. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


