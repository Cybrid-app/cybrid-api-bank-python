"""
    Cybrid Bank API

    # Cybrid API documentation  Welcome to Cybrid, an all-in-one crypto platform that enables you to easily **build** and **launch** white-label crypto products or services.  In these documents, you'll find details on how our REST API operates and generally how our platform functions.  If you're looking for our UI SDK Widgets for Web or Mobile (iOS/Android), generated API clients, or demo applications, head over to our [Github repo](https://github.com/Cybrid-app).  💡 We recommend bookmarking the [Cybrid LinkTree](https://linktr.ee/cybridtechnologies) which contains many helpful links to platform resources.  ## Getting Started  This is Cybrid's public interactive API documentation, which allows you to fully test our APIs. If you'd like to use a different tool to exercise our APIs, you can download the [Open API 3.0 yaml](<api_platform_bank_swagger_schema_url>) for import.  If you're new to our APIs and the Cybrid Platform, follow the below guides to get set up and familiar with the platform:  1. [Introduction](https://docs.cybrid.xyz/docs/introduction) 2. [Platform Introduction](https://docs.cybrid.xyz/docs/how-is-cybrid-architected) 3. [Testing with Hosted Web Demo App](https://docs.cybrid.xyz/docs/testing-with-hosted-web-demo-app)  In [Getting Started in the Cybrid Sandbox](https://docs.cybrid.xyz/docs/how-do-i-get-started-with-the-sandbox), we walk you through how to use the [Cybrid Sandbox](https://id.sandbox.cybrid.app/) to create a test bank and generate API keys. In [Getting Ready for Trading](https://kb.cybrid.xyz/getting-ready-for-trading), we walk through creating customers, customer identities, accounts, as well as executing quotes and trades.  ## Working with the Cybrid Platform  There are three primary ways you can interact with the Cybrid platform:  1. Directly via our RESTful API (this documentation) 2. Using our API clients available in a variety of languages ([Angular](https://github.com/Cybrid-app/cybrid-api-bank-angular), [Java](https://github.com/Cybrid-app/cybrid-api-bank-java), [Kotlin](https://github.com/Cybrid-app/cybrid-api-bank-kotlin), [Python](https://github.com/Cybrid-app/cybrid-api-bank-python), [Ruby](https://github.com/Cybrid-app/cybrid-api-bank-ruby), [Swift](https://github.com/Cybrid-app/cybrid-api-bank-swift) or [Typescript](https://github.com/Cybrid-app/cybrid-api-bank-typescript)) 3. Integrating a platform specific SDK ([Web](https://github.com/Cybrid-app/cybrid-sdk-web), [Android](https://github.com/Cybrid-app/cybrid-sdk-android), [iOS](https://github.com/Cybrid-app/cybrid-sdk-ios))  Our complete set of APIs allows you to manage resources across three distinct areas: your `Organization`, your `Banks` and your `Identities`. For most of your testing and interaction you'll be using the `Bank` API, which is where the majority of APIs reside.  *The complete set of APIs can be found on the following pages:*  | API                                                              | Description                                                 | |------------------------------------------------------------------|-------------------------------------------------------------| | [Organization API](<api_platform_organization_swagger_ui_url>)   | APIs to manage organizations                                | | [Bank API](<api_platform_bank_swagger_ui_url>)                   | APIs to manage banks (and all downstream customer activity) | | [Identities API](<api_idp_swagger_ui_url>)                       | APIs to manage organization and bank identities             |  For questions please contact [Support](mailto:support@cybrid.xyz) at any time for assistance, or contact the [Product Team](mailto:product@cybrid.xyz) for product suggestions.  ## Authenticating with the API  The Cybrid Platform uses OAuth 2.0 Bearer Tokens to authenticate requests to the platform. Credentials to create `Organization` and `Bank` tokens can be generated via the [Cybrid Sandbox](<api_idp_url>). Access tokens can be generated for a `Customer` as well via the [Cybrid IdP](<api_idp_url>) as well.  An `Organization` access token applies broadly to the whole Organization and all of its `Banks`, whereas, a `Bank` access token is specific to an individual Bank. `Customer` tokens, similarly, are scoped to a specific customer in a bank.  Both `Organization` and `Bank` tokens can be created using the OAuth Client Credential Grant flow. Each Organization and Bank has its own unique `Client ID` and `Secret` that allows for machine-to-machine authentication.  A `Bank` can then generate `Customer` access tokens via API using our [Identities API](<api_idp_swagger_ui_url>).  <font color=\"orange\">**⚠️ Never share your Client ID or Secret publicly or in your source code repository.**</font>  Your `Client ID` and `Secret` can be exchanged for a time-limited `Bearer Token` by interacting with the Cybrid Identity Provider or through interacting with the **Authorize** button in this document.  The following curl command can be used to quickly generate a `Bearer Token` for use in testing the API or demo applications.  ``` # Example request when using Bank credentials curl -X POST <api_idp_url>/oauth/token -d '{     \"grant_type\": \"client_credentials\",     \"client_id\": \"<Your Client ID>\",     \"client_secret\": \"<Your Secret>\",     \"scope\": \"<api_platform_bank_scopes>\"   }' -H \"Content-Type: application/json\"  # When using Organization credentials set `scope` to '<api_platform_organization_scopes>' ``` <font color=\"orange\">**⚠️ Note: The above curl will create a bearer token with full scope access. Delete scopes if you'd like to restrict access.**</font>  ## Authentication Scopes  The Cybrid platform supports the use of scopes to control the level of access a token is limited to. Scopes do not grant access to resources; instead, they provide limits, in support of the least privilege principal.  The following scopes are available on the platform and can be requested when generating either an Organization, Bank or Customer token. Generally speaking, the _Read_ scope is required to read and list resources, the _Write_ scope is required to update a resource and the _Execute_ scope is required to create a resource.  | Resource              | Read scope (Token Type)                                    | Write scope (Token Type)                      | Execute scope (Token Type)                       | |-----------------------|------------------------------------------------------------|-----------------------------------------------|--------------------------------------------------| | Account               | accounts:read (Organization, Bank, Customer)               |                                               | accounts:execute (Bank, Customer)                | | Bank                  | banks:read (Organization, Bank)                            | banks:write (Organization, Bank)              | banks:execute (Organization)                     | | Customer              | customers:read (Organization, Bank, Customer)              | customers:write (Bank, Customer)              | customers:execute (Bank)                         | | Counterparty          | counterparties:read (Organization, Bank, Customer)         | counterparties:write (Bank, Customer)         | counterparties:execute (Bank)                    | | Deposit Address       | deposit_addresses:read (Organization, Bank, Customer)      | deposit_addresses:write (Bank, Customer)      | deposit_addresses:execute (Bank, Customer)       | | External Bank Account | external_bank_accounts:read (Organization, Bank, Customer) | external_bank_accounts:write (Bank, Customer) | external_bank_accounts:execute (Bank, Customer)  | | External Wallet       | external_wallet:read (Organization, Bank, Customer)        |                                               | external_wallet:execute (Bank, Customer)         | | Organization          | organizations:read (Organization)                          | organizations:write (Organization)            |                                                  | | User                  | users:read (Organization)                                  |                                               | users:execute (Organization)                     | | Price                 | prices:read (Bank, Customer)                               |                                               |                                                  | | Quote                 | quotes:read (Organization, Bank, Customer)                 |                                               | quotes:execute (Organization, Bank, Customer)    | | Trade                 | trades:read (Organization, Bank, Customer)                 |                                               | trades:execute (Organization, Bank, Customer)    | | Transfer              | transfers:read (Organization, Bank, Customer)              |                                               | transfers:execute (Organization, Bank, Customer) | | Workflow              | workflows:read (Organization, Bank, Customer)              |                                               | workflows:execute (Bank, Customer)               | | Invoice               | invoices:read (Organization, Bank, Customer)               | invoices:write (Bank, Customer)               | invoices:execute (Bank, Customer)                |  ## Available Endpoints  The available APIs for the [Identity](<api_idp_swagger_ui_url>), [Organization](<api_platform_organization_swagger_ui_url>) and [Bank](<api_platform_bank_swagger_ui_url>) API services are listed below:  | API Service  | Model                | API Endpoint Path              | Description                                                                                       | |--------------|----------------------|--------------------------------|---------------------------------------------------------------------------------------------------| | Identity     | Bank                 | /api/bank_applications         | Create and list banks                                                                             | | Identity     | CustomerToken        | /api/customer_tokens           | Create customer JWT access tokens                                                                 | | Identity     | Organization         | /api/organization_applications | Create and list organizations                                                                     | | Identity     | Organization         | /api/users                     | Create and list organization users                                                                | | Organization | Organization         | /api/organizations             | APIs to retrieve and update organization name                                                     | | Bank         | Account              | /api/accounts                  | Create and list accounts, which hold a specific asset for a customers                             | | Bank         | Asset                | /api/assets                    | Get a list of assets supported by the platform (ex: BTC, ETH)                                     | | Bank         | Bank                 | /api/banks                     | Create, update and list banks, the parent to customers, accounts, etc                             | | Bank         | Customer             | /api/customers                 | Create and list customers                                                                         | | Bank         | Counterparty         | /api/counterparties            | Create and list counterparties                                                                    | | Bank         | DepositAddress       | /api/deposit_addresses         | Create, get and list deposit addresses                                                            | | Bank         | ExternalBankAccount  | /api/external_bank_accounts    | Create, get and list external bank accounts, which connect customer bank accounts to the platform | | Bank         | ExternalWallet       | /api/external_wallets          | Create, get, list and delete external wallets, which connect customer wallets to the platform     | | Bank         | IdentityVerification | /api/identity_verifications    | Create and list identity verifications, which are performed on customers for KYC                  | | Bank         | Invoice              | /api/invoices                  | Create, get, cancel and list invoices                                                             | | Bank         | PaymentInstruction   | /api/payment_instructions      | Create, get and list payment instructions for invoices                                            | | Bank         | Price                | /api/prices                    | Get the current prices for assets on the platform                                                 | | Bank         | Quote                | /api/quotes                    | Create and list quotes, which are required to execute trades                                      | | Bank         | Symbol               | /api/symbols                   | Get a list of symbols supported for trade (ex: BTC-USD)                                           | | Bank         | Trade                | /api/trades                    | Create and list trades, which buy or sell cryptocurrency                                          | | Bank         | Transfer             | /api/transfers                 | Create, get and list transfers (e.g., funding, book)                                              | | Bank         | Workflow             | /api/workflows                 | Create, get and list workflows                                                                    |  ## Understanding Object Models & Endpoints  **Organizations**  An `Organization` is meant to represent the organization partnering with Cybrid to use our platform.  An `Organization` typically does not directly interact with `customers`. Instead, an Organization has one or more `banks`, which encompass the financial service offerings of the platform.  **Banks**  A `Bank` is owned by an `Organization` and can be thought of as an environment or container for `customers` and product offerings. Banks are created in either `Sandbox` or `Production` mode, where `Sandbox` is the environment that you would test, prototype and build in prior to moving to `Production`.  An `Organization` can have multiple `banks`, in either `Sandbox` or `Production` environments. A `Sandbox Bank` will be backed by stubbed data and process flows. For instance, funding source transfer processes as well as trades will be simulated rather than performed, however asset prices are representative of real-world values. You have an unlimited amount of simulated fiat currency for testing purposes.  **Customers**  `Customers` represent your banking users on the platform. At present, we offer support for `Individuals` as Customers.  `Customers` must be verified (i.e., KYC'd) in our system before they can play any part on the platform, which means they must have an associated and a passing `Identity Verification`. See the Identity Verifications section for more details on how a customer can be verified.  `Customers` must also have an `Account` to be able to transact, in the desired asset class. See the Accounts APIs for more details on setting up accounts for the customer.   # noqa: E501

    The version of the OpenAPI document: v0.0.0
    Contact: support@cybrid.app
    Generated by: https://openapi-generator.tech
"""


