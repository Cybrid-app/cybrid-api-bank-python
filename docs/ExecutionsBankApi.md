# cybrid_api_bank.ExecutionsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_execution**](ExecutionsBankApi.md#create_execution) | **POST** /api/executions | Create Execution
[**get_execution**](ExecutionsBankApi.md#get_execution) | **GET** /api/executions/{execution_guid} | Get Execution


# **create_execution**
> Execution create_execution(post_execution)

Create Execution

Creates an execution.  post  Required scope: **executions:execute**

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

