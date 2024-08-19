# cybrid_api_bank.CustomersBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersBankApi.md#create_customer) | **POST** /api/customers | Create Customer
[**get_customer**](CustomersBankApi.md#get_customer) | **GET** /api/customers/{customer_guid} | Get Customer
[**list_customers**](CustomersBankApi.md#list_customers) | **GET** /api/customers | Get customers list
[**update_customer**](CustomersBankApi.md#update_customer) | **PATCH** /api/customers/{customer_guid} | Patch Customer


# **create_customer**
> Customer create_customer(post_customer)

Create Customer

Creates a customer.  ## Customer Type  Customer resources are an abstraction for real world individuals and businesses on the Cybrid Platform and are used throughout the platform to perform high level operations, e.g., create a quote, execute a trade, etc..  Customers can have additional resources attached to them, e.g., identity verifications, accounts, etc.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the customer details in our private store | | unverified | The Platform has not yet verified the customer's identity | | verified | The Platform has verified the customer's identity | | rejected | The Platform was not able to successfully verify the customer's identity | | frozen | The customer has been frozen on the Platform |    Required scope: **customers:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import customers_bank_api
from cybrid_api_bank.model.customer import Customer
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.post_customer import PostCustomer
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
    api_instance = customers_bank_api.CustomersBankApi(api_client)
    post_customer = PostCustomer(
        type="business",
        name=PostCustomerName(
            first="first_example",
            middle="middle_example",
            last="last_example",
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
        phone_number="phone_number_example",
        email_address="email_address_example",
        identification_numbers=[
            PostIdentificationNumber(
                type="drivers_license",
                issuing_country_code="issuing_country_code_example",
                identification_number="identification_number_example",
            ),
        ],
        labels=[
            "labels_example",
        ],
    ) # PostCustomer | 

    # example passing only required values which don't have defaults set
    try:
        # Create Customer
        api_response = api_instance.create_customer(post_customer)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CustomersBankApi->create_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_customer** | [**PostCustomer**](PostCustomer.md)|  |

### Return type

[**Customer**](Customer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | customer created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> Customer get_customer(customer_guid)

Get Customer

Retrieves a customer.  Required scope: **customers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import customers_bank_api
from cybrid_api_bank.model.customer import Customer
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
    api_instance = customers_bank_api.CustomersBankApi(api_client)
    customer_guid = "customer_guid_example" # str | Identifier for the customer.
    include_pii = True # bool | Include PII in the response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Customer
        api_response = api_instance.get_customer(customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CustomersBankApi->get_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Customer
        api_response = api_instance.get_customer(customer_guid, include_pii=include_pii)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CustomersBankApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_guid** | **str**| Identifier for the customer. |
 **include_pii** | **bool**| Include PII in the response. | [optional]

### Return type

[**Customer**](Customer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | customer found |  -  |
**401** | Unauthorized - Authentication failed, invalid subject |  -  |
**403** | Invalid scope |  -  |
**404** | customer not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> CustomerList list_customers()

Get customers list

Retrieves a listing of customers.  Required scope: **customers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import customers_bank_api
from cybrid_api_bank.model.customer_list import CustomerList
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
    api_instance = customers_bank_api.CustomersBankApi(api_client)
    page = ListRequestPage(0) # int |  (optional)
    per_page = ListRequestPerPage(1) # int |  (optional)
    type = "type_example" # str | Comma separated types to list customers for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list customers for. (optional)
    guid = "guid_example" # str | Comma separated customer_guids to list customers for. (optional)
    label = "label_example" # str | Comma separated labels to list customers for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get customers list
        api_response = api_instance.list_customers(page=page, per_page=per_page, type=type, bank_guid=bank_guid, guid=guid, label=label)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CustomersBankApi->list_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional]
 **per_page** | **int**|  | [optional]
 **type** | **str**| Comma separated types to list customers for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list customers for. | [optional]
 **guid** | **str**| Comma separated customer_guids to list customers for. | [optional]
 **label** | **str**| Comma separated labels to list customers for. | [optional]

### Return type

[**CustomerList**](CustomerList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of customers |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed, invalid subject, |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> Customer update_customer(customer_guid, patch_customer)

Patch Customer

Update a customer.  Required scope: **customers:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import customers_bank_api
from cybrid_api_bank.model.customer import Customer
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.patch_customer import PatchCustomer
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
    api_instance = customers_bank_api.CustomersBankApi(api_client)
    customer_guid = "customer_guid_example" # str | Identifier for the customer.
    patch_customer = PatchCustomer(
        state="unverified",
    ) # PatchCustomer | 

    # example passing only required values which don't have defaults set
    try:
        # Patch Customer
        api_response = api_instance.update_customer(customer_guid, patch_customer)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling CustomersBankApi->update_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_guid** | **str**| Identifier for the customer. |
 **patch_customer** | [**PatchCustomer**](PatchCustomer.md)|  |

### Return type

[**Customer**](Customer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | customer found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

