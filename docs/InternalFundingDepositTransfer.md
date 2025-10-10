# InternalFundingDepositTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**transfer_type** | **str** |  | [optional] 
**organization_guid** | **str** |  | [optional] 
**bank_guid** | **str** |  | [optional] 
**customer_guid** | **str, none_type** |  | [optional] 
**amount** | **int, none_type** |  | [optional] 
**amount_asset** | **str** |  | [optional] 
**payment_rail** | **str** |  | [optional] 
**estimated_amount** | **int** |  | [optional] 
**bank_fee** | **int** |  | [optional] 
**bank_fee_asset** | **str** |  | [optional] 
**platform_fee** | **int** |  | [optional] 
**platform_fee_asset** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**failure_code** | **str, none_type** | The failure code for failed transfers. | [optional] 
**fiat_account_guid** | **str** |  | [optional] 
**fiat_account_organization_guid** | **str** |  | [optional] 
**fiat_account_bank_guid** | **str** |  | [optional] 
**fiat_account_customer_guid** | **str, none_type** |  | [optional] 
**principal_account_guid** | **str** |  | [optional] 
**bank_fee_account_guid** | **str, none_type** |  | [optional] 
**bank_fee_account_organization_guid** | **str, none_type** |  | [optional] 
**bank_fee_account_bank_guid** | **str, none_type** |  | [optional] 
**bank_fee_account_customer_guid** | **str, none_type** |  | [optional] 
**platform_fee_account_guid** | **str, none_type** |  | [optional] 
**transfer_details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The raw details on the transfer from the bank. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


