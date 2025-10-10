# cybrid_api_bank.AssetsBankApi

All URIs are relative to *http://api-platform-bank.local.cybrid.com:3002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_assets**](AssetsBankApi.md#list_assets) | **GET** /api/assets | Get assets list


# **list_assets**
> AssetList list_assets()

Get assets list

Retrieves a listing of assets.

### Example


```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import assets_bank_api
from cybrid_api_bank.model.asset_list import AssetList
from pprint import pprint
# Defining the host is optional and defaults to http://api-platform-bank.local.cybrid.com:3002
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "http://api-platform-bank.local.cybrid.com:3002"
)


# Enter a context with an instance of the API client
with cybrid_api_bank.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_bank_api.AssetsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    code = "code_example" # str | Comma separated codes to list assets for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get assets list
        api_response = api_instance.list_assets(page=page, per_page=per_page, code=code)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling AssetsBankApi->list_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **code** | **str**| Comma separated codes to list assets for. | [optional]

### Return type

[**AssetList**](AssetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

