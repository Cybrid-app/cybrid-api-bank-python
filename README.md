# cybrid-api-bank-python
# Cybrid API documentation

Welcome to Cybrid, an all-in-one crypto platform that enables you to easily **build** and **launch** white-label crypto products or services.

In these documents, you'll find details on how our REST API operates and generally how our platform functions.

If you're looking for our UI SDK Widgets for Web or Mobile (iOS/Android), generated API clients, or demo applications, head over to our [Github repo](https://github.com/Cybrid-app).

💡 We recommend bookmarking the [Cybrid LinkTree](https://linktr.ee/cybridtechnologies) which contains many helpful links to platform resources.

## Getting Started

This is Cybrid's public interactive API documentation, which allows you to fully test our APIs. If you'd like to use a different tool to exercise our APIs, you can download the [Open API 3.0 yaml](<api_platform_bank_swagger_schema_url>) for import.

If you're new to our APIs and the Cybrid Platform, follow the below guides to get set up and familiar with the platform:

1. [Introduction](https://docs.cybrid.xyz/docs/introduction)
2. [Platform Introduction](https://docs.cybrid.xyz/docs/how-is-cybrid-architected)
3. [Testing with Hosted Web Demo App](https://docs.cybrid.xyz/docs/testing-with-hosted-web-demo-app)

In [Getting Started in the Cybrid Sandbox](https://docs.cybrid.xyz/docs/how-do-i-get-started-with-the-sandbox), we walk you through how to use the [Cybrid Sandbox](https://id.sandbox.cybrid.app/) to create a test bank and generate API keys. In [Getting Ready for Trading](https://kb.cybrid.xyz/getting-ready-for-trading), we walk through creating customers, customer identities, accounts, as well as executing quotes and trades.

## Working with the Cybrid Platform

There are three primary ways you can interact with the Cybrid platform:

1. Directly via our RESTful API (this documentation)
2. Using our API clients available in a variety of languages ([Angular](https://github.com/Cybrid-app/cybrid-api-bank-angular), [Java](https://github.com/Cybrid-app/cybrid-api-bank-java), [Kotlin](https://github.com/Cybrid-app/cybrid-api-bank-kotlin), [Python](https://github.com/Cybrid-app/cybrid-api-bank-python), [Ruby](https://github.com/Cybrid-app/cybrid-api-bank-ruby), [Swift](https://github.com/Cybrid-app/cybrid-api-bank-swift) or [Typescript](https://github.com/Cybrid-app/cybrid-api-bank-typescript))
3. Integrating a platform specific SDK ([Web](https://github.com/Cybrid-app/cybrid-sdk-web), [Android](https://github.com/Cybrid-app/cybrid-sdk-android), [iOS](https://github.com/Cybrid-app/cybrid-sdk-ios))

Our complete set of APIs allows you to manage resources across three distinct areas: your `Organization`, your `Banks` and your `Identities`. For most of your testing and interaction you'll be using the `Bank` API, which is where the majority of APIs reside.

*The complete set of APIs can be found on the following pages:*

| API                                                              | Description                                                 |
|------------------------------------------------------------------|-------------------------------------------------------------|
| [Organization API](<api_platform_organization_swagger_ui_url>)   | APIs to manage organizations                                |
| [Bank API](<api_platform_bank_swagger_ui_url>)                   | APIs to manage banks (and all downstream customer activity) |
| [Identities API](<api_idp_swagger_ui_url>)                       | APIs to manage organization and bank identities             |

For questions please contact [Support](mailto:support@cybrid.xyz) at any time for assistance, or contact the [Product Team](mailto:product@cybrid.xyz) for product suggestions.

## Authenticating with the API

The Cybrid Platform uses OAuth 2.0 Bearer Tokens to authenticate requests to the platform. Credentials to create `Organization` and `Bank` tokens can be generated via the [Cybrid Sandbox](<api_idp_url>). Access tokens can be generated for a `Customer` as well via the [Cybrid IdP](<api_idp_url>) as well.

An `Organization` access token applies broadly to the whole Organization and all of its `Banks`, whereas, a `Bank` access token is specific to an individual Bank. `Customer` tokens, similarly, are scoped to a specific customer in a bank.

Both `Organization` and `Bank` tokens can be created using the OAuth Client Credential Grant flow. Each Organization and Bank has its own unique `Client ID` and `Secret` that allows for machine-to-machine authentication.

A `Bank` can then generate `Customer` access tokens via API using our [Identities API](<api_idp_swagger_ui_url>).

<font color=\"orange\">**⚠️ Never share your Client ID or Secret publicly or in your source code repository.**</font>

Your `Client ID` and `Secret` can be exchanged for a time-limited `Bearer Token` by interacting with the Cybrid Identity Provider or through interacting with the **Authorize** button in this document.

The following curl command can be used to quickly generate a `Bearer Token` for use in testing the API or demo applications.

```
# Example request when using Bank credentials
curl -X POST <api_idp_url>/oauth/token -d '{
    \"grant_type\": \"client_credentials\",
    \"client_id\": \"<Your Client ID>\",
    \"client_secret\": \"<Your Secret>\",
    \"scope\": \"<api_platform_bank_scopes>\"
  }' -H \"Content-Type: application/json\"

# When using Organization credentials set `scope` to '<api_platform_organization_scopes>'
```
<font color=\"orange\">**⚠️ Note: The above curl will create a bearer token with full scope access. Delete scopes if you'd like to restrict access.**</font>

## Authentication Scopes

The Cybrid platform supports the use of scopes to control the level of access a token is limited to. Scopes do not grant access to resources; instead, they provide limits, in support of the least privilege principal.

The following scopes are available on the platform and can be requested when generating either an Organization, Bank or Customer token. Generally speaking, the _Read_ scope is required to read and list resources, the _Write_ scope is required to update a resource and the _Execute_ scope is required to create a resource.

| Resource              | Read scope (Token Type)                                    | Write scope (Token Type)                      | Execute scope (Token Type)                       |
|-----------------------|------------------------------------------------------------|-----------------------------------------------|--------------------------------------------------|
| Account               | accounts:read (Organization, Bank, Customer)               |                                               | accounts:execute (Bank, Customer)                |
| Bank                  | banks:read (Organization, Bank)                            | banks:write (Organization, Bank)              | banks:execute (Organization)                     |
| Customer              | customers:read (Organization, Bank, Customer)              | customers:write (Bank, Customer)              | customers:execute (Bank)                         |
| Counterparty          | counterparties:read (Organization, Bank, Customer)         | counterparties:write (Bank, Customer)         | counterparties:execute (Bank)                    |
| Deposit Address       | deposit_addresses:read (Organization, Bank, Customer)      | deposit_addresses:write (Bank, Customer)      | deposit_addresses:execute (Bank, Customer)       |
| External Bank Account | external_bank_accounts:read (Organization, Bank, Customer) | external_bank_accounts:write (Bank, Customer) | external_bank_accounts:execute (Bank, Customer)  |
| External Wallet       | external_wallet:read (Organization, Bank, Customer)        |                                               | external_wallet:execute (Bank, Customer)         |
| Organization          | organizations:read (Organization)                          | organizations:write (Organization)            |                                                  |
| User                  | users:read (Organization)                                  |                                               | users:execute (Organization)                     |
| Price                 | prices:read (Bank, Customer)                               |                                               |                                                  |
| Quote                 | quotes:read (Organization, Bank, Customer)                 |                                               | quotes:execute (Organization, Bank, Customer)    |
| Trade                 | trades:read (Organization, Bank, Customer)                 |                                               | trades:execute (Organization, Bank, Customer)    |
| Transfer              | transfers:read (Organization, Bank, Customer)              |                                               | transfers:execute (Organization, Bank, Customer) |
| Workflow              | workflows:read (Organization, Bank, Customer)              |                                               | workflows:execute (Bank, Customer)               |
| Invoice               | invoices:read (Organization, Bank, Customer)               | invoices:write (Bank, Customer)               | invoices:execute (Bank, Customer)                |

## Available Endpoints

The available APIs for the [Identity](<api_idp_swagger_ui_url>), [Organization](<api_platform_organization_swagger_ui_url>) and [Bank](<api_platform_bank_swagger_ui_url>) API services are listed below:

| API Service  | Model                | API Endpoint Path              | Description                                                                                       |
|--------------|----------------------|--------------------------------|---------------------------------------------------------------------------------------------------|
| Identity     | Bank                 | /api/bank_applications         | Create and list banks                                                                             |
| Identity     | CustomerToken        | /api/customer_tokens           | Create customer JWT access tokens                                                                 |
| Identity     | Organization         | /api/organization_applications | Create and list organizations                                                                     |
| Identity     | Organization         | /api/users                     | Create and list organization users                                                                |
| Organization | Organization         | /api/organizations             | APIs to retrieve and update organization name                                                     |
| Bank         | Account              | /api/accounts                  | Create and list accounts, which hold a specific asset for a customers                             |
| Bank         | Asset                | /api/assets                    | Get a list of assets supported by the platform (ex: BTC, ETH)                                     |
| Bank         | Bank                 | /api/banks                     | Create, update and list banks, the parent to customers, accounts, etc                             |
| Bank         | Customer             | /api/customers                 | Create and list customers                                                                         |
| Bank         | Counterparty         | /api/counterparties            | Create and list counterparties                                                                    |
| Bank         | DepositAddress       | /api/deposit_addresses         | Create, get and list deposit addresses                                                            |
| Bank         | ExternalBankAccount  | /api/external_bank_accounts    | Create, get and list external bank accounts, which connect customer bank accounts to the platform |
| Bank         | ExternalWallet       | /api/external_wallets          | Create, get, list and delete external wallets, which connect customer wallets to the platform     |
| Bank         | IdentityVerification | /api/identity_verifications    | Create and list identity verifications, which are performed on customers for KYC                  |
| Bank         | Invoice              | /api/invoices                  | Create, get, cancel and list invoices                                                             |
| Bank         | PaymentInstruction   | /api/payment_instructions      | Create, get and list payment instructions for invoices                                            |
| Bank         | Price                | /api/prices                    | Get the current prices for assets on the platform                                                 |
| Bank         | Quote                | /api/quotes                    | Create and list quotes, which are required to execute trades                                      |
| Bank         | Symbol               | /api/symbols                   | Get a list of symbols supported for trade (ex: BTC-USD)                                           |
| Bank         | Trade                | /api/trades                    | Create and list trades, which buy or sell cryptocurrency                                          |
| Bank         | Transfer             | /api/transfers                 | Create, get and list transfers (e.g., funding, book)                                              |
| Bank         | Workflow             | /api/workflows                 | Create, get and list workflows                                                                    |

## Understanding Object Models & Endpoints

**Organizations**

An `Organization` is meant to represent the organization partnering with Cybrid to use our platform.

An `Organization` typically does not directly interact with `customers`. Instead, an Organization has one or more `banks`, which encompass the financial service offerings of the platform.

**Banks**

A `Bank` is owned by an `Organization` and can be thought of as an environment or container for `customers` and product offerings. Banks are created in either `Sandbox` or `Production` mode, where `Sandbox` is the environment that you would test, prototype and build in prior to moving to `Production`.

An `Organization` can have multiple `banks`, in either `Sandbox` or `Production` environments. A `Sandbox Bank` will be backed by stubbed data and process flows. For instance, funding source transfer processes as well as trades will be simulated rather than performed, however asset prices are representative of real-world values. You have an unlimited amount of simulated fiat currency for testing purposes.

**Customers**

`Customers` represent your banking users on the platform. At present, we offer support for `Individuals` as Customers.

`Customers` must be verified (i.e., KYC'd) in our system before they can play any part on the platform, which means they must have an associated and a passing `Identity Verification`. See the Identity Verifications section for more details on how a customer can be verified.

`Customers` must also have an `Account` to be able to transact, in the desired asset class. See the Accounts APIs for more details on setting up accounts for the customer.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.0.0
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
# Defining the host is optional and defaults to http://api-platform-bank.local.cybrid.com:3002
# See configuration.py for a list of all supported configuration parameters.
configuration = cybrid_api_bank.Configuration(
    host = "http://api-platform-bank.local.cybrid.com:3002"
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
    host = "http://api-platform-bank.local.cybrid.com:3002"
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
        labels=[
            "labels_example",
        ],
    ) # PostAccount | 

    try:
        # Create Account
        api_response = api_instance.create_account(post_account)
        pprint(api_response)
    except cybrid_api_bank.ApiException as e:
        print("Exception when calling AccountsBankApi->create_account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api-platform-bank.local.cybrid.com:3002*

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
*CounterpartiesBankApi* | [**create_counterparty**](docs/CounterpartiesBankApi.md#create_counterparty) | **POST** /api/counterparties | Create Counterparty
*CounterpartiesBankApi* | [**get_counterparty**](docs/CounterpartiesBankApi.md#get_counterparty) | **GET** /api/counterparties/{counterparty_guid} | Get Counterparty
*CounterpartiesBankApi* | [**list_counterparties**](docs/CounterpartiesBankApi.md#list_counterparties) | **GET** /api/counterparties | Get counterparties list
*CustomersBankApi* | [**create_customer**](docs/CustomersBankApi.md#create_customer) | **POST** /api/customers | Create Customer
*CustomersBankApi* | [**get_customer**](docs/CustomersBankApi.md#get_customer) | **GET** /api/customers/{customer_guid} | Get Customer
*CustomersBankApi* | [**list_customers**](docs/CustomersBankApi.md#list_customers) | **GET** /api/customers | Get customers list
*CustomersBankApi* | [**update_customer**](docs/CustomersBankApi.md#update_customer) | **PATCH** /api/customers/{customer_guid} | Patch Customer
*DepositAddressesBankApi* | [**create_deposit_address**](docs/DepositAddressesBankApi.md#create_deposit_address) | **POST** /api/deposit_addresses | Create Deposit Address
*DepositAddressesBankApi* | [**get_deposit_address**](docs/DepositAddressesBankApi.md#get_deposit_address) | **GET** /api/deposit_addresses/{deposit_address_guid} | Get Deposit Address
*DepositAddressesBankApi* | [**list_deposit_addresses**](docs/DepositAddressesBankApi.md#list_deposit_addresses) | **GET** /api/deposit_addresses | List Deposit Addresses
*DepositBankAccountsBankApi* | [**create_deposit_bank_account**](docs/DepositBankAccountsBankApi.md#create_deposit_bank_account) | **POST** /api/deposit_bank_accounts | Create Deposit Bank Account
*DepositBankAccountsBankApi* | [**get_deposit_bank_account**](docs/DepositBankAccountsBankApi.md#get_deposit_bank_account) | **GET** /api/deposit_bank_accounts/{deposit_bank_account_guid} | Get Deposit Bank Account
*DepositBankAccountsBankApi* | [**list_deposit_bank_accounts**](docs/DepositBankAccountsBankApi.md#list_deposit_bank_accounts) | **GET** /api/deposit_bank_accounts | List Deposit Bank Accounts
*ExecutionsBankApi* | [**create_execution**](docs/ExecutionsBankApi.md#create_execution) | **POST** /api/executions | Create Execution
*ExecutionsBankApi* | [**get_execution**](docs/ExecutionsBankApi.md#get_execution) | **GET** /api/executions/{execution_guid} | Get Execution
*ExternalBankAccountsBankApi* | [**create_external_bank_account**](docs/ExternalBankAccountsBankApi.md#create_external_bank_account) | **POST** /api/external_bank_accounts | Create ExternalBankAccount
*ExternalBankAccountsBankApi* | [**delete_external_bank_account**](docs/ExternalBankAccountsBankApi.md#delete_external_bank_account) | **DELETE** /api/external_bank_accounts/{external_bank_account_guid} | Delete External Bank Account
*ExternalBankAccountsBankApi* | [**get_external_bank_account**](docs/ExternalBankAccountsBankApi.md#get_external_bank_account) | **GET** /api/external_bank_accounts/{external_bank_account_guid} | Get External Bank Account
*ExternalBankAccountsBankApi* | [**list_external_bank_accounts**](docs/ExternalBankAccountsBankApi.md#list_external_bank_accounts) | **GET** /api/external_bank_accounts | Get external bank accounts list
*ExternalBankAccountsBankApi* | [**patch_external_bank_account**](docs/ExternalBankAccountsBankApi.md#patch_external_bank_account) | **PATCH** /api/external_bank_accounts/{external_bank_account_guid} | Patch ExternalBankAccount
*ExternalWalletsBankApi* | [**create_external_wallet**](docs/ExternalWalletsBankApi.md#create_external_wallet) | **POST** /api/external_wallets | Create ExternalWallet
*ExternalWalletsBankApi* | [**delete_external_wallet**](docs/ExternalWalletsBankApi.md#delete_external_wallet) | **DELETE** /api/external_wallets/{external_wallet_guid} | Delete External Wallet
*ExternalWalletsBankApi* | [**get_external_wallet**](docs/ExternalWalletsBankApi.md#get_external_wallet) | **GET** /api/external_wallets/{external_wallet_guid} | Get External Wallet
*ExternalWalletsBankApi* | [**list_external_wallets**](docs/ExternalWalletsBankApi.md#list_external_wallets) | **GET** /api/external_wallets | Get external wallets list
*FilesBankApi* | [**create_file**](docs/FilesBankApi.md#create_file) | **POST** /api/files | Create File
*FilesBankApi* | [**get_file**](docs/FilesBankApi.md#get_file) | **GET** /api/files/{file_guid} | Get File
*FilesBankApi* | [**list_files**](docs/FilesBankApi.md#list_files) | **GET** /api/files | List Files
*IdentityVerificationsBankApi* | [**create_identity_verification**](docs/IdentityVerificationsBankApi.md#create_identity_verification) | **POST** /api/identity_verifications | Create Identity Verification
*IdentityVerificationsBankApi* | [**get_identity_verification**](docs/IdentityVerificationsBankApi.md#get_identity_verification) | **GET** /api/identity_verifications/{identity_verification_guid} | Get Identity Verification
*IdentityVerificationsBankApi* | [**list_identity_verifications**](docs/IdentityVerificationsBankApi.md#list_identity_verifications) | **GET** /api/identity_verifications | List Identity Verifications
*InternalBankApi* | [**internal_claim_exchange_settlement_payment_order**](docs/InternalBankApi.md#internal_claim_exchange_settlement_payment_order) | **POST** /api/internal/exchange_settlement_payment_orders/{guid}/claim | Claim Exchange Settlement Payment Order
*InternalBankApi* | [**internal_claim_expected_payment**](docs/InternalBankApi.md#internal_claim_expected_payment) | **POST** /api/internal/expected_payments/{guid}/claim | Claim Expected Payment
*InternalBankApi* | [**internal_create_account**](docs/InternalBankApi.md#internal_create_account) | **POST** /api/internal/accounts | Create Account
*InternalBankApi* | [**internal_create_activity_limit_configuration**](docs/InternalBankApi.md#internal_create_activity_limit_configuration) | **POST** /api/internal/activity_limit_configurations | Create ActivityLimitConfiguration
*InternalBankApi* | [**internal_create_activity_report**](docs/InternalBankApi.md#internal_create_activity_report) | **POST** /api/internal/activity_reports | Create Activity Report
*InternalBankApi* | [**internal_create_bank**](docs/InternalBankApi.md#internal_create_bank) | **POST** /api/internal/banks | Create Bank
*InternalBankApi* | [**internal_create_bank_account_service**](docs/InternalBankApi.md#internal_create_bank_account_service) | **POST** /api/internal/bank_account_services | Create BankAccountService
*InternalBankApi* | [**internal_create_compliance_decision**](docs/InternalBankApi.md#internal_create_compliance_decision) | **POST** /api/internal/compliance_decisions | Create Compliance Decision
*InternalBankApi* | [**internal_create_country_code_configuration**](docs/InternalBankApi.md#internal_create_country_code_configuration) | **POST** /api/internal/country_code_configurations | Create CountryCodeConfiguration
*InternalBankApi* | [**internal_create_crypto_asset_configuration**](docs/InternalBankApi.md#internal_create_crypto_asset_configuration) | **POST** /api/internal/crypto_asset_configurations | Create CryptoAssetConfiguration
*InternalBankApi* | [**internal_create_cybrid_account**](docs/InternalBankApi.md#internal_create_cybrid_account) | **POST** /api/internal/cybrid_accounts | Create CybridAccount
*InternalBankApi* | [**internal_create_cybrid_gas_account_configuration**](docs/InternalBankApi.md#internal_create_cybrid_gas_account_configuration) | **POST** /api/internal/cybrid_gas_account_configurations | Create CybridGasAccountConfiguration
*InternalBankApi* | [**internal_create_deposit_bank_account**](docs/InternalBankApi.md#internal_create_deposit_bank_account) | **POST** /api/internal/deposit_bank_accounts | Create Deposit Bank Account
*InternalBankApi* | [**internal_create_exchange**](docs/InternalBankApi.md#internal_create_exchange) | **POST** /api/internal/exchanges | Create Exchange
*InternalBankApi* | [**internal_create_exchange_account**](docs/InternalBankApi.md#internal_create_exchange_account) | **POST** /api/internal/exchange_accounts | Create ExchangeAccount
*InternalBankApi* | [**internal_create_exchange_monitor**](docs/InternalBankApi.md#internal_create_exchange_monitor) | **POST** /api/internal/exchange_monitors | Create ExchangeMonitor
*InternalBankApi* | [**internal_create_exchange_order**](docs/InternalBankApi.md#internal_create_exchange_order) | **POST** /api/internal/exchange_orders | Create ExchangeOrder
*InternalBankApi* | [**internal_create_exchange_settlement**](docs/InternalBankApi.md#internal_create_exchange_settlement) | **POST** /api/internal/exchange_settlements | Create Exchange Settlement
*InternalBankApi* | [**internal_create_exchange_settlement_approval**](docs/InternalBankApi.md#internal_create_exchange_settlement_approval) | **POST** /api/internal/exchange_settlements/{guid}/approval | Create Exchange Settlement Approval
*InternalBankApi* | [**internal_create_exchange_settlement_completion**](docs/InternalBankApi.md#internal_create_exchange_settlement_completion) | **POST** /api/internal/exchange_settlements/{guid}/completion | Create Exchange Settlement Completion
*InternalBankApi* | [**internal_create_exchange_settlement_configuration**](docs/InternalBankApi.md#internal_create_exchange_settlement_configuration) | **POST** /api/internal/exchange_settlement_configurations | Create ExchangeSettlementConfiguration
*InternalBankApi* | [**internal_create_exchange_settlement_payment_order**](docs/InternalBankApi.md#internal_create_exchange_settlement_payment_order) | **POST** /api/internal/exchange_settlement_payment_orders | Create Exchange Settlement Payment Order
*InternalBankApi* | [**internal_create_expected_payment**](docs/InternalBankApi.md#internal_create_expected_payment) | **POST** /api/internal/expected_payments | Create Expected Payment
*InternalBankApi* | [**internal_create_external_bank_account**](docs/InternalBankApi.md#internal_create_external_bank_account) | **POST** /api/internal/external_bank_accounts | Create ExternalBankAccount
*InternalBankApi* | [**internal_create_external_wallet**](docs/InternalBankApi.md#internal_create_external_wallet) | **POST** /api/internal/external_wallets | Create ExternalWallet
*InternalBankApi* | [**internal_create_fee**](docs/InternalBankApi.md#internal_create_fee) | **POST** /api/internal/fees | Create Fee
*InternalBankApi* | [**internal_create_fee_configuration**](docs/InternalBankApi.md#internal_create_fee_configuration) | **POST** /api/internal/fee_configurations | Create FeeConfiguration
*InternalBankApi* | [**internal_create_fiat_asset_configuration**](docs/InternalBankApi.md#internal_create_fiat_asset_configuration) | **POST** /api/internal/fiat_asset_configurations | Create FiatAssetConfiguration
*InternalBankApi* | [**internal_create_file**](docs/InternalBankApi.md#internal_create_file) | **POST** /api/internal/files | Create File
*InternalBankApi* | [**internal_create_internal_bank_account**](docs/InternalBankApi.md#internal_create_internal_bank_account) | **POST** /api/internal/internal_bank_accounts | Create InternalBankAccount
*InternalBankApi* | [**internal_create_internal_bank_account_configuration**](docs/InternalBankApi.md#internal_create_internal_bank_account_configuration) | **POST** /api/internal/internal_bank_account_configurations | Create InternalBankAccountConfiguration
*InternalBankApi* | [**internal_create_internal_wallet**](docs/InternalBankApi.md#internal_create_internal_wallet) | **POST** /api/internal/internal_wallets | Create InternalWallet
*InternalBankApi* | [**internal_create_internal_wallet_configuration**](docs/InternalBankApi.md#internal_create_internal_wallet_configuration) | **POST** /api/internal/internal_wallet_configurations | Create InternalWalletConfiguration
*InternalBankApi* | [**internal_create_payout_symbol_configuration**](docs/InternalBankApi.md#internal_create_payout_symbol_configuration) | **POST** /api/internal/payout_symbol_configurations | Create PayoutSymbolConfiguration
*InternalBankApi* | [**internal_create_quote**](docs/InternalBankApi.md#internal_create_quote) | **POST** /api/internal/quotes | Create InternalQuote
*InternalBankApi* | [**internal_create_reconciliation**](docs/InternalBankApi.md#internal_create_reconciliation) | **POST** /api/internal/reconciliations | Create Reconciliation
*InternalBankApi* | [**internal_create_stage**](docs/InternalBankApi.md#internal_create_stage) | **POST** /api/internal/stages | Create Stage
*InternalBankApi* | [**internal_create_trade**](docs/InternalBankApi.md#internal_create_trade) | **POST** /api/internal/trades | Create Internal Trade
*InternalBankApi* | [**internal_create_trading_symbol_configuration**](docs/InternalBankApi.md#internal_create_trading_symbol_configuration) | **POST** /api/internal/trading_symbol_configurations | Create TradingSymbolConfiguration
*InternalBankApi* | [**internal_create_transaction_monitor**](docs/InternalBankApi.md#internal_create_transaction_monitor) | **POST** /api/internal/transaction_monitors | Create TransactionMonitor
*InternalBankApi* | [**internal_create_transfer**](docs/InternalBankApi.md#internal_create_transfer) | **POST** /api/internal/transfers | Create Transfer
*InternalBankApi* | [**internal_create_transfer_rail_configuration**](docs/InternalBankApi.md#internal_create_transfer_rail_configuration) | **POST** /api/internal/transfer_rail_configurations | Create TransferRailConfiguration
*InternalBankApi* | [**internal_create_transfer_screening**](docs/InternalBankApi.md#internal_create_transfer_screening) | **POST** /api/internal/transfer_screenings | Create TransferScreening
*InternalBankApi* | [**internal_create_wallet_service**](docs/InternalBankApi.md#internal_create_wallet_service) | **POST** /api/internal/wallet_services | Create WalletService
*InternalBankApi* | [**internal_crypto_funding_deposit_transfer**](docs/InternalBankApi.md#internal_crypto_funding_deposit_transfer) | **POST** /api/internal/crypto_funding_deposit_transfers | Create Crypto Funding Deposit Transfer
*InternalBankApi* | [**internal_delete_activity_limit_configuration**](docs/InternalBankApi.md#internal_delete_activity_limit_configuration) | **DELETE** /api/internal/activity_limit_configurations/{guid} | Delete ActivityLimitConfiguration
*InternalBankApi* | [**internal_delete_external_bank_account**](docs/InternalBankApi.md#internal_delete_external_bank_account) | **DELETE** /api/internal/external_bank_accounts/{external_bank_account_guid} | Delete External Bank Account
*InternalBankApi* | [**internal_funding_deposit_transfer**](docs/InternalBankApi.md#internal_funding_deposit_transfer) | **POST** /api/internal/funding_deposit_transfers | Create Funding Deposit Transfer
*InternalBankApi* | [**internal_get_bank**](docs/InternalBankApi.md#internal_get_bank) | **GET** /api/internal/banks/{bank_guid} | Get Bank
*InternalBankApi* | [**internal_get_bank_account_service**](docs/InternalBankApi.md#internal_get_bank_account_service) | **GET** /api/internal/bank_account_services/{bank_account_service_guid} | Get BankAccountService
*InternalBankApi* | [**internal_get_customer**](docs/InternalBankApi.md#internal_get_customer) | **GET** /api/internal/customers/{customer_guid} | Get Customer
*InternalBankApi* | [**internal_get_cybrid_account**](docs/InternalBankApi.md#internal_get_cybrid_account) | **GET** /api/internal/cybrid_accounts/{account_guid} | Get CybridAccount
*InternalBankApi* | [**internal_get_exchange**](docs/InternalBankApi.md#internal_get_exchange) | **GET** /api/internal/exchanges/{exchange_guid} | Get Exchange
*InternalBankApi* | [**internal_get_exchange_account**](docs/InternalBankApi.md#internal_get_exchange_account) | **GET** /api/internal/exchange_accounts/{account_guid} | Get ExchangeAccount
*InternalBankApi* | [**internal_get_exchange_settlement**](docs/InternalBankApi.md#internal_get_exchange_settlement) | **GET** /api/internal/exchange_settlements/{guid} | Get Exchange Settlement
*InternalBankApi* | [**internal_get_exchange_settlement_obligation**](docs/InternalBankApi.md#internal_get_exchange_settlement_obligation) | **GET** /api/internal/exchange_settlement_obligations/{guid} | Get Exchange Settlement Obligation
*InternalBankApi* | [**internal_get_exchange_settlement_payment_order**](docs/InternalBankApi.md#internal_get_exchange_settlement_payment_order) | **GET** /api/internal/exchange_settlement_payment_orders/{guid} | Get Exchange Settlement Payment Order
*InternalBankApi* | [**internal_get_execution**](docs/InternalBankApi.md#internal_get_execution) | **GET** /api/internal/executions/{execution_guid} | Get Execution
*InternalBankApi* | [**internal_get_expected_payment**](docs/InternalBankApi.md#internal_get_expected_payment) | **GET** /api/internal/expected_payments/{guid} | Get Expected Payment
*InternalBankApi* | [**internal_get_external_bank_account**](docs/InternalBankApi.md#internal_get_external_bank_account) | **GET** /api/internal/external_bank_accounts/{external_bank_account_guid} | Get ExternalBankAccount
*InternalBankApi* | [**internal_get_external_wallet**](docs/InternalBankApi.md#internal_get_external_wallet) | **GET** /api/internal/external_wallets/{external_wallet_guid} | Get ExternalWallet
*InternalBankApi* | [**internal_get_external_wallet_screening**](docs/InternalBankApi.md#internal_get_external_wallet_screening) | **GET** /api/internal/external_wallet_screenings/{external_wallet_screening_guid} | Get ExternalWalletScreening
*InternalBankApi* | [**internal_get_file**](docs/InternalBankApi.md#internal_get_file) | **GET** /api/internal/files/{file_guid} | Get File
*InternalBankApi* | [**internal_get_internal_bank_account**](docs/InternalBankApi.md#internal_get_internal_bank_account) | **GET** /api/internal/internal_bank_accounts/{internal_bank_account_guid} | Get InternalBankAccount
*InternalBankApi* | [**internal_get_internal_wallet**](docs/InternalBankApi.md#internal_get_internal_wallet) | **GET** /api/internal/internal_wallets/{internal_wallet_guid} | Get InternalWallet
*InternalBankApi* | [**internal_get_invoice**](docs/InternalBankApi.md#internal_get_invoice) | **GET** /api/internal/invoices/{invoice_guid} | Get Invoice
*InternalBankApi* | [**internal_get_plan**](docs/InternalBankApi.md#internal_get_plan) | **GET** /api/internal/plans/{plan_guid} | Get Plan
*InternalBankApi* | [**internal_get_quote**](docs/InternalBankApi.md#internal_get_quote) | **GET** /api/internal/quotes/{quote_guid} | Get Internal Quote
*InternalBankApi* | [**internal_get_reconciliation**](docs/InternalBankApi.md#internal_get_reconciliation) | **GET** /api/internal/reconciliations/{guid} | Get Reconciliation
*InternalBankApi* | [**internal_get_trade**](docs/InternalBankApi.md#internal_get_trade) | **GET** /api/internal/trades/{trade_guid} | Get Internal Trade
*InternalBankApi* | [**internal_get_transfer**](docs/InternalBankApi.md#internal_get_transfer) | **GET** /api/internal/transfers/{guid} | Get Transfer
*InternalBankApi* | [**internal_get_transfer_screening**](docs/InternalBankApi.md#internal_get_transfer_screening) | **GET** /api/internal/transfer_screenings/{transfer_screening_guid} | Get TransferScreening
*InternalBankApi* | [**internal_get_wallet_service**](docs/InternalBankApi.md#internal_get_wallet_service) | **GET** /api/internal/wallet_services/{wallet_service_guid} | Get WalletService
*InternalBankApi* | [**internal_list_accounts**](docs/InternalBankApi.md#internal_list_accounts) | **GET** /api/internal/accounts | List Accounts
*InternalBankApi* | [**internal_list_activity_limit_configurations**](docs/InternalBankApi.md#internal_list_activity_limit_configurations) | **GET** /api/internal/activity_limit_configurations | List ActivityLimitConfigurations
*InternalBankApi* | [**internal_list_bank_account_services**](docs/InternalBankApi.md#internal_list_bank_account_services) | **GET** /api/internal/bank_account_services | List BankAccountServices
*InternalBankApi* | [**internal_list_banks**](docs/InternalBankApi.md#internal_list_banks) | **GET** /api/internal/banks | List Banks
*InternalBankApi* | [**internal_list_crypto_asset_configurations**](docs/InternalBankApi.md#internal_list_crypto_asset_configurations) | **GET** /api/internal/crypto_asset_configurations | List CryptoAssetConfiguration
*InternalBankApi* | [**internal_list_customers**](docs/InternalBankApi.md#internal_list_customers) | **GET** /api/internal/customers | List Customers
*InternalBankApi* | [**internal_list_cybrid_accounts**](docs/InternalBankApi.md#internal_list_cybrid_accounts) | **GET** /api/internal/cybrid_accounts | List CybridAccounts
*InternalBankApi* | [**internal_list_deposit_bank_accounts**](docs/InternalBankApi.md#internal_list_deposit_bank_accounts) | **GET** /api/internal/deposit_bank_accounts | List Deposit Bank Accounts
*InternalBankApi* | [**internal_list_exchange_orders**](docs/InternalBankApi.md#internal_list_exchange_orders) | **GET** /api/internal/exchange_orders | List ExchangeOrder
*InternalBankApi* | [**internal_list_exchange_settlement_configurations**](docs/InternalBankApi.md#internal_list_exchange_settlement_configurations) | **GET** /api/internal/exchange_settlement_configurations | List ExchangeSettlementConfigurations
*InternalBankApi* | [**internal_list_exchange_settlement_payment_orders**](docs/InternalBankApi.md#internal_list_exchange_settlement_payment_orders) | **GET** /api/internal/exchange_settlement_payment_orders | List Exchange Settlement Payment Orders
*InternalBankApi* | [**internal_list_exchanges**](docs/InternalBankApi.md#internal_list_exchanges) | **GET** /api/internal/exchanges | List Exchanges
*InternalBankApi* | [**internal_list_expected_payments**](docs/InternalBankApi.md#internal_list_expected_payments) | **GET** /api/internal/expected_payments | List Expected Payments
*InternalBankApi* | [**internal_list_external_bank_accounts**](docs/InternalBankApi.md#internal_list_external_bank_accounts) | **GET** /api/internal/external_bank_accounts | List ExternalBankAccounts
*InternalBankApi* | [**internal_list_external_wallets**](docs/InternalBankApi.md#internal_list_external_wallets) | **GET** /api/internal/external_wallets | List ExternalWallets
*InternalBankApi* | [**internal_list_fee_configurations**](docs/InternalBankApi.md#internal_list_fee_configurations) | **GET** /api/internal/fee_configurations | List FeeConfiguration
*InternalBankApi* | [**internal_list_fees**](docs/InternalBankApi.md#internal_list_fees) | **GET** /api/internal/fees | List Fees
*InternalBankApi* | [**internal_list_internal_bank_accounts**](docs/InternalBankApi.md#internal_list_internal_bank_accounts) | **GET** /api/internal/internal_bank_accounts | List InternalBankAccounts
*InternalBankApi* | [**internal_list_internal_wallets**](docs/InternalBankApi.md#internal_list_internal_wallets) | **GET** /api/internal/internal_wallets | List InternalWallets
*InternalBankApi* | [**internal_list_invoices**](docs/InternalBankApi.md#internal_list_invoices) | **GET** /api/internal/invoices | List Invoices
*InternalBankApi* | [**internal_list_reconciliations**](docs/InternalBankApi.md#internal_list_reconciliations) | **GET** /api/internal/reconciliations | List Reconciliations
*InternalBankApi* | [**internal_list_trades**](docs/InternalBankApi.md#internal_list_trades) | **GET** /api/internal/trades | List Trades
*InternalBankApi* | [**internal_list_trading_symbol_configurations**](docs/InternalBankApi.md#internal_list_trading_symbol_configurations) | **GET** /api/internal/trading_symbol_configurations | List TradingSymbolConfigurations
*InternalBankApi* | [**internal_list_transactions**](docs/InternalBankApi.md#internal_list_transactions) | **GET** /api/internal/transactions | List Transactions
*InternalBankApi* | [**internal_list_transfers**](docs/InternalBankApi.md#internal_list_transfers) | **GET** /api/internal/transfers | List Transfers
*InternalBankApi* | [**internal_list_wallet_services**](docs/InternalBankApi.md#internal_list_wallet_services) | **GET** /api/internal/wallet_services | List WalletServices
*InternalBankApi* | [**internal_patch_account**](docs/InternalBankApi.md#internal_patch_account) | **PATCH** /api/internal/accounts/{account_guid} | Patch Account
*InternalBankApi* | [**internal_patch_activity_limit_configuration**](docs/InternalBankApi.md#internal_patch_activity_limit_configuration) | **PATCH** /api/internal/activity_limit_configurations/{guid} | Patch ActivityLimitConfiguration
*InternalBankApi* | [**internal_patch_bank**](docs/InternalBankApi.md#internal_patch_bank) | **PATCH** /api/internal/banks/{bank_guid} | Patch Bank
*InternalBankApi* | [**internal_patch_bank_account_service**](docs/InternalBankApi.md#internal_patch_bank_account_service) | **PATCH** /api/internal/bank_account_services/{guid} | Patch Internal BankAccount
*InternalBankApi* | [**internal_patch_business_detail**](docs/InternalBankApi.md#internal_patch_business_detail) | **PATCH** /api/internal/business_details/{guid} | Patch Business Details
*InternalBankApi* | [**internal_patch_counterparty**](docs/InternalBankApi.md#internal_patch_counterparty) | **PATCH** /api/internal/counterparties/{counterparty_guid} | Patch Counterparty
*InternalBankApi* | [**internal_patch_crypto_asset_configuration**](docs/InternalBankApi.md#internal_patch_crypto_asset_configuration) | **PATCH** /api/internal/crypto_asset_configurations/{guid} | Patch CryptoAssetConfiguration
*InternalBankApi* | [**internal_patch_customer**](docs/InternalBankApi.md#internal_patch_customer) | **PATCH** /api/internal/customers/{customer_guid} | Patch Customer
*InternalBankApi* | [**internal_patch_cybrid_account**](docs/InternalBankApi.md#internal_patch_cybrid_account) | **PATCH** /api/internal/cybrid_accounts/{guid} | Patch Cybrid Account
*InternalBankApi* | [**internal_patch_deposit_address**](docs/InternalBankApi.md#internal_patch_deposit_address) | **PATCH** /api/internal/deposit_addresses/{guid} | Patch Deposit Address
*InternalBankApi* | [**internal_patch_deposit_bank_account**](docs/InternalBankApi.md#internal_patch_deposit_bank_account) | **PATCH** /api/internal/deposit_bank_accounts/{deposit_bank_account_guid} | Patch DepositBankAccount
*InternalBankApi* | [**internal_patch_exchange_account**](docs/InternalBankApi.md#internal_patch_exchange_account) | **PATCH** /api/internal/exchange_accounts/{guid} | Patch Exchange Account
*InternalBankApi* | [**internal_patch_exchange_order**](docs/InternalBankApi.md#internal_patch_exchange_order) | **PATCH** /api/internal/exchange_orders/{guid} | Patch ExchangeOrder
*InternalBankApi* | [**internal_patch_exchange_settlement**](docs/InternalBankApi.md#internal_patch_exchange_settlement) | **PATCH** /api/internal/exchange_settlements/{exchange_settlement_guid} | Patch Exchange Settlement
*InternalBankApi* | [**internal_patch_external_bank_account**](docs/InternalBankApi.md#internal_patch_external_bank_account) | **PATCH** /api/internal/external_bank_accounts/{external_bank_account_guid} | Patch ExternalBankAccount
*InternalBankApi* | [**internal_patch_external_wallet**](docs/InternalBankApi.md#internal_patch_external_wallet) | **PATCH** /api/internal/external_wallets/{external_wallet_guid} | Patch ExternalWallet
*InternalBankApi* | [**internal_patch_external_wallet_screening**](docs/InternalBankApi.md#internal_patch_external_wallet_screening) | **PATCH** /api/internal/external_wallet_screenings/{external_wallet_screening_guid} | Patch External Wallet Screening
*InternalBankApi* | [**internal_patch_fee**](docs/InternalBankApi.md#internal_patch_fee) | **PATCH** /api/internal/fees/{guid} | Patch Fee
*InternalBankApi* | [**internal_patch_files**](docs/InternalBankApi.md#internal_patch_files) | **PATCH** /api/internal/files/{file_guid} | Patch Files
*InternalBankApi* | [**internal_patch_identity_verification**](docs/InternalBankApi.md#internal_patch_identity_verification) | **PATCH** /api/internal/identity_verifications/{identity_verification_guid} | Patch Identity Verification
*InternalBankApi* | [**internal_patch_internal_bank_account**](docs/InternalBankApi.md#internal_patch_internal_bank_account) | **PATCH** /api/internal/internal_bank_accounts/{guid} | Patch Internal Bank Account
*InternalBankApi* | [**internal_patch_internal_wallet**](docs/InternalBankApi.md#internal_patch_internal_wallet) | **PATCH** /api/internal/internal_wallets/{guid} | Patch Internal Wallet
*InternalBankApi* | [**internal_patch_internal_wallet_group**](docs/InternalBankApi.md#internal_patch_internal_wallet_group) | **PATCH** /api/internal/internal_wallet_groups/{guid} | Patch Internal Wallet
*InternalBankApi* | [**internal_patch_invoice**](docs/InternalBankApi.md#internal_patch_invoice) | **PATCH** /api/internal/invoices/{invoice_guid} | Patch Invoice
*InternalBankApi* | [**internal_patch_payment_instruction**](docs/InternalBankApi.md#internal_patch_payment_instruction) | **PATCH** /api/internal/payment_instructions/{guid} | Patch Payment Instruction
*InternalBankApi* | [**internal_patch_person_detail**](docs/InternalBankApi.md#internal_patch_person_detail) | **PATCH** /api/internal/person_details/{guid} | Patch Person Details
*InternalBankApi* | [**internal_patch_trade**](docs/InternalBankApi.md#internal_patch_trade) | **PATCH** /api/internal/trades/{trade_guid} | Patch Trade
*InternalBankApi* | [**internal_patch_trading_symbol_configuration**](docs/InternalBankApi.md#internal_patch_trading_symbol_configuration) | **PATCH** /api/internal/trading_symbol_configurations/{guid} | Patch TradingSymbolConfiguration
*InternalBankApi* | [**internal_patch_transfer**](docs/InternalBankApi.md#internal_patch_transfer) | **PATCH** /api/internal/transfers/{transfer_guid} | Patch Transfer
*InternalBankApi* | [**internal_patch_transfer_screening**](docs/InternalBankApi.md#internal_patch_transfer_screening) | **PATCH** /api/internal/transfer_screenings/{transfer_screening_guid} | Patch External Wallet Screening
*InternalBankApi* | [**internal_patch_wallet_service**](docs/InternalBankApi.md#internal_patch_wallet_service) | **PATCH** /api/internal/wallet_services/{guid} | Patch Internal Wallet
*InternalBankApi* | [**internal_patch_workflow**](docs/InternalBankApi.md#internal_patch_workflow) | **PATCH** /api/internal/workflows/{workflow_guid} | Patch Workflow
*InternalBankApi* | [**internal_signal_external_wallet_screening**](docs/InternalBankApi.md#internal_signal_external_wallet_screening) | **POST** /api/internal/external_wallet_screenings/{external_wallet_screening_guid}/signal | Signal External Wallet Screening
*InternalBankApi* | [**internal_signal_identity_verification**](docs/InternalBankApi.md#internal_signal_identity_verification) | **POST** /api/internal/identity_verifications/{identity_verification_guid}/signal | Signal Identity Verification
*InternalBankApi* | [**internal_signal_invoice**](docs/InternalBankApi.md#internal_signal_invoice) | **POST** /api/internal/invoices/{invoice_guid}/signal | Signal Invoice
*InternalBankApi* | [**internal_signal_transfer**](docs/InternalBankApi.md#internal_signal_transfer) | **POST** /api/internal/transfers/{transfer_guid}/signal | Signal Transfer
*InternalBankApi* | [**patch_internal_execution**](docs/InternalBankApi.md#patch_internal_execution) | **PATCH** /api/internal/executions/{execution_guid} | Patch Execution
*InternalBankApi* | [**patch_internal_plan**](docs/InternalBankApi.md#patch_internal_plan) | **PATCH** /api/internal/plans/{plan_guid} | Patch Plan
*InternalBankApi* | [**patch_internal_stage**](docs/InternalBankApi.md#patch_internal_stage) | **PATCH** /api/internal/stages/{stage_guid} | Patch Stage
*InvoicesBankApi* | [**cancel_invoice**](docs/InvoicesBankApi.md#cancel_invoice) | **DELETE** /api/invoices/{invoice_guid} | Cancel Invoice
*InvoicesBankApi* | [**create_invoice**](docs/InvoicesBankApi.md#create_invoice) | **POST** /api/invoices | Create Invoice
*InvoicesBankApi* | [**get_invoice**](docs/InvoicesBankApi.md#get_invoice) | **GET** /api/invoices/{invoice_guid} | Get Invoice
*InvoicesBankApi* | [**list_invoices**](docs/InvoicesBankApi.md#list_invoices) | **GET** /api/invoices | List Invoices
*PaymentInstructionsBankApi* | [**create_payment_instruction**](docs/PaymentInstructionsBankApi.md#create_payment_instruction) | **POST** /api/payment_instructions | Create Payment Instruction
*PaymentInstructionsBankApi* | [**get_payment_instruction**](docs/PaymentInstructionsBankApi.md#get_payment_instruction) | **GET** /api/payment_instructions/{payment_instruction_guid} | Get Payment Instruction
*PaymentInstructionsBankApi* | [**list_payment_instructions**](docs/PaymentInstructionsBankApi.md#list_payment_instructions) | **GET** /api/payment_instructions | List Payment Instructions
*PersonaSessionsBankApi* | [**create_persona_session**](docs/PersonaSessionsBankApi.md#create_persona_session) | **POST** /api/persona_sessions | Create Persona Session
*PlansBankApi* | [**create_plan**](docs/PlansBankApi.md#create_plan) | **POST** /api/plans | Create Plan
*PlansBankApi* | [**get_plan**](docs/PlansBankApi.md#get_plan) | **GET** /api/plans/{plan_guid} | Get Plan
*PricesBankApi* | [**list_prices**](docs/PricesBankApi.md#list_prices) | **GET** /api/prices | Get Price
*QuotesBankApi* | [**create_quote**](docs/QuotesBankApi.md#create_quote) | **POST** /api/quotes | Create Quote
*QuotesBankApi* | [**get_quote**](docs/QuotesBankApi.md#get_quote) | **GET** /api/quotes/{quote_guid} | Get Quote
*QuotesBankApi* | [**list_quotes**](docs/QuotesBankApi.md#list_quotes) | **GET** /api/quotes | Get quotes list
*SymbolsBankApi* | [**list_symbols**](docs/SymbolsBankApi.md#list_symbols) | **GET** /api/symbols | Get Symbols list
*TradesBankApi* | [**create_trade**](docs/TradesBankApi.md#create_trade) | **POST** /api/trades | Create Trade
*TradesBankApi* | [**get_trade**](docs/TradesBankApi.md#get_trade) | **GET** /api/trades/{trade_guid} | Get Trade
*TradesBankApi* | [**list_trades**](docs/TradesBankApi.md#list_trades) | **GET** /api/trades | Get trades list
*TransfersBankApi* | [**create_transfer**](docs/TransfersBankApi.md#create_transfer) | **POST** /api/transfers | Create Transfer
*TransfersBankApi* | [**get_transfer**](docs/TransfersBankApi.md#get_transfer) | **GET** /api/transfers/{transfer_guid} | Get Transfer
*TransfersBankApi* | [**list_transfers**](docs/TransfersBankApi.md#list_transfers) | **GET** /api/transfers | Get transfers list
*TransfersBankApi* | [**update_transfer**](docs/TransfersBankApi.md#update_transfer) | **PATCH** /api/transfers/{transfer_guid} | Patch Transfer
*WorkflowsBankApi* | [**create_workflow**](docs/WorkflowsBankApi.md#create_workflow) | **POST** /api/workflows | Create Workflow
*WorkflowsBankApi* | [**get_workflow**](docs/WorkflowsBankApi.md#get_workflow) | **GET** /api/workflows/{workflow_guid} | Get Workflow
*WorkflowsBankApi* | [**list_workflows**](docs/WorkflowsBankApi.md#list_workflows) | **GET** /api/workflows | Get workflows list


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountAssociation](docs/AccountAssociation.md)
 - [AccountList](docs/AccountList.md)
 - [AccountState](docs/AccountState.md)
 - [AccountType](docs/AccountType.md)
 - [ActivityLimit](docs/ActivityLimit.md)
 - [ActivitySide](docs/ActivitySide.md)
 - [ActivityType](docs/ActivityType.md)
 - [Asset](docs/Asset.md)
 - [AssetList](docs/AssetList.md)
 - [AssetTypes](docs/AssetTypes.md)
 - [Bank](docs/Bank.md)
 - [BankFeature](docs/BankFeature.md)
 - [BankList](docs/BankList.md)
 - [BankSupportedPayoutSymbolsInner](docs/BankSupportedPayoutSymbolsInner.md)
 - [BankType](docs/BankType.md)
 - [ComplianceCheck](docs/ComplianceCheck.md)
 - [ComplianceCheckOutcome](docs/ComplianceCheckOutcome.md)
 - [ComplianceCheckType](docs/ComplianceCheckType.md)
 - [ComplianceDecision](docs/ComplianceDecision.md)
 - [ComplianceDecisionState](docs/ComplianceDecisionState.md)
 - [ComplianceDecisionType](docs/ComplianceDecisionType.md)
 - [Counterparty](docs/Counterparty.md)
 - [CounterpartyAddress](docs/CounterpartyAddress.md)
 - [CounterpartyAliasesInner](docs/CounterpartyAliasesInner.md)
 - [CounterpartyList](docs/CounterpartyList.md)
 - [CounterpartyName](docs/CounterpartyName.md)
 - [CounterpartyState](docs/CounterpartyState.md)
 - [CounterpartyType](docs/CounterpartyType.md)
 - [Customer](docs/Customer.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [CustomerAliasesInner](docs/CustomerAliasesInner.md)
 - [CustomerList](docs/CustomerList.md)
 - [CustomerName](docs/CustomerName.md)
 - [CustomerState](docs/CustomerState.md)
 - [CustomerType](docs/CustomerType.md)
 - [DepositAddress](docs/DepositAddress.md)
 - [DepositAddressFormat](docs/DepositAddressFormat.md)
 - [DepositAddressList](docs/DepositAddressList.md)
 - [DepositAddressState](docs/DepositAddressState.md)
 - [DepositBankAccount](docs/DepositBankAccount.md)
 - [DepositBankAccountAccountDetailsInner](docs/DepositBankAccountAccountDetailsInner.md)
 - [DepositBankAccountCounterpartyAddress](docs/DepositBankAccountCounterpartyAddress.md)
 - [DepositBankAccountList](docs/DepositBankAccountList.md)
 - [DepositBankAccountRoutingDetailsInner](docs/DepositBankAccountRoutingDetailsInner.md)
 - [DepositBankAccountRoutingNumberType](docs/DepositBankAccountRoutingNumberType.md)
 - [DepositBankAccountState](docs/DepositBankAccountState.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Execution](docs/Execution.md)
 - [ExecutionTravelRuleInfo](docs/ExecutionTravelRuleInfo.md)
 - [ExternalBankAccount](docs/ExternalBankAccount.md)
 - [ExternalBankAccountBalances](docs/ExternalBankAccountBalances.md)
 - [ExternalBankAccountKind](docs/ExternalBankAccountKind.md)
 - [ExternalBankAccountList](docs/ExternalBankAccountList.md)
 - [ExternalBankAccountPiiInner](docs/ExternalBankAccountPiiInner.md)
 - [ExternalBankAccountPiiInnerAddressesInner](docs/ExternalBankAccountPiiInnerAddressesInner.md)
 - [ExternalBankAccountPiiInnerRoutingDetailsInner](docs/ExternalBankAccountPiiInnerRoutingDetailsInner.md)
 - [ExternalBankAccountState](docs/ExternalBankAccountState.md)
 - [ExternalWallet](docs/ExternalWallet.md)
 - [ExternalWalletEnvironment](docs/ExternalWalletEnvironment.md)
 - [ExternalWalletList](docs/ExternalWalletList.md)
 - [ExternalWalletState](docs/ExternalWalletState.md)
 - [FeeAssociation](docs/FeeAssociation.md)
 - [IdentificationNumber](docs/IdentificationNumber.md)
 - [IdentityVerification](docs/IdentityVerification.md)
 - [IdentityVerificationBusinessAssociate](docs/IdentityVerificationBusinessAssociate.md)
 - [IdentityVerificationDocument](docs/IdentityVerificationDocument.md)
 - [IdentityVerificationDocumentFile](docs/IdentityVerificationDocumentFile.md)
 - [IdentityVerificationList](docs/IdentityVerificationList.md)
 - [IdentityVerificationMethod](docs/IdentityVerificationMethod.md)
 - [IdentityVerificationOptions](docs/IdentityVerificationOptions.md)
 - [IdentityVerificationOutcome](docs/IdentityVerificationOutcome.md)
 - [IdentityVerificationPersonaState](docs/IdentityVerificationPersonaState.md)
 - [IdentityVerificationState](docs/IdentityVerificationState.md)
 - [IdentityVerificationType](docs/IdentityVerificationType.md)
 - [IdentityVerificationWithDetails](docs/IdentityVerificationWithDetails.md)
 - [IdentityVerificationWithDetailsPii](docs/IdentityVerificationWithDetailsPii.md)
 - [IdentityVerificationWithDetailsPiiAddress](docs/IdentityVerificationWithDetailsPiiAddress.md)
 - [IdentityVerificationWithDetailsPiiAliasesInner](docs/IdentityVerificationWithDetailsPiiAliasesInner.md)
 - [IdentityVerificationWithDetailsPiiName](docs/IdentityVerificationWithDetailsPiiName.md)
 - [InternalActivityLimit](docs/InternalActivityLimit.md)
 - [InternalActivityLimitConfiguration](docs/InternalActivityLimitConfiguration.md)
 - [InternalActivityLimitConfigurationList](docs/InternalActivityLimitConfigurationList.md)
 - [InternalActivityReport](docs/InternalActivityReport.md)
 - [InternalActivityReportItem](docs/InternalActivityReportItem.md)
 - [InternalBank](docs/InternalBank.md)
 - [InternalBankAccountService](docs/InternalBankAccountService.md)
 - [InternalBankAccountServiceList](docs/InternalBankAccountServiceList.md)
 - [InternalBankList](docs/InternalBankList.md)
 - [InternalBusinessDetail](docs/InternalBusinessDetail.md)
 - [InternalComplianceDecision](docs/InternalComplianceDecision.md)
 - [InternalCountryCodeConfiguration](docs/InternalCountryCodeConfiguration.md)
 - [InternalCreateExchangeSettlementApproval202Response](docs/InternalCreateExchangeSettlementApproval202Response.md)
 - [InternalCryptoAssetConfiguration](docs/InternalCryptoAssetConfiguration.md)
 - [InternalCryptoAssetConfigurationList](docs/InternalCryptoAssetConfigurationList.md)
 - [InternalCryptoFundingDepositTransfer](docs/InternalCryptoFundingDepositTransfer.md)
 - [InternalCybridAccount](docs/InternalCybridAccount.md)
 - [InternalCybridAccountList](docs/InternalCybridAccountList.md)
 - [InternalCybridGasAccountConfiguration](docs/InternalCybridGasAccountConfiguration.md)
 - [InternalExchange](docs/InternalExchange.md)
 - [InternalExchangeAccount](docs/InternalExchangeAccount.md)
 - [InternalExchangeList](docs/InternalExchangeList.md)
 - [InternalExchangeMonitor](docs/InternalExchangeMonitor.md)
 - [InternalExchangeOrder](docs/InternalExchangeOrder.md)
 - [InternalExchangeOrderList](docs/InternalExchangeOrderList.md)
 - [InternalExchangeSettlement](docs/InternalExchangeSettlement.md)
 - [InternalExchangeSettlementConfiguration](docs/InternalExchangeSettlementConfiguration.md)
 - [InternalExchangeSettlementConfigurationList](docs/InternalExchangeSettlementConfigurationList.md)
 - [InternalExchangeSettlementObligation](docs/InternalExchangeSettlementObligation.md)
 - [InternalExchangeSettlementOrderAmountsInner](docs/InternalExchangeSettlementOrderAmountsInner.md)
 - [InternalExchangeSettlementPaymentOrder](docs/InternalExchangeSettlementPaymentOrder.md)
 - [InternalExchangeSettlementPaymentOrderList](docs/InternalExchangeSettlementPaymentOrderList.md)
 - [InternalExchangeSettlementTradeAmountsInner](docs/InternalExchangeSettlementTradeAmountsInner.md)
 - [InternalExecution](docs/InternalExecution.md)
 - [InternalExpectedPayment](docs/InternalExpectedPayment.md)
 - [InternalExpectedPaymentList](docs/InternalExpectedPaymentList.md)
 - [InternalExternalBankAccount](docs/InternalExternalBankAccount.md)
 - [InternalExternalBankAccountList](docs/InternalExternalBankAccountList.md)
 - [InternalExternalBankAccountPiiInner](docs/InternalExternalBankAccountPiiInner.md)
 - [InternalExternalWallet](docs/InternalExternalWallet.md)
 - [InternalExternalWalletList](docs/InternalExternalWalletList.md)
 - [InternalExternalWalletScreening](docs/InternalExternalWalletScreening.md)
 - [InternalFee](docs/InternalFee.md)
 - [InternalFeeAssociation](docs/InternalFeeAssociation.md)
 - [InternalFeeCharge](docs/InternalFeeCharge.md)
 - [InternalFeeChargeList](docs/InternalFeeChargeList.md)
 - [InternalFeeConfiguration](docs/InternalFeeConfiguration.md)
 - [InternalFeeConfigurationList](docs/InternalFeeConfigurationList.md)
 - [InternalFiatAssetConfiguration](docs/InternalFiatAssetConfiguration.md)
 - [InternalFundingDepositTransfer](docs/InternalFundingDepositTransfer.md)
 - [InternalInternalBankAccount](docs/InternalInternalBankAccount.md)
 - [InternalInternalBankAccountConfiguration](docs/InternalInternalBankAccountConfiguration.md)
 - [InternalInternalBankAccountList](docs/InternalInternalBankAccountList.md)
 - [InternalInternalInvoiceList](docs/InternalInternalInvoiceList.md)
 - [InternalInternalWallet](docs/InternalInternalWallet.md)
 - [InternalInternalWalletConfiguration](docs/InternalInternalWalletConfiguration.md)
 - [InternalInternalWalletGroup](docs/InternalInternalWalletGroup.md)
 - [InternalInternalWalletList](docs/InternalInternalWalletList.md)
 - [InternalInvoice](docs/InternalInvoice.md)
 - [InternalPayoutSymbolConfiguration](docs/InternalPayoutSymbolConfiguration.md)
 - [InternalPersonDetail](docs/InternalPersonDetail.md)
 - [InternalPlan](docs/InternalPlan.md)
 - [InternalPostAccount](docs/InternalPostAccount.md)
 - [InternalPostDepositBankAccount](docs/InternalPostDepositBankAccount.md)
 - [InternalPostFeeConfiguration](docs/InternalPostFeeConfiguration.md)
 - [InternalPostQuote](docs/InternalPostQuote.md)
 - [InternalQuote](docs/InternalQuote.md)
 - [InternalReconciliation](docs/InternalReconciliation.md)
 - [InternalReconciliationList](docs/InternalReconciliationList.md)
 - [InternalStage](docs/InternalStage.md)
 - [InternalTrade](docs/InternalTrade.md)
 - [InternalTradingSymbolConfiguration](docs/InternalTradingSymbolConfiguration.md)
 - [InternalTradingSymbolConfigurationList](docs/InternalTradingSymbolConfigurationList.md)
 - [InternalTransaction](docs/InternalTransaction.md)
 - [InternalTransactionMonitor](docs/InternalTransactionMonitor.md)
 - [InternalTransactionsList](docs/InternalTransactionsList.md)
 - [InternalTransactionsListPageInfo](docs/InternalTransactionsListPageInfo.md)
 - [InternalTransfer](docs/InternalTransfer.md)
 - [InternalTransferAssociation](docs/InternalTransferAssociation.md)
 - [InternalTransferDestinationAccount](docs/InternalTransferDestinationAccount.md)
 - [InternalTransferList](docs/InternalTransferList.md)
 - [InternalTransferRailConfiguration](docs/InternalTransferRailConfiguration.md)
 - [InternalTransferScreening](docs/InternalTransferScreening.md)
 - [InternalTransferSourceAccount](docs/InternalTransferSourceAccount.md)
 - [InternalWalletService](docs/InternalWalletService.md)
 - [InternalWalletServiceList](docs/InternalWalletServiceList.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceList](docs/InvoiceList.md)
 - [ListRequestPage](docs/ListRequestPage.md)
 - [ListRequestPerPage](docs/ListRequestPerPage.md)
 - [ParamInternalActivityLimit](docs/ParamInternalActivityLimit.md)
 - [PatchBank](docs/PatchBank.md)
 - [PatchCustomer](docs/PatchCustomer.md)
 - [PatchExternalBankAccount](docs/PatchExternalBankAccount.md)
 - [PatchInternalAccount](docs/PatchInternalAccount.md)
 - [PatchInternalAccountAssociation](docs/PatchInternalAccountAssociation.md)
 - [PatchInternalActivityLimitConfiguration](docs/PatchInternalActivityLimitConfiguration.md)
 - [PatchInternalBank](docs/PatchInternalBank.md)
 - [PatchInternalBankAccountService](docs/PatchInternalBankAccountService.md)
 - [PatchInternalBusinessDetail](docs/PatchInternalBusinessDetail.md)
 - [PatchInternalCounterparty](docs/PatchInternalCounterparty.md)
 - [PatchInternalCryptoAssetConfiguration](docs/PatchInternalCryptoAssetConfiguration.md)
 - [PatchInternalCustomer](docs/PatchInternalCustomer.md)
 - [PatchInternalCybridAccount](docs/PatchInternalCybridAccount.md)
 - [PatchInternalDepositAddress](docs/PatchInternalDepositAddress.md)
 - [PatchInternalDepositBankAccount](docs/PatchInternalDepositBankAccount.md)
 - [PatchInternalExchangeAccount](docs/PatchInternalExchangeAccount.md)
 - [PatchInternalExchangeOrder](docs/PatchInternalExchangeOrder.md)
 - [PatchInternalExchangeSettlement](docs/PatchInternalExchangeSettlement.md)
 - [PatchInternalExecution](docs/PatchInternalExecution.md)
 - [PatchInternalExternalBankAccount](docs/PatchInternalExternalBankAccount.md)
 - [PatchInternalExternalWallet](docs/PatchInternalExternalWallet.md)
 - [PatchInternalExternalWalletScreening](docs/PatchInternalExternalWalletScreening.md)
 - [PatchInternalFeeAssociation](docs/PatchInternalFeeAssociation.md)
 - [PatchInternalFeeCharge](docs/PatchInternalFeeCharge.md)
 - [PatchInternalFile](docs/PatchInternalFile.md)
 - [PatchInternalIdentityVerification](docs/PatchInternalIdentityVerification.md)
 - [PatchInternalInternalBankAccount](docs/PatchInternalInternalBankAccount.md)
 - [PatchInternalInternalWallet](docs/PatchInternalInternalWallet.md)
 - [PatchInternalInternalWalletGroup](docs/PatchInternalInternalWalletGroup.md)
 - [PatchInternalInvoice](docs/PatchInternalInvoice.md)
 - [PatchInternalPaymentInstruction](docs/PatchInternalPaymentInstruction.md)
 - [PatchInternalPersonDetail](docs/PatchInternalPersonDetail.md)
 - [PatchInternalPlan](docs/PatchInternalPlan.md)
 - [PatchInternalStage](docs/PatchInternalStage.md)
 - [PatchInternalTrade](docs/PatchInternalTrade.md)
 - [PatchInternalTradingSymbolConfiguration](docs/PatchInternalTradingSymbolConfiguration.md)
 - [PatchInternalTransfer](docs/PatchInternalTransfer.md)
 - [PatchInternalTransferScreening](docs/PatchInternalTransferScreening.md)
 - [PatchInternalWalletService](docs/PatchInternalWalletService.md)
 - [PatchInternalWorkflow](docs/PatchInternalWorkflow.md)
 - [PatchTransfer](docs/PatchTransfer.md)
 - [PatchTransferParticipant](docs/PatchTransferParticipant.md)
 - [PaymentInstruction](docs/PaymentInstruction.md)
 - [PaymentInstructionList](docs/PaymentInstructionList.md)
 - [PersonaSession](docs/PersonaSession.md)
 - [Plan](docs/Plan.md)
 - [PlanTravelRuleInfo](docs/PlanTravelRuleInfo.md)
 - [PlatformFile](docs/PlatformFile.md)
 - [PlatformFileList](docs/PlatformFileList.md)
 - [PostAccount](docs/PostAccount.md)
 - [PostBank](docs/PostBank.md)
 - [PostBankAccountDetails](docs/PostBankAccountDetails.md)
 - [PostCounterparty](docs/PostCounterparty.md)
 - [PostCounterpartyAddress](docs/PostCounterpartyAddress.md)
 - [PostCounterpartyAliasesInner](docs/PostCounterpartyAliasesInner.md)
 - [PostCounterpartyName](docs/PostCounterpartyName.md)
 - [PostCustomer](docs/PostCustomer.md)
 - [PostCustomerAddress](docs/PostCustomerAddress.md)
 - [PostCustomerAliasesInner](docs/PostCustomerAliasesInner.md)
 - [PostCustomerName](docs/PostCustomerName.md)
 - [PostDepositAddress](docs/PostDepositAddress.md)
 - [PostDepositBankAccount](docs/PostDepositBankAccount.md)
 - [PostExecution](docs/PostExecution.md)
 - [PostExternalBankAccount](docs/PostExternalBankAccount.md)
 - [PostExternalBankAccountCounterpartyAddress](docs/PostExternalBankAccountCounterpartyAddress.md)
 - [PostExternalBankAccountCounterpartyName](docs/PostExternalBankAccountCounterpartyName.md)
 - [PostExternalWallet](docs/PostExternalWallet.md)
 - [PostFee](docs/PostFee.md)
 - [PostFile](docs/PostFile.md)
 - [PostIdentificationNumber](docs/PostIdentificationNumber.md)
 - [PostIdentityVerification](docs/PostIdentityVerification.md)
 - [PostIdentityVerificationAddress](docs/PostIdentityVerificationAddress.md)
 - [PostIdentityVerificationAliasesInner](docs/PostIdentityVerificationAliasesInner.md)
 - [PostIdentityVerificationName](docs/PostIdentityVerificationName.md)
 - [PostInternalAccountAssociation](docs/PostInternalAccountAssociation.md)
 - [PostInternalActivityLimitConfiguration](docs/PostInternalActivityLimitConfiguration.md)
 - [PostInternalActivityReport](docs/PostInternalActivityReport.md)
 - [PostInternalBank](docs/PostInternalBank.md)
 - [PostInternalBankAccountService](docs/PostInternalBankAccountService.md)
 - [PostInternalClaimExchangeSettlementPaymentOrder](docs/PostInternalClaimExchangeSettlementPaymentOrder.md)
 - [PostInternalClaimExpectedPayment](docs/PostInternalClaimExpectedPayment.md)
 - [PostInternalComplianceDecision](docs/PostInternalComplianceDecision.md)
 - [PostInternalCountryCodeConfiguration](docs/PostInternalCountryCodeConfiguration.md)
 - [PostInternalCryptoAssetConfiguration](docs/PostInternalCryptoAssetConfiguration.md)
 - [PostInternalCryptoFundingDepositTransfer](docs/PostInternalCryptoFundingDepositTransfer.md)
 - [PostInternalCybridAccount](docs/PostInternalCybridAccount.md)
 - [PostInternalCybridGasAccountConfiguration](docs/PostInternalCybridGasAccountConfiguration.md)
 - [PostInternalExchange](docs/PostInternalExchange.md)
 - [PostInternalExchangeAccount](docs/PostInternalExchangeAccount.md)
 - [PostInternalExchangeMonitor](docs/PostInternalExchangeMonitor.md)
 - [PostInternalExchangeOrder](docs/PostInternalExchangeOrder.md)
 - [PostInternalExchangeSettlement](docs/PostInternalExchangeSettlement.md)
 - [PostInternalExchangeSettlementConfiguration](docs/PostInternalExchangeSettlementConfiguration.md)
 - [PostInternalExchangeSettlementPaymentOrder](docs/PostInternalExchangeSettlementPaymentOrder.md)
 - [PostInternalExpectedPayment](docs/PostInternalExpectedPayment.md)
 - [PostInternalExternalBankAccount](docs/PostInternalExternalBankAccount.md)
 - [PostInternalExternalBankAccountCounterpartyAddress](docs/PostInternalExternalBankAccountCounterpartyAddress.md)
 - [PostInternalExternalBankAccountCounterpartyBankAccount](docs/PostInternalExternalBankAccountCounterpartyBankAccount.md)
 - [PostInternalExternalBankAccountCounterpartyName](docs/PostInternalExternalBankAccountCounterpartyName.md)
 - [PostInternalExternalWallet](docs/PostInternalExternalWallet.md)
 - [PostInternalFeeAssociation](docs/PostInternalFeeAssociation.md)
 - [PostInternalFeeCharge](docs/PostInternalFeeCharge.md)
 - [PostInternalFiatAssetConfiguration](docs/PostInternalFiatAssetConfiguration.md)
 - [PostInternalFundingDepositTransfer](docs/PostInternalFundingDepositTransfer.md)
 - [PostInternalInternalBankAccount](docs/PostInternalInternalBankAccount.md)
 - [PostInternalInternalBankAccountConfiguration](docs/PostInternalInternalBankAccountConfiguration.md)
 - [PostInternalInternalBankAccountRoutingDetail](docs/PostInternalInternalBankAccountRoutingDetail.md)
 - [PostInternalInternalWallet](docs/PostInternalInternalWallet.md)
 - [PostInternalInternalWalletConfiguration](docs/PostInternalInternalWalletConfiguration.md)
 - [PostInternalInternalWalletRoutingDetail](docs/PostInternalInternalWalletRoutingDetail.md)
 - [PostInternalPayoutSymbolConfiguration](docs/PostInternalPayoutSymbolConfiguration.md)
 - [PostInternalReconciliation](docs/PostInternalReconciliation.md)
 - [PostInternalStage](docs/PostInternalStage.md)
 - [PostInternalSystemTransaction](docs/PostInternalSystemTransaction.md)
 - [PostInternalTrade](docs/PostInternalTrade.md)
 - [PostInternalTradingSymbolConfiguration](docs/PostInternalTradingSymbolConfiguration.md)
 - [PostInternalTransactionMonitor](docs/PostInternalTransactionMonitor.md)
 - [PostInternalTransfer](docs/PostInternalTransfer.md)
 - [PostInternalTransferRailConfiguration](docs/PostInternalTransferRailConfiguration.md)
 - [PostInternalTransferScreening](docs/PostInternalTransferScreening.md)
 - [PostInternalWalletService](docs/PostInternalWalletService.md)
 - [PostInvoice](docs/PostInvoice.md)
 - [PostPaymentInstruction](docs/PostPaymentInstruction.md)
 - [PostPersonaSession](docs/PostPersonaSession.md)
 - [PostPlan](docs/PostPlan.md)
 - [PostPlanDestinationAccount](docs/PostPlanDestinationAccount.md)
 - [PostPlanSourceAccount](docs/PostPlanSourceAccount.md)
 - [PostPlanTravelRuleInfo](docs/PostPlanTravelRuleInfo.md)
 - [PostQuote](docs/PostQuote.md)
 - [PostQuoteEntry](docs/PostQuoteEntry.md)
 - [PostSignalInternalExternalWalletScreening](docs/PostSignalInternalExternalWalletScreening.md)
 - [PostSignalInternalIdentityVerification](docs/PostSignalInternalIdentityVerification.md)
 - [PostSignalInternalIdentityVerificationBankAccountHolderAddress](docs/PostSignalInternalIdentityVerificationBankAccountHolderAddress.md)
 - [PostSignalInternalIdentityVerificationBankAccountHolderName](docs/PostSignalInternalIdentityVerificationBankAccountHolderName.md)
 - [PostSupportedPayoutSymbols](docs/PostSupportedPayoutSymbols.md)
 - [PostTrade](docs/PostTrade.md)
 - [PostTransfer](docs/PostTransfer.md)
 - [PostTransferParticipant](docs/PostTransferParticipant.md)
 - [PostUltimateBeneficialOwner](docs/PostUltimateBeneficialOwner.md)
 - [PostWorkflow](docs/PostWorkflow.md)
 - [Quote](docs/Quote.md)
 - [QuoteEntry](docs/QuoteEntry.md)
 - [QuoteEntryDestinationAccount](docs/QuoteEntryDestinationAccount.md)
 - [QuoteEntrySourceAccount](docs/QuoteEntrySourceAccount.md)
 - [QuoteList](docs/QuoteList.md)
 - [QuoteSide](docs/QuoteSide.md)
 - [QuoteType](docs/QuoteType.md)
 - [Stage](docs/Stage.md)
 - [SymbolPrice](docs/SymbolPrice.md)
 - [SymbolPriceResponse](docs/SymbolPriceResponse.md)
 - [Symbols](docs/Symbols.md)
 - [Trade](docs/Trade.md)
 - [TradeFailureCode](docs/TradeFailureCode.md)
 - [TradeList](docs/TradeList.md)
 - [TradeSide](docs/TradeSide.md)
 - [TradeState](docs/TradeState.md)
 - [TradeType](docs/TradeType.md)
 - [Transfer](docs/Transfer.md)
 - [TransferAccountType](docs/TransferAccountType.md)
 - [TransferDestinationAccount](docs/TransferDestinationAccount.md)
 - [TransferEntry](docs/TransferEntry.md)
 - [TransferEntryDestinationAccount](docs/TransferEntryDestinationAccount.md)
 - [TransferFailureCode](docs/TransferFailureCode.md)
 - [TransferHoldDetails](docs/TransferHoldDetails.md)
 - [TransferList](docs/TransferList.md)
 - [TransferParticipant](docs/TransferParticipant.md)
 - [TransferSide](docs/TransferSide.md)
 - [TransferSourceAccount](docs/TransferSourceAccount.md)
 - [TransferState](docs/TransferState.md)
 - [TransferType](docs/TransferType.md)
 - [TravelRuleInfoParty](docs/TravelRuleInfoParty.md)
 - [Workflow](docs/Workflow.md)
 - [WorkflowState](docs/WorkflowState.md)
 - [WorkflowType](docs/WorkflowType.md)
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
 - **bank_applications:execute**: bank_applications execute
 - **accounts:read**: accounts read
 - **accounts:execute**: accounts execute
 - **counterparties:read**: counterparties read
 - **counterparties:pii:read**: counterparties pii read
 - **counterparties:write**: counterparties write
 - **counterparties:execute**: counterparties execute
 - **customers:read**: customers read
 - **customers:pii:read**: customers pii read
 - **customers:write**: customers write
 - **customers:execute**: customers execute
 - **prices:read**: prices read
 - **quotes:execute**: quotes execute
 - **quotes:read**: quotes read
 - **trades:execute**: trades execute
 - **trades:read**: trades read
 - **transfers:execute**: transfers execute
 - **transfers:read**: transfers read
 - **transfers:write**: transfers write
 - **external_bank_accounts:read**: external_bank_accounts read
 - **external_bank_accounts:pii:read**: external_bank_accounts pii read
 - **external_bank_accounts:write**: external_bank_accounts write
 - **external_bank_accounts:execute**: external_bank_accounts execute
 - **external_wallets:read**: external_wallets read
 - **external_wallets:execute**: external_wallets execute
 - **workflows:read**: workflows read
 - **workflows:execute**: workflows execute
 - **deposit_addresses:read**: deposit_addresses read
 - **deposit_addresses:execute**: deposit_addresses execute
 - **deposit_bank_accounts:read**: deposit_bank_accounts read
 - **deposit_bank_accounts:execute**: deposit_bank_accounts execute
 - **invoices:read**: invoices read
 - **invoices:write**: invoices write
 - **invoices:execute**: invoices execute
 - **identity_verifications:read**: identity_verifications read
 - **identity_verifications:pii:read**: identity_verifications pii read
 - **identity_verifications:write**: identity_verifications write
 - **identity_verifications:execute**: identity_verifications execute
 - **persona_sessions:execute**: persona_sessions execute
 - **plans:execute**: plans execute
 - **plans:read**: plans read
 - **executions:execute**: executions execute
 - **executions:read**: executions read
 - **files:read**: files read
 - **files:pii:read**: files pii read
 - **files:execute**: files execute


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

