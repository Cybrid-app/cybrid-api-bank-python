# cybrid_api_bank.RewardsBankApi

All URIs are relative to *https://bank.demo.cybrid.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rewards**](RewardsBankApi.md#create_rewards) | **POST** /api/rewards | Create Reward
[**get_reward**](RewardsBankApi.md#get_reward) | **GET** /api/rewards/{reward_guid} | Get Reward
[**list_rewards**](RewardsBankApi.md#list_rewards) | **GET** /api/rewards | Get rewards list


# **create_rewards**
> Reward create_rewards(post_reward)

Create Reward

Creates a reward.  Required scope: **rewards:execute**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import rewards_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.reward import Reward
from cybrid_api_bank.model.post_reward import PostReward
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
    api_instance = rewards_bank_api.RewardsBankApi(api_client)
    post_reward = PostReward(
        customer_guid="customer_guid_example",
        symbol="symbol_example",
        receive_amount=1,
        deliver_amount=1,
    ) # PostReward | 

    # example passing only required values which don't have defaults set
    try:
        # Create Reward
        api_response = api_instance.create_rewards(post_reward)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling RewardsBankApi->create_rewards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_reward** | [**PostReward**](PostReward.md)|  |

### Return type

[**Reward**](Reward.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | reward created |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward**
> Reward get_reward(reward_guid)

Get Reward

Retrieves a reward.  Required scope: **rewards:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import rewards_bank_api
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.reward import Reward
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
    api_instance = rewards_bank_api.RewardsBankApi(api_client)
    reward_guid = "reward_guid_example" # str | Identifier for the reward.

    # example passing only required values which don't have defaults set
    try:
        # Get Reward
        api_response = api_instance.get_reward(reward_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling RewardsBankApi->get_reward: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_guid** | **str**| Identifier for the reward. |

### Return type

[**Reward**](Reward.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reward found |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |
**404** | reward not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rewards**
> RewardList list_rewards()

Get rewards list

Retrieves a listing of rewards.  Required scope: **rewards:read**

### Example

* Bearer (JWT) Authentication (BearerAuth):
* OAuth Authentication (oauth2):

```python
import time
import cybrid_api_bank
from cybrid_api_bank.api import rewards_bank_api
from cybrid_api_bank.model.reward_list import RewardList
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
    api_instance = rewards_bank_api.RewardsBankApi(api_client)
    page = ListRequestPage(0) # int | The page index to retrieve. (optional)
    per_page = ListRequestPerPage(1) # int | The number of entities per page to return. (optional)
    guid = "guid_example" # str | Comma separated reward_guids to list rewards for. (optional)
    bank_guid = "bank_guid_example" # str | Comma separated bank_guids to list rewards for. (optional)
    customer_guid = "customer_guid_example" # str | Comma separated customer_guids to list rewards for. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get rewards list
        api_response = api_instance.list_rewards(page=page, per_page=per_page, guid=guid, bank_guid=bank_guid, customer_guid=customer_guid)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling RewardsBankApi->list_rewards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page index to retrieve. | [optional]
 **per_page** | **int**| The number of entities per page to return. | [optional]
 **guid** | **str**| Comma separated reward_guids to list rewards for. | [optional]
 **bank_guid** | **str**| Comma separated bank_guids to list rewards for. | [optional]
 **customer_guid** | **str**| Comma separated customer_guids to list rewards for. | [optional]

### Return type

[**RewardList**](RewardList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get list of rewards |  -  |
**400** | Invalid requests |  -  |
**401** | Unauthorized - Authentication failed,  |  -  |
**403** | Invalid scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

