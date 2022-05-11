# cybrid_api_bank.VerificationKeysBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_verification_key**](VerificationKeysBankApi.md#create_verification_key) | **POST** /api/bank_verification_keys | Create VerificationKey
[**get_verification_key**](VerificationKeysBankApi.md#get_verification_key) | **GET** /api/bank_verification_keys/{verification_key_guid} | Get VerificationKey
[**list_verification_keys**](VerificationKeysBankApi.md#list_verification_keys) | **GET** /api/bank_verification_keys | Get Verification Keys list


# **create_verification_key**
> VerificationKey create_verification_key(post_verification_key)

Create VerificationKey

Creates a verification key.   Example code (python) for generating a Verification Key  ```python import base64  from cryptography.hazmat.primitives import hashes from cryptography.hazmat.primitives import serialization from cryptography.hazmat.primitives.asymmetric import padding from cryptography.hazmat.primitives.asymmetric import rsa  nonce = \"wen moon\" private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048) signature = base64.b64encode(private_key.sign(     data=nonce.encode('ascii'), padding=padding.PKCS1v15(), algorithm=hashes.SHA512())).decode('ascii') public_key = base64.b64encode(private_key.public_key().public_bytes(     encoding=serialization.Encoding.DER, format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode('ascii') ````  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the verification in our private key store | | pending | The Platform is verifying the verification key's signature | | verified | The Platform has verified the verification key's signature and the key can be used | | failed | The Platform was not able to verify the verification key's signature and the key cannot be used |    Required scope: **banks:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import verification_keys_bank_api
from cybrid_api_bank.model.verification_key import VerificationKey
from cybrid_api_bank.model.post_verification_key import PostVerificationKey
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
    api_instance = verification_keys_bank_api.VerificationKeysBankApi(api_client)
    post_verification_key = PostVerificationKey(
        type="attestation",
        algorithm="RS512",
        public_key="public_key_example",
        nonce="nonce_example",
        signature="signature_example",
    ) # PostVerificationKey | 

    # example passing only required values which don't have defaults set
    try:
        # Create VerificationKey
        api_response = api_instance.create_verification_key(post_verification_key)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling VerificationKeysBankApi->create_verification_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_verification_key** | [**PostVerificationKey**](PostVerificationKey.md)|  |

### Return type

[**VerificationKey**](VerificationKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | verification key created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verification_key**
> VerificationKey get_verification_key(verification_key_guid)

Get VerificationKey

Retrieves a verification key.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import verification_keys_bank_api
from cybrid_api_bank.model.verification_key import VerificationKey
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
    api_instance = verification_keys_bank_api.VerificationKeysBankApi(api_client)
    verification_key_guid = "verification_key_guid_example" # str | Identifier for the verification key.

    # example passing only required values which don't have defaults set
    try:
        # Get VerificationKey
        api_response = api_instance.get_verification_key(verification_key_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling VerificationKeysBankApi->get_verification_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_key_guid** | **str**| Identifier for the verification key. |

### Return type

[**VerificationKey**](VerificationKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification Key found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_verification_keys**
> VerificationKeyList list_verification_keys()

Get Verification Keys list

Retrieves a listing of verification keys of a bank.  Required scope: **banks:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import verification_keys_bank_api
from cybrid_api_bank.model.verification_key_list import VerificationKeyList
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
    api_instance = verification_keys_bank_api.VerificationKeysBankApi(api_client)
    page = ListRequestPage(0) # ListRequestPage |  (optional)
    per_page = ListRequestPerPage(10) # ListRequestPerPage |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Verification Keys list
        api_response = api_instance.list_verification_keys(page=page, per_page=per_page)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling VerificationKeysBankApi->list_verification_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **ListRequestPage**|  | [optional]
 **per_page** | **ListRequestPerPage**|  | [optional]

### Return type

[**VerificationKeyList**](VerificationKeyList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of verification keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

