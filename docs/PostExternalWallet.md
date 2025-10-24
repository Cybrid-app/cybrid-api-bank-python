# PostExternalWallet

Request body for external wallet creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the external wallet. | 
**asset** | **str** | The asset code. | 
**address** | **str** | The blockchain wallet address for the wallet. | 
**customer_guid** | **str, none_type** | The customer identifier. | [optional] 
**counterparty_guid** | **str, none_type** | The counterparty identifier. | [optional] 
**tag** | **str, none_type** | The blockchain tag to use when transferring crypto to the wallet. | [optional] 
**expected_behaviours** | **[str], none_type** | The optional expected behaviour to simulate. Only applicable wallets under sandbox banks. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


