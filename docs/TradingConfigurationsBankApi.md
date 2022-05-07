# cybrid_api_bank.TradingConfigurationsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trading_configuration**](TradingConfigurationsBankApi.md#create_trading_configuration) | **POST** /api/trading_configurations | Create TradingConfiguration
[**get_trading_configuration**](TradingConfigurationsBankApi.md#get_trading_configuration) | **GET** /api/trading_configurations/{trading_configuration_guid} | Get TradingConfiguration
[**list_trading_configurations**](TradingConfigurationsBankApi.md#list_trading_configurations) | **GET** /api/trading_configurations | List trading configurations


# **create_trading_configuration**
> TradingConfiguration create_trading_configuration(post_trading_configuration)

Create TradingConfiguration

Creates a trading configuration.  Required scope: **banks:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import trading_configurations_bank_api
from cybrid_api_bank.model.post_trading_configuration import PostTradingConfiguration
from cybrid_api_bank.model.trading_configuration import TradingConfiguration
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
    api_instance = trading_configurations_bank_api.TradingConfigurationsBankApi(api_client)
    post_trading_configuration = PostTradingConfiguration(
        asset="asset_example",
        fees=[
            PostFee(
                type="spread",
                spread_fee=1,
                fixed_fee=1,
            ),
        ],
    ) # PostTradingConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        # Create TradingConfiguration
        api_response = api_instance.create_trading_configuration(post_trading_configuration)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TradingConfigurationsBankApi->create_trading_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_trading_configuration** | [**PostTradingConfiguration**](PostTradingConfiguration.md)|  |

### Return type

[**TradingConfiguration**](TradingConfiguration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | trading configuration created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trading_configuration**
> TradingConfiguration get_trading_configuration(trading_configuration_guid)

Get TradingConfiguration

Retrieves a trading configuration.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import trading_configurations_bank_api
from cybrid_api_bank.model.trading_configuration import TradingConfiguration
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
    api_instance = trading_configurations_bank_api.TradingConfigurationsBankApi(api_client)
    trading_configuration_guid = "trading_configuration_guid_example" # str | Identifier for the trading configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get TradingConfiguration
        api_response = api_instance.get_trading_configuration(trading_configuration_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TradingConfigurationsBankApi->get_trading_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trading_configuration_guid** | **str**| Identifier for the trading configuration. |

### Return type

[**TradingConfiguration**](TradingConfiguration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | trading configuration found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trading_configurations**
> TradingConfigurationList list_trading_configurations()

List trading configurations

Retrieves a listing of trading configurations for a bank.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import trading_configurations_bank_api
from cybrid_api_bank.model.trading_configuration_list import TradingConfigurationList
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
    api_instance = trading_configurations_bank_api.TradingConfigurationsBankApi(api_client)
    page = ListRequestPage(0) # ListRequestPage |  (optional)
    per_page = ListRequestPerPage(10) # ListRequestPerPage |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List trading configurations
        api_response = api_instance.list_trading_configurations(page=page, per_page=per_page)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TradingConfigurationsBankApi->list_trading_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **ListRequestPage**|  | [optional]
 **per_page** | **ListRequestPerPage**|  | [optional]

### Return type

[**TradingConfigurationList**](TradingConfigurationList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of trading configurations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

