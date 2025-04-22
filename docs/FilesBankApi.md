# cybrid_api_bank.FilesBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesBankApi.md#create_file) | **POST** /api/files | Create File
[**get_file**](FilesBankApi.md#get_file) | **GET** /api/files/{file_guid} | Get File
[**list_files**](FilesBankApi.md#list_files) | **GET** /api/files | List Files


# **create_file**
> PlatformFile create_file(post_file)

Create File

Creates a file.  #### This feature is currently in preview mode and is not yet available for partner use.  ## Data  The attribute contains the base64 encoded file content. The value needs to be smaller than 10MB otherwise the Platform will reject the request. To upload files larger than 10MB do not provide the content and use the returned upload URL to provide the file.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the file in our private store | | completed | The Platform has completed storing the file | | failed | The Platform failed to store the file |    Required scope: **files:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import files_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.platform_file import PlatformFile
from cybrid_api_bank.model.post_file import PostFile
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
    api_instance = files_bank_api.FilesBankApi(api_client)
    post_file = PostFile(
        type="drivers_license_front",
        customer_guid="customer_guid_example",
        filename="filename_example",
        content_type="image/jpeg",
        data="data_example",
    ) # PostFile | 

    # example passing only required values which don't have defaults set
    try:
        # Create File
        api_response = api_instance.create_file(post_file)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FilesBankApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_file** | [**PostFile**](PostFile.md)|  |

### Return type

[**PlatformFile**](PlatformFile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | file created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> PlatformFile get_file(file_guid)

Get File

Retrieves a file.  Required scope: **files:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import files_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.platform_file import PlatformFile
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
    api_instance = files_bank_api.FilesBankApi(api_client)
    file_guid = "file_guid_example" # str | Identifier for the file.
    include_download_url = "include_download_url_example" # str | Include download information in response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get File
        api_response = api_instance.get_file(file_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FilesBankApi->get_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get File
        api_response = api_instance.get_file(file_guid, include_download_url=include_download_url)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FilesBankApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_guid** | **str**| Identifier for the file. |
 **include_download_url** | **str**| Include download information in response. | [optional]

### Return type

[**PlatformFile**](PlatformFile.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | file found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | file not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> PlatformFileList list_files()

List Files

Retrieves a list of files.  Required scope: **files:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import files_bank_api
from cybrid_api_bank.model.platform_file_list import PlatformFileList
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
    api_instance = files_bank_api.FilesBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated file_guids to list files for. (optional)
    type = "type_example" # str | Comma separated file types to list files for. (optional)
    state = "state_example" # str | Comma separated file states to list files for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list files for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list files for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Files
        api_response = api_instance.list_files(page=page, per_page=per_page, guid=guid, type=type, state=state, bank_guid=bank_guid, customer_guid=customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling FilesBankApi->list_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated file_guids to list files for. | [optional]
 **type** | **str**| Comma separated file types to list files for. | [optional]
 **state** | **str**| Comma separated file states to list files for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list files for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list files for. | [optional]

### Return type

[**PlatformFileList**](PlatformFileList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of files |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

