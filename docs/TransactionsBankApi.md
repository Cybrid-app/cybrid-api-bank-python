# cybrid_api_bank.TransactionsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_transactions**](TransactionsBankApi.md#list_transactions) | **GET** /api/transactions | List Transactions


# **list_transactions**
> TransactionList list_transactions(account_guid)

List Transactions

Retrieves a listing of transactions (an account statement) for an account.  Required scope: **transactions:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import transactions_bank_api
from cybrid_api_bank.model.transaction_list import TransactionList
from cybrid_api_bank.model.error_response import ErrorResponse
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
    api_instance = transactions_bank_api.TransactionsBankApi(api_client)
    account_guid = "account_guid_example" # str | 
    cursor = "cursor_example" # str, none_type |  (optional)
    per_page = ListRequestPerPage(1) # int |  (optional)
    direction = "credit" # str |  (optional)
    created_at_gte = "created_at_gte_example" # str | Created at start date-time inclusive lower bound, ISO8601. (optional)
    created_at_lt = "created_at_lt_example" # str | Created at end date-time exclusive upper bound, ISO8601. (optional)
    include_balances = True # bool | Include the running posted balance on the account as of each transaction. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Transactions
        api_response = api_instance.list_transactions(account_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TransactionsBankApi->list_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Transactions
        api_response = api_instance.list_transactions(account_guid, cursor=cursor, per_page=per_page, direction=direction, created_at_gte=created_at_gte, created_at_lt=created_at_lt, include_balances=include_balances)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TransactionsBankApi->list_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**|  |
 **cursor** | **str, none_type**|  | [optional]
 **per_page** | **int**|  | [optional]
 **direction** | **str**|  | [optional]
 **created_at_gte** | **str**| Created at start date-time inclusive lower bound, ISO8601. | [optional]
 **created_at_lt** | **str**| Created at end date-time exclusive upper bound, ISO8601. | [optional]
 **include_balances** | **bool**| Include the running posted balance on the account as of each transaction. | [optional]

### Return type

[**TransactionList**](TransactionList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of transactions |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed |  -  |
**403** | Invalid scope |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

