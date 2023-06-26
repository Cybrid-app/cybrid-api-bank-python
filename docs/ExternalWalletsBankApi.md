# cybrid_api_bank.ExternalWalletsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_wallet**](ExternalWalletsBankApi.md#create_external_wallet) | **POST** /api/external_wallets | Create ExternalWallet
[**delete_external_wallet**](ExternalWalletsBankApi.md#delete_external_wallet) | **DELETE** /api/external_wallets/{external_wallet_guid} | Delete External Wallet
[**get_external_wallet**](ExternalWalletsBankApi.md#get_external_wallet) | **GET** /api/external_wallets/{external_wallet_guid} | Get External Wallet
[**list_external_wallets**](ExternalWalletsBankApi.md#list_external_wallets) | **GET** /api/external_wallets | Get external wallets list


# **create_external_wallet**
> ExternalWallet create_external_wallet(post_external_wallet)

Create ExternalWallet

Create an ExternalWallet.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the external wallet details in our private store | | pending | The Platform is waiting for the external wallet to be created | | completed | The Platform has created the external wallet | | failed | The Platform was not able to successfully create the external wallet | | deleting | The Platform is deleting the external wallet | | deleted | The Platform has deleted the external wallet |    External wallets can be added to the bank by leaving the customer_guid blank. External wallets added to the bank can be used by any customer of the bank.  External wallets can also be added to a specific customer by providing the customer_guid. External wallets added to a customer can only be used by that customer.  Required scope: **external_wallets:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_wallets_bank_api
from cybrid_api_bank.model.post_external_wallet import PostExternalWallet
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.external_wallet import ExternalWallet
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
    api_instance = external_wallets_bank_api.ExternalWalletsBankApi(api_client)
    post_external_wallet = PostExternalWallet(
        name="name_example",
        customer_guid="customer_guid_example",
        asset="asset_example",
        address="address_example",
        tag="tag_example",
    ) # PostExternalWallet | 

    # example passing only required values which don't have defaults set
    try:
        # Create ExternalWallet
        api_response = api_instance.create_external_wallet(post_external_wallet)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalWalletsBankApi->create_external_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_external_wallet** | [**PostExternalWallet**](PostExternalWallet.md)|  |

### Return type

[**ExternalWallet**](ExternalWallet.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ExternalWallet created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**409** | Data already exists |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_wallet**
> ExternalWallet delete_external_wallet(external_wallet_guid)

Delete External Wallet

Deletes an external wallet.  Required scope: **external_wallets:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_wallets_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.external_wallet import ExternalWallet
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
    api_instance = external_wallets_bank_api.ExternalWalletsBankApi(api_client)
    external_wallet_guid = "external_wallet_guid_example" # str | Identifier for the external wallet.

    # example passing only required values which don't have defaults set
    try:
        # Delete External Wallet
        api_response = api_instance.delete_external_wallet(external_wallet_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalWalletsBankApi->delete_external_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_wallet_guid** | **str**| Identifier for the external wallet. |

### Return type

[**ExternalWallet**](ExternalWallet.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External wallet deleted |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | ExternalWallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_wallet**
> ExternalWallet get_external_wallet(external_wallet_guid)

Get External Wallet

Retrieves an external_wallet.  Required scope: **external_wallets:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_wallets_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.external_wallet import ExternalWallet
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
    api_instance = external_wallets_bank_api.ExternalWalletsBankApi(api_client)
    external_wallet_guid = "external_wallet_guid_example" # str | Identifier for the external_wallet.

    # example passing only required values which don't have defaults set
    try:
        # Get External Wallet
        api_response = api_instance.get_external_wallet(external_wallet_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalWalletsBankApi->get_external_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_wallet_guid** | **str**| Identifier for the external_wallet. |

### Return type

[**ExternalWallet**](ExternalWallet.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External wallet found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | ExternalWallet not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_wallets**
> ExternalWalletList list_external_wallets()

Get external wallets list

Retrieves a listing of external wallets.  Required scope: **external_wallets:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_wallets_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.external_wallet_list import ExternalWalletList
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
    api_instance = external_wallets_bank_api.ExternalWalletsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated external_wallet_guids to list external_wallets for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list external_wallets for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list external_wallets for. (optional)
    state = "state_example" # str | Comma separated states to list external_wallets for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get external wallets list
        api_response = api_instance.list_external_wallets(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, state=state)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalWalletsBankApi->list_external_wallets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated external_wallet_guids to list external_wallets for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list external_wallets for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list external_wallets for. | [optional]
 **state** | **str**| Comma separated states to list external_wallets for. | [optional]

### Return type

[**ExternalWalletList**](ExternalWalletList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of external_wallets |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

