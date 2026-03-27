# PostBankAccountDetails

Bank account details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | The account number or unique identifier for the account. | 
**payment_rail** | **str** | The payment rail used for the account. | 
**bank_code** | **str, none_type** | The bank code. | [optional] 
**account_identifier_type** | **str, none_type** | The type of account identifier. Must be PHONE_NUMBER for mobile wallet rails. Required when payment_rail is EASY_PAISA, payment_rail is FINJA, payment_rail is JAZZ_CASH, payment_rail is NAYA_PAY, or payment_rail is SADA_PAY. | [optional] 
**bank_code_type** | **str, none_type** | The type of bank code. Required when payment_rail is EFT, payment_rail is ACH, payment_rail is RTP, payment_rail is WIRE, payment_rail is SPEI, payment_rail is PIX, payment_rail is COELSA, payment_rail is PSE, payment_rail is ETRANSFER, payment_rail is IFSC, payment_rail is SBP, payment_rail is BEFTN, payment_rail is NGBANK, payment_rail is LBTR, or payment_rail is UNSPECIFIED. | [optional] 
**account_type** | **str, none_type** | The type of account. Required when payment_rail is PSE or payment_rail is LBTR. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


