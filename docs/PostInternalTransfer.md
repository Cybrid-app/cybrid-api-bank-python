# PostInternalTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_type** | **str** | The type of internal transfer. | 
**environment** | **str** | The environment to transfer funds in. | 
**quote_guid** | **str, none_type** | The associated quote&#39;s identifier. | [optional] 
**transfer_guid** | **str, none_type** | The associated tranfer&#39;s identifier. Used for returns. | [optional] 
**source_account_guid** | **str, none_type** | The source account guid. | [optional] 
**destination_account_guid** | **str, none_type** | The destination account guid. | [optional] 
**supports_reconciliation** | **bool, none_type** | Flag indicating if the transfer supports reconciliation. | [optional] 
**requires_manual_confirmation** | **bool, none_type** | Override indicating if the transfer requires manual confirmation. | [optional] 
**external_id** | **str, none_type** | The external identifier for the transfer. | [optional] 
**labels** | **[str], none_type** | The labels associated with the transfer. | [optional] 
**associations** | [**[InternalTransferAssociation]**](InternalTransferAssociation.md) | Transfers associated with this record. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


