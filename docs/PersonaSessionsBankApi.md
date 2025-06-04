# cybrid_api_bank.PersonaSessionsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_persona_session**](PersonaSessionsBankApi.md#create_persona_session) | **POST** /api/persona_sessions | Create Persona Session


# **create_persona_session**
> PersonaSession create_persona_session(post_persona_session)

Create Persona Session

Create a Persona session.  Required scope: **persona_sessions:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import persona_sessions_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.post_persona_session import PostPersonaSession
from cybrid_api_bank.model.persona_session import PersonaSession
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
    api_instance = persona_sessions_bank_api.PersonaSessionsBankApi(api_client)
    post_persona_session = PostPersonaSession(
        persona_inquiry_id="persona_inquiry_id_example",
        customer_guid="customer_guid_example",
        identity_verification_guid="identity_verification_guid_example",
    ) # PostPersonaSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create Persona Session
        api_response = api_instance.create_persona_session(post_persona_session)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling PersonaSessionsBankApi->create_persona_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_persona_session** | [**PostPersonaSession**](PostPersonaSession.md)|  |

### Return type

[**PersonaSession**](PersonaSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | session created |  -  |
**409** | Inquiry already completed |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | Identity verification not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

