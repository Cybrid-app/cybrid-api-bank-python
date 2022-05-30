# cybrid_api_bank.AssetsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_assets**](AssetsBankApi.md#list_assets) | **GET** /api/assets | Get assets list


# **list_assets**
> AssetList list_assets()

Get assets list

Retrieves a listing of assets.  Required scope: **prices:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import assets_bank_api
from cybrid_api_bank.model.asset_list import AssetList
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.list_request_page import ListRequestPage
from cybrid_api_bank.model.list_request_per_page import ListRequestPerPage
from pprint import pprint
# Defining the host is optional and defaults to https://bank.demo.cybrid.app
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "https://bank.demo.cybrid.app"
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
    host = "https://bank.demo.cybrid.app"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_bank_api.AssetsBankApi(api_client)
    page = ListRequestPage(0) # ListRequestPage | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(10) # ListRequestPerPage | The number of entities per page to return. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get assets list
        api_response = api_instance.list_assets(page=page, per_page=per_page)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling AssetsBankApi->list_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **ListRequestPage**| The page index to retrieve. | [optional]
 **per_page** | **ListRequestPerPage**| The number of entities per page to return. | [optional]

### Return type

[**AssetList**](AssetList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of assets |  -  |
**400** | Invalid requests - Malformed Authentication Header |  -  |
**401** | Unauthorized - Authentication failed, invalid subject |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

