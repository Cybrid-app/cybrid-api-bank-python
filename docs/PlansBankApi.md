# cybrid_api_bank.PlansBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan**](PlansBankApi.md#create_plan) | **POST** /api/plans | Create Plan
[**get_plan**](PlansBankApi.md#get_plan) | **GET** /api/plans/{plan_guid} | Get Plan


# **create_plan**
> Plan create_plan(post_plan)

Create Plan

Creates a plan.  ## Plan creation  Plans can be created for a Bank or a Customer.  To create plan for your Bank, omit the `customer_guid` parameter in the request body. To create plans for your Customers, include the `customer_guid` parameter in the request body.   Required scope: **plans:execute**

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

