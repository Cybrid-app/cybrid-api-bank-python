# cybrid_api_bank.QuotesBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote**](QuotesBankApi.md#create_quote) | **POST** /api/quotes | Create Quote
[**get_quote**](QuotesBankApi.md#get_quote) | **GET** /api/quotes/{quote_guid} | Get Quote
[**list_quotes**](QuotesBankApi.md#list_quotes) | **GET** /api/quotes | Get quotes list


# **create_quote**
> Quote create_quote(post_quote)

Create Quote

Creates a quote.  ## Quote creation  Quotes can be created for a Bank or a Customer.  To create quotes for your Bank, omit the `customer_guid` parameter in the request body. To create quotes for your Customers, include the `customer_guid` parameter in the request body.  ## Failure codes  | Code | Description | |------|-------------| | invalid_amount | The amount on the invoice is unprocessable | | insufficient_balance | There are insufficient funds to process the quote | | invalid_invoice | The invoice cannot be processed |    Required scope: **quotes:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import quotes_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.quote import Quote
from cybrid_api_bank.model.post_quote import PostQuote
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
    api_instance = quotes_bank_api.QuotesBankApi(api_client)
    post_quote = PostQuote(
        product_type="trading",
        bank_guid="bank_guid_example",
        customer_guid="customer_guid_example",
        receive_amount=1,
        deliver_amount=1,
        asset="asset_example",
        network_address="network_address_example",
        fees=[
            PostFee(
                type="spread",
                spread_fee=1,
                fixed_fee=1,
            ),
        ],
        side="deposit",
        symbol="symbol_example",
        destination_accounts=[
            PostQuoteEntry(
                type="external_wallet",
                guid="guid_example",
                receive_amount=1,
                deliver_amount=1,
            ),
        ],
        reference_trade_guid="reference_trade_guid_example",
        source_account_guid="source_account_guid_example",
        destination_account_guid="destination_account_guid_example",
    ) # PostQuote | 

    # example passing only required values which don't have defaults set
    try:
        # Create Quote
        api_response = api_instance.create_quote(post_quote)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling QuotesBankApi->create_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_quote** | [**PostQuote**](PostQuote.md)|  |

### Return type

[**Quote**](Quote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | quote created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote**
> Quote get_quote(quote_guid)

Get Quote

Retrieves a quote.  Required scope: **quotes:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import quotes_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.quote import Quote
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
    api_instance = quotes_bank_api.QuotesBankApi(api_client)
    quote_guid = "quote_guid_example" # str | Identifier for the quote.

    # example passing only required values which don't have defaults set
    try:
        # Get Quote
        api_response = api_instance.get_quote(quote_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling QuotesBankApi->get_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_guid** | **str**| Identifier for the quote. |

### Return type

[**Quote**](Quote.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quote found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | quote not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotes**
> QuoteList list_quotes()

Get quotes list

Retrieves a listing of quotes for all customers of a bank.  Required scope: **quotes:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import quotes_bank_api
from cybrid_api_bank.model.quote_list import QuoteList
from cybrid_api_bank.model.error_response import ErrorResponse
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
    api_instance = quotes_bank_api.QuotesBankApi(api_client)
    page = ListRequestPage(0) # int |  (optional)
    per_page = ListRequestPerPage(1) # int |  (optional)
    guid = "guid_example" # str | Comma separated quote_guids to list quotes for. (optional)
    product_type = "product_type_example" # str | Comma separated product_types to list accounts for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list quotes for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list quotes for. (optional)
    side = "side_example" # str | Comma separated sides to list quotes for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get quotes list
        api_response = api_instance.list_quotes(page=page, per_page=per_page, guid=guid, product_type=product_type, bank_guid=bank_guid, customer_guid=customer_guid, side=side)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling QuotesBankApi->list_quotes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional]
 **per_page** | **int**|  | [optional]
 **guid** | **str**| Comma separated quote_guids to list quotes for. | [optional]
 **product_type** | **str**| Comma separated product_types to list accounts for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list quotes for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list quotes for. | [optional]
 **side** | **str**| Comma separated sides to list quotes for. | [optional]

### Return type

[**QuoteList**](QuoteList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of quotes |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

