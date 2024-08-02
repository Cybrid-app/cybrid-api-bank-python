# cybrid_api_bank.CounterpartiesBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_counterparty**](CounterpartiesBankApi.md#create_counterparty) | **POST** /api/counterparties | Create Counterparty
[**get_counterparty**](CounterpartiesBankApi.md#get_counterparty) | **GET** /api/counterparties/{counterparty_guid} | Get Counterparty
[**list_counterparties**](CounterpartiesBankApi.md#list_counterparties) | **GET** /api/counterparties | Get counterparties list


# **create_counterparty**
> Counterparty create_counterparty(post_counterparty)

Create Counterparty

Creates a counterparty.  ## Counterparty Type  Counterparty resources are an abstraction for real world individuals and businesses that are not directly on the Cybrid Platform.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the counterparty details in our private store | | unverified | The Platform has not yet verified the counterparty's identity | | verified | The Platform has verified the counterparty's identity | | rejected | The Platform was not able to successfully verify the counterparty's identity |    Required scope: **counterparties:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import counterparties_bank_api
from cybrid_api_bank.model.post_counterparty import PostCounterparty
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.counterparty import Counterparty
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
    api_instance = counterparties_bank_api.CounterpartiesBankApi(api_client)
    post_counterparty = PostCounterparty(
        type="business",
        customer_guid="customer_guid_example",
        name=PostCounterpartyName(
            first="first_example",
            middle="middle_example",
            last="last_example",
            full="full_example",
        ),
        address=PostCustomerAddress(
            street="street_example",
            street2="street2_example",
            city="city_example",
            subdivision="subdivision_example",
            postal_code="postal_code_example",
            country_code="country_code_example",
        ),
        date_of_birth=dateutil_parser('1970-01-01').date(),
        labels=[
            "labels_example",
        ],
    ) # PostCounterparty | 

    # example passing only required values which don't have defaults set
    try:
        # Create Counterparty
        api_response = api_instance.create_counterparty(post_counterparty)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CounterpartiesBankApi->create_counterparty: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_counterparty** | [**PostCounterparty**](PostCounterparty.md)|  |

### Return type

[**Counterparty**](Counterparty.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | counterparty created |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counterparty**
> Counterparty get_counterparty(counterparty_guid)

Get Counterparty

Retrieves a counterparty.  Required scope: **counterparties:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import counterparties_bank_api
from cybrid_api_bank.model.counterparty import Counterparty
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
    api_instance = counterparties_bank_api.CounterpartiesBankApi(api_client)
    counterparty_guid = "counterparty_guid_example" # str | Identifier for the counterparty.
    include_pii = True # bool | Include PII in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Counterparty
        api_response = api_instance.get_counterparty(counterparty_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CounterpartiesBankApi->get_counterparty: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Counterparty
        api_response = api_instance.get_counterparty(counterparty_guid, include_pii=include_pii)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CounterpartiesBankApi->get_counterparty: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_guid** | **str**| Identifier for the counterparty. |
 **include_pii** | **bool**| Include PII in the response. | [optional]

### Return type

[**Counterparty**](Counterparty.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | counterparty found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_counterparties**
> CounterpartyList list_counterparties()

Get counterparties list

Retrieves a listing of counterparties.  Required scope: **counterparties:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import counterparties_bank_api
from cybrid_api_bank.model.counterparty_list import CounterpartyList
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
    api_instance = counterparties_bank_api.CounterpartiesBankApi(api_client)
    page = ListRequestPage(0) # int |  (optional)
    per_page = ListRequestPerPage(1) # int |  (optional)
    type = "type_example" # str | Comma separated types to list counterparties for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list counterparties for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list counterparties for. (optional)
    guid = "guid_example" # str | Comma separated counterparty_guids to list counterparties for. (optional)
    label = "label_example" # str | Comma separated labels to list counterparties for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get counterparties list
        api_response = api_instance.list_counterparties(page=page, per_page=per_page, type=type, bank_guid=bank_guid, customer_guid=customer_guid, guid=guid, label=label)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CounterpartiesBankApi->list_counterparties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional]
 **per_page** | **int**|  | [optional]
 **type** | **str**| Comma separated types to list counterparties for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list counterparties for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list counterparties for. | [optional]
 **guid** | **str**| Comma separated counterparty_guids to list counterparties for. | [optional]
 **label** | **str**| Comma separated labels to list counterparties for. | [optional]

### Return type

[**CounterpartyList**](CounterpartyList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of counterparties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

