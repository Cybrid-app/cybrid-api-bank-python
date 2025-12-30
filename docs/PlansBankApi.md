# cybrid_api_bank.PlansBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan**](PlansBankApi.md#create_plan) | **POST** /api/plans | Create Plan
[**get_plan**](PlansBankApi.md#get_plan) | **GET** /api/plans/{plan_guid} | Get Plan
[**list_plans**](PlansBankApi.md#list_plans) | **GET** /api/plans | Get plans list


# **create_plan**
> Plan create_plan(post_plan)

Create Plan

Creates a plan.  ## Create a plan  Plans can be created for a Bank or a Customer.  To create plan for your Bank, omit the `customer_guid` parameter in the request body. To create plans for your Customers, include the `customer_guid` parameter in the request body.  | State | Description | |-------|-------------| | storing | The Platform is storing the plan details in our private store | | planning | The Platform is currently building the plan | | completed | The Platform has successfully completed the plan | | failed | The Platform was not able to successfully complete the plan |    Required scope: **plans:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import plans_bank_api
from cybrid_api_bank.model.plan import Plan
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.post_plan import PostPlan
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
    api_instance = plans_bank_api.PlansBankApi(api_client)
    post_plan = PostPlan(
        type="remittance",
        bank_guid="bank_guid_example",
        customer_guid="customer_guid_example",
        source_account=PostPlanSourceAccount(
            guid="guid_example",
            amount=1,
        ),
        destination_account=PostPlanDestinationAccount(
            guid="guid_example",
            amount=1,
        ),
        travel_rule_info=PostPlanTravelRuleInfo(
            ultimate_originating_party_guid="ultimate_originating_party_guid_example",
            ultimate_receiving_party_guid="ultimate_receiving_party_guid_example",
        ),
    ) # PostPlan | 

    # example passing only required values which don't have defaults set
    try:
        # Create Plan
        api_response = api_instance.create_plan(post_plan)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PlansBankApi->create_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_plan** | [**PostPlan**](PostPlan.md)|  |

### Return type

[**Plan**](Plan.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | plan created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan**
> Plan get_plan(plan_guid)

Get Plan

Retrieves a plan.  Required scope: **plans:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import plans_bank_api
from cybrid_api_bank.model.plan import Plan
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
    api_instance = plans_bank_api.PlansBankApi(api_client)
    plan_guid = "plan_guid_example" # str | Identifier for the payment instruction.

    # example passing only required values which don't have defaults set
    try:
        # Get Plan
        api_response = api_instance.get_plan(plan_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PlansBankApi->get_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_guid** | **str**| Identifier for the payment instruction. |

### Return type

[**Plan**](Plan.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | plan found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | plan not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plans**
> PlanList list_plans()

Get plans list

Retrieves a listing of plans. Records are sorted by creation date in descending order.  Required scope: **plans:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import plans_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.plan_list import PlanList
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
    api_instance = plans_bank_api.PlansBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated plan_guids to list plans for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list plans for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list plans for. (optional)
    type = "type_example" # str | Comma separated types to list plans for. (optional)
    state = "state_example" # str | Comma separated states to list plans for. (optional)
    source_account_guid = "source_account_guid_example" # str | Comma separated source account guids to list plans for. (optional)
    destination_account_guid = "destination_account_guid_example" # str | Comma separated destination account guids to list plans for. (optional)
    created_at_gte = "created_at_gte_example" # str | Created at start date-time inclusive lower bound, ISO8601. (optional)
    created_at_lt = "created_at_lt_example" # str | Created at end date-time exclusive upper bound, ISO8601. (optional)
    updated_at_gte = "updated_at_gte_example" # str | Updated at start date-time inclusive lower bound, ISO8601. (optional)
    updated_at_lt = "updated_at_lt_example" # str | Updated at end date-time exclusive upper bound, ISO8601. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get plans list
        api_response = api_instance.list_plans(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, type=type, state=state, source_account_guid=source_account_guid, destination_account_guid=destination_account_guid, created_at_gte=created_at_gte, created_at_lt=created_at_lt, updated_at_gte=updated_at_gte, updated_at_lt=updated_at_lt)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PlansBankApi->list_plans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated plan_guids to list plans for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list plans for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list plans for. | [optional]
 **type** | **str**| Comma separated types to list plans for. | [optional]
 **state** | **str**| Comma separated states to list plans for. | [optional]
 **source_account_guid** | **str**| Comma separated source account guids to list plans for. | [optional]
 **destination_account_guid** | **str**| Comma separated destination account guids to list plans for. | [optional]
 **created_at_gte** | **str**| Created at start date-time inclusive lower bound, ISO8601. | [optional]
 **created_at_lt** | **str**| Created at end date-time exclusive upper bound, ISO8601. | [optional]
 **updated_at_gte** | **str**| Updated at start date-time inclusive lower bound, ISO8601. | [optional]
 **updated_at_lt** | **str**| Updated at end date-time exclusive upper bound, ISO8601. | [optional]

### Return type

[**PlanList**](PlanList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of plans |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

