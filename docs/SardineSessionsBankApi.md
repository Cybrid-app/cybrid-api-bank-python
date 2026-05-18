# cybrid_api_bank.SardineSessionsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sardine_session**](SardineSessionsBankApi.md#create_sardine_session) | **POST** /api/sardine_sessions | Create Sardine Session


# **create_sardine_session**
> SardineSession create_sardine_session(post_sardine_session)

Create Sardine Session

Create a Sardine session.  Required scope: **sardine_sessions:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import sardine_sessions_bank_api
from cybrid_api_bank.model.post_sardine_session import PostSardineSession
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.sardine_session import SardineSession
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
    api_instance = sardine_sessions_bank_api.SardineSessionsBankApi(api_client)
    post_sardine_session = PostSardineSession(
        customer_guid="customer_guid_example",
    ) # PostSardineSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create Sardine Session
        api_response = api_instance.create_sardine_session(post_sardine_session)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling SardineSessionsBankApi->create_sardine_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_sardine_session** | [**PostSardineSession**](PostSardineSession.md)|  |

### Return type

[**SardineSession**](SardineSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | session created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

