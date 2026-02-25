# AccountAssociation



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the transfer account. | 
**type** | **str** | The type of transfer account; one of trading, fiat, external_bank_account, or external_wallet. | 
**asset** | **str** | The account asset, e.g., USD. | 
**organization_guid** | **str, none_type** | The account&#39;s organization identifier. | [optional] 
**bank_guid** | **str, none_type** | The account&#39;s bank identifier. | [optional] 
**customer_guid** | **str, none_type** | The account&#39;s customer identifier. | [optional] 
**counterparty_guid** | **str, none_type** | The account&#39;s counterparty identifier. | [optional] 
**requested_amount** | **int, none_type** | The requested amount in base units intended to transfer from or to the account. | [optional] 
**quoted_amount** | **int, none_type** | The quoted amount in base units to transfer from or to the account. | [optional] 
**executed_amount** | **int, none_type** | The executed amount in base units transferred from or to the account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


