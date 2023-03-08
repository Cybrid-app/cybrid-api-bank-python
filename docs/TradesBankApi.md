# cybrid_api_bank.TradesBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trade**](TradesBankApi.md#create_trade) | **POST** /api/trades | Create Trade
[**get_trade**](TradesBankApi.md#get_trade) | **GET** /api/trades/{trade_guid} | Get Trade
[**list_trades**](TradesBankApi.md#list_trades) | **GET** /api/trades | Get trades list


# **create_trade**
> Trade create_trade(post_trade)

Create Trade

Creates a trade.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the trade details in our private store | | initiating | The Platform has begun to perform the trade | | pending | The Platform is executing the trade | | settling | The Platform is settling the trade | | completed | The Platform has successfully completed the trade | | failed | The Platform was not able to successfully complete the trade |    Required scope: **trades:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import trades_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.trade import Trade
from cybrid_api_bank.model.post_trade import PostTrade
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
    api_instance = trades_bank_api.TradesBankApi(api_client)
    post_trade = PostTrade(
        quote_guid="quote_guid_example",
        expected_error="unexpected_error",
    ) # PostTrade | 

    # example passing only required values which don't have defaults set
    try:
        # Create Trade
        api_response = api_instance.create_trade(post_trade)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TradesBankApi->create_trade: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_trade** | [**PostTrade**](PostTrade.md)|  |

### Return type

[**Trade**](Trade.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Trade created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**409** | Data already exists |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade**
> Trade get_trade(trade_guid)

Get Trade

Retrieves a trade.  Required scope: **trades:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import trades_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.trade import Trade
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
    api_instance = trades_bank_api.TradesBankApi(api_client)
    trade_guid = "trade_guid_example" # str | Identifier for the trade.

    # example passing only required values which don't have defaults set
    try:
        # Get Trade
        api_response = api_instance.get_trade(trade_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TradesBankApi->get_trade: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_guid** | **str**| Identifier for the trade. |

### Return type

[**Trade**](Trade.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | trade found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | trade not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trades**
> TradeList list_trades()

Get trades list

Retrieves a listing of trades.  Required scope: **trades:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import trades_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.trade_list import TradeList
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
    api_instance = trades_bank_api.TradesBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated trade_guids to list trades for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list trades for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list trades for. (optional)
    account_guid = "account_guid_example" # str | Comma separated account_guids to list trades for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get trades list
        api_response = api_instance.list_trades(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, account_guid=account_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TradesBankApi->list_trades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated trade_guids to list trades for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list trades for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list trades for. | [optional]
 **account_guid** | **str**| Comma separated account_guids to list trades for. | [optional]

### Return type

[**TradeList**](TradeList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of trades |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

