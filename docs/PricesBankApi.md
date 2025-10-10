# cybrid_api_bank.PricesBankApi

All URIs are relative to *http://api-platform-bank.local.cybrid.com:3002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_prices**](PricesBankApi.md#list_prices) | **GET** /api/prices | Get Price


# **list_prices**
> SymbolPriceResponse list_prices()

Get Price

Retrieves a listing of symbol prices.  ## Symbols  Symbol are pairs and are in the format asset-counter_asset, e.g., 'BTC-USD' for the Bitcoin/ USD pair. See the Symbols API for a complete list of cryptocurrencies supported.    Required scope: **prices:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import prices_bank_api
from cybrid_api_bank.model.symbol_price_response import SymbolPriceResponse
from cybrid_api_bank.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-platform-bank.local.cybrid.com:3002
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "http://api-platform-bank.local.cybrid.com:3002"
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
    host = "http://api-platform-bank.local.cybrid.com:3002"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = prices_bank_api.PricesBankApi(api_client)
    symbol = "symbol_example" # str | Comma separated trading symbols to list prices for. (optional)
    trading_symbol = "trading_symbol_example" # str | Comma separated trading symbols to list prices for. (optional)
    payout_symbol = "payout_symbol_example" # str | Comma separated payout symbols to list prices for. (optional)
    payout_country_code = "payout_country_code_example" # str | Comma separated payout country codes to list prices for. (optional)
    payout_participants_type = "payout_participants_type_example" # str | Comma separated payout participants types to list prices for. (optional)
    payout_route = "payout_route_example" # str | Comma separated payout routes to list prices for. (optional)
    bank_guid = "bank_guid_example" # str | The bank identifier to retrieve prices for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Price
        api_response = api_instance.list_prices(symbol=symbol, trading_symbol=trading_symbol, payout_symbol=payout_symbol, payout_country_code=payout_country_code, payout_participants_type=payout_participants_type, payout_route=payout_route, bank_guid=bank_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PricesBankApi->list_prices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Comma separated trading symbols to list prices for. | [optional]
 **trading_symbol** | **str**| Comma separated trading symbols to list prices for. | [optional]
 **payout_symbol** | **str**| Comma separated payout symbols to list prices for. | [optional]
 **payout_country_code** | **str**| Comma separated payout country codes to list prices for. | [optional]
 **payout_participants_type** | **str**| Comma separated payout participants types to list prices for. | [optional]
 **payout_route** | **str**| Comma separated payout routes to list prices for. | [optional]
 **bank_guid** | **str**| The bank identifier to retrieve prices for. | [optional]

### Return type

[**SymbolPriceResponse**](SymbolPriceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of price |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

