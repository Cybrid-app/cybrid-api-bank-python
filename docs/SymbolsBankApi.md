# cybrid_api_bank.SymbolsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_symbols**](SymbolsBankApi.md#list_symbols) | **GET** /api/symbols | Get Symbols list


# **list_symbols**
> Symbols list_symbols()

Get Symbols list

Retrieves a listing of symbols.

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import symbols_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.symbols import Symbols
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
    api_instance = symbols_bank_api.SymbolsBankApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Symbols list
        api_response = api_instance.list_symbols()
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling SymbolsBankApi->list_symbols: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Symbols**](Symbols.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of symbols |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

