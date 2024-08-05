# DepositBankAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the identity verification. | [optional] 
**type** | **str** | The account type; one of main or sub_account. | [optional] 
**bank_guid** | **str** | The address&#39; bank identifier. | [optional] 
**customer_guid** | **str, none_type** | The address&#39; customer identifier. | [optional] 
**account_guid** | **str** | The address&#39; account identifier. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the record was created at. | [optional] 
**updated_at** | **datetime** | ISO8601 datetime the record was last updated at. | [optional] 
**asset** | **str** | The asset the transfer is related to, e.g., USD. | [optional] 
**state** | **str** | The state of the address; one of storing or created. | [optional] 
**unique_memo_id** | **str** | The unique memo identifier for the address. This is used to identify the recipient when sending funds to the account. This value MUST be included in all wire transfers to this account. | [optional] 
**counterparty_name** | **str, none_type** | The name of the account holder. | [optional] 
**counterparty_address** | [**DepositBankAccountCounterpartyAddress**](DepositBankAccountCounterpartyAddress.md) |  | [optional] 
**account_details** | [**[DepositBankAccountAccountDetailsInner], none_type**](DepositBankAccountAccountDetailsInner.md) | The account details for the bank account. | [optional] 
**routing_details** | [**[DepositBankAccountRoutingDetailsInner], none_type**](DepositBankAccountRoutingDetailsInner.md) | The account details for the bank account. | [optional] 
**labels** | **[str], none_type** | The labels associated with the address. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


