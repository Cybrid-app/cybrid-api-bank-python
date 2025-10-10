# InternalInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the payment instruction. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**type** | **str** | The type of invoice; one of lightning. | [optional] 
**organization_guid** | **str** |  | [optional] 
**bank_guid** | **str** |  | [optional] 
**customer_guid** | **str** |  | [optional] 
**provider_id** | **str, none_type** |  | [optional] 
**amount** | **int, none_type** |  | [optional] 
**amount_asset** | **str** |  | [optional] 
**bank_fee** | **int, none_type** |  | [optional] 
**bank_fee_asset** | **str, none_type** |  | [optional] 
**platform_fee** | **int, none_type** |  | [optional] 
**platform_fee_asset** | **str, none_type** |  | [optional] 
**credit_account_guid** | **str** |  | [optional] 
**credit_account_organization_guid** | **str** |  | [optional] 
**credit_account_bank_guid** | **str** |  | [optional] 
**credit_account_customer_guid** | **str, none_type** |  | [optional] 
**principal_account_guid** | **str** |  | [optional] 
**bank_fee_account_guid** | **str, none_type** |  | [optional] 
**bank_fee_account_organization_guid** | **str, none_type** |  | [optional] 
**bank_fee_account_bank_guid** | **str, none_type** |  | [optional] 
**bank_fee_account_customer_guid** | **str, none_type** |  | [optional] 
**platform_fee_account_guid** | **str, none_type** |  | [optional] 
**state** | **str** | The state of the invoice; one of storing, unpaid, cancelling, cancelled, settling, or paid. | [optional] 
**labels** | **[str], none_type** | The labels associated with the invoice. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


