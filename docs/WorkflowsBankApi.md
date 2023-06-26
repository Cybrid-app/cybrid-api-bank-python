# cybrid_api_bank.WorkflowsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsBankApi.md#create_workflow) | **POST** /api/workflows | Create Workflow
[**get_workflow**](WorkflowsBankApi.md#get_workflow) | **GET** /api/workflows/{workflow_guid} | Get Workflow
[**list_workflows**](WorkflowsBankApi.md#list_workflows) | **GET** /api/workflows | Get workflows list


# **create_workflow**
> Workflow create_workflow(post_workflow)

Create Workflow

Creates a workflow.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the workflow details in our private store | | completed | The Platform has created the workflow | | failed | The workflow was not completed successfully |    Required scope: **workflows:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import workflows_bank_api
from cybrid_api_bank.model.post_workflow import PostWorkflow
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.workflow import Workflow
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
    api_instance = workflows_bank_api.WorkflowsBankApi(api_client)
    post_workflow = PostWorkflow(
        type="plaid",
        kind="link_token_create",
        customer_guid="customer_guid_example",
        external_bank_account_guid="external_bank_account_guid_example",
        language="en",
        link_customization_name="link_customization_name_example",
        redirect_uri="redirect_uri_example",
        android_package_name="android_package_name_example",
    ) # PostWorkflow | 

    # example passing only required values which don't have defaults set
    try:
        # Create Workflow
        api_response = api_instance.create_workflow(post_workflow)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling WorkflowsBankApi->create_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_workflow** | [**PostWorkflow**](PostWorkflow.md)|  |

### Return type

[**Workflow**](Workflow.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workflow created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**422** | Unable to process request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> WorkflowWithDetails get_workflow(workflow_guid)

Get Workflow

Retrieves a workflow.  Required scope: **workflows:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import workflows_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.workflow_with_details import WorkflowWithDetails
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
    api_instance = workflows_bank_api.WorkflowsBankApi(api_client)
    workflow_guid = "workflow_guid_example" # str | Identifier for the workflow.

    # example passing only required values which don't have defaults set
    try:
        # Get Workflow
        api_response = api_instance.get_workflow(workflow_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling WorkflowsBankApi->get_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_guid** | **str**| Identifier for the workflow. |

### Return type

[**WorkflowWithDetails**](WorkflowWithDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | trade found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | workflow not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflows**
> WorkflowsList list_workflows()

Get workflows list

Retrieves a listing of workflows.  Required scope: **workflows:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import workflows_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.workflows_list import WorkflowsList
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
    api_instance = workflows_bank_api.WorkflowsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated workflow_guids to list workflows for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list workflows for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list workflows for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get workflows list
        api_response = api_instance.list_workflows(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling WorkflowsBankApi->list_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated workflow_guids to list workflows for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list workflows for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list workflows for. | [optional]

### Return type

[**WorkflowsList**](WorkflowsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of workflows |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

