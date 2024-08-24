# cybrid_api_bank.ExternalBankAccountsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_bank_account**](ExternalBankAccountsBankApi.md#create_external_bank_account) | **POST** /api/external_bank_accounts | Create ExternalBankAccount
[**delete_external_bank_account**](ExternalBankAccountsBankApi.md#delete_external_bank_account) | **DELETE** /api/external_bank_accounts/{external_bank_account_guid} | Delete External Bank Account
[**get_external_bank_account**](ExternalBankAccountsBankApi.md#get_external_bank_account) | **GET** /api/external_bank_accounts/{external_bank_account_guid} | Get External Bank Account
[**list_external_bank_accounts**](ExternalBankAccountsBankApi.md#list_external_bank_accounts) | **GET** /api/external_bank_accounts | Get external bank accounts list
[**patch_external_bank_account**](ExternalBankAccountsBankApi.md#patch_external_bank_account) | **PATCH** /api/external_bank_accounts/{external_bank_account_guid} | Patch ExternalBankAccount


# **create_external_bank_account**
> ExternalBankAccount create_external_bank_account(post_external_bank_account)

Create ExternalBankAccount

Create an ExternalBankAccount.  ## Account creation  Accounts can be created for a Bank or a Customer.  To create accounts for your Bank, omit the `customer_guid` parameter in the request body. To create accounts for your Customers, include the `customer_guid` parameter in the request body.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the external bank account details in our private store | | completed | The Platform has created the external bank account | | unverified | The external bank account is created, but it has not yet been verified | | failed | The Platform was not able to successfully create the external bank account | | refresh_required | The Platform has created the external bank account, but needs to be refreshed | | deleting | The Platform is deleting the external bank account | | deleted | The Platform has deleted the external bank account |  ## Failure codes  | Code | Description | |------|-------------| | invalid_routing_number | The provided routing number is invalid | | refresh_required | The Plaid processor token used to create the account needs to be refreshed | | plaid_processor_token | An account could not be created due to an invalid Plaid processor token or an error with Plaid |    Required scope: **external_bank_accounts:execute**

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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    post_external_bank_account = PostExternalBankAccount(
        name="name_example",
        account_kind="plaid",
        customer_guid="customer_guid_example",
        asset="asset_example",
        plaid_public_token="plaid_public_token_example",
        plaid_account_id="plaid_account_id_example",
        plaid_processor_token="plaid_processor_token_example",
        plaid_institution_id="plaid_institution_id_example",
        plaid_account_mask="plaid_account_mask_example",
        plaid_account_name="plaid_account_name_example",
        counterparty_bank_account=PostExternalBankAccountCounterpartyBankAccount(
            routing_number_type="CPA",
            routing_number="routing_number_example",
            account_number="account_number_example",
        ),
        counterparty_name=PostExternalBankAccountCounterpartyName(
            first="first_example",
            middle="middle_example",
            last="last_example",
            full="full_example",
        ),
        counterparty_address=PostExternalBankAccountCounterpartyAddress(
            street="street_example",
            street2="street2_example",
            city="city_example",
            subdivision="subdivision_example",
            postal_code="postal_code_example",
            country_code="country_code_example",
        ),
        counterparty_email_address="counterparty_email_address_example",
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
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_bank_account**
> ExternalBankAccount delete_external_bank_account(external_bank_account_guid)

Delete External Bank Account

Deletes an external bank account.  Required scope: **external_bank_accounts:execute**

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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    external_bank_account_guid = "external_bank_account_guid_example" # str | Identifier for the external bank account.

    # example passing only required values which don't have defaults set
    try:
        # Delete External Bank Account
        api_response = api_instance.delete_external_bank_account(external_bank_account_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->delete_external_bank_account: %s\n" % e)
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
**200** | External bank account deleted |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | ExternalBankAccount not found |  -  |

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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    external_bank_account_guid = "external_bank_account_guid_example" # str | Identifier for the external bank account.
    force_balance_refresh = True # bool | Force the balance on the account to be retrieved. (optional)
    include_balances = True # bool | Include balance information in the response. If `force_balance_refresh` is `true`, the most up to date balance will be returned. If `force_balance_refresh` is `false`, the cached balance will be returned. `balance_updated_at` in the response will provide the timestamp the balance was last updated. (optional)
    include_pii = True # bool | Include the account holder's PII in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get External Bank Account
        api_response = api_instance.get_external_bank_account(external_bank_account_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->get_external_bank_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get External Bank Account
        api_response = api_instance.get_external_bank_account(external_bank_account_guid, force_balance_refresh=force_balance_refresh, include_balances=include_balances, include_pii=include_pii)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->get_external_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_bank_account_guid** | **str**| Identifier for the external bank account. |
 **force_balance_refresh** | **bool**| Force the balance on the account to be retrieved. | [optional]
 **include_balances** | **bool**| Include balance information in the response. If &#x60;force_balance_refresh&#x60; is &#x60;true&#x60;, the most up to date balance will be returned. If &#x60;force_balance_refresh&#x60; is &#x60;false&#x60;, the cached balance will be returned. &#x60;balance_updated_at&#x60; in the response will provide the timestamp the balance was last updated. | [optional]
 **include_pii** | **bool**| Include the account holder&#39;s PII in the response. | [optional]

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
**422** | Unable to process request |  -  |

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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated external_bank_account_guids to list external_bank_accounts for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list external_bank_accounts for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list external_bank_accounts for. (optional)
    asset = "asset_example" # str | Comma separated assets to list external_bank_accounts for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get external bank accounts list
        api_response = api_instance.list_external_bank_accounts(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, asset=asset)
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
 **asset** | **str**| Comma separated assets to list external_bank_accounts for. | [optional]

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
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_external_bank_account**
> ExternalBankAccount patch_external_bank_account(external_bank_account_guid, patch_external_bank_account)

Patch ExternalBankAccount

Patch an external bank account.  Required scope: **external_bank_accounts:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import external_bank_accounts_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.patch_external_bank_account import PatchExternalBankAccount
from cybrid_api_bank.model.external_bank_account import ExternalBankAccount
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
    api_instance = external_bank_accounts_bank_api.ExternalBankAccountsBankApi(api_client)
    external_bank_account_guid = "external_bank_account_guid_example" # str | Identifier for the external bank account.
    patch_external_bank_account = PatchExternalBankAccount(
        state="completed",
    ) # PatchExternalBankAccount | 

    # example passing only required values which don't have defaults set
    try:
        # Patch ExternalBankAccount
        api_response = api_instance.patch_external_bank_account(external_bank_account_guid, patch_external_bank_account)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExternalBankAccountsBankApi->patch_external_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_bank_account_guid** | **str**| Identifier for the external bank account. |
 **patch_external_bank_account** | [**PatchExternalBankAccount**](PatchExternalBankAccount.md)|  |

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
**200** | external bank account found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | ExternalBankAccount not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

