# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | The unique identifier for the platform account. | 
**amount** | **int** | The transaction amount in base units. | 
**asset** | **str** | The asset code, e.g., USD. | 
**bank_guid** | **str** | The unique identifier for the bank. | 
**direction** | **str** | The direction of the transaction; one of credit or debit. | 
**posted** | **bool** | Whether the transaction has posted. | 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | 
**customer_guid** | **str, none_type** | The unique identifier for the customer. Absent for bank-owned accounts. | [optional] 
**category** | **str, none_type** | The type of ledger line item, e.g., principal or fee. | [optional] 
**resource** | [**TransactionResource**](TransactionResource.md) |  | [optional] 
**balance** | [**Balance**](Balance.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


