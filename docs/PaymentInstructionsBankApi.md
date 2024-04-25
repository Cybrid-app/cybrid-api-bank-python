# cybrid_api_bank.PaymentInstructionsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_instruction**](PaymentInstructionsBankApi.md#create_payment_instruction) | **POST** /api/payment_instructions | Create Payment Instruction
[**get_payment_instruction**](PaymentInstructionsBankApi.md#get_payment_instruction) | **GET** /api/payment_instructions/{payment_instruction_guid} | Get Payment Instruction
[**list_payment_instructions**](PaymentInstructionsBankApi.md#list_payment_instructions) | **GET** /api/payment_instructions | List Payment Instructions


# **create_payment_instruction**
> PaymentInstruction create_payment_instruction(post_payment_instruction)

Create Payment Instruction

Creates a payment instruction.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the payment instruction details in our private store | | created | The Platform has created the payment instruction | | expired | The PaymentInstruction is no longer valid |    Required scope: **invoices:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import payment_instructions_bank_api
from cybrid_api_bank.model.post_payment_instruction import PostPaymentInstruction
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.payment_instruction import PaymentInstruction
from pprint import pprint
# Defining the host is optional and defaults to https://bank.sandbox.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.sandbox.cybrid.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = cybrid_api_bank.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.sandbox.cybrid.app"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_instructions_bank_api.PaymentInstructionsBankApi(api_client)
    post_payment_instruction = PostPaymentInstruction(
        invoice_guid="invoice_guid_example",
        expected_behaviour="invoice_paid_immediately",
    ) # PostPaymentInstruction | 

    # example passing only required values which don't have defaults set
    try:
        # Create Payment Instruction
        api_response = api_instance.create_payment_instruction(post_payment_instruction)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PaymentInstructionsBankApi->create_payment_instruction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_payment_instruction** | [**PostPaymentInstruction**](PostPaymentInstruction.md)|  |

### Return type

[**PaymentInstruction**](PaymentInstruction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Payment Instruction created |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_instruction**
> PaymentInstruction get_payment_instruction(payment_instruction_guid)

Get Payment Instruction

Retrieves a payment_instruction.  Required scope: **invoices:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import payment_instructions_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.payment_instruction import PaymentInstruction
from pprint import pprint
# Defining the host is optional and defaults to https://bank.sandbox.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.sandbox.cybrid.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = cybrid_api_bank.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.sandbox.cybrid.app"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_instructions_bank_api.PaymentInstructionsBankApi(api_client)
    payment_instruction_guid = "payment_instruction_guid_example" # str | Identifier for the payment instruction.

    # example passing only required values which don't have defaults set
    try:
        # Get Payment Instruction
        api_response = api_instance.get_payment_instruction(payment_instruction_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PaymentInstructionsBankApi->get_payment_instruction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_instruction_guid** | **str**| Identifier for the payment instruction. |

### Return type

[**PaymentInstruction**](PaymentInstruction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | payment_instruction found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | payment_instruction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_instructions**
> PaymentInstructionList list_payment_instructions()

List Payment Instructions

Retrieves a list of payment instructions.  Required scope: **invoices:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import payment_instructions_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.payment_instruction_list import PaymentInstructionList
from pprint import pprint
# Defining the host is optional and defaults to https://bank.sandbox.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.sandbox.cybrid.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = cybrid_api_bank.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: oauth2
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.sandbox.cybrid.app"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payment_instructions_bank_api.PaymentInstructionsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated guids to list payment instructions for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list payment instructions for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list payment instructions for. (optional)
    invoice_guid = "invoice_guid_example" # str | Comma separated invoice_guids to list payment instructions for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payment Instructions
        api_response = api_instance.list_payment_instructions(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, invoice_guid=invoice_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PaymentInstructionsBankApi->list_payment_instructions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated guids to list payment instructions for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list payment instructions for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list payment instructions for. | [optional]
 **invoice_guid** | **str**| Comma separated invoice_guids to list payment instructions for. | [optional]

### Return type

[**PaymentInstructionList**](PaymentInstructionList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of payment instructions |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

