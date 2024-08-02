# cybrid_api_bank.BanksBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank**](BanksBankApi.md#create_bank) | **POST** /api/banks | Create Bank
[**get_bank**](BanksBankApi.md#get_bank) | **GET** /api/banks/{bank_guid} | Get Bank
[**list_banks**](BanksBankApi.md#list_banks) | **GET** /api/banks | Get banks list
[**update_bank**](BanksBankApi.md#update_bank) | **PATCH** /api/banks/{bank_guid} | Patch Bank


# **create_bank**
> Bank create_bank(post_bank)

Create Bank

Creates a bank.  ## Bank Type  Bank's can be created in either `sandbox` or `production` mode. Sandbox Banks will not transact in real fiat dollars or cryptocurrencies.  Via the API, only `sandbox` banks can be created. In order to enable a `production` bank please contact [Support](mailto:support@cybrid.app).  ## Attestation Identity Records  Attestation Identity Records is a method the Cybrid Platform uses to verify the identity of a Bank's customers. Please see the documentation under the create Identity Record API for more technical detail.  This feature must specifically be enabled in the Bank's `features` array by including the `attestation_identity_records` flag. At present, attestation identity records is the supported method for verifying a customer's identity on the platform.  Please contact [Support](mailto:support@cybrid.app) to inquire about enabling this option for your Organization.    Required scope: **banks:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import banks_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.bank import Bank
from cybrid_api_bank.model.post_bank import PostBank
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
    api_instance = banks_bank_api.BanksBankApi(api_client)
    post_bank = PostBank(
        name="name_example",
        type="sandbox",
        supported_trading_symbols=[
            "supported_trading_symbols_example",
        ],
        features=[
            "attestation_identity_records",
        ],
        supported_fiat_account_assets=[
            "supported_fiat_account_assets_example",
        ],
        supported_country_codes=[
            "supported_country_codes_example",
        ],
    ) # PostBank | 

    # example passing only required values which don't have defaults set
    try:
        # Create Bank
        api_response = api_instance.create_bank(post_bank)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling BanksBankApi->create_bank: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_bank** | [**PostBank**](PostBank.md)|  |

### Return type

[**Bank**](Bank.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bank created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed, invalid subject |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank**
> Bank get_bank(bank_guid)

Get Bank

Retrieves a bank.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import banks_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.bank import Bank
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
    api_instance = banks_bank_api.BanksBankApi(api_client)
    bank_guid = "bank_guid_example" # str | Identifier for the bank.

    # example passing only required values which don't have defaults set
    try:
        # Get Bank
        api_response = api_instance.get_bank(bank_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling BanksBankApi->get_bank: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_guid** | **str**| Identifier for the bank. |

### Return type

[**Bank**](Bank.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bank found |  -  |
**401** | Unauthorized - Authentication failed, invalid subject |  -  |
**403** | Invalid scope |  -  |
**404** | bank not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_banks**
> BankList list_banks()

Get banks list

Retrieves a listing of bank.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import banks_bank_api
from cybrid_api_bank.model.bank_list import BankList
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
    api_instance = banks_bank_api.BanksBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    type = "type_example" # str | Comma separated types to list banks for. (optional)
    guid = "guid_example" # str | Comma separated bank_guids to list banks for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get banks list
        api_response = api_instance.list_banks(page=page, per_page=per_page, type=type, guid=guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling BanksBankApi->list_banks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **type** | **str**| Comma separated types to list banks for. | [optional]
 **guid** | **str**| Comma separated bank_guids to list banks for. | [optional]

### Return type

[**BankList**](BankList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of banks |  -  |
**401** | Unauthorized - invalid subject, Authentication failed |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank**
> Bank update_bank(bank_guid, patch_bank)

Patch Bank

Update a bank.  Required scope: **banks:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import banks_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.patch_bank import PatchBank
from cybrid_api_bank.model.bank import Bank
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
    api_instance = banks_bank_api.BanksBankApi(api_client)
    bank_guid = "bank_guid_example" # str | Identifier for the bank.
    patch_bank = PatchBank(
        name="name_example",
        supported_trading_symbols=[
            "supported_trading_symbols_example",
        ],
    ) # PatchBank | 

    # example passing only required values which don't have defaults set
    try:
        # Patch Bank
        api_response = api_instance.update_bank(bank_guid, patch_bank)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling BanksBankApi->update_bank: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_guid** | **str**| Identifier for the bank. |
 **patch_bank** | [**PatchBank**](PatchBank.md)|  |

### Return type

[**Bank**](Bank.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bank found |  -  |
**401** | Unauthorized - Authentication failed, invalid subject |  -  |
**403** | Invalid scope |  -  |
**404** | bank not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

