# cybrid_api_bank.QuotesBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote**](QuotesBankApi.md#create_quote) | **POST** /api/quotes | Create Quote
[**get_quote**](QuotesBankApi.md#get_quote) | **GET** /api/quotes/{quote_guid} | Get Quote
[**list_quotes**](QuotesBankApi.md#list_quotes) | **GET** /api/quotes | Get quotes list


# **create_quote**
> Quote create_quote(post_quote)

Create Quote

Creates a quote.  Required scope: **quotes:execute**

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
# Defining the host is optional and defaults to https://bank.demo.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.demo.cybrid.app"
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
    host = "https://bank.demo.cybrid.app"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quotes_bank_api.QuotesBankApi(api_client)
    post_quote = PostQuote(
        customer_guid="customer_guid_example",
        symbol="symbol_example",
        side="buy",
        receive_amount=1,
        deliver_amount=1,
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
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |
**500** | Internal server error |  -  |

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
# Defining the host is optional and defaults to https://bank.demo.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.demo.cybrid.app"
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
    host = "https://bank.demo.cybrid.app"
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
**400** | Invalid requests - malformed authentication header |  -  |
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
from cybrid_api_bank.model.list_request_page import ListRequestPage
from cybrid_api_bank.model.list_request_per_page import ListRequestPerPage
from pprint import pprint
# Defining the host is optional and defaults to https://bank.demo.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.demo.cybrid.app"
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
    host = "https://bank.demo.cybrid.app"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quotes_bank_api.QuotesBankApi(api_client)
    page = ListRequestPage(0) # ListRequestPage |  (optional)
    per_page = ListRequestPerPage(10) # ListRequestPerPage |  (optional)
    guid = "guid_example" # str | Comma separated quote_guids to list quotes for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list quotes for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list quotes for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get quotes list
        api_response = api_instance.list_quotes(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling QuotesBankApi->list_quotes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **ListRequestPage**|  | [optional]
 **per_page** | **ListRequestPerPage**|  | [optional]
 **guid** | **str**| Comma separated quote_guids to list quotes for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list quotes for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list quotes for. | [optional]

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
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

