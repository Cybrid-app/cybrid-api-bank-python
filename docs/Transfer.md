# Transfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Auto-generated unique identifier for the trade. | [optional] 
**transfer_type** | **str** | The type of transfer. | [optional] 
**customer_guid** | **str** | The associated customer&#39;s identifier. | [optional] 
**quote_guid** | **str** | The associated quote&#39;s identifier. | [optional] 
**asset** | **str** | The asset the transfer is related to, e.g., USD. | [optional] 
**side** | **str** | The direction of the quote: either &#39;buy&#39; or &#39;sell&#39;. | [optional] 
**state** | **str** | The trade&#39;s state | [optional] 
**amount** | **int** | The amount being transferred. | [optional] 
**fee** | **int** | The fee associated with the trade. | [optional] 
**created_at** | **datetime** | ISO8601 datetime the bank was created at. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


