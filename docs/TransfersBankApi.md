# cybrid_api_bank.TransfersBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfer**](TransfersBankApi.md#create_transfer) | **POST** /api/transfers | Create Transfer
[**get_transfer**](TransfersBankApi.md#get_transfer) | **GET** /api/transfers/{transfer_guid} | Get Transfer
[**list_transfers**](TransfersBankApi.md#list_transfers) | **GET** /api/transfers | Get transfers list


# **create_transfer**
> Transfer create_transfer(post_transfer)

Create Transfer

Creates a transfer.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the trade details in our private store | | reviewing | The Platform is reviewing the transfer for compliance | | pending | The Platform is executing the transfer | | completed | The Platform has successfully completed the transfer | | failed | The Platform was not able to successfully complete the transfer |  ## Failure codes  | Code | Description | |------|-------------| | non_sufficient_funds | The customer does not have enough funds to complete the transfer | | refresh_required | The transfer's associated external_bank_account needs to be reconnected via Plaid | | party_name_invalid | The transfer's associated external bank account has an invalid party name | | payment_rail_invalid | The payment rail specified for the transfer is not supported by the external bank account | | compliance_rejection | The transfer was rejected for compliance reasons | | cancelled | The transfer was manually cancelled | | reversed | The transfer was reversed | | limit_exceeded | The customer is over the limits that have been set for them for this activity | | network_fee_too_low | The transfer was rejected due to the network fee being too low | | amount_too_low | The transfer was rejected due to the amount being too low |    Required scope: **transfers:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import transfers_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.post_transfer import PostTransfer
from cybrid_api_bank.model.transfer import Transfer
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
    api_instance = transfers_bank_api.TransfersBankApi(api_client)
    post_transfer = PostTransfer(
        quote_guid="quote_guid_example",
        transfer_type="funding",
        customer_guid="customer_guid_example",
        source_account_guid="source_account_guid_example",
        destination_account_guid="destination_account_guid_example",
        external_wallet_guid="external_wallet_guid_example",
        external_bank_account_guid="external_bank_account_guid_example",
        network_fee_account_guid="network_fee_account_guid_example",
        payment_rail="payment_rail_example",
        beneficiary_memo="beneficiary_memo_example",
        labels=[
            "labels_example",
        ],
    ) # PostTransfer | 

    # example passing only required values which don't have defaults set
    try:
        # Create Transfer
        api_response = api_instance.create_transfer(post_transfer)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TransfersBankApi->create_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_transfer** | [**PostTransfer**](PostTransfer.md)|  |

### Return type

[**Transfer**](Transfer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer created |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer**
> Transfer get_transfer(transfer_guid)

Get Transfer

Retrieves a transfer.  Required scope: **transfers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import transfers_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.transfer import Transfer
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
    api_instance = transfers_bank_api.TransfersBankApi(api_client)
    transfer_guid = "transfer_guid_example" # str | Identifier for the transfer.

    # example passing only required values which don't have defaults set
    try:
        # Get Transfer
        api_response = api_instance.get_transfer(transfer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TransfersBankApi->get_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_guid** | **str**| Identifier for the transfer. |

### Return type

[**Transfer**](Transfer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transfer found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | transfer not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transfers**
> TransferList list_transfers()

Get transfers list

Retrieves a listing of transfers.  Required scope: **transfers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import transfers_bank_api
from cybrid_api_bank.model.transfer_list import TransferList
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
    api_instance = transfers_bank_api.TransfersBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated transfer_guids to list transfers for. (optional)
    transfer_type = "transfer_type_example" # str | Comma separated transfer_types to list accounts for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list transfers for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list transfers for. (optional)
    account_guid = "account_guid_example" # str | Comma separated account_guids to list transfers for. (optional)
    state = "state_example" # str | Comma separated states to list transfers for. (optional)
    side = "side_example" # str | Comma separated sides to list transfers for. (optional)
    label = "label_example" # str | Comma separated labels to list transfers for. (optional)
    txn_hash = "txn_hash_example" # str | Comma separated transaction hashes to list transfers for. (optional)
    created_at_gte = "created_at_gte_example" # str | Created at start date inclusive lower bound, ISO8601 (optional)
    created_at_lt = "created_at_lt_example" # str | Created at end date exclusive upper bound, ISO8601. (optional)
    updated_at_gte = "updated_at_gte_example" # str | Created at start date inclusive lower bound, ISO8601 (optional)
    updated_at_lt = "updated_at_lt_example" # str | Created at end date exclusive upper bound, ISO8601. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get transfers list
        api_response = api_instance.list_transfers(page=page, per_page=per_page, guid=guid, transfer_type=transfer_type, bank_guid=bank_guid, customer_guid=customer_guid, account_guid=account_guid, state=state, side=side, label=label, txn_hash=txn_hash, created_at_gte=created_at_gte, created_at_lt=created_at_lt, updated_at_gte=updated_at_gte, updated_at_lt=updated_at_lt)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling TransfersBankApi->list_transfers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated transfer_guids to list transfers for. | [optional]
 **transfer_type** | **str**| Comma separated transfer_types to list accounts for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list transfers for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list transfers for. | [optional]
 **account_guid** | **str**| Comma separated account_guids to list transfers for. | [optional]
 **state** | **str**| Comma separated states to list transfers for. | [optional]
 **side** | **str**| Comma separated sides to list transfers for. | [optional]
 **label** | **str**| Comma separated labels to list transfers for. | [optional]
 **txn_hash** | **str**| Comma separated transaction hashes to list transfers for. | [optional]
 **created_at_gte** | **str**| Created at start date inclusive lower bound, ISO8601 | [optional]
 **created_at_lt** | **str**| Created at end date exclusive upper bound, ISO8601. | [optional]
 **updated_at_gte** | **str**| Created at start date inclusive lower bound, ISO8601 | [optional]
 **updated_at_lt** | **str**| Created at end date exclusive upper bound, ISO8601. | [optional]

### Return type

[**TransferList**](TransferList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of transfers |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