import unittest

import cybrid_api_bank
from cybrid_api_bank.api.internal_bank_api import InternalBankApi  # noqa: E501


class TestInternalBankApi(unittest.TestCase):
    """InternalBankApi unit test stubs"""

    def setUp(self):
        self.api = InternalBankApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_internal_claim_exchange_settlement_payment_order(self):
        """Test case for internal_claim_exchange_settlement_payment_order

        Claim Exchange Settlement Payment Order  # noqa: E501
        """
        pass

    def test_internal_claim_expected_payment(self):
        """Test case for internal_claim_expected_payment

        Claim Expected Payment  # noqa: E501
        """
        pass

    def test_internal_create_account(self):
        """Test case for internal_create_account

        Create Account  # noqa: E501
        """
        pass

    def test_internal_create_activity_limit_configuration(self):
        """Test case for internal_create_activity_limit_configuration

        Create ActivityLimitConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_activity_report(self):
        """Test case for internal_create_activity_report

        Create Activity Report  # noqa: E501
        """
        pass

    def test_internal_create_bank(self):
        """Test case for internal_create_bank

        Create Bank  # noqa: E501
        """
        pass

    def test_internal_create_bank_account_service(self):
        """Test case for internal_create_bank_account_service

        Create BankAccountService  # noqa: E501
        """
        pass

    def test_internal_create_compliance_decision(self):
        """Test case for internal_create_compliance_decision

        Create Compliance Decision  # noqa: E501
        """
        pass

    def test_internal_create_country_code_configuration(self):
        """Test case for internal_create_country_code_configuration

        Create CountryCodeConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_crypto_asset_configuration(self):
        """Test case for internal_create_crypto_asset_configuration

        Create CryptoAssetConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_cybrid_account(self):
        """Test case for internal_create_cybrid_account

        Create CybridAccount  # noqa: E501
        """
        pass

    def test_internal_create_cybrid_gas_account_configuration(self):
        """Test case for internal_create_cybrid_gas_account_configuration

        Create CybridGasAccountConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_deposit_bank_account(self):
        """Test case for internal_create_deposit_bank_account

        Create Deposit Bank Account  # noqa: E501
        """
        pass

    def test_internal_create_exchange(self):
        """Test case for internal_create_exchange

        Create Exchange  # noqa: E501
        """
        pass

    def test_internal_create_exchange_account(self):
        """Test case for internal_create_exchange_account

        Create ExchangeAccount  # noqa: E501
        """
        pass

    def test_internal_create_exchange_monitor(self):
        """Test case for internal_create_exchange_monitor

        Create ExchangeMonitor  # noqa: E501
        """
        pass

    def test_internal_create_exchange_order(self):
        """Test case for internal_create_exchange_order

        Create ExchangeOrder  # noqa: E501
        """
        pass

    def test_internal_create_exchange_settlement(self):
        """Test case for internal_create_exchange_settlement

        Create Exchange Settlement  # noqa: E501
        """
        pass

    def test_internal_create_exchange_settlement_approval(self):
        """Test case for internal_create_exchange_settlement_approval

        Create Exchange Settlement Approval  # noqa: E501
        """
        pass

    def test_internal_create_exchange_settlement_completion(self):
        """Test case for internal_create_exchange_settlement_completion

        Create Exchange Settlement Completion  # noqa: E501
        """
        pass

    def test_internal_create_exchange_settlement_configuration(self):
        """Test case for internal_create_exchange_settlement_configuration

        Create ExchangeSettlementConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_exchange_settlement_payment_order(self):
        """Test case for internal_create_exchange_settlement_payment_order

        Create Exchange Settlement Payment Order  # noqa: E501
        """
        pass

    def test_internal_create_expected_payment(self):
        """Test case for internal_create_expected_payment

        Create Expected Payment  # noqa: E501
        """
        pass

    def test_internal_create_external_bank_account(self):
        """Test case for internal_create_external_bank_account

        Create ExternalBankAccount  # noqa: E501
        """
        pass

    def test_internal_create_external_wallet(self):
        """Test case for internal_create_external_wallet

        Create ExternalWallet  # noqa: E501
        """
        pass

    def test_internal_create_fee(self):
        """Test case for internal_create_fee

        Create Fee  # noqa: E501
        """
        pass

    def test_internal_create_fee_configuration(self):
        """Test case for internal_create_fee_configuration

        Create FeeConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_fiat_asset_configuration(self):
        """Test case for internal_create_fiat_asset_configuration

        Create FiatAssetConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_file(self):
        """Test case for internal_create_file

        Create File  # noqa: E501
        """
        pass

    def test_internal_create_internal_bank_account(self):
        """Test case for internal_create_internal_bank_account

        Create InternalBankAccount  # noqa: E501
        """
        pass

    def test_internal_create_internal_bank_account_configuration(self):
        """Test case for internal_create_internal_bank_account_configuration

        Create InternalBankAccountConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_internal_wallet(self):
        """Test case for internal_create_internal_wallet

        Create InternalWallet  # noqa: E501
        """
        pass

    def test_internal_create_internal_wallet_configuration(self):
        """Test case for internal_create_internal_wallet_configuration

        Create InternalWalletConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_payout_symbol_configuration(self):
        """Test case for internal_create_payout_symbol_configuration

        Create PayoutSymbolConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_quote(self):
        """Test case for internal_create_quote

        Create InternalQuote  # noqa: E501
        """
        pass

    def test_internal_create_reconciliation(self):
        """Test case for internal_create_reconciliation

        Create Reconciliation  # noqa: E501
        """
        pass

    def test_internal_create_stage(self):
        """Test case for internal_create_stage

        Create Stage  # noqa: E501
        """
        pass

    def test_internal_create_trade(self):
        """Test case for internal_create_trade

        Create Internal Trade  # noqa: E501
        """
        pass

    def test_internal_create_trading_symbol_configuration(self):
        """Test case for internal_create_trading_symbol_configuration

        Create TradingSymbolConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_transaction_monitor(self):
        """Test case for internal_create_transaction_monitor

        Create TransactionMonitor  # noqa: E501
        """
        pass

    def test_internal_create_transfer(self):
        """Test case for internal_create_transfer

        Create Transfer  # noqa: E501
        """
        pass

    def test_internal_create_transfer_rail_configuration(self):
        """Test case for internal_create_transfer_rail_configuration

        Create TransferRailConfiguration  # noqa: E501
        """
        pass

    def test_internal_create_transfer_screening(self):
        """Test case for internal_create_transfer_screening

        Create TransferScreening  # noqa: E501
        """
        pass

    def test_internal_create_wallet_service(self):
        """Test case for internal_create_wallet_service

        Create WalletService  # noqa: E501
        """
        pass

    def test_internal_crypto_funding_deposit_transfer(self):
        """Test case for internal_crypto_funding_deposit_transfer

        Create Crypto Funding Deposit Transfer  # noqa: E501
        """
        pass

    def test_internal_delete_activity_limit_configuration(self):
        """Test case for internal_delete_activity_limit_configuration

        Delete ActivityLimitConfiguration  # noqa: E501
        """
        pass

    def test_internal_delete_external_bank_account(self):
        """Test case for internal_delete_external_bank_account

        Delete External Bank Account  # noqa: E501
        """
        pass

    def test_internal_funding_deposit_transfer(self):
        """Test case for internal_funding_deposit_transfer

        Create Funding Deposit Transfer  # noqa: E501
        """
        pass

    def test_internal_get_bank(self):
        """Test case for internal_get_bank

        Get Bank  # noqa: E501
        """
        pass

    def test_internal_get_bank_account_service(self):
        """Test case for internal_get_bank_account_service

        Get BankAccountService  # noqa: E501
        """
        pass

    def test_internal_get_customer(self):
        """Test case for internal_get_customer

        Get Customer  # noqa: E501
        """
        pass

    def test_internal_get_cybrid_account(self):
        """Test case for internal_get_cybrid_account

        Get CybridAccount  # noqa: E501
        """
        pass

    def test_internal_get_exchange(self):
        """Test case for internal_get_exchange

        Get Exchange  # noqa: E501
        """
        pass

    def test_internal_get_exchange_account(self):
        """Test case for internal_get_exchange_account

        Get ExchangeAccount  # noqa: E501
        """
        pass

    def test_internal_get_exchange_settlement(self):
        """Test case for internal_get_exchange_settlement

        Get Exchange Settlement  # noqa: E501
        """
        pass

    def test_internal_get_exchange_settlement_obligation(self):
        """Test case for internal_get_exchange_settlement_obligation

        Get Exchange Settlement Obligation  # noqa: E501
        """
        pass

    def test_internal_get_exchange_settlement_payment_order(self):
        """Test case for internal_get_exchange_settlement_payment_order

        Get Exchange Settlement Payment Order  # noqa: E501
        """
        pass

    def test_internal_get_execution(self):
        """Test case for internal_get_execution

        Get Execution  # noqa: E501
        """
        pass

    def test_internal_get_expected_payment(self):
        """Test case for internal_get_expected_payment

        Get Expected Payment  # noqa: E501
        """
        pass

    def test_internal_get_external_bank_account(self):
        """Test case for internal_get_external_bank_account

        Get ExternalBankAccount  # noqa: E501
        """
        pass

    def test_internal_get_external_wallet(self):
        """Test case for internal_get_external_wallet

        Get ExternalWallet  # noqa: E501
        """
        pass

    def test_internal_get_external_wallet_screening(self):
        """Test case for internal_get_external_wallet_screening

        Get ExternalWalletScreening  # noqa: E501
        """
        pass

    def test_internal_get_file(self):
        """Test case for internal_get_file

        Get File  # noqa: E501
        """
        pass

    def test_internal_get_internal_bank_account(self):
        """Test case for internal_get_internal_bank_account

        Get InternalBankAccount  # noqa: E501
        """
        pass

    def test_internal_get_internal_wallet(self):
        """Test case for internal_get_internal_wallet

        Get InternalWallet  # noqa: E501
        """
        pass

    def test_internal_get_invoice(self):
        """Test case for internal_get_invoice

        Get Invoice  # noqa: E501
        """
        pass

    def test_internal_get_plan(self):
        """Test case for internal_get_plan

        Get Plan  # noqa: E501
        """
        pass

    def test_internal_get_quote(self):
        """Test case for internal_get_quote

        Get Internal Quote  # noqa: E501
        """
        pass

    def test_internal_get_reconciliation(self):
        """Test case for internal_get_reconciliation

        Get Reconciliation  # noqa: E501
        """
        pass

    def test_internal_get_trade(self):
        """Test case for internal_get_trade

        Get Internal Trade  # noqa: E501
        """
        pass

    def test_internal_get_transfer(self):
        """Test case for internal_get_transfer

        Get Transfer  # noqa: E501
        """
        pass

    def test_internal_get_transfer_screening(self):
        """Test case for internal_get_transfer_screening

        Get TransferScreening  # noqa: E501
        """
        pass

    def test_internal_get_wallet_service(self):
        """Test case for internal_get_wallet_service

        Get WalletService  # noqa: E501
        """
        pass

    def test_internal_list_accounts(self):
        """Test case for internal_list_accounts

        List Accounts  # noqa: E501
        """
        pass

    def test_internal_list_activity_limit_configurations(self):
        """Test case for internal_list_activity_limit_configurations

        List ActivityLimitConfigurations  # noqa: E501
        """
        pass

    def test_internal_list_bank_account_services(self):
        """Test case for internal_list_bank_account_services

        List BankAccountServices  # noqa: E501
        """
        pass

    def test_internal_list_banks(self):
        """Test case for internal_list_banks

        List Banks  # noqa: E501
        """
        pass

    def test_internal_list_crypto_asset_configurations(self):
        """Test case for internal_list_crypto_asset_configurations

        List CryptoAssetConfiguration  # noqa: E501
        """
        pass

    def test_internal_list_customers(self):
        """Test case for internal_list_customers

        List Customers  # noqa: E501
        """
        pass

    def test_internal_list_cybrid_accounts(self):
        """Test case for internal_list_cybrid_accounts

        List CybridAccounts  # noqa: E501
        """
        pass

    def test_internal_list_deposit_bank_accounts(self):
        """Test case for internal_list_deposit_bank_accounts

        List Deposit Bank Accounts  # noqa: E501
        """
        pass

    def test_internal_list_exchange_orders(self):
        """Test case for internal_list_exchange_orders

        List ExchangeOrder  # noqa: E501
        """
        pass

    def test_internal_list_exchange_settlement_configurations(self):
        """Test case for internal_list_exchange_settlement_configurations

        List ExchangeSettlementConfigurations  # noqa: E501
        """
        pass

    def test_internal_list_exchange_settlement_payment_orders(self):
        """Test case for internal_list_exchange_settlement_payment_orders

        List Exchange Settlement Payment Orders  # noqa: E501
        """
        pass

    def test_internal_list_exchanges(self):
        """Test case for internal_list_exchanges

        List Exchanges  # noqa: E501
        """
        pass

    def test_internal_list_expected_payments(self):
        """Test case for internal_list_expected_payments

        List Expected Payments  # noqa: E501
        """
        pass

    def test_internal_list_external_bank_accounts(self):
        """Test case for internal_list_external_bank_accounts

        List ExternalBankAccounts  # noqa: E501
        """
        pass

    def test_internal_list_external_wallets(self):
        """Test case for internal_list_external_wallets

        List ExternalWallets  # noqa: E501
        """
        pass

    def test_internal_list_fee_configurations(self):
        """Test case for internal_list_fee_configurations

        List FeeConfiguration  # noqa: E501
        """
        pass

    def test_internal_list_fees(self):
        """Test case for internal_list_fees

        List Fees  # noqa: E501
        """
        pass

    def test_internal_list_internal_bank_accounts(self):
        """Test case for internal_list_internal_bank_accounts

        List InternalBankAccounts  # noqa: E501
        """
        pass

    def test_internal_list_internal_wallets(self):
        """Test case for internal_list_internal_wallets

        List InternalWallets  # noqa: E501
        """
        pass

    def test_internal_list_invoices(self):
        """Test case for internal_list_invoices

        List Invoices  # noqa: E501
        """
        pass

    def test_internal_list_reconciliations(self):
        """Test case for internal_list_reconciliations

        List Reconciliations  # noqa: E501
        """
        pass

    def test_internal_list_trades(self):
        """Test case for internal_list_trades

        List Trades  # noqa: E501
        """
        pass

    def test_internal_list_trading_symbol_configurations(self):
        """Test case for internal_list_trading_symbol_configurations

        List TradingSymbolConfigurations  # noqa: E501
        """
        pass

    def test_internal_list_transactions(self):
        """Test case for internal_list_transactions

        List Transactions  # noqa: E501
        """
        pass

    def test_internal_list_transfers(self):
        """Test case for internal_list_transfers

        List Transfers  # noqa: E501
        """
        pass

    def test_internal_list_wallet_services(self):
        """Test case for internal_list_wallet_services

        List WalletServices  # noqa: E501
        """
        pass

    def test_internal_patch_account(self):
        """Test case for internal_patch_account

        Patch Account  # noqa: E501
        """
        pass

    def test_internal_patch_activity_limit_configuration(self):
        """Test case for internal_patch_activity_limit_configuration

        Patch ActivityLimitConfiguration  # noqa: E501
        """
        pass

    def test_internal_patch_bank(self):
        """Test case for internal_patch_bank

        Patch Bank  # noqa: E501
        """
        pass

    def test_internal_patch_bank_account_service(self):
        """Test case for internal_patch_bank_account_service

        Patch Internal BankAccount  # noqa: E501
        """
        pass

    def test_internal_patch_business_detail(self):
        """Test case for internal_patch_business_detail

        Patch Business Details  # noqa: E501
        """
        pass

    def test_internal_patch_counterparty(self):
        """Test case for internal_patch_counterparty

        Patch Counterparty  # noqa: E501
        """
        pass

    def test_internal_patch_crypto_asset_configuration(self):
        """Test case for internal_patch_crypto_asset_configuration

        Patch CryptoAssetConfiguration  # noqa: E501
        """
        pass

    def test_internal_patch_customer(self):
        """Test case for internal_patch_customer

        Patch Customer  # noqa: E501
        """
        pass

    def test_internal_patch_cybrid_account(self):
        """Test case for internal_patch_cybrid_account

        Patch Cybrid Account  # noqa: E501
        """
        pass

    def test_internal_patch_deposit_address(self):
        """Test case for internal_patch_deposit_address

        Patch Deposit Address  # noqa: E501
        """
        pass

    def test_internal_patch_deposit_bank_account(self):
        """Test case for internal_patch_deposit_bank_account

        Patch DepositBankAccount  # noqa: E501
        """
        pass

    def test_internal_patch_exchange_account(self):
        """Test case for internal_patch_exchange_account

        Patch Exchange Account  # noqa: E501
        """
        pass

    def test_internal_patch_exchange_order(self):
        """Test case for internal_patch_exchange_order

        Patch ExchangeOrder  # noqa: E501
        """
        pass

    def test_internal_patch_exchange_settlement(self):
        """Test case for internal_patch_exchange_settlement

        Patch Exchange Settlement  # noqa: E501
        """
        pass

    def test_internal_patch_external_bank_account(self):
        """Test case for internal_patch_external_bank_account

        Patch ExternalBankAccount  # noqa: E501
        """
        pass

    def test_internal_patch_external_wallet(self):
        """Test case for internal_patch_external_wallet

        Patch ExternalWallet  # noqa: E501
        """
        pass

    def test_internal_patch_external_wallet_screening(self):
        """Test case for internal_patch_external_wallet_screening

        Patch External Wallet Screening  # noqa: E501
        """
        pass

    def test_internal_patch_fee(self):
        """Test case for internal_patch_fee

        Patch Fee  # noqa: E501
        """
        pass

    def test_internal_patch_files(self):
        """Test case for internal_patch_files

        Patch Files  # noqa: E501
        """
        pass

    def test_internal_patch_identity_verification(self):
        """Test case for internal_patch_identity_verification

        Patch Identity Verification  # noqa: E501
        """
        pass

    def test_internal_patch_internal_bank_account(self):
        """Test case for internal_patch_internal_bank_account

        Patch Internal Bank Account  # noqa: E501
        """
        pass

    def test_internal_patch_internal_wallet(self):
        """Test case for internal_patch_internal_wallet

        Patch Internal Wallet  # noqa: E501
        """
        pass

    def test_internal_patch_internal_wallet_group(self):
        """Test case for internal_patch_internal_wallet_group

        Patch Internal Wallet  # noqa: E501
        """
        pass

    def test_internal_patch_invoice(self):
        """Test case for internal_patch_invoice

        Patch Invoice  # noqa: E501
        """
        pass

    def test_internal_patch_payment_instruction(self):
        """Test case for internal_patch_payment_instruction

        Patch Payment Instruction  # noqa: E501
        """
        pass

    def test_internal_patch_person_detail(self):
        """Test case for internal_patch_person_detail

        Patch Person Details  # noqa: E501
        """
        pass

    def test_internal_patch_trade(self):
        """Test case for internal_patch_trade

        Patch Trade  # noqa: E501
        """
        pass

    def test_internal_patch_trading_symbol_configuration(self):
        """Test case for internal_patch_trading_symbol_configuration

        Patch TradingSymbolConfiguration  # noqa: E501
        """
        pass

    def test_internal_patch_transfer(self):
        """Test case for internal_patch_transfer

        Patch Transfer  # noqa: E501
        """
        pass

    def test_internal_patch_transfer_screening(self):
        """Test case for internal_patch_transfer_screening

        Patch External Wallet Screening  # noqa: E501
        """
        pass

    def test_internal_patch_wallet_service(self):
        """Test case for internal_patch_wallet_service

        Patch Internal Wallet  # noqa: E501
        """
        pass

    def test_internal_patch_workflow(self):
        """Test case for internal_patch_workflow

        Patch Workflow  # noqa: E501
        """
        pass

    def test_internal_signal_external_wallet_screening(self):
        """Test case for internal_signal_external_wallet_screening

        Signal External Wallet Screening  # noqa: E501
        """
        pass

    def test_internal_signal_identity_verification(self):
        """Test case for internal_signal_identity_verification

        Signal Identity Verification  # noqa: E501
        """
        pass

    def test_internal_signal_invoice(self):
        """Test case for internal_signal_invoice

        Signal Invoice  # noqa: E501
        """
        pass

    def test_internal_signal_transfer(self):
        """Test case for internal_signal_transfer

        Signal Transfer  # noqa: E501
        """
        pass

    def test_patch_internal_execution(self):
        """Test case for patch_internal_execution

        Patch Execution  # noqa: E501
        """
        pass

    def test_patch_internal_plan(self):
        """Test case for patch_internal_plan

        Patch Plan  # noqa: E501
        """
        pass

    def test_patch_internal_stage(self):
        """Test case for patch_internal_stage

        Patch Stage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
