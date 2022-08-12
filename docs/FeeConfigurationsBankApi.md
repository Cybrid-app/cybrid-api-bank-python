# cybrid_api_bank.FeeConfigurationsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fee_configuration**](FeeConfigurationsBankApi.md#create_fee_configuration) | **POST** /api/fee_configurations | Create FeeConfiguration
[**get_fee_configuration**](FeeConfigurationsBankApi.md#get_fee_configuration) | **GET** /api/fee_configurations/{fee_configuration_guid} | Get FeeConfiguration
[**list_fee_configurations**](FeeConfigurationsBankApi.md#list_fee_configurations) | **GET** /api/fee_configurations | List fee configurations


# **create_fee_configuration**
> FeeConfiguration create_fee_configuration(post_fee_configuration)

Create FeeConfiguration

Creates a fee configuration.  Required scope: **banks:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import fee_configurations_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.post_fee_configuration import PostFeeConfiguration
from cybrid_api_bank.model.fee_configuration import FeeConfiguration
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
    api_instance = fee_configurations_bank_api.FeeConfigurationsBankApi(api_client)
    post_fee_configuration = PostFeeConfiguration(
        product_type="trading",
        asset="asset_example",
        fees=[
            PostFee(
                type="spread",
                spread_fee=1,
                fixed_fee=1,
            ),
        ],
        product_provider="compound",
    ) # PostFeeConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        # Create FeeConfiguration
        api_response = api_instance.create_fee_configuration(post_fee_configuration)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FeeConfigurationsBankApi->create_fee_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_fee_configuration** | [**PostFeeConfiguration**](PostFeeConfiguration.md)|  |

### Return type

[**FeeConfiguration**](FeeConfiguration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | fee configuration created |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_configuration**
> FeeConfiguration get_fee_configuration(fee_configuration_guid)

Get FeeConfiguration

Retrieves a fee configuration.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import fee_configurations_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.fee_configuration import FeeConfiguration
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
    api_instance = fee_configurations_bank_api.FeeConfigurationsBankApi(api_client)
    fee_configuration_guid = "fee_configuration_guid_example" # str | Identifier for the fee configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get FeeConfiguration
        api_response = api_instance.get_fee_configuration(fee_configuration_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FeeConfigurationsBankApi->get_fee_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_configuration_guid** | **str**| Identifier for the fee configuration. |

### Return type

[**FeeConfiguration**](FeeConfiguration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fee configuration found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | fee_configuration not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fee_configurations**
> FeeConfigurationList list_fee_configurations()

List fee configurations

Retrieves a listing of fee configurations for a bank.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import fee_configurations_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.fee_configuration_list import FeeConfigurationList
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
    api_instance = fee_configurations_bank_api.FeeConfigurationsBankApi(api_client)
    page = ListRequestPage(0) # int |  (optional)
    per_page = ListRequestPerPage(1) # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List fee configurations
        api_response = api_instance.list_fee_configurations(page=page, per_page=per_page)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FeeConfigurationsBankApi->list_fee_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional]
 **per_page** | **int**|  | [optional]

### Return type

[**FeeConfigurationList**](FeeConfigurationList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of fee configurations |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

