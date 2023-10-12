# cybrid_api_bank.IdentityVerificationsBankApi

All URIs are relative to *https://bank.sandbox.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_verification**](IdentityVerificationsBankApi.md#create_identity_verification) | **POST** /api/identity_verifications | Create Identity Verification
[**get_identity_verification**](IdentityVerificationsBankApi.md#get_identity_verification) | **GET** /api/identity_verifications/{identity_verification_guid} | Get Identity Verification
[**list_identity_verifications**](IdentityVerificationsBankApi.md#list_identity_verifications) | **GET** /api/identity_verifications | List Identity Verifications


# **create_identity_verification**
> IdentityVerification create_identity_verification(post_identity_verification)

Create Identity Verification

Creates an Identity Verification.  ## Identity Verifications  Identity Verifications confirm an individual's identity with for the purpose of inclusion on the platform. This know-your-customer (KYC) process is a requirement for individuals to be able to transact. At present, we offer support for Cybrid performing the verification or working with partners to accept their KYC/AML process and have it attested to in our platform.  ## State  | State | Description | |-------|-------------| | storing | The Platform is storing the identity verification details in our private store | | waiting | The Platform is waiting for the customer to complete the identity verification process | | expired | The identity verification process has expired | | completed | The identity verification process has been completed |  ## Outcome  | State | Description | |-------|-------------| | passed | The customer has passed the identity verification process | | failed | The customer has failed the identity verification process |  ## Failure Codes  | Code | Description | |-------|-------------| | id_check_failure | Failure due to an issue verifying the provided ID | | id_quality_check_failure | Failure due to an issue verifying the provided ID based on the image quality | | id_barcode_check_failure | Failure due to an issue verifying the provided ID based on the barcode | | id_expiration_check_failure | Failure due to an issue verifying the provided ID based on the expiration date | | id_double_side_check_failure | Failure due to an issue verifying the provided ID based on both sides not being provided | | id_type_allowed_check_failure | Failure due to an issue verifying the provided ID based on the type provided | | id_country_allowed_check_failure | Failure due to an issue verifying the provided ID based on the issuing country | | database_check_failure | Failure due to an issue verifying the provided information against authoritative data sources | | selfie_failure | Failure due to an issue verifying the provided selfie photo | | duplicate_person_check_failure | Failure due to a customer already existing for this person | | name_check_failure | Failure due to an issue verifying the name of the person | | address_check_failure | Failure due to an issue verifying the address of the person | | dob_check_failure | Failure due to an issue verifying the date of birth of the person | | id_number_check_failure | Failure due to an issue verifying an identification number of the person | | phone_number_check_failure | Failure due to an issue verifying the phone number of the person | | email_address_check_failure | Failure due to an issue verifying the email address of the person | | plaid_failure | Failure due to an issue interacting with Plaid | | decision_timeout | Failure due to an issue verifying the email address of the person | | requested_failure | In sandbox, the caller requested that the process failed |    Required scope: **customers:write**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import identity_verifications_bank_api
from cybrid_api_bank.model.post_identity_verification import PostIdentityVerification
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.identity_verification import IdentityVerification
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
    api_instance = identity_verifications_bank_api.IdentityVerificationsBankApi(api_client)
    post_identity_verification = PostIdentityVerification(
        type="kyc",
        method="id_and_selfie",
        customer_guid="customer_guid_example",
        country_code="country_code_example",
        name=PostIdentityVerificationName(
            first="first_example",
            middle="middle_example",
            last="last_example",
            full="full_example",
        ),
        address=PostIdentityVerificationAddress(
            street="street_example",
            street2="street2_example",
            city="city_example",
            subdivision="subdivision_example",
            postal_code="postal_code_example",
            country_code="country_code_example",
        ),
        date_of_birth=dateutil_parser('1970-01-01').date(),
        phone_number="phone_number_example",
        email_address="email_address_example",
        identification_numbers=[
            PostIdentificationNumber(
                type="drivers_license",
                issuing_country_code="issuing_country_code_example",
                identification_number="identification_number_example",
            ),
        ],
        external_bank_account_guid="external_bank_account_guid_example",
        expected_behaviours=[
            "passed_immediately",
        ],
    ) # PostIdentityVerification | 

    # example passing only required values which don't have defaults set
    try:
        # Create Identity Verification
        api_response = api_instance.create_identity_verification(post_identity_verification)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling IdentityVerificationsBankApi->create_identity_verification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_identity_verification** | [**PostIdentityVerification**](PostIdentityVerification.md)|  |

### Return type

[**IdentityVerification**](IdentityVerification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identity Verification created |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_verification**
> IdentityVerificationWithDetails get_identity_verification(identity_verification_guid)

Get Identity Verification

Retrieves an identity verification.  Required scope: **customers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import identity_verifications_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.identity_verification_with_details import IdentityVerificationWithDetails
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
    api_instance = identity_verifications_bank_api.IdentityVerificationsBankApi(api_client)
    identity_verification_guid = "identity_verification_guid_example" # str | Identifier for the identity verification.

    # example passing only required values which don't have defaults set
    try:
        # Get Identity Verification
        api_response = api_instance.get_identity_verification(identity_verification_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling IdentityVerificationsBankApi->get_identity_verification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_verification_guid** | **str**| Identifier for the identity verification. |

### Return type

[**IdentityVerificationWithDetails**](IdentityVerificationWithDetails.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | identity verification found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | identity_verification not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_verifications**
> IdentityVerificationList list_identity_verifications()

List Identity Verifications

Retrieves a list of identity verifications.  Required scope: **customers:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import identity_verifications_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.identity_verification_list import IdentityVerificationList
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
    api_instance = identity_verifications_bank_api.IdentityVerificationsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated guids to list identity verifications for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list identity verifications for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list identity verifications for. (optional)
    state = "state_example" # str | Comma separated states to list identity verifications for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Identity Verifications
        api_response = api_instance.list_identity_verifications(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid, state=state)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling IdentityVerificationsBankApi->list_identity_verifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated guids to list identity verifications for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list identity verifications for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list identity verifications for. | [optional]
 **state** | **str**| Comma separated states to list identity verifications for. | [optional]

### Return type

[**IdentityVerificationList**](IdentityVerificationList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of identity verifications |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

