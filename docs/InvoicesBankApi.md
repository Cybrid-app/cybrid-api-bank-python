# cybrid_api_bank.InvoicesBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_invoice**](InvoicesBankApi.md#cancel_invoice) | **DELETE** /api/invoices/{invoice_guid} | Cancel Invoice
[**create_invoice**](InvoicesBankApi.md#create_invoice) | **POST** /api/invoices | Create Invoice
[**get_invoice**](InvoicesBankApi.md#get_invoice) | **GET** /api/invoices/{invoice_guid} | Get Invoice
[**list_invoices**](InvoicesBankApi.md#list_invoices) | **GET** /api/invoices | List Invoices


# **cancel_invoice**
> Invoice cancel_invoice(invoice_guid)

Cancel Invoice

Cancels an invoice.  Required scope: **invoices:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import invoices_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.invoice import Invoice
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
    api_instance = invoices_bank_api.InvoicesBankApi(api_client)
    invoice_guid = "invoice_guid_example" # str | Identifier for the invoice.

    # example passing only required values which don't have defaults set
    try:
        # Cancel Invoice
        api_response = api_instance.cancel_invoice(invoice_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling InvoicesBankApi->cancel_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_guid** | **str**| Identifier for the invoice. |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice cancelled |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | Invoice not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice**
> Invoice create_invoice(post_invoice)

Create Invoice

Creates a invoice.  ## State  | State | Description | |-------|-------------| | storing    | The Platform is storing the invoice details in our private store | | unpaid     | The invoice is unpaid. Payment instructions can be generated for an invoice in this state | | cancelling | The invocie is in the process of being cancelled | | cancelled  | The invoice has been cancelled |  | settling   | The invoice has been paid and the funds associated with this invoice are in the process of being settled | | paid       | The invoice has been paid and the funds associated with this invoice have been settled |     Required scope: **invoices:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import invoices_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.invoice import Invoice
from cybrid_api_bank.model.post_invoice import PostInvoice
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
    api_instance = invoices_bank_api.InvoicesBankApi(api_client)
    post_invoice = PostInvoice(
        asset="asset_example",
        customer_guid="customer_guid_example",
        receive_amount=1,
        deliver_amount=1,
        account_guid="account_guid_example",
        labels=[
            "labels_example",
        ],
    ) # PostInvoice | 

    # example passing only required values which don't have defaults set
    try:
        # Create Invoice
        api_response = api_instance.create_invoice(post_invoice)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling InvoicesBankApi->create_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_invoice** | [**PostInvoice**](PostInvoice.md)|  |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Invoice created |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> Invoice get_invoice(invoice_guid)

Get Invoice

Retrieves a invoice.  Required scope: **invoices:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import invoices_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.invoice import Invoice
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
    api_instance = invoices_bank_api.InvoicesBankApi(api_client)
    invoice_guid = "invoice_guid_example" # str | Identifier for the payment instruction.

    # example passing only required values which don't have defaults set
    try:
        # Get Invoice
        api_response = api_instance.get_invoice(invoice_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling InvoicesBankApi->get_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_guid** | **str**| Identifier for the payment instruction. |

### Return type

[**Invoice**](Invoice.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | invoice not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> InvoiceList list_invoices()

List Invoices

Retrieves a list of invoices.  Required scope: **invoices:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import invoices_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.invoice_list import InvoiceList
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
    api_instance = invoices_bank_api.InvoicesBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated guids to list invoices for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list invoices for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list invoices for. (optional)
    account_guid = "account_guid_example" # str | Comma separated account_guids to list invoices for. (optional)
    state = "state_example" # str | Comma separated states to list invoices for. (optional)
    asset = "asset_example" # str | Comma separated assets to list invoices for. (optional)
    environment = "sandbox" # str |  (optional)
    label = "label_example" # str | Comma separated labels to list invoices for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Invoices
        api_response = api_instance.list_invoices(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, account_guid=account_guid, state=state, asset=asset, environment=environment, label=label)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling InvoicesBankApi->list_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated guids to list invoices for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list invoices for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list invoices for. | [optional]
 **account_guid** | **str**| Comma separated account_guids to list invoices for. | [optional]
 **state** | **str**| Comma separated states to list invoices for. | [optional]
 **asset** | **str**| Comma separated assets to list invoices for. | [optional]
 **environment** | **str**|  | [optional]
 **label** | **str**| Comma separated labels to list invoices for. | [optional]

### Return type

[**InvoiceList**](InvoiceList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of invoices |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

