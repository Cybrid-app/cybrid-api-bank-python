# cybrid-api-bank-python
# Cybrid API documentation

Welcome to Cybrid, an all-in-one crypto platform that enables you to easily **build** and **launch** white-label crypto products or services.

In these documents, you'll find details on how our REST API operates and generally how our platform functions.

If you're looking for our UI SDK Widgets for Web or Mobile (iOS/Android), generated API clients, or demo applications, head over to our [Github repo](https://github.com/Cybrid-app).

💡 We recommend bookmarking the [Cybrid LinkTree](https://linktr.ee/cybridtechnologies) which contains many helpful links to platform resources.

## Getting Started

This is Cybrid's public interactive API documentation, which allows you to fully test our APIs. If you'd like to use a different tool to exercise our APIs, you can download the [Open API 3.0 yaml](https://bank.demo.cybrid.app/api/schema/v1/swagger.yaml) for import.

If you're new to our APIs and the Cybrid Platform, follow the below guides to get set up and familiar with the platform:

1. [Getting Started in the Cybrid Sandbox](https://www.cybrid.xyz/guides/getting-started)
2. [Getting Ready for Trading](https://www.cybrid.xyz/guides/getting-ready-for-trading)
3. [Running the Web Demo App](https://www.cybrid.xyz/guides/running-the-cybrid-web-demo-crypto-app) (or, alternatively, [Testing with Hosted Web Demo App](https://www.cybrid.xyz/guides/testing-with-the-web-demo-crypo-app))

In [Getting Started in the Cybrid Sandbox](https://www.cybrid.xyz/guides/getting-started), we walk you through how to use the [Cybrid Sandbox](https://id.demo.cybrid.app/) to create a test bank, generate API keys, and set banks fees. In [Getting Ready for Trading](https://www.cybrid.xyz/guides/getting-ready-for-trading), we walk through creating customers, customer identities, accounts, as well as executing quotes and trades.

If you've already run through the first two guides, you can follow the [Running the Web Demo App](https://www.cybrid.xyz/guides/running-the-cybrid-web-demo-crypto-app) guide to test our web SDK with your sandbox `bank` and `customer`.

## Working with the Cybrid Platform

There are three primary ways you can interact with the Cybrid platform:

1. Directly via our RESTful API (this documentation)
2. Using our API clients available in a variety of languages ([Angular](https://github.com/Cybrid-app/cybrid-api-bank-angular), [Java](https://github.com/Cybrid-app/cybrid-api-bank-java), [Kotlin](https://github.com/Cybrid-app/cybrid-api-bank-kotlin), [Python](https://github.com/Cybrid-app/cybrid-api-bank-python), [Ruby](https://github.com/Cybrid-app/cybrid-api-bank-ruby), [Swift](https://github.com/Cybrid-app/cybrid-api-bank-swift) or [Typescript](https://github.com/Cybrid-app/cybrid-api-bank-typescript))
3. Integrating a platform specific SDK ([Web](https://github.com/Cybrid-app/cybrid-sdk-web), [Android](https://github.com/Cybrid-app/cybrid-sdk-android), [iOS](https://github.com/Cybrid-app/cybrid-sdk-ios))

Our complete set of APIs allows you to manage resources across three distinct areas: your `Organization`, your `Banks` and your `Identities`. For most of your testing and interaction you'll be using the `Bank` API, which is where the majority of APIs reside.

*The complete set of APIs can be found on the following pages:*

| API                                                              | Description                                                 |
|------------------------------------------------------------------|-------------------------------------------------------------|
| [Organization API](https://organization.demo.cybrid.app/api/schema/swagger-ui)   | APIs to manage organizations                                |
| [Bank API](https://bank.demo.cybrid.app/api/schema/swagger-ui)                   | APIs to manage banks (and all downstream customer activity) |
| [Identities API](https://id.demo.cybrid.app/api/schema/swagger-ui)                       | APIs to manage organization and bank identities             |

For questions please contact [Support](mailto:support@cybrid.xyz) at any time for assistance, or contact the [Product Team](mailto:product@cybrid.xyz) for product suggestions.

## Authenticating with the API

The Cybrid Platform uses OAuth 2.0 Bearer Tokens to authenticate requests to the platform. Credentials to create `Organization` and `Bank` tokens can be generated via the [Cybrid Sandbox](https://id.demo.cybrid.app). Access tokens can be generated for a `Customer` as well via the [Cybrid IdP](https://id.demo.cybrid.app) as well.

An `Organization` access token applies broadly to the whole Organization and all of its `Banks`, whereas, a `Bank` access token is specific to an individual Bank. `Customer` tokens, similarly, are scoped to a specific customer in a bank.

Both `Organization` and `Bank` tokens can be created using the OAuth Client Credential Grant flow. Each Organization and Bank has its own unique `Client ID` and `Secret` that allows for machine-to-machine authentication.

A `Bank` can then generate `Customer` access tokens via API using our [Identities API](https://id.demo.cybrid.app/api/schema/swagger-ui).

<font color=\"orange\">**⚠️ Never share your Client ID or Secret publicly or in your source code repository.**</font>

Your `Client ID` and `Secret` can be exchanged for a time-limited `Bearer Token` by interacting with the Cybrid Identity Provider or through interacting with the **Authorize** button in this document.

The following curl command can be used to quickly generate a `Bearer Token` for use in testing the API or demo applications.

```
# Example request when using Bank credentials
curl -X POST https://id.demo.cybrid.app/oauth/token -d '{
    \"grant_type\": \"client_credentials\",
    \"client_id\": \"<Your Client ID>\",
    \"client_secret\": \"<Your Secret>\",
    \"scope\": \"banks:read banks:write accounts:read accounts:execute customers:read customers:write customers:execute prices:read quotes:execute quotes:read trades:execute trades:read transfers:execute transfers:read rewards:execute rewards:read external_bank_accounts:read external_bank_accounts:write external_bank_accounts:execute workflows:read workflows:execute deposit_addresses:read deposit_addresses:execute\"
  }' -H \"Content-Type: application/json\"

# When using Organization credentials set `scope` to 'organizations:read organizations:write banks:read banks:write banks:execute customers:read accounts:read quotes:read trades:read transfers:read external_bank_accounts:read workflows:read deposit_addresses:read'
```
<font color=\"orange\">**⚠️ Note: The above curl will create a bearer token with full scope access. Delete scopes if you'd like to restrict access.**</font>

## Authentication Scopes

The Cybrid platform supports the use of scopes to control the level of access a token is limited to. Scopes do not grant access to resources; instead, they provide limits, in support of the least privilege principal.

The following scopes are available on the platform and can be requested when generating either an Organization, Bank or Customer token. Generally speaking, the _Read_ scope is required to read and list resources, the _Write_ scope is required to update a resource and the _Execute_ scope is required to create a resource.

| Resource              | Read scope (Token Type)                                    | Write scope (Token Type)                      | Execute scope (Token Type)                      |
|-----------------------|------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------|
| Account               | accounts:read (Organization, Bank, Customer)               |                                               | accounts:execute (Bank, Customer)               |
| Bank                  | banks:read (Organization, Bank)                            | banks:write (Organization, Bank)              | banks:execute (Organization)                    |
| Customer              | customers:read (Organization, Bank, Customer)              | customers:write (Bank, Customer)              | customers:execute (Bank)                        |
| Deposit Address       | deposit_addresses:read (Organization, Bank, Customer)      | deposit_addresses:write (Bank, Customer)      | deposit_addresses:execute (Bank, Customer)      |
| External Bank Account | external_bank_accounts:read (Organization, Bank, Customer) | external_bank_accounts:write (Bank, Customer) | external_bank_accounts:execute (Bank, Customer) |
| Organization          | organizations:read (Organization)                          | organizations:write (Organization)            |                                                 |
| Price                 | prices:read (Bank, Customer)                               |                                               |                                                 |
| Quote                 | quotes:read (Organization, Bank, Customer)                 |                                               | quotes:execute (Bank, Customer)                 |
| Reward                | rewards:read (Bank, Customer)                              |                                               | rewards:execute (Bank)                          |
| Trade                 | trades:read (Organization, Bank, Customer)                 |                                               | trades:execute (Bank, Customer)                 |
| Transfer              | transfers:read (Organization, Bank, Customer)              |                                               | transfers:execute (Bank, Customer)              |
| Workflow              | workflows:read (Organization, Bank, Customer)              |                                               | workflows:execute (Bank, Customer)              |

## Available Endpoints

The available APIs for the [Identity](https://id.demo.cybrid.app/api/schema/swagger-ui), [Organization](https://organization.demo.cybrid.app/api/schema/swagger-ui) and [Bank](https://bank.demo.cybrid.app/api/schema/swagger-ui) API services are listed below:

| API Service  | Model                | API Endpoint Path              | Description                                                                                       |
|--------------|----------------------|--------------------------------|---------------------------------------------------------------------------------------------------|
| Identity     | Bank                 | /api/bank_applications         | Create and list banks                                                                             |
| Identity     | CustomerToken        | /api/customer_tokens           | Create customer JWT access tokens                                                                 |
| Identity     | Organization         | /api/organization_applications | Create and list organizations                                                                     |
| Organization | Organization         | /api/organizations             | APIs to retrieve and update organization name                                                     |
| Bank         | Account              | /api/accounts                  | Create and list accounts, which hold a specific asset for a customers                             |
| Bank         | Asset                | /api/assets                    | Get a list of assets supported by the platform (ex: BTC, ETH)                                     |
| Bank         | Bank                 | /api/banks                     | Create, update and list banks, the parent to customers, accounts, etc                             |
| Bank         | BankVerificationKey  | /api/bank_verification_keys    | Create, list and retrive verification keys, used for signing identities                           |
| Bank         | Customer             | /api/customers                 | Create and list customers                                                                         |
| Bank         | DepositAddress       | /api/deposit_addresses         | Create, get and list deposit addresses                                                            |
| Bank         | ExternalBankAccount  | /api/external_bank_accounts    | Create, get and list external bank accounts, which connect customer bank accounts to the platform |
| Bank         | FeeConfiguration     | /api/fee_configurations        | Create and list bank fees (spread or fixed)                                                       |
| Bank         | IdentityRecord       | /api/identity_records          | Create and list identity records, which are attached to customers for KYC                         |
| Bank         | IdentityVerification | /api/identity_verifications    | Create and list identity verifications, which are performed on customers for KYC                  |
| Bank         | Price                | /api/prices                    | Get the current prices for assets on the platform                                                 |
| Bank         | Quote                | /api/quotes                    | Create and list quotes, which are required to execute trades                                      |
| Bank         | Reward               | /api/rewards                   | Create a new reward (automates quote/trade for simplicity)                                        |
| Bank         | Symbol               | /api/symbols                   | Get a list of symbols supported for trade (ex: BTC-USD)                                           |
| Bank         | Trade                | /api/trades                    | Create and list trades, which buy or sell cryptocurrency                                          |
| Bank         | Transfer             | /api/transfers                 | Create, get and list transfers (e.g., funding, book)                                              |
| Bank         | Workflow             | /api/workflows                 | Create, get and list workflows                                                                    |

## Understanding Object Models & Endpoints

**Organizations**

An `Organization` is meant to represent the organization partnering with Cybrid to use our platform.

An `Organization` does not directly interact with `customers`. Instead, an Organization has one or more `banks`, which encompass the financial service offerings of the platform.

**Banks**

A `Bank` is owned by an `Organization` and can be thought of as an environment or container for `customers` and product offerings. Banks are created in either `Sandbox` or `Production` mode, where `Sandbox` is the environment that you would test, prototype and build in prior to moving to `Production`.

An `Organization` can have multiple `banks`, in either `Sandbox` or `Production` environments. A `Sandbox Bank` will be backed by stubbed data and process flows. For instance, funding source transfer processes as well as trades will be simulated rather than performed, however asset prices are representative of real-world values. You have an unlimited amount of simulated fiat currency for testing purposes.

**Customers**

`Customers` represent your banking users on the platform. At present, we offer support for `Individuals` as Customers.

`Customers` must be verified (i.e., KYC'd) in our system before they can play any part on the platform, which means they must have an associated and valid `Identity Record`. See the Identity Records section for more details on how a customer can be verified.

`Customers` must also have an `Account` to be able to transact, in the desired asset class. See the Accounts APIs for more details on setting up accounts for the customer.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.62.24
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
from cybrid_api_bank.model.error_response import ErrorResponse
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
*BanksBankApi* | [**update_bank**](docs/BanksBankApi.md#update_bank) | **PATCH** /api/banks/{bank_guid} | Patch Bank
*CustomersBankApi* | [**create_customer**](docs/CustomersBankApi.md#create_customer) | **POST** /api/customers | Create Customer
*CustomersBankApi* | [**get_customer**](docs/CustomersBankApi.md#get_customer) | **GET** /api/customers/{customer_guid} | Get Customer
*CustomersBankApi* | [**list_customers**](docs/CustomersBankApi.md#list_customers) | **GET** /api/customers | Get customers list
*DepositAddressesBankApi* | [**create_deposit_address**](docs/DepositAddressesBankApi.md#create_deposit_address) | **POST** /api/deposit_addresses | Create Deposit Address
*DepositAddressesBankApi* | [**get_deposit_address**](docs/DepositAddressesBankApi.md#get_deposit_address) | **GET** /api/deposit_addresses/{deposit_address_guid} | Get Deposit Address
*DepositAddressesBankApi* | [**list_deposit_addresses**](docs/DepositAddressesBankApi.md#list_deposit_addresses) | **GET** /api/deposit_addresses | List Deposit Addresses
*ExternalBankAccountsBankApi* | [**create_external_bank_account**](docs/ExternalBankAccountsBankApi.md#create_external_bank_account) | **POST** /api/external_bank_accounts | Create ExternalBankAccount
*ExternalBankAccountsBankApi* | [**delete_external_bank_account**](docs/ExternalBankAccountsBankApi.md#delete_external_bank_account) | **DELETE** /api/external_bank_accounts/{external_bank_account_guid} | Delete External Bank Account
*ExternalBankAccountsBankApi* | [**get_external_bank_account**](docs/ExternalBankAccountsBankApi.md#get_external_bank_account) | **GET** /api/external_bank_accounts/{external_bank_account_guid} | Get External Bank Account
*ExternalBankAccountsBankApi* | [**list_external_bank_accounts**](docs/ExternalBankAccountsBankApi.md#list_external_bank_accounts) | **GET** /api/external_bank_accounts | Get external bank accounts list
*ExternalBankAccountsBankApi* | [**patch_external_bank_account**](docs/ExternalBankAccountsBankApi.md#patch_external_bank_account) | **PATCH** /api/external_bank_accounts/{external_bank_account_guid} | Patch ExternalBankAccount
*FeeConfigurationsBankApi* | [**create_fee_configuration**](docs/FeeConfigurationsBankApi.md#create_fee_configuration) | **POST** /api/fee_configurations | Create Fee Configuration
*FeeConfigurationsBankApi* | [**get_fee_configuration**](docs/FeeConfigurationsBankApi.md#get_fee_configuration) | **GET** /api/fee_configurations/{fee_configuration_guid} | Get Fee Configuration
*FeeConfigurationsBankApi* | [**list_fee_configurations**](docs/FeeConfigurationsBankApi.md#list_fee_configurations) | **GET** /api/fee_configurations | List Fee Configurations
*IdentityVerificationsBankApi* | [**create_identity_verification**](docs/IdentityVerificationsBankApi.md#create_identity_verification) | **POST** /api/identity_verifications | Create Identity Verification
*IdentityVerificationsBankApi* | [**get_identity_verification**](docs/IdentityVerificationsBankApi.md#get_identity_verification) | **GET** /api/identity_verifications/{identity_verification_guid} | Get Identity Verification
*IdentityVerificationsBankApi* | [**list_identity_verifications**](docs/IdentityVerificationsBankApi.md#list_identity_verifications) | **GET** /api/identity_verifications | List Identity Verifications
*IdentityRecordsBankApi* | [**create_identity_record**](docs/IdentityRecordsBankApi.md#create_identity_record) | **POST** /api/identity_records | Create Identity Record
*IdentityRecordsBankApi* | [**get_identity_record**](docs/IdentityRecordsBankApi.md#get_identity_record) | **GET** /api/identity_records/{identity_record_guid} | Get Identity Record
*IdentityRecordsBankApi* | [**list_identity_records**](docs/IdentityRecordsBankApi.md#list_identity_records) | **GET** /api/identity_records | List Identity Records
*PricesBankApi* | [**list_prices**](docs/PricesBankApi.md#list_prices) | **GET** /api/prices | Get Price
*QuotesBankApi* | [**create_quote**](docs/QuotesBankApi.md#create_quote) | **POST** /api/quotes | Create Quote
*QuotesBankApi* | [**get_quote**](docs/QuotesBankApi.md#get_quote) | **GET** /api/quotes/{quote_guid} | Get Quote
*QuotesBankApi* | [**list_quotes**](docs/QuotesBankApi.md#list_quotes) | **GET** /api/quotes | Get quotes list
*RewardsBankApi* | [**create_rewards**](docs/RewardsBankApi.md#create_rewards) | **POST** /api/rewards | Create Reward
*RewardsBankApi* | [**get_reward**](docs/RewardsBankApi.md#get_reward) | **GET** /api/rewards/{reward_guid} | Get Reward
*RewardsBankApi* | [**list_rewards**](docs/RewardsBankApi.md#list_rewards) | **GET** /api/rewards | Get rewards list
*SymbolsBankApi* | [**list_symbols**](docs/SymbolsBankApi.md#list_symbols) | **GET** /api/symbols | Get Symbols list
*TradesBankApi* | [**create_trade**](docs/TradesBankApi.md#create_trade) | **POST** /api/trades | Create Trade
*TradesBankApi* | [**get_trade**](docs/TradesBankApi.md#get_trade) | **GET** /api/trades/{trade_guid} | Get Trade
*TradesBankApi* | [**list_trades**](docs/TradesBankApi.md#list_trades) | **GET** /api/trades | Get trades list
*TransfersBankApi* | [**create_transfer**](docs/TransfersBankApi.md#create_transfer) | **POST** /api/transfers | Create Transfer
*TransfersBankApi* | [**get_transfer**](docs/TransfersBankApi.md#get_transfer) | **GET** /api/transfers/{transfer_guid} | Get Transfer
*TransfersBankApi* | [**list_transfers**](docs/TransfersBankApi.md#list_transfers) | **GET** /api/transfers | Get transfers list
*VerificationKeysBankApi* | [**create_verification_key**](docs/VerificationKeysBankApi.md#create_verification_key) | **POST** /api/bank_verification_keys | Create VerificationKey
*VerificationKeysBankApi* | [**get_verification_key**](docs/VerificationKeysBankApi.md#get_verification_key) | **GET** /api/bank_verification_keys/{verification_key_guid} | Get VerificationKey
*VerificationKeysBankApi* | [**list_verification_keys**](docs/VerificationKeysBankApi.md#list_verification_keys) | **GET** /api/bank_verification_keys | Get Verification Keys list
*WorkflowsBankApi* | [**create_workflow**](docs/WorkflowsBankApi.md#create_workflow) | **POST** /api/workflows | Create Workflow
*WorkflowsBankApi* | [**get_workflow**](docs/WorkflowsBankApi.md#get_workflow) | **GET** /api/workflows/{workflow_guid} | Get Workflow
*WorkflowsBankApi* | [**list_workflows**](docs/WorkflowsBankApi.md#list_workflows) | **GET** /api/workflows | Get workflows list


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
 - [DepositAddress](docs/DepositAddress.md)
 - [DepositAddressList](docs/DepositAddressList.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExternalBankAccount](docs/ExternalBankAccount.md)
 - [ExternalBankAccountList](docs/ExternalBankAccountList.md)
 - [Fee](docs/Fee.md)
 - [FeeConfiguration](docs/FeeConfiguration.md)
 - [FeeConfigurationList](docs/FeeConfigurationList.md)
 - [IdentityRecord](docs/IdentityRecord.md)
 - [IdentityRecordList](docs/IdentityRecordList.md)
 - [IdentityVerification](docs/IdentityVerification.md)
 - [IdentityVerificationList](docs/IdentityVerificationList.md)
 - [IdentityVerificationWithDetails](docs/IdentityVerificationWithDetails.md)
 - [IdentityVerificationWithDetailsAllOf](docs/IdentityVerificationWithDetailsAllOf.md)
 - [ListRequestPage](docs/ListRequestPage.md)
 - [ListRequestPerPage](docs/ListRequestPerPage.md)
 - [PatchBank](docs/PatchBank.md)
 - [PatchExternalBankAccount](docs/PatchExternalBankAccount.md)
 - [PostAccount](docs/PostAccount.md)
 - [PostBank](docs/PostBank.md)
 - [PostCustomer](docs/PostCustomer.md)
 - [PostDepositAddress](docs/PostDepositAddress.md)
 - [PostExternalBankAccount](docs/PostExternalBankAccount.md)
 - [PostFee](docs/PostFee.md)
 - [PostFeeConfiguration](docs/PostFeeConfiguration.md)
 - [PostIdentityRecord](docs/PostIdentityRecord.md)
 - [PostIdentityRecordAttestationDetails](docs/PostIdentityRecordAttestationDetails.md)
 - [PostIdentityVerification](docs/PostIdentityVerification.md)
 - [PostOneTimeAddress](docs/PostOneTimeAddress.md)
 - [PostQuote](docs/PostQuote.md)
 - [PostReward](docs/PostReward.md)
 - [PostTrade](docs/PostTrade.md)
 - [PostTransfer](docs/PostTransfer.md)
 - [PostVerificationKey](docs/PostVerificationKey.md)
 - [PostWorkflow](docs/PostWorkflow.md)
 - [Quote](docs/Quote.md)
 - [QuoteList](docs/QuoteList.md)
 - [Reward](docs/Reward.md)
 - [RewardList](docs/RewardList.md)
 - [SymbolPrice](docs/SymbolPrice.md)
 - [SymbolPriceResponse](docs/SymbolPriceResponse.md)
 - [Symbols](docs/Symbols.md)
 - [Trade](docs/Trade.md)
 - [TradeList](docs/TradeList.md)
 - [Transfer](docs/Transfer.md)
 - [TransferList](docs/TransferList.md)
 - [VerificationKey](docs/VerificationKey.md)
 - [VerificationKeyList](docs/VerificationKeyList.md)
 - [Workflow](docs/Workflow.md)
 - [WorkflowWithDetails](docs/WorkflowWithDetails.md)
 - [WorkflowWithDetailsAllOf](docs/WorkflowWithDetailsAllOf.md)
 - [WorkflowsList](docs/WorkflowsList.md)


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
 - **transfers:execute**: transfers execute
 - **transfers:read**: transfers read
 - **rewards:execute**: rewards execute
 - **rewards:read**: rewards read
 - **external_bank_accounts:read**: external_bank_accounts read
 - **external_bank_accounts:write**: external_bank_accounts write
 - **external_bank_accounts:execute**: external_bank_accounts execute
 - **workflows:read**: workflows read
 - **workflows:execute**: workflows execute
 - **deposit_addresses:read**: deposit_addresses read
 - **deposit_addresses:execute**: deposit_addresses execute


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

