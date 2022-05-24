# cybrid-api-bank-python
# Welcome

Welcome to the Cybrid platform; enabling turnkey crypto banking services!

In these documents, you will find information on the operations provided by our platform, as well as details on how our REST API operates more generally.

Our complete set of APIs allows you to manage all your resources: your Organization, your banks and your identities. The complete set of APIs can be found on the following pages:

| API                                                            | Description                  |
|----------------------------------------------------------------|------------------------------|
| [Organization API](https://organization.demo.cybrid.app/api/schema/swagger-ui) | APIs to manage organizations |
| [Bank API](https://bank.demo.cybrid.app/api/schema/swagger-ui)                 | APIs to manage banks         |
| [Identities API](https://id.demo.cybrid.app/api/schema/swagger-ui)                     | APIs to manage identities    |

When you're ready, [request access](https://www.cybrid.xyz/access) to your Dashboard to view and administer your Organization. Once you've logged in, you can begin creating Banks, either for sandbox or production usage, and start enabling your customers to leverage DeFi and web3 with confidence.

If you have any questions, please contact [Support](mailto:support@cybrid.app) at any time so that we can help.

## Authentication

The Cybrid Platform uses OAuth 2.0 Bearer Tokens to authenticate requests to the platform. Credentials to create Organization and Bank tokens can be generated via your Dashboard ([request access](https://www.cybrid.xyz/access)).

An Organization Token applies broadly to the whole Organization and all of its Banks, whereas, a Bank Token is specific to an individual Bank.

Both Organization and Bank tokens can be created using the OAuth Client Credential Grant flow. Each Organization and Bank has its own unique Client ID and Secret that allows for machine-to-machine authentication.

**Never share your Client ID or Secret publicly or in your source code repository**

Your Client ID and Secret can be exchanged for a time-limited Bearer Token by interacting with the Cybrid Identity Provider or through interacting with the **Authorize** button in this document:

```
curl -X POST https://id.demo.cybrid.app/oauth/token -d '{
    \"grant_type\": \"client_credentials\",
    \"client_id\": \"<Your Client ID>\",
    \"client_secret\": \"<Your Secret>\",
    \"scope\": \"<Your requested scopes -- space separated>\"
  }' -H \"Content-Type: application/json\"
```

## Scopes

The Cybrid platform supports the use of scopes to control the level of access a token is limited to. Scopes do not grant access to resources; instead, they provide limits, in support of the least privilege principal.

The following scopes are available on the platform and can be requested when generating either an Organization or a Bank token. Generally speaking, the _Read_ scope is required to read and list resources, the _Write_ scope is required to update a resource and the _Execute_ scope is required to create a resource.

| Resource      | Read scope         | Write scope          | Execute scope     | Token Type         |
|---------------|--------------------|----------------------|-------------------|--------------------|
| Organizations | organizations:read | organizations:write  |                   | Organization/ Bank |
| Banks         | banks:read         | banks:write          | banks:execute     | Organization/ Bank |
| Customers     | customers:read     | customers:write      | customers:execute | Bank               |
| Assets        | prices:read        |                      |                   | Bank               |
| Accounts      | accounts:read      |                      | accounts:execute  | Bank               |
| Prices        | prices:read        |                      |                   | Bank               |
| Symbols       | prices:read        |                      |                   | Bank               |
| Quotes        | quotes:read        |                      | quotes:execute    | Bank               |
| Trades        | trades:read        |                      | trades:execute    | Bank               |

## Organizations

An Organization is meant to model the organization partnering with Cybrid to use our platform.

An Organization does not directly interact with customers. Instead, an Organization has one or more banks, which encompass the financial service offerings of the platform.

## Banks

A Bank is owned by an Organization and can be thought of as an environment or container for Customers and product offerings. An example of a Bank would be your customer facing banking website, or an internal staging environment for testing and integration.

An Organization can have multiple banks, in sandbox or production environments. A sandbox Bank will be backed by stubbed data and process flows. For instance, identity record and funding source processes will be simulated rather than performed.

## Customers

Customers represent your banking users on the platform. At present, we offer support for Individuals as Customers.

Customers must be verified in our system before they can play any part on the platform. See the Identity Records section for more details on how a customer can be verified.

Customers must also have an account to be able to transact. See the Accounts APIs for more details on setting up accounts for the customer.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.14.7
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cybrid_api_bank
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cybrid_api_bank
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cybrid_api_bank
from pprint import pprint
from cybrid_api_bank.api import accounts_bank_api
from cybrid_api_bank.model.account import Account
from cybrid_api_bank.model.account_list import AccountList
from cybrid_api_bank.model.list_request_page import ListRequestPage
from cybrid_api_bank.model.list_request_per_page import ListRequestPerPage
from cybrid_api_bank.model.post_account import PostAccount
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
    api_instance = accounts_bank_api.AccountsBankApi(api_client)
    post_account = PostAccount(
        type="trading",
        customer_guid="customer_guid_example",
        asset="asset_example",
        name="name_example",
    ) # PostAccount | 

    try:
        # Create Account
        api_response = api_instance.create_account(post_account)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling AccountsBankApi->create_account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://bank.demo.cybrid.app*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsBankApi* | [**create_account**](docs/AccountsBankApi.md#create_account) | **POST** /api/accounts | Create Account
*AccountsBankApi* | [**get_account**](docs/AccountsBankApi.md#get_account) | **GET** /api/accounts/{account_guid} | Get Account
*AccountsBankApi* | [**list_accounts**](docs/AccountsBankApi.md#list_accounts) | **GET** /api/accounts | List Accounts
*AssetsBankApi* | [**list_assets**](docs/AssetsBankApi.md#list_assets) | **GET** /api/assets | Get assets list
*BanksBankApi* | [**create_bank**](docs/BanksBankApi.md#create_bank) | **POST** /api/banks | Create Bank
*BanksBankApi* | [**get_bank**](docs/BanksBankApi.md#get_bank) | **GET** /api/banks/{bank_guid} | Get Bank
*BanksBankApi* | [**list_banks**](docs/BanksBankApi.md#list_banks) | **GET** /api/banks | Get banks list
*CustomersBankApi* | [**create_customer**](docs/CustomersBankApi.md#create_customer) | **POST** /api/customers | Create Customer
*CustomersBankApi* | [**get_customer**](docs/CustomersBankApi.md#get_customer) | **GET** /api/customers/{customer_guid} | Get Customer
*CustomersBankApi* | [**list_customers**](docs/CustomersBankApi.md#list_customers) | **GET** /api/customers | Get customers list
*IdentityRecordsBankApi* | [**create_identity_record**](docs/IdentityRecordsBankApi.md#create_identity_record) | **POST** /api/identity_records | Create Identity Record
*IdentityRecordsBankApi* | [**get_identity_record**](docs/IdentityRecordsBankApi.md#get_identity_record) | **GET** /api/identity_records/{identity_record_guid} | Get Identity Record
*IdentityRecordsBankApi* | [**list_identity_records**](docs/IdentityRecordsBankApi.md#list_identity_records) | **GET** /api/identity_records | List Identity Records
*PricesBankApi* | [**list_prices**](docs/PricesBankApi.md#list_prices) | **GET** /api/prices | Get Price
*QuotesBankApi* | [**create_quote**](docs/QuotesBankApi.md#create_quote) | **POST** /api/quotes | Create Quote
*QuotesBankApi* | [**get_quote**](docs/QuotesBankApi.md#get_quote) | **GET** /api/quotes/{quote_guid} | Get Quote
*QuotesBankApi* | [**list_quotes**](docs/QuotesBankApi.md#list_quotes) | **GET** /api/quotes | Get quotes list
*SymbolsBankApi* | [**list_symbols**](docs/SymbolsBankApi.md#list_symbols) | **GET** /api/symbols | Get Symbols list
*TradesBankApi* | [**create_trade**](docs/TradesBankApi.md#create_trade) | **POST** /api/trades | Create Trade
*TradesBankApi* | [**get_trade**](docs/TradesBankApi.md#get_trade) | **GET** /api/trades/{trade_guid} | Get Trade
*TradesBankApi* | [**list_trades**](docs/TradesBankApi.md#list_trades) | **GET** /api/trades | Get trades list
*TradingConfigurationsBankApi* | [**create_trading_configuration**](docs/TradingConfigurationsBankApi.md#create_trading_configuration) | **POST** /api/trading_configurations | Create TradingConfiguration
*TradingConfigurationsBankApi* | [**get_trading_configuration**](docs/TradingConfigurationsBankApi.md#get_trading_configuration) | **GET** /api/trading_configurations/{trading_configuration_guid} | Get TradingConfiguration
*TradingConfigurationsBankApi* | [**list_trading_configurations**](docs/TradingConfigurationsBankApi.md#list_trading_configurations) | **GET** /api/trading_configurations | List trading configurations
*VerificationKeysBankApi* | [**create_verification_key**](docs/VerificationKeysBankApi.md#create_verification_key) | **POST** /api/bank_verification_keys | Create VerificationKey
*VerificationKeysBankApi* | [**get_verification_key**](docs/VerificationKeysBankApi.md#get_verification_key) | **GET** /api/bank_verification_keys/{verification_key_guid} | Get VerificationKey
*VerificationKeysBankApi* | [**list_verification_keys**](docs/VerificationKeysBankApi.md#list_verification_keys) | **GET** /api/bank_verification_keys | Get Verification Keys list


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountList](docs/AccountList.md)
 - [Asset](docs/Asset.md)
 - [AssetList](docs/AssetList.md)
 - [AttestationDetails](docs/AttestationDetails.md)
 - [Bank](docs/Bank.md)
 - [BankList](docs/BankList.md)
 - [Customer](docs/Customer.md)
 - [CustomerList](docs/CustomerList.md)
 - [CybridAccount](docs/CybridAccount.md)
 - [Exchange](docs/Exchange.md)
 - [ExchangeAccount](docs/ExchangeAccount.md)
 - [Fee](docs/Fee.md)
 - [IdentityRecord](docs/IdentityRecord.md)
 - [IdentityRecordList](docs/IdentityRecordList.md)
 - [ListRequestPage](docs/ListRequestPage.md)
 - [ListRequestPerPage](docs/ListRequestPerPage.md)
 - [PostAccount](docs/PostAccount.md)
 - [PostBank](docs/PostBank.md)
 - [PostCustomer](docs/PostCustomer.md)
 - [PostFee](docs/PostFee.md)
 - [PostIdentityRecord](docs/PostIdentityRecord.md)
 - [PostIdentityRecordAttestationDetails](docs/PostIdentityRecordAttestationDetails.md)
 - [PostQuote](docs/PostQuote.md)
 - [PostTrade](docs/PostTrade.md)
 - [PostTradingConfiguration](docs/PostTradingConfiguration.md)
 - [PostVerificationKey](docs/PostVerificationKey.md)
 - [Quote](docs/Quote.md)
 - [QuoteList](docs/QuoteList.md)
 - [SymbolPrice](docs/SymbolPrice.md)
 - [SymbolPriceResponse](docs/SymbolPriceResponse.md)
 - [Symbols](docs/Symbols.md)
 - [SystemAccount](docs/SystemAccount.md)
 - [Trade](docs/Trade.md)
 - [TradeList](docs/TradeList.md)
 - [TradingConfiguration](docs/TradingConfiguration.md)
 - [TradingConfigurationList](docs/TradingConfigurationList.md)
 - [VerificationKey](docs/VerificationKey.md)
 - [VerificationKeyList](docs/VerificationKeyList.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication (JWT)


## oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **banks:read**: banks read
 - **banks:write**: banks write
 - **accounts:read**: accounts read
 - **accounts:execute**: accounts execute
 - **customers:read**: customers read
 - **customers:write**: customers write
 - **customers:execute**: customers execute
 - **prices:read**: prices read
 - **quotes:execute**: quotes execute
 - **quotes:read**: quotes read
 - **trades:execute**: trades execute
 - **trades:read**: trades read


## Author

support@cybrid.app


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in cybrid_api_bank.apis and cybrid_api_bank.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from cybrid_api_bank.api.default_api import DefaultApi`
- `from cybrid_api_bank.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import cybrid_api_bank
from cybrid_api_bank.apis import *
from cybrid_api_bank.models import *
```

