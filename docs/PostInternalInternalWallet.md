# PostInternalInternalWallet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of internal wallet. | 
**name** | **str** | The name of the account. | 
**asset** | **str** | The asset code. | 
**account_kind** | **str** | The type of account. | 
**environment** | **str** | The account environment. | 
**provider_id** | **str** | The id of the account at the third-party provider. | [optional] 
**wallet_service_guid** | **str** | The wallet service guid; required when specifying the provider_id. | [optional] 
**internal_wallet_group_guid** | **str** | The unique identifier of the wallet group. | [optional] 
**bank_guid** | **str, none_type** | The unique identifier for the bank associated with the trading deposits wallet. | [optional] 
**customer_guid** | **str, none_type** | The unique identifier for the customer associated with the trading deposits wallet. | [optional] 
**routing_details** | [**[PostInternalInternalWalletRoutingDetail], none_type**](PostInternalInternalWalletRoutingDetail.md) | The routing details for this wallet. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


