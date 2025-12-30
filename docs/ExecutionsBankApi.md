# cybrid_api_bank.ExecutionsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_execution**](ExecutionsBankApi.md#create_execution) | **POST** /api/executions | Create Execution
[**get_execution**](ExecutionsBankApi.md#get_execution) | **GET** /api/executions/{execution_guid} | Get Execution
[**list_executions**](ExecutionsBankApi.md#list_executions) | **GET** /api/executions | Get executions list


# **create_execution**
> Execution create_execution(post_execution)

Create Execution

Creates an execution.  ## Create a plan execution  | State | Description | |-------|-------------| | storing | The Platform is storing the execution details in our private store | | executing | The Platform is executing the plan | | completed | The Platform has successfully completed the plan execution | | failed | The Platform was not able to successfully complete the plan execution |    Required scope: **executions:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import executions_bank_api
from cybrid_api_bank.model.post_execution import PostExecution
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.execution import Execution
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
    api_instance = executions_bank_api.ExecutionsBankApi(api_client)
    post_execution = PostExecution(
        plan_guid="plan_guid_example",
    ) # PostExecution | 

    # example passing only required values which don't have defaults set
    try:
        # Create Execution
        api_response = api_instance.create_execution(post_execution)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExecutionsBankApi->create_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_execution** | [**PostExecution**](PostExecution.md)|  |

### Return type

[**Execution**](Execution.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | execution created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> Execution get_execution(execution_guid)

Get Execution

Retrieves a execution.  Required scope: **executions:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import executions_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.execution import Execution
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
    api_instance = executions_bank_api.ExecutionsBankApi(api_client)
    execution_guid = "execution_guid_example" # str | Identifier for the payment instruction.

    # example passing only required values which don't have defaults set
    try:
        # Get Execution
        api_response = api_instance.get_execution(execution_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExecutionsBankApi->get_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_guid** | **str**| Identifier for the payment instruction. |

### Return type

[**Execution**](Execution.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | execution found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | execution not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_executions**
> ExecutionList list_executions()

Get executions list

Retrieves a listing of executions. Records are sorted by creation date in descending order.  Required scope: **executions:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import executions_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.execution_list import ExecutionList
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
    api_instance = executions_bank_api.ExecutionsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated execution_guids to list executions for. (optional)
    plan_guid = "plan_guid_example" # str | Comma separated plan_guids to list executions for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list executions for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list executions for. (optional)
    type = "type_example" # str | Comma separated types to list executions for. (optional)
    state = "state_example" # str | Comma separated states to list executions for. (optional)
    source_account_guid = "source_account_guid_example" # str | Comma separated source account guids to list executions for. (optional)
    destination_account_guid = "destination_account_guid_example" # str | Comma separated destination account guids to list executions for. (optional)
    created_at_gte = "created_at_gte_example" # str | Created at start date-time inclusive lower bound, ISO8601. (optional)
    created_at_lt = "created_at_lt_example" # str | Created at end date-time exclusive upper bound, ISO8601. (optional)
    updated_at_gte = "updated_at_gte_example" # str | Updated at start date-time inclusive lower bound, ISO8601. (optional)
    updated_at_lt = "updated_at_lt_example" # str | Updated at end date-time exclusive upper bound, ISO8601. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get executions list
        api_response = api_instance.list_executions(page=page, per_page=per_page, guid=guid, plan_guid=plan_guid, bank_guid=bank_guid, customer_guid=customer_guid, type=type, state=state, source_account_guid=source_account_guid, destination_account_guid=destination_account_guid, created_at_gte=created_at_gte, created_at_lt=created_at_lt, updated_at_gte=updated_at_gte, updated_at_lt=updated_at_lt)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling ExecutionsBankApi->list_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated execution_guids to list executions for. | [optional]
 **plan_guid** | **str**| Comma separated plan_guids to list executions for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list executions for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list executions for. | [optional]
 **type** | **str**| Comma separated types to list executions for. | [optional]
 **state** | **str**| Comma separated states to list executions for. | [optional]
 **source_account_guid** | **str**| Comma separated source account guids to list executions for. | [optional]
 **destination_account_guid** | **str**| Comma separated destination account guids to list executions for. | [optional]
 **created_at_gte** | **str**| Created at start date-time inclusive lower bound, ISO8601. | [optional]
 **created_at_lt** | **str**| Created at end date-time exclusive upper bound, ISO8601. | [optional]
 **updated_at_gte** | **str**| Updated at start date-time inclusive lower bound, ISO8601. | [optional]
 **updated_at_lt** | **str**| Updated at end date-time exclusive upper bound, ISO8601. | [optional]

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of executions |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

