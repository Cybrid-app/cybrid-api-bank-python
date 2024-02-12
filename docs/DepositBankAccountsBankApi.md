# cybrid_api_bank.DepositBankAccountsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deposit_bank_account**](DepositBankAccountsBankApi.md#create_deposit_bank_account) | **POST** /api/deposit_bank_accounts | Create Deposit Bank Account
[**get_deposit_bank_account**](DepositBankAccountsBankApi.md#get_deposit_bank_account) | **GET** /api/deposit_bank_accounts/{deposit_bank_account_guid} | Get Deposit Bank Account
[**list_deposit_bank_accounts**](DepositBankAccountsBankApi.md#list_deposit_bank_accounts) | **GET** /api/deposit_bank_accounts | List Deposit Bank Accounts


# **create_deposit_bank_account**
> DepositBankAccount create_deposit_bank_account(post_deposit_bank_account)

Create Deposit Bank Account

Creates a deposit bank account.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the deposit bank account details in our private store | | created | The Platform has created the deposit bank account |    Required scope: **deposit_bank_accounts:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import deposit_bank_accounts_bank_api
from cybrid_api_bank.model.post_deposit_bank_account import PostDepositBankAccount
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.deposit_bank_account import DepositBankAccount
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
    api_instance = deposit_bank_accounts_bank_api.DepositBankAccountsBankApi(api_client)
    post_deposit_bank_account = PostDepositBankAccount(
        account_guid="account_guid_example",
        customer_guid="customer_guid_example",
        labels=[
            "labels_example",
        ],
    ) # PostDepositBankAccount | 

    # example passing only required values which don't have defaults set
    try:
        # Create Deposit Bank Account
        api_response = api_instance.create_deposit_bank_account(post_deposit_bank_account)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling DepositBankAccountsBankApi->create_deposit_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_deposit_bank_account** | [**PostDepositBankAccount**](PostDepositBankAccount.md)|  |

### Return type

[**DepositBankAccount**](DepositBankAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deposit Bank Account created |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit_bank_account**
> DepositBankAccount get_deposit_bank_account(deposit_bank_account_guid)

Get Deposit Bank Account

Retrieves a deposit bank account.  Required scope: **deposit_bank_accounts:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import deposit_bank_accounts_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.deposit_bank_account import DepositBankAccount
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
    api_instance = deposit_bank_accounts_bank_api.DepositBankAccountsBankApi(api_client)
    deposit_bank_account_guid = "deposit_bank_account_guid_example" # str | Identifier for the deposit bank account.

    # example passing only required values which don't have defaults set
    try:
        # Get Deposit Bank Account
        api_response = api_instance.get_deposit_bank_account(deposit_bank_account_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling DepositBankAccountsBankApi->get_deposit_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_bank_account_guid** | **str**| Identifier for the deposit bank account. |

### Return type

[**DepositBankAccount**](DepositBankAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deposit bank account found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | deposit_bank_account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deposit_bank_accounts**
> DepositBankAccountList list_deposit_bank_accounts()

List Deposit Bank Accounts

Retrieves a list of deposit bank accounts.  Required scope: **deposit_bank_accounts:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import deposit_bank_accounts_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.deposit_bank_account_list import DepositBankAccountList
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
    api_instance = deposit_bank_accounts_bank_api.DepositBankAccountsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated guids to list deposit bank accounts for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list deposit bank accounts for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list deposit bank accounts for. (optional)
    label = "label_example" # str | Comma separated labels to list deposit bank accounts for. (optional)
    unique_memo_id = "unique_memo_id_example" # str | Comma separated unique memo ids to list deposit bank accounts for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Deposit Bank Accounts
        api_response = api_instance.list_deposit_bank_accounts(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, label=label, unique_memo_id=unique_memo_id)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling DepositBankAccountsBankApi->list_deposit_bank_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated guids to list deposit bank accounts for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list deposit bank accounts for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list deposit bank accounts for. | [optional]
 **label** | **str**| Comma separated labels to list deposit bank accounts for. | [optional]
 **unique_memo_id** | **str**| Comma separated unique memo ids to list deposit bank accounts for. | [optional]

### Return type

[**DepositBankAccountList**](DepositBankAccountList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of deposit bank accounts |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

