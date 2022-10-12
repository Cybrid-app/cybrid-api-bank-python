# cybrid_api_bank.ExternalBankAccountsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_bank_account**](ExternalBankAccountsBankApi.md#create_external_bank_account) | **POST** /api/external_bank_accounts | Create ExternalBankAccount
[**get_external_bank_account**](ExternalBankAccountsBankApi.md#get_external_bank_account) | **GET** /api/external_bank_accounts/{external_bank_account_guid} | Get External Bank Account
[**list_external_bank_accounts**](ExternalBankAccountsBankApi.md#list_external_bank_accounts) | **GET** /api/external_bank_accounts | Get external bank accounts list


# **create_external_bank_account**
> ExternalBankAccount create_external_bank_account(post_external_bank_account)

Create ExternalBankAccount

Create an ExternalBankAccount.  Required scope: **external_bank_accounts:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_bank_accounts_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.post_external_bank_account import PostExternalBankAccount
from cybrid_api_bank.model.external_bank_account import ExternalBankAccount
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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    post_external_bank_account = PostExternalBankAccount(
        name="name_example",
        account_kind="plaid",
        customer_guid="customer_guid_example",
        asset="asset_example",
        plaid_public_token="plaid_public_token_example",
        plaid_account_id="plaid_account_id_example",
    ) # PostExternalBankAccount | 

    # example passing only required values which don't have defaults set
    try:
        # Create ExternalBankAccount
        api_response = api_instance.create_external_bank_account(post_external_bank_account)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->create_external_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_external_bank_account** | [**PostExternalBankAccount**](PostExternalBankAccount.md)|  |

### Return type

[**ExternalBankAccount**](ExternalBankAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ExternalBankAccount created |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_bank_account**
> ExternalBankAccount get_external_bank_account(external_bank_account_guid)

Get External Bank Account

Retrieves an external bank account.  Required scope: **external_bank_accounts:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_bank_accounts_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.external_bank_account import ExternalBankAccount
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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    external_bank_account_guid = "external_bank_account_guid_example" # str | Identifier for the external bank account.

    # example passing only required values which don't have defaults set
    try:
        # Get External Bank Account
        api_response = api_instance.get_external_bank_account(external_bank_account_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->get_external_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_bank_account_guid** | **str**| Identifier for the external bank account. |

### Return type

[**ExternalBankAccount**](ExternalBankAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External bank account found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | ExternalBankAccount not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_bank_accounts**
> ExternalBankAccountList list_external_bank_accounts()

Get external bank accounts list

Retrieves a listing of external bank accounts.  Required scope: **external_bank_accounts:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_bank_accounts_bank_api
from cybrid_api_bank.model.external_bank_account_list import ExternalBankAccountList
from cybrid_api_bank.model.error_response import ErrorResponse
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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated external_bank_account_guids to list external_bank_accounts for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list external_bank_accounts for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list external_bank_accounts for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get external bank accounts list
        api_response = api_instance.list_external_bank_accounts(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->list_external_bank_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated external_bank_account_guids to list external_bank_accounts for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list external_bank_accounts for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list external_bank_accounts for. | [optional]

### Return type

[**ExternalBankAccountList**](ExternalBankAccountList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of external_bank_accounts |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

