# ExternalBankAccountPiiInnerRoutingDetailsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number_type** | **str** | The type of routing number; one of CPA, ABA, or IFSC. | 
**routing_number** | **str** | The routing number. | 
**payment_rail** | **str, none_type** | The payment rail this routing entry is configured for; one of EFT, ACH, RTP, WIRE, SPEI, PIX, COELSA, PSE, ETRANSFER, IFSC, SBP, BEFTN, NGBANK, LBTR, SEPA, EASY_PAISA, FINJA, JAZZ_CASH, NAYA_PAY, SADA_PAY, KEBANK, MPESA, or UNSPECIFIED. Null for accounts that did not specify a rail. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


