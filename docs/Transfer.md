# Transfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the trade. | [optional] 
**transfer_type** | **str** | The type of transfer. | [optional] 
**bank_guid** | **str, none_type** | The associated bank&#39;s identifier. | [optional] 
**customer_guid** | **str, none_type** | The associated customer&#39;s identifier. | [optional] 
**quote_guid** | **str** | The associated quote&#39;s identifier. | [optional] 
**external_bank_account_guid** | **str, none_type** | The associated external bank account&#39;s identifier. | [optional] 
**asset** | **str** | The asset the transfer is related to, e.g., USD. | [optional] 
**side** | **str** | The direction of the quote: &#39;deposit&#39; or &#39;withdrawal&#39;. | [optional] 
**state** | **str** | The trade&#39;s state | [optional] 
**amount** | **int, none_type** | The actual amount in base units of the asset. | [optional] 
**estimated_amount** | **int** | The estimated amount in base units of the asset. | [optional] 
**fee** | **int** | The fee associated with the trade. | [optional] 
**estimated_network_fee** | **int, none_type** | The estimated network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers. | [optional] 
**network_fee** | **int, none_type** | The actual network fee in base units of network_fee_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_asset** | **str, none_type** | The asset code of the network fee. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount** | **int, none_type** | The equivalent fiat network fee in base units of network_fee_liability_amount_asset. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**network_fee_liability_amount_asset** | **str, none_type** | The fiat asset the network_fee_liability_amount is denominated in. Only present on &#x60;crypto&#x60; transfers that have successfully completed. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the bank was created at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


