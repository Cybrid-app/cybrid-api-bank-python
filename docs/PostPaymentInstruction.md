# PostPaymentInstruction

Request body for payment instruction creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_guid** | **str** | The invoice guid. | 
**expected_behaviour** | **str, none_type** | The optional expected behaviour to simulate. | [optional]  if omitted the server will use the default value of "invoice_paid_immediately"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


