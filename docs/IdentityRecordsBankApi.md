# cybrid_api_bank.IdentityRecordsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_record**](IdentityRecordsBankApi.md#create_identity_record) | **POST** /api/identity_records | Create Identity Record
[**get_identity_record**](IdentityRecordsBankApi.md#get_identity_record) | **GET** /api/identity_records/{identity_record_guid} | Get Identity Record
[**list_identity_records**](IdentityRecordsBankApi.md#list_identity_records) | **GET** /api/identity_records | List Identity Records


# **create_identity_record**
> IdentityRecord create_identity_record(post_identity_record)

Create Identity Record

Creates an identity record.  ## Identity Records  Identity Records verify an individual for inclusion on the platform. This know-your-customer (KYC) process is a requirement for individuals to be able to transact. At present, we offer support for Attestation Identity Records.  Once an Identity Record has been submitted, it will be reviewed by our system and transit through a lifecycle before ultimately being `verified` or `failed`. If an Identity Record is ends up `failed`, contextual information as to the reason may be provided on the resource and additional attempts can be made.  ## Attestation Identity Records  An Attestation Identity Record is a confirmation of fact that the Organization has completed their own KYC process and can vouch for its correctness.  Prior to uploading `verified` attestation identity records, an Organization must register their signing public key with their Bank through the create Verification Key API.  To create an attestation identity record, a signed JWT is required as proof that the Customer's identity has been verified by the Organization. When creating the JWT, the Organization must use the RS512 signing algorithm.  The JWT must contain the following headers:  - **alg**: The RS512 algorithm value, e.g., 'RS512'. - **kid**: Set to the guid of the verification key that has been registered for the Bank  The JWT must contain the following claims:  - **iss**: Set to http://api.cybrid.app/banks/{bank_guid} - **aud**: Set to http://api.cybrid.app - **sub**: Set to http://api.cybrid.app/customers/{customer_guid} - **iat**: Set to the time at which the JWT was issued - **exp**: Set to the time after which the JWT expires - **jti**: Set to a unique identifier for the JWT  Example code (python) for generating an Attestation Identity Record JWT token:  ```python # Assumes an RSA private key has been generated (`private_key`), a Verification Key has been created and a `verification_key_guid` is available. # # `customer_guid` should be set to the guid assigned to a Customer that has been created. # `bank_guid` should be set to the guid of your bank #  import uuid  from datetime import datetime, timezone, timedelta from jwcrypto import jwt, jwk from cryptography.hazmat.primitives import serialization from cryptography.hazmat.primitives.serialization import load_pem_private_key  algorithm = 'RS512' issued_at = datetime.now(timezone.utc) expired_at = issued_at + timedelta(days=365)  with open(\"verification_key.pem\", 'rb') as pem_in:   pem_lines = pem_in.read()  private_key = load_pem_private_key(pem_lines, None)  ### DISCLAIMER:- Since NO ENCRYPTION is used in the key storage/formatting. Please DO NOT use this code in production environment. signing_key = jwk.JWK.from_pem(     private_key.private_bytes(         encoding=serialization.Encoding.PEM,         format=serialization.PrivateFormat.PKCS8,         encryption_algorithm=serialization.NoEncryption()     ) ) signing_key.update({\"kid\": verification_key_guid})  attestation_jwt = jwt.JWT(     header={         \"alg\": algorithm,         \"kid\": verification_key_guid     },     claims={         \"iss\": f\"http://api.cybrid.app/banks/{bank_guid}\",         \"aud\": \"http://api.cybrid.app\",         \"sub\": f\"http://api.cybrid.app/customers/{customer_guid}\",         \"iat\": int(issued_at.timestamp()),         \"exp\": int(expired_at.timestamp()),         \"jti\": str(uuid.uuid4())     },     key=signing_key,     algs=[algorithm] ) attestation_jwt.make_signed_token(signing_key)  token = attestation_jwt.serialize(compact=True) print(\"Token is : \", token) ```  ## Attestation State  | State | Description | |-------|-------------| | storing | The Platform is storing the attestation in our private store | | pending | The Platform is verifying the attestation's JWT | | verified | The Platform has verified the attestation and the customer is able to transact | | failed | The Platform was not able to verify the attestation and the customer is not able to transact |    Required scope: **customers:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import identity_records_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.identity_record import IdentityRecord
from cybrid_api_bank.model.post_identity_record import PostIdentityRecord
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
    api_instance = identity_records_bank_api.IdentityRecordsBankApi(api_client)
    post_identity_record = PostIdentityRecord(
        customer_guid="customer_guid_example",
        type="attestation",
        attestation_details=PostIdentityRecordAttestationDetails(
            token="token_example",
        ),
    ) # PostIdentityRecord | 

    # example passing only required values which don't have defaults set
    try:
        # Create Identity Record
        api_response = api_instance.create_identity_record(post_identity_record)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling IdentityRecordsBankApi->create_identity_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_identity_record** | [**PostIdentityRecord**](PostIdentityRecord.md)|  |

### Return type

[**IdentityRecord**](IdentityRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identity Record created |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed, |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_record**
> IdentityRecord get_identity_record(identity_record_guid)

Get Identity Record

Retrieves an identity record.  Required scope: **customers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import identity_records_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.identity_record import IdentityRecord
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
    api_instance = identity_records_bank_api.IdentityRecordsBankApi(api_client)
    identity_record_guid = "identity_record_guid_example" # str | Identifier for the identity record.

    # example passing only required values which don't have defaults set
    try:
        # Get Identity Record
        api_response = api_instance.get_identity_record(identity_record_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling IdentityRecordsBankApi->get_identity_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_record_guid** | **str**| Identifier for the identity record. |

### Return type

[**IdentityRecord**](IdentityRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identity Record found |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | identity record not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_records**
> IdentityRecordList list_identity_records()

List Identity Records

Retrieves a listing of identity records for a bank.  Required scope: **customers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import identity_records_bank_api
from cybrid_api_bank.model.identity_record_list import IdentityRecordList
from cybrid_api_bank.model.error_response import ErrorResponse
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
    api_instance = identity_records_bank_api.IdentityRecordsBankApi(api_client)
    customer_guid = "customer_guid_example" # str | Comma separated customer identifier to list identity records for. (optional)
    page = ListRequestPage(0) # int |  (optional)
    per_page = ListRequestPerPage(1) # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Identity Records
        api_response = api_instance.list_identity_records(customer_guid=customer_guid, page=page, per_page=per_page)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling IdentityRecordsBankApi->list_identity_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_guid** | **str**| Comma separated customer identifier to list identity records for. | [optional]
 **page** | **int**|  | [optional]
 **per_page** | **int**|  | [optional]

### Return type

[**IdentityRecordList**](IdentityRecordList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of identity records |  -  |
**400** | Invalid requests - malformed authentication header |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

