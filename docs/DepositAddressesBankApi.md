# cybrid_api_bank.DepositAddressesBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deposit_address**](DepositAddressesBankApi.md#create_deposit_address) | **POST** /api/deposit_addresses | Create Deposit Address
[**get_deposit_address**](DepositAddressesBankApi.md#get_deposit_address) | **GET** /api/deposit_addresses/{deposit_address_guid} | Get Deposit Address
[**list_deposit_addresses**](DepositAddressesBankApi.md#list_deposit_addresses) | **GET** /api/deposit_addresses | List Deposit Addresses


# **create_deposit_address**
> DepositAddress create_deposit_address(post_deposit_address)

Create Deposit Address

Create an Deposit Address.  Required scope: **deposit_addresses:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import deposit_addresses_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.deposit_address import DepositAddress
from cybrid_api_bank.model.post_deposit_address import PostDepositAddress
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
    api_instance = deposit_addresses_bank_api.DepositAddressesBankApi(api_client)
    post_deposit_address = PostDepositAddress(
        account_guid="account_guid_example",
    ) # PostDepositAddress | 

    # example passing only required values which don't have defaults set
    try:
        # Create Deposit Address
        api_response = api_instance.create_deposit_address(post_deposit_address)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling DepositAddressesBankApi->create_deposit_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_deposit_address** | [**PostDepositAddress**](PostDepositAddress.md)|  |

### Return type

[**DepositAddress**](DepositAddress.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deposit Address created |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit_address**
> DepositAddress get_deposit_address(deposit_address_guid)

Get Deposit Address

Retrieves a deposit address.  Required scope: **deposit_addresses:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import deposit_addresses_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.deposit_address import DepositAddress
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
    api_instance = deposit_addresses_bank_api.DepositAddressesBankApi(api_client)
    deposit_address_guid = "deposit_address_guid_example" # str | Identifier for the deposit address.

    # example passing only required values which don't have defaults set
    try:
        # Get Deposit Address
        api_response = api_instance.get_deposit_address(deposit_address_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling DepositAddressesBankApi->get_deposit_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_address_guid** | **str**| Identifier for the deposit address. |

### Return type

[**DepositAddress**](DepositAddress.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deposit address found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | deposit_address not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deposit_addresses**
> DepositAddressList list_deposit_addresses()

List Deposit Addresses

Retrieves a list of deposit addresses.  Required scope: **deposit_addresses:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import deposit_addresses_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.deposit_address_list import DepositAddressList
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
    api_instance = deposit_addresses_bank_api.DepositAddressesBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated guids to list deposit addresses for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list deposit addresses for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list deposit addresses for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Deposit Addresses
        api_response = api_instance.list_deposit_addresses(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling DepositAddressesBankApi->list_deposit_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated guids to list deposit addresses for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list deposit addresses for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list deposit addresses for. | [optional]

### Return type

[**DepositAddressList**](DepositAddressList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of deposit addresses |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

