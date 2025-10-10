"""
    Cybrid Bank API

    # Cybrid API documentation  Welcome to Cybrid, an all-in-one crypto platform that enables you to easily **build** and **launch** white-label crypto products or services.  In these documents, you'll find details on how our REST API operates and generally how our platform functions.  If you're looking for our UI SDK Widgets for Web or Mobile (iOS/Android), generated API clients, or demo applications, head over to our [Github repo](https://github.com/Cybrid-app).  💡 We recommend bookmarking the [Cybrid LinkTree](https://linktr.ee/cybridtechnologies) which contains many helpful links to platform resources.  ## Getting Started  This is Cybrid's public interactive API documentation, which allows you to fully test our APIs. If you'd like to use a different tool to exercise our APIs, you can download the [Open API 3.0 yaml](<api_platform_bank_swagger_schema_url>) for import.  If you're new to our APIs and the Cybrid Platform, follow the below guides to get set up and familiar with the platform:  1. [Introduction](https://docs.cybrid.xyz/docs/introduction) 2. [Platform Introduction](https://docs.cybrid.xyz/docs/how-is-cybrid-architected) 3. [Testing with Hosted Web Demo App](https://docs.cybrid.xyz/docs/testing-with-hosted-web-demo-app)  In [Getting Started in the Cybrid Sandbox](https://docs.cybrid.xyz/docs/how-do-i-get-started-with-the-sandbox), we walk you through how to use the [Cybrid Sandbox](https://id.sandbox.cybrid.app/) to create a test bank and generate API keys. In [Getting Ready for Trading](https://kb.cybrid.xyz/getting-ready-for-trading), we walk through creating customers, customer identities, accounts, as well as executing quotes and trades.  ## Working with the Cybrid Platform  There are three primary ways you can interact with the Cybrid platform:  1. Directly via our RESTful API (this documentation) 2. Using our API clients available in a variety of languages ([Angular](https://github.com/Cybrid-app/cybrid-api-bank-angular), [Java](https://github.com/Cybrid-app/cybrid-api-bank-java), [Kotlin](https://github.com/Cybrid-app/cybrid-api-bank-kotlin), [Python](https://github.com/Cybrid-app/cybrid-api-bank-python), [Ruby](https://github.com/Cybrid-app/cybrid-api-bank-ruby), [Swift](https://github.com/Cybrid-app/cybrid-api-bank-swift) or [Typescript](https://github.com/Cybrid-app/cybrid-api-bank-typescript)) 3. Integrating a platform specific SDK ([Web](https://github.com/Cybrid-app/cybrid-sdk-web), [Android](https://github.com/Cybrid-app/cybrid-sdk-android), [iOS](https://github.com/Cybrid-app/cybrid-sdk-ios))  Our complete set of APIs allows you to manage resources across three distinct areas: your `Organization`, your `Banks` and your `Identities`. For most of your testing and interaction you'll be using the `Bank` API, which is where the majority of APIs reside.  *The complete set of APIs can be found on the following pages:*  | API                                                              | Description                                                 | |------------------------------------------------------------------|-------------------------------------------------------------| | [Organization API](<api_platform_organization_swagger_ui_url>)   | APIs to manage organizations                                | | [Bank API](<api_platform_bank_swagger_ui_url>)                   | APIs to manage banks (and all downstream customer activity) | | [Identities API](<api_idp_swagger_ui_url>)                       | APIs to manage organization and bank identities             |  For questions please contact [Support](mailto:support@cybrid.xyz) at any time for assistance, or contact the [Product Team](mailto:product@cybrid.xyz) for product suggestions.  ## Authenticating with the API  The Cybrid Platform uses OAuth 2.0 Bearer Tokens to authenticate requests to the platform. Credentials to create `Organization` and `Bank` tokens can be generated via the [Cybrid Sandbox](<api_idp_url>). Access tokens can be generated for a `Customer` as well via the [Cybrid IdP](<api_idp_url>) as well.  An `Organization` access token applies broadly to the whole Organization and all of its `Banks`, whereas, a `Bank` access token is specific to an individual Bank. `Customer` tokens, similarly, are scoped to a specific customer in a bank.  Both `Organization` and `Bank` tokens can be created using the OAuth Client Credential Grant flow. Each Organization and Bank has its own unique `Client ID` and `Secret` that allows for machine-to-machine authentication.  A `Bank` can then generate `Customer` access tokens via API using our [Identities API](<api_idp_swagger_ui_url>).  <font color=\"orange\">**⚠️ Never share your Client ID or Secret publicly or in your source code repository.**</font>  Your `Client ID` and `Secret` can be exchanged for a time-limited `Bearer Token` by interacting with the Cybrid Identity Provider or through interacting with the **Authorize** button in this document.  The following curl command can be used to quickly generate a `Bearer Token` for use in testing the API or demo applications.  ``` # Example request when using Bank credentials curl -X POST <api_idp_url>/oauth/token -d '{     \"grant_type\": \"client_credentials\",     \"client_id\": \"<Your Client ID>\",     \"client_secret\": \"<Your Secret>\",     \"scope\": \"<api_platform_bank_scopes>\"   }' -H \"Content-Type: application/json\"  # When using Organization credentials set `scope` to '<api_platform_organization_scopes>' ``` <font color=\"orange\">**⚠️ Note: The above curl will create a bearer token with full scope access. Delete scopes if you'd like to restrict access.**</font>  ## Authentication Scopes  The Cybrid platform supports the use of scopes to control the level of access a token is limited to. Scopes do not grant access to resources; instead, they provide limits, in support of the least privilege principal.  The following scopes are available on the platform and can be requested when generating either an Organization, Bank or Customer token. Generally speaking, the _Read_ scope is required to read and list resources, the _Write_ scope is required to update a resource and the _Execute_ scope is required to create a resource.  | Resource              | Read scope (Token Type)                                    | Write scope (Token Type)                      | Execute scope (Token Type)                       | |-----------------------|------------------------------------------------------------|-----------------------------------------------|--------------------------------------------------| | Account               | accounts:read (Organization, Bank, Customer)               |                                               | accounts:execute (Bank, Customer)                | | Bank                  | banks:read (Organization, Bank)                            | banks:write (Organization, Bank)              | banks:execute (Organization)                     | | Customer              | customers:read (Organization, Bank, Customer)              | customers:write (Bank, Customer)              | customers:execute (Bank)                         | | Counterparty          | counterparties:read (Organization, Bank, Customer)         | counterparties:write (Bank, Customer)         | counterparties:execute (Bank)                    | | Deposit Address       | deposit_addresses:read (Organization, Bank, Customer)      | deposit_addresses:write (Bank, Customer)      | deposit_addresses:execute (Bank, Customer)       | | External Bank Account | external_bank_accounts:read (Organization, Bank, Customer) | external_bank_accounts:write (Bank, Customer) | external_bank_accounts:execute (Bank, Customer)  | | External Wallet       | external_wallet:read (Organization, Bank, Customer)        |                                               | external_wallet:execute (Bank, Customer)         | | Organization          | organizations:read (Organization)                          | organizations:write (Organization)            |                                                  | | User                  | users:read (Organization)                                  |                                               | users:execute (Organization)                     | | Price                 | prices:read (Bank, Customer)                               |                                               |                                                  | | Quote                 | quotes:read (Organization, Bank, Customer)                 |                                               | quotes:execute (Organization, Bank, Customer)    | | Trade                 | trades:read (Organization, Bank, Customer)                 |                                               | trades:execute (Organization, Bank, Customer)    | | Transfer              | transfers:read (Organization, Bank, Customer)              |                                               | transfers:execute (Organization, Bank, Customer) | | Workflow              | workflows:read (Organization, Bank, Customer)              |                                               | workflows:execute (Bank, Customer)               | | Invoice               | invoices:read (Organization, Bank, Customer)               | invoices:write (Bank, Customer)               | invoices:execute (Bank, Customer)                |  ## Available Endpoints  The available APIs for the [Identity](<api_idp_swagger_ui_url>), [Organization](<api_platform_organization_swagger_ui_url>) and [Bank](<api_platform_bank_swagger_ui_url>) API services are listed below:  | API Service  | Model                | API Endpoint Path              | Description                                                                                       | |--------------|----------------------|--------------------------------|---------------------------------------------------------------------------------------------------| | Identity     | Bank                 | /api/bank_applications         | Create and list banks                                                                             | | Identity     | CustomerToken        | /api/customer_tokens           | Create customer JWT access tokens                                                                 | | Identity     | Organization         | /api/organization_applications | Create and list organizations                                                                     | | Identity     | Organization         | /api/users                     | Create and list organization users                                                                | | Organization | Organization         | /api/organizations             | APIs to retrieve and update organization name                                                     | | Bank         | Account              | /api/accounts                  | Create and list accounts, which hold a specific asset for a customers                             | | Bank         | Asset                | /api/assets                    | Get a list of assets supported by the platform (ex: BTC, ETH)                                     | | Bank         | Bank                 | /api/banks                     | Create, update and list banks, the parent to customers, accounts, etc                             | | Bank         | Customer             | /api/customers                 | Create and list customers                                                                         | | Bank         | Counterparty         | /api/counterparties            | Create and list counterparties                                                                    | | Bank         | DepositAddress       | /api/deposit_addresses         | Create, get and list deposit addresses                                                            | | Bank         | ExternalBankAccount  | /api/external_bank_accounts    | Create, get and list external bank accounts, which connect customer bank accounts to the platform | | Bank         | ExternalWallet       | /api/external_wallets          | Create, get, list and delete external wallets, which connect customer wallets to the platform     | | Bank         | IdentityVerification | /api/identity_verifications    | Create and list identity verifications, which are performed on customers for KYC                  | | Bank         | Invoice              | /api/invoices                  | Create, get, cancel and list invoices                                                             | | Bank         | PaymentInstruction   | /api/payment_instructions      | Create, get and list payment instructions for invoices                                            | | Bank         | Price                | /api/prices                    | Get the current prices for assets on the platform                                                 | | Bank         | Quote                | /api/quotes                    | Create and list quotes, which are required to execute trades                                      | | Bank         | Symbol               | /api/symbols                   | Get a list of symbols supported for trade (ex: BTC-USD)                                           | | Bank         | Trade                | /api/trades                    | Create and list trades, which buy or sell cryptocurrency                                          | | Bank         | Transfer             | /api/transfers                 | Create, get and list transfers (e.g., funding, book)                                              | | Bank         | Workflow             | /api/workflows                 | Create, get and list workflows                                                                    |  ## Understanding Object Models & Endpoints  **Organizations**  An `Organization` is meant to represent the organization partnering with Cybrid to use our platform.  An `Organization` typically does not directly interact with `customers`. Instead, an Organization has one or more `banks`, which encompass the financial service offerings of the platform.  **Banks**  A `Bank` is owned by an `Organization` and can be thought of as an environment or container for `customers` and product offerings. Banks are created in either `Sandbox` or `Production` mode, where `Sandbox` is the environment that you would test, prototype and build in prior to moving to `Production`.  An `Organization` can have multiple `banks`, in either `Sandbox` or `Production` environments. A `Sandbox Bank` will be backed by stubbed data and process flows. For instance, funding source transfer processes as well as trades will be simulated rather than performed, however asset prices are representative of real-world values. You have an unlimited amount of simulated fiat currency for testing purposes.  **Customers**  `Customers` represent your banking users on the platform. At present, we offer support for `Individuals` as Customers.  `Customers` must be verified (i.e., KYC'd) in our system before they can play any part on the platform, which means they must have an associated and a passing `Identity Verification`. See the Identity Verifications section for more details on how a customer can be verified.  `Customers` must also have an `Account` to be able to transact, in the desired asset class. See the Accounts APIs for more details on setting up accounts for the customer.   # noqa: E501

    The version of the OpenAPI document: v0.0.0
    Contact: support@cybrid.app
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cybrid_api_bank.api_client import ApiClient, Endpoint as _Endpoint
from cybrid_api_bank.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cybrid_api_bank.model.account import Account
from cybrid_api_bank.model.account_list import AccountList
from cybrid_api_bank.model.counterparty import Counterparty
from cybrid_api_bank.model.customer import Customer
from cybrid_api_bank.model.customer_list import CustomerList
from cybrid_api_bank.model.deposit_address import DepositAddress
from cybrid_api_bank.model.deposit_bank_account import DepositBankAccount
from cybrid_api_bank.model.deposit_bank_account_list import DepositBankAccountList
from cybrid_api_bank.model.error_response import ErrorResponse
from cybrid_api_bank.model.identity_verification import IdentityVerification
from cybrid_api_bank.model.internal_activity_limit_configuration import InternalActivityLimitConfiguration
from cybrid_api_bank.model.internal_activity_limit_configuration_list import InternalActivityLimitConfigurationList
from cybrid_api_bank.model.internal_activity_report import InternalActivityReport
from cybrid_api_bank.model.internal_bank import InternalBank
from cybrid_api_bank.model.internal_bank_account_service import InternalBankAccountService
from cybrid_api_bank.model.internal_bank_account_service_list import InternalBankAccountServiceList
from cybrid_api_bank.model.internal_bank_list import InternalBankList
from cybrid_api_bank.model.internal_business_detail import InternalBusinessDetail
from cybrid_api_bank.model.internal_compliance_decision import InternalComplianceDecision
from cybrid_api_bank.model.internal_country_code_configuration import InternalCountryCodeConfiguration
from cybrid_api_bank.model.internal_create_exchange_settlement_approval202_response import InternalCreateExchangeSettlementApproval202Response
from cybrid_api_bank.model.internal_crypto_asset_configuration import InternalCryptoAssetConfiguration
from cybrid_api_bank.model.internal_crypto_asset_configuration_list import InternalCryptoAssetConfigurationList
from cybrid_api_bank.model.internal_crypto_funding_deposit_transfer import InternalCryptoFundingDepositTransfer
from cybrid_api_bank.model.internal_cybrid_account import InternalCybridAccount
from cybrid_api_bank.model.internal_cybrid_account_list import InternalCybridAccountList
from cybrid_api_bank.model.internal_cybrid_gas_account_configuration import InternalCybridGasAccountConfiguration
from cybrid_api_bank.model.internal_exchange import InternalExchange
from cybrid_api_bank.model.internal_exchange_account import InternalExchangeAccount
from cybrid_api_bank.model.internal_exchange_list import InternalExchangeList
from cybrid_api_bank.model.internal_exchange_monitor import InternalExchangeMonitor
from cybrid_api_bank.model.internal_exchange_order import InternalExchangeOrder
from cybrid_api_bank.model.internal_exchange_order_list import InternalExchangeOrderList
from cybrid_api_bank.model.internal_exchange_settlement import InternalExchangeSettlement
from cybrid_api_bank.model.internal_exchange_settlement_configuration import InternalExchangeSettlementConfiguration
from cybrid_api_bank.model.internal_exchange_settlement_configuration_list import InternalExchangeSettlementConfigurationList
from cybrid_api_bank.model.internal_exchange_settlement_obligation import InternalExchangeSettlementObligation
from cybrid_api_bank.model.internal_exchange_settlement_payment_order import InternalExchangeSettlementPaymentOrder
from cybrid_api_bank.model.internal_exchange_settlement_payment_order_list import InternalExchangeSettlementPaymentOrderList
from cybrid_api_bank.model.internal_execution import InternalExecution
from cybrid_api_bank.model.internal_expected_payment import InternalExpectedPayment
from cybrid_api_bank.model.internal_expected_payment_list import InternalExpectedPaymentList
from cybrid_api_bank.model.internal_external_bank_account import InternalExternalBankAccount
from cybrid_api_bank.model.internal_external_bank_account_list import InternalExternalBankAccountList
from cybrid_api_bank.model.internal_external_wallet import InternalExternalWallet
from cybrid_api_bank.model.internal_external_wallet_list import InternalExternalWalletList
from cybrid_api_bank.model.internal_external_wallet_screening import InternalExternalWalletScreening
from cybrid_api_bank.model.internal_fee_charge import InternalFeeCharge
from cybrid_api_bank.model.internal_fee_charge_list import InternalFeeChargeList
from cybrid_api_bank.model.internal_fee_configuration import InternalFeeConfiguration
from cybrid_api_bank.model.internal_fee_configuration_list import InternalFeeConfigurationList
from cybrid_api_bank.model.internal_fiat_asset_configuration import InternalFiatAssetConfiguration
from cybrid_api_bank.model.internal_funding_deposit_transfer import InternalFundingDepositTransfer
from cybrid_api_bank.model.internal_internal_bank_account import InternalInternalBankAccount
from cybrid_api_bank.model.internal_internal_bank_account_configuration import InternalInternalBankAccountConfiguration
from cybrid_api_bank.model.internal_internal_bank_account_list import InternalInternalBankAccountList
from cybrid_api_bank.model.internal_internal_invoice_list import InternalInternalInvoiceList
from cybrid_api_bank.model.internal_internal_wallet import InternalInternalWallet
from cybrid_api_bank.model.internal_internal_wallet_configuration import InternalInternalWalletConfiguration
from cybrid_api_bank.model.internal_internal_wallet_group import InternalInternalWalletGroup
from cybrid_api_bank.model.internal_internal_wallet_list import InternalInternalWalletList
from cybrid_api_bank.model.internal_invoice import InternalInvoice
from cybrid_api_bank.model.internal_payout_symbol_configuration import InternalPayoutSymbolConfiguration
from cybrid_api_bank.model.internal_person_detail import InternalPersonDetail
from cybrid_api_bank.model.internal_plan import InternalPlan
from cybrid_api_bank.model.internal_post_account import InternalPostAccount
from cybrid_api_bank.model.internal_post_deposit_bank_account import InternalPostDepositBankAccount
from cybrid_api_bank.model.internal_post_fee_configuration import InternalPostFeeConfiguration
from cybrid_api_bank.model.internal_post_quote import InternalPostQuote
from cybrid_api_bank.model.internal_quote import InternalQuote
from cybrid_api_bank.model.internal_reconciliation import InternalReconciliation
from cybrid_api_bank.model.internal_reconciliation_list import InternalReconciliationList
from cybrid_api_bank.model.internal_stage import InternalStage
from cybrid_api_bank.model.internal_trade import InternalTrade
from cybrid_api_bank.model.internal_trading_symbol_configuration import InternalTradingSymbolConfiguration
from cybrid_api_bank.model.internal_trading_symbol_configuration_list import InternalTradingSymbolConfigurationList
from cybrid_api_bank.model.internal_transaction_monitor import InternalTransactionMonitor
from cybrid_api_bank.model.internal_transactions_list import InternalTransactionsList
from cybrid_api_bank.model.internal_transfer import InternalTransfer
from cybrid_api_bank.model.internal_transfer_list import InternalTransferList
from cybrid_api_bank.model.internal_transfer_rail_configuration import InternalTransferRailConfiguration
from cybrid_api_bank.model.internal_transfer_screening import InternalTransferScreening
from cybrid_api_bank.model.internal_wallet_service import InternalWalletService
from cybrid_api_bank.model.internal_wallet_service_list import InternalWalletServiceList
from cybrid_api_bank.model.patch_internal_account import PatchInternalAccount
from cybrid_api_bank.model.patch_internal_activity_limit_configuration import PatchInternalActivityLimitConfiguration
from cybrid_api_bank.model.patch_internal_bank import PatchInternalBank
from cybrid_api_bank.model.patch_internal_bank_account_service import PatchInternalBankAccountService
from cybrid_api_bank.model.patch_internal_business_detail import PatchInternalBusinessDetail
from cybrid_api_bank.model.patch_internal_counterparty import PatchInternalCounterparty
from cybrid_api_bank.model.patch_internal_crypto_asset_configuration import PatchInternalCryptoAssetConfiguration
from cybrid_api_bank.model.patch_internal_customer import PatchInternalCustomer
from cybrid_api_bank.model.patch_internal_cybrid_account import PatchInternalCybridAccount
from cybrid_api_bank.model.patch_internal_deposit_address import PatchInternalDepositAddress
from cybrid_api_bank.model.patch_internal_deposit_bank_account import PatchInternalDepositBankAccount
from cybrid_api_bank.model.patch_internal_exchange_account import PatchInternalExchangeAccount
from cybrid_api_bank.model.patch_internal_exchange_order import PatchInternalExchangeOrder
from cybrid_api_bank.model.patch_internal_exchange_settlement import PatchInternalExchangeSettlement
from cybrid_api_bank.model.patch_internal_execution import PatchInternalExecution
from cybrid_api_bank.model.patch_internal_external_bank_account import PatchInternalExternalBankAccount
from cybrid_api_bank.model.patch_internal_external_wallet import PatchInternalExternalWallet
from cybrid_api_bank.model.patch_internal_external_wallet_screening import PatchInternalExternalWalletScreening
from cybrid_api_bank.model.patch_internal_fee_charge import PatchInternalFeeCharge
from cybrid_api_bank.model.patch_internal_file import PatchInternalFile
from cybrid_api_bank.model.patch_internal_identity_verification import PatchInternalIdentityVerification
from cybrid_api_bank.model.patch_internal_internal_bank_account import PatchInternalInternalBankAccount
from cybrid_api_bank.model.patch_internal_internal_wallet import PatchInternalInternalWallet
from cybrid_api_bank.model.patch_internal_internal_wallet_group import PatchInternalInternalWalletGroup
from cybrid_api_bank.model.patch_internal_invoice import PatchInternalInvoice
from cybrid_api_bank.model.patch_internal_payment_instruction import PatchInternalPaymentInstruction
from cybrid_api_bank.model.patch_internal_person_detail import PatchInternalPersonDetail
from cybrid_api_bank.model.patch_internal_plan import PatchInternalPlan
from cybrid_api_bank.model.patch_internal_stage import PatchInternalStage
from cybrid_api_bank.model.patch_internal_trade import PatchInternalTrade
from cybrid_api_bank.model.patch_internal_trading_symbol_configuration import PatchInternalTradingSymbolConfiguration
from cybrid_api_bank.model.patch_internal_transfer import PatchInternalTransfer
from cybrid_api_bank.model.patch_internal_transfer_screening import PatchInternalTransferScreening
from cybrid_api_bank.model.patch_internal_wallet_service import PatchInternalWalletService
from cybrid_api_bank.model.patch_internal_workflow import PatchInternalWorkflow
from cybrid_api_bank.model.payment_instruction import PaymentInstruction
from cybrid_api_bank.model.platform_file import PlatformFile
from cybrid_api_bank.model.post_file import PostFile
from cybrid_api_bank.model.post_internal_activity_limit_configuration import PostInternalActivityLimitConfiguration
from cybrid_api_bank.model.post_internal_activity_report import PostInternalActivityReport
from cybrid_api_bank.model.post_internal_bank import PostInternalBank
from cybrid_api_bank.model.post_internal_bank_account_service import PostInternalBankAccountService
from cybrid_api_bank.model.post_internal_claim_exchange_settlement_payment_order import PostInternalClaimExchangeSettlementPaymentOrder
from cybrid_api_bank.model.post_internal_claim_expected_payment import PostInternalClaimExpectedPayment
from cybrid_api_bank.model.post_internal_compliance_decision import PostInternalComplianceDecision
from cybrid_api_bank.model.post_internal_country_code_configuration import PostInternalCountryCodeConfiguration
from cybrid_api_bank.model.post_internal_crypto_asset_configuration import PostInternalCryptoAssetConfiguration
from cybrid_api_bank.model.post_internal_crypto_funding_deposit_transfer import PostInternalCryptoFundingDepositTransfer
from cybrid_api_bank.model.post_internal_cybrid_account import PostInternalCybridAccount
from cybrid_api_bank.model.post_internal_cybrid_gas_account_configuration import PostInternalCybridGasAccountConfiguration
from cybrid_api_bank.model.post_internal_exchange import PostInternalExchange
from cybrid_api_bank.model.post_internal_exchange_account import PostInternalExchangeAccount
from cybrid_api_bank.model.post_internal_exchange_monitor import PostInternalExchangeMonitor
from cybrid_api_bank.model.post_internal_exchange_order import PostInternalExchangeOrder
from cybrid_api_bank.model.post_internal_exchange_settlement import PostInternalExchangeSettlement
from cybrid_api_bank.model.post_internal_exchange_settlement_configuration import PostInternalExchangeSettlementConfiguration
from cybrid_api_bank.model.post_internal_exchange_settlement_payment_order import PostInternalExchangeSettlementPaymentOrder
from cybrid_api_bank.model.post_internal_expected_payment import PostInternalExpectedPayment
from cybrid_api_bank.model.post_internal_external_bank_account import PostInternalExternalBankAccount
from cybrid_api_bank.model.post_internal_external_wallet import PostInternalExternalWallet
from cybrid_api_bank.model.post_internal_fee_charge import PostInternalFeeCharge
from cybrid_api_bank.model.post_internal_fiat_asset_configuration import PostInternalFiatAssetConfiguration
from cybrid_api_bank.model.post_internal_funding_deposit_transfer import PostInternalFundingDepositTransfer
from cybrid_api_bank.model.post_internal_internal_bank_account import PostInternalInternalBankAccount
from cybrid_api_bank.model.post_internal_internal_bank_account_configuration import PostInternalInternalBankAccountConfiguration
from cybrid_api_bank.model.post_internal_internal_wallet import PostInternalInternalWallet
from cybrid_api_bank.model.post_internal_internal_wallet_configuration import PostInternalInternalWalletConfiguration
from cybrid_api_bank.model.post_internal_payout_symbol_configuration import PostInternalPayoutSymbolConfiguration
from cybrid_api_bank.model.post_internal_reconciliation import PostInternalReconciliation
from cybrid_api_bank.model.post_internal_stage import PostInternalStage
from cybrid_api_bank.model.post_internal_trade import PostInternalTrade
from cybrid_api_bank.model.post_internal_trading_symbol_configuration import PostInternalTradingSymbolConfiguration
from cybrid_api_bank.model.post_internal_transaction_monitor import PostInternalTransactionMonitor
from cybrid_api_bank.model.post_internal_transfer import PostInternalTransfer
from cybrid_api_bank.model.post_internal_transfer_rail_configuration import PostInternalTransferRailConfiguration
from cybrid_api_bank.model.post_internal_transfer_screening import PostInternalTransferScreening
from cybrid_api_bank.model.post_internal_wallet_service import PostInternalWalletService
from cybrid_api_bank.model.post_signal_internal_external_wallet_screening import PostSignalInternalExternalWalletScreening
from cybrid_api_bank.model.post_signal_internal_identity_verification import PostSignalInternalIdentityVerification
from cybrid_api_bank.model.trade_list import TradeList
from cybrid_api_bank.model.transfer import Transfer
from cybrid_api_bank.model.workflow import Workflow


class InternalBankApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.internal_claim_exchange_settlement_payment_order_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementPaymentOrder,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_payment_orders/{guid}/claim',
                'operation_id': 'internal_claim_exchange_settlement_payment_order',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'post_internal_claim_exchange_settlement_payment_order',
                ],
                'required': [
                    'guid',
                    'post_internal_claim_exchange_settlement_payment_order',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'post_internal_claim_exchange_settlement_payment_order':
                        (PostInternalClaimExchangeSettlementPaymentOrder,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'post_internal_claim_exchange_settlement_payment_order': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_claim_expected_payment_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExpectedPayment,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/expected_payments/{guid}/claim',
                'operation_id': 'internal_claim_expected_payment',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'post_internal_claim_expected_payment',
                ],
                'required': [
                    'guid',
                    'post_internal_claim_expected_payment',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'post_internal_claim_expected_payment':
                        (PostInternalClaimExpectedPayment,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'post_internal_claim_expected_payment': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_account_endpoint = _Endpoint(
            settings={
                'response_type': (Account,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/accounts',
                'operation_id': 'internal_create_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'internal_post_account',
                ],
                'required': [
                    'internal_post_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'internal_post_account':
                        (InternalPostAccount,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'internal_post_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_activity_limit_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalActivityLimitConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/activity_limit_configurations',
                'operation_id': 'internal_create_activity_limit_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_activity_limit_configuration',
                ],
                'required': [
                    'post_internal_activity_limit_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_activity_limit_configuration':
                        (PostInternalActivityLimitConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_activity_limit_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_activity_report_endpoint = _Endpoint(
            settings={
                'response_type': (InternalActivityReport,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/activity_reports',
                'operation_id': 'internal_create_activity_report',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_activity_report',
                ],
                'required': [
                    'post_internal_activity_report',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_activity_report':
                        (PostInternalActivityReport,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_activity_report': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_bank_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBank,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/banks',
                'operation_id': 'internal_create_bank',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_bank',
                ],
                'required': [
                    'post_internal_bank',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_bank':
                        (PostInternalBank,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_bank': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_bank_account_service_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBankAccountService,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/bank_account_services',
                'operation_id': 'internal_create_bank_account_service',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_bank_account_service',
                ],
                'required': [
                    'post_internal_bank_account_service',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_bank_account_service':
                        (PostInternalBankAccountService,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_bank_account_service': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_compliance_decision_endpoint = _Endpoint(
            settings={
                'response_type': (InternalComplianceDecision,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/compliance_decisions',
                'operation_id': 'internal_create_compliance_decision',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_compliance_decision',
                ],
                'required': [
                    'post_internal_compliance_decision',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_compliance_decision':
                        (PostInternalComplianceDecision,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_compliance_decision': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_country_code_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCountryCodeConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/country_code_configurations',
                'operation_id': 'internal_create_country_code_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_country_code_configuration',
                ],
                'required': [
                    'post_internal_country_code_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_country_code_configuration':
                        (PostInternalCountryCodeConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_country_code_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_crypto_asset_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCryptoAssetConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/crypto_asset_configurations',
                'operation_id': 'internal_create_crypto_asset_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_crypto_asset_configuration',
                ],
                'required': [
                    'post_internal_crypto_asset_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_crypto_asset_configuration':
                        (PostInternalCryptoAssetConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_crypto_asset_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_cybrid_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCybridAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/cybrid_accounts',
                'operation_id': 'internal_create_cybrid_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_cybrid_account',
                ],
                'required': [
                    'post_internal_cybrid_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_cybrid_account':
                        (PostInternalCybridAccount,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_cybrid_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_cybrid_gas_account_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCybridGasAccountConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/cybrid_gas_account_configurations',
                'operation_id': 'internal_create_cybrid_gas_account_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_cybrid_gas_account_configuration',
                ],
                'required': [
                    'post_internal_cybrid_gas_account_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_cybrid_gas_account_configuration':
                        (PostInternalCybridGasAccountConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_cybrid_gas_account_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_deposit_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (DepositBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/deposit_bank_accounts',
                'operation_id': 'internal_create_deposit_bank_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'internal_post_deposit_bank_account',
                ],
                'required': [
                    'internal_post_deposit_bank_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'internal_post_deposit_bank_account':
                        (InternalPostDepositBankAccount,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'internal_post_deposit_bank_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchange,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchanges',
                'operation_id': 'internal_create_exchange',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange',
                ],
                'required': [
                    'post_internal_exchange',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange':
                        (PostInternalExchange,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_accounts',
                'operation_id': 'internal_create_exchange_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange_account',
                ],
                'required': [
                    'post_internal_exchange_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange_account':
                        (PostInternalExchangeAccount,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_monitor_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeMonitor,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_monitors',
                'operation_id': 'internal_create_exchange_monitor',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange_monitor',
                ],
                'required': [
                    'post_internal_exchange_monitor',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange_monitor':
                        (PostInternalExchangeMonitor,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange_monitor': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_order_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeOrder,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_orders',
                'operation_id': 'internal_create_exchange_order',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange_order',
                ],
                'required': [
                    'post_internal_exchange_order',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange_order':
                        (PostInternalExchangeOrder,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange_order': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_settlement_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlement,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlements',
                'operation_id': 'internal_create_exchange_settlement',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange_settlement',
                ],
                'required': [
                    'post_internal_exchange_settlement',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange_settlement':
                        (PostInternalExchangeSettlement,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange_settlement': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_settlement_approval_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCreateExchangeSettlementApproval202Response,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlements/{guid}/approval',
                'operation_id': 'internal_create_exchange_settlement_approval',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_create_exchange_settlement_completion_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCreateExchangeSettlementApproval202Response,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlements/{guid}/completion',
                'operation_id': 'internal_create_exchange_settlement_completion',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_create_exchange_settlement_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_configurations',
                'operation_id': 'internal_create_exchange_settlement_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange_settlement_configuration',
                ],
                'required': [
                    'post_internal_exchange_settlement_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange_settlement_configuration':
                        (PostInternalExchangeSettlementConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange_settlement_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_exchange_settlement_payment_order_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementPaymentOrder,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_payment_orders',
                'operation_id': 'internal_create_exchange_settlement_payment_order',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_exchange_settlement_payment_order',
                ],
                'required': [
                    'post_internal_exchange_settlement_payment_order',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_exchange_settlement_payment_order':
                        (PostInternalExchangeSettlementPaymentOrder,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_exchange_settlement_payment_order': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_expected_payment_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExpectedPayment,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/expected_payments',
                'operation_id': 'internal_create_expected_payment',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_expected_payment',
                ],
                'required': [
                    'post_internal_expected_payment',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_expected_payment':
                        (PostInternalExpectedPayment,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_expected_payment': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_external_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_bank_accounts',
                'operation_id': 'internal_create_external_bank_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_external_bank_account',
                ],
                'required': [
                    'post_internal_external_bank_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_external_bank_account':
                        (PostInternalExternalBankAccount,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_external_bank_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_external_wallet_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWallet,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallets',
                'operation_id': 'internal_create_external_wallet',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_external_wallet',
                ],
                'required': [
                    'post_internal_external_wallet',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_external_wallet':
                        (PostInternalExternalWallet,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_external_wallet': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_fee_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFeeCharge,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/fees',
                'operation_id': 'internal_create_fee',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_fee_charge',
                ],
                'required': [
                    'post_internal_fee_charge',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_fee_charge':
                        (PostInternalFeeCharge,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_fee_charge': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_fee_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFeeConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/fee_configurations',
                'operation_id': 'internal_create_fee_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'internal_post_fee_configuration',
                ],
                'required': [
                    'internal_post_fee_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'internal_post_fee_configuration':
                        (InternalPostFeeConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'internal_post_fee_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_fiat_asset_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFiatAssetConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/fiat_asset_configurations',
                'operation_id': 'internal_create_fiat_asset_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_fiat_asset_configuration',
                ],
                'required': [
                    'post_internal_fiat_asset_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_fiat_asset_configuration':
                        (PostInternalFiatAssetConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_fiat_asset_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_file_endpoint = _Endpoint(
            settings={
                'response_type': (PlatformFile,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/files',
                'operation_id': 'internal_create_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_file',
                ],
                'required': [
                    'post_file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_file':
                        (PostFile,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_file': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_internal_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_bank_accounts',
                'operation_id': 'internal_create_internal_bank_account',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_internal_bank_account',
                ],
                'required': [
                    'post_internal_internal_bank_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_internal_bank_account':
                        (PostInternalInternalBankAccount,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_internal_bank_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_internal_bank_account_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalBankAccountConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_bank_account_configurations',
                'operation_id': 'internal_create_internal_bank_account_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_internal_bank_account_configuration',
                ],
                'required': [
                    'post_internal_internal_bank_account_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_internal_bank_account_configuration':
                        (PostInternalInternalBankAccountConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_internal_bank_account_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_internal_wallet_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalWallet,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_wallets',
                'operation_id': 'internal_create_internal_wallet',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_internal_wallet',
                ],
                'required': [
                    'post_internal_internal_wallet',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_internal_wallet':
                        (PostInternalInternalWallet,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_internal_wallet': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_internal_wallet_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalWalletConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_wallet_configurations',
                'operation_id': 'internal_create_internal_wallet_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_internal_wallet_configuration',
                ],
                'required': [
                    'post_internal_internal_wallet_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_internal_wallet_configuration':
                        (PostInternalInternalWalletConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_internal_wallet_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_payout_symbol_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalPayoutSymbolConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/payout_symbol_configurations',
                'operation_id': 'internal_create_payout_symbol_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_payout_symbol_configuration',
                ],
                'required': [
                    'post_internal_payout_symbol_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_payout_symbol_configuration':
                        (PostInternalPayoutSymbolConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_payout_symbol_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_quote_endpoint = _Endpoint(
            settings={
                'response_type': (InternalQuote,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/quotes',
                'operation_id': 'internal_create_quote',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'internal_post_quote',
                ],
                'required': [
                    'internal_post_quote',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'internal_post_quote':
                        (InternalPostQuote,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'internal_post_quote': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_reconciliation_endpoint = _Endpoint(
            settings={
                'response_type': (InternalReconciliation,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/reconciliations',
                'operation_id': 'internal_create_reconciliation',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_reconciliation',
                ],
                'required': [
                    'post_internal_reconciliation',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_reconciliation':
                        (PostInternalReconciliation,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_reconciliation': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_stage_endpoint = _Endpoint(
            settings={
                'response_type': (InternalStage,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/stages',
                'operation_id': 'internal_create_stage',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_stage',
                ],
                'required': [
                    'post_internal_stage',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_stage':
                        (PostInternalStage,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_stage': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_trade_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTrade,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trades',
                'operation_id': 'internal_create_trade',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_trade',
                ],
                'required': [
                    'post_internal_trade',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_trade':
                        (PostInternalTrade,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_trade': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_trading_symbol_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTradingSymbolConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trading_symbol_configurations',
                'operation_id': 'internal_create_trading_symbol_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_trading_symbol_configuration',
                ],
                'required': [
                    'post_internal_trading_symbol_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_trading_symbol_configuration':
                        (PostInternalTradingSymbolConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_trading_symbol_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_transaction_monitor_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransactionMonitor,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transaction_monitors',
                'operation_id': 'internal_create_transaction_monitor',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_transaction_monitor',
                ],
                'required': [
                    'post_internal_transaction_monitor',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_transaction_monitor':
                        (PostInternalTransactionMonitor,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_transaction_monitor': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransfer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfers',
                'operation_id': 'internal_create_transfer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_transfer',
                ],
                'required': [
                    'post_internal_transfer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_transfer':
                        (PostInternalTransfer,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_transfer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_transfer_rail_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransferRailConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfer_rail_configurations',
                'operation_id': 'internal_create_transfer_rail_configuration',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_transfer_rail_configuration',
                ],
                'required': [
                    'post_internal_transfer_rail_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_transfer_rail_configuration':
                        (PostInternalTransferRailConfiguration,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_transfer_rail_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_transfer_screening_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransferScreening,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfer_screenings',
                'operation_id': 'internal_create_transfer_screening',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_transfer_screening',
                ],
                'required': [
                    'post_internal_transfer_screening',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_transfer_screening':
                        (PostInternalTransferScreening,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_transfer_screening': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_create_wallet_service_endpoint = _Endpoint(
            settings={
                'response_type': (InternalWalletService,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/wallet_services',
                'operation_id': 'internal_create_wallet_service',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_wallet_service',
                ],
                'required': [
                    'post_internal_wallet_service',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_wallet_service':
                        (PostInternalWalletService,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_wallet_service': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_crypto_funding_deposit_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCryptoFundingDepositTransfer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/crypto_funding_deposit_transfers',
                'operation_id': 'internal_crypto_funding_deposit_transfer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_crypto_funding_deposit_transfer',
                ],
                'required': [
                    'post_internal_crypto_funding_deposit_transfer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_crypto_funding_deposit_transfer':
                        (PostInternalCryptoFundingDepositTransfer,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_crypto_funding_deposit_transfer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_delete_activity_limit_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalActivityLimitConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/activity_limit_configurations/{guid}',
                'operation_id': 'internal_delete_activity_limit_configuration',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_delete_external_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_bank_accounts/{external_bank_account_guid}',
                'operation_id': 'internal_delete_external_bank_account',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_bank_account_guid',
                ],
                'required': [
                    'external_bank_account_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_bank_account_guid':
                        (str,),
                },
                'attribute_map': {
                    'external_bank_account_guid': 'external_bank_account_guid',
                },
                'location_map': {
                    'external_bank_account_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_funding_deposit_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFundingDepositTransfer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/funding_deposit_transfers',
                'operation_id': 'internal_funding_deposit_transfer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'post_internal_funding_deposit_transfer',
                ],
                'required': [
                    'post_internal_funding_deposit_transfer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'post_internal_funding_deposit_transfer':
                        (PostInternalFundingDepositTransfer,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'post_internal_funding_deposit_transfer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_get_bank_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBank,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/banks/{bank_guid}',
                'operation_id': 'internal_get_bank',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'bank_guid',
                ],
                'required': [
                    'bank_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bank_guid':
                        (str,),
                },
                'attribute_map': {
                    'bank_guid': 'bank_guid',
                },
                'location_map': {
                    'bank_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_bank_account_service_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBankAccountService,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/bank_account_services/{bank_account_service_guid}',
                'operation_id': 'internal_get_bank_account_service',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'bank_account_service_guid',
                ],
                'required': [
                    'bank_account_service_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bank_account_service_guid':
                        (str,),
                },
                'attribute_map': {
                    'bank_account_service_guid': 'bank_account_service_guid',
                },
                'location_map': {
                    'bank_account_service_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_customer_endpoint = _Endpoint(
            settings={
                'response_type': (Customer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/customers/{customer_guid}',
                'operation_id': 'internal_get_customer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_guid',
                ],
                'required': [
                    'customer_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_guid':
                        (str,),
                },
                'attribute_map': {
                    'customer_guid': 'customer_guid',
                },
                'location_map': {
                    'customer_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_cybrid_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCybridAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/cybrid_accounts/{account_guid}',
                'operation_id': 'internal_get_cybrid_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_guid',
                ],
                'required': [
                    'account_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_guid':
                        (str,),
                },
                'attribute_map': {
                    'account_guid': 'account_guid',
                },
                'location_map': {
                    'account_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_exchange_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchange,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchanges/{exchange_guid}',
                'operation_id': 'internal_get_exchange',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'exchange_guid',
                ],
                'required': [
                    'exchange_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'exchange_guid':
                        (str,),
                },
                'attribute_map': {
                    'exchange_guid': 'exchange_guid',
                },
                'location_map': {
                    'exchange_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_exchange_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_accounts/{account_guid}',
                'operation_id': 'internal_get_exchange_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_guid',
                ],
                'required': [
                    'account_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_guid':
                        (str,),
                },
                'attribute_map': {
                    'account_guid': 'account_guid',
                },
                'location_map': {
                    'account_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_exchange_settlement_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlement,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlements/{guid}',
                'operation_id': 'internal_get_exchange_settlement',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_exchange_settlement_obligation_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementObligation,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_obligations/{guid}',
                'operation_id': 'internal_get_exchange_settlement_obligation',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_exchange_settlement_payment_order_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementPaymentOrder,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_payment_orders/{guid}',
                'operation_id': 'internal_get_exchange_settlement_payment_order',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_execution_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExecution,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/executions/{execution_guid}',
                'operation_id': 'internal_get_execution',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'execution_guid',
                ],
                'required': [
                    'execution_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'execution_guid':
                        (str,),
                },
                'attribute_map': {
                    'execution_guid': 'execution_guid',
                },
                'location_map': {
                    'execution_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_expected_payment_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExpectedPayment,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/expected_payments/{guid}',
                'operation_id': 'internal_get_expected_payment',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_external_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_bank_accounts/{external_bank_account_guid}',
                'operation_id': 'internal_get_external_bank_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_bank_account_guid',
                    'force_balance_refresh',
                    'include_balances',
                    'include_pii',
                ],
                'required': [
                    'external_bank_account_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_bank_account_guid':
                        (str,),
                    'force_balance_refresh':
                        (bool,),
                    'include_balances':
                        (bool,),
                    'include_pii':
                        (bool,),
                },
                'attribute_map': {
                    'external_bank_account_guid': 'external_bank_account_guid',
                    'force_balance_refresh': 'force_balance_refresh',
                    'include_balances': 'include_balances',
                    'include_pii': 'include_pii',
                },
                'location_map': {
                    'external_bank_account_guid': 'path',
                    'force_balance_refresh': 'query',
                    'include_balances': 'query',
                    'include_pii': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_external_wallet_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWallet,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallets/{external_wallet_guid}',
                'operation_id': 'internal_get_external_wallet',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_wallet_guid',
                ],
                'required': [
                    'external_wallet_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_wallet_guid':
                        (str,),
                },
                'attribute_map': {
                    'external_wallet_guid': 'external_wallet_guid',
                },
                'location_map': {
                    'external_wallet_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_external_wallet_screening_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWalletScreening,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallet_screenings/{external_wallet_screening_guid}',
                'operation_id': 'internal_get_external_wallet_screening',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_wallet_screening_guid',
                ],
                'required': [
                    'external_wallet_screening_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_wallet_screening_guid':
                        (str,),
                },
                'attribute_map': {
                    'external_wallet_screening_guid': 'external_wallet_screening_guid',
                },
                'location_map': {
                    'external_wallet_screening_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_file_endpoint = _Endpoint(
            settings={
                'response_type': (PlatformFile,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/files/{file_guid}',
                'operation_id': 'internal_get_file',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_guid',
                ],
                'required': [
                    'file_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_guid':
                        (str,),
                },
                'attribute_map': {
                    'file_guid': 'file_guid',
                },
                'location_map': {
                    'file_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_internal_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_bank_accounts/{internal_bank_account_guid}',
                'operation_id': 'internal_get_internal_bank_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'internal_bank_account_guid',
                ],
                'required': [
                    'internal_bank_account_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'internal_bank_account_guid':
                        (str,),
                },
                'attribute_map': {
                    'internal_bank_account_guid': 'internal_bank_account_guid',
                },
                'location_map': {
                    'internal_bank_account_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_internal_wallet_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalWallet,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_wallets/{internal_wallet_guid}',
                'operation_id': 'internal_get_internal_wallet',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'internal_wallet_guid',
                ],
                'required': [
                    'internal_wallet_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'internal_wallet_guid':
                        (str,),
                },
                'attribute_map': {
                    'internal_wallet_guid': 'internal_wallet_guid',
                },
                'location_map': {
                    'internal_wallet_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_invoice_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInvoice,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/invoices/{invoice_guid}',
                'operation_id': 'internal_get_invoice',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'invoice_guid',
                ],
                'required': [
                    'invoice_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'invoice_guid':
                        (str,),
                },
                'attribute_map': {
                    'invoice_guid': 'invoice_guid',
                },
                'location_map': {
                    'invoice_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_plan_endpoint = _Endpoint(
            settings={
                'response_type': (InternalPlan,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/plans/{plan_guid}',
                'operation_id': 'internal_get_plan',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'plan_guid',
                ],
                'required': [
                    'plan_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'plan_guid':
                        (str,),
                },
                'attribute_map': {
                    'plan_guid': 'plan_guid',
                },
                'location_map': {
                    'plan_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_quote_endpoint = _Endpoint(
            settings={
                'response_type': (InternalQuote,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/quotes/{quote_guid}',
                'operation_id': 'internal_get_quote',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'quote_guid',
                ],
                'required': [
                    'quote_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'quote_guid':
                        (str,),
                },
                'attribute_map': {
                    'quote_guid': 'quote_guid',
                },
                'location_map': {
                    'quote_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_reconciliation_endpoint = _Endpoint(
            settings={
                'response_type': (InternalReconciliation,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/reconciliations/{guid}',
                'operation_id': 'internal_get_reconciliation',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_trade_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTrade,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trades/{trade_guid}',
                'operation_id': 'internal_get_trade',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'trade_guid',
                ],
                'required': [
                    'trade_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'trade_guid':
                        (str,),
                },
                'attribute_map': {
                    'trade_guid': 'trade_guid',
                },
                'location_map': {
                    'trade_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransfer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfers/{guid}',
                'operation_id': 'internal_get_transfer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'include_provider_info',
                ],
                'required': [
                    'guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'include_provider_info':
                        (bool,),
                },
                'attribute_map': {
                    'guid': 'guid',
                    'include_provider_info': 'include_provider_info',
                },
                'location_map': {
                    'guid': 'path',
                    'include_provider_info': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_transfer_screening_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransferScreening,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfer_screenings/{transfer_screening_guid}',
                'operation_id': 'internal_get_transfer_screening',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_screening_guid',
                ],
                'required': [
                    'transfer_screening_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'transfer_screening_guid':
                        (str,),
                },
                'attribute_map': {
                    'transfer_screening_guid': 'transfer_screening_guid',
                },
                'location_map': {
                    'transfer_screening_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_get_wallet_service_endpoint = _Endpoint(
            settings={
                'response_type': (InternalWalletService,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/wallet_services/{wallet_service_guid}',
                'operation_id': 'internal_get_wallet_service',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'wallet_service_guid',
                ],
                'required': [
                    'wallet_service_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'wallet_service_guid':
                        (str,),
                },
                'attribute_map': {
                    'wallet_service_guid': 'wallet_service_guid',
                },
                'location_map': {
                    'wallet_service_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (AccountList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/accounts',
                'operation_id': 'internal_list_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'owner',
                    'guid',
                    'customer_guid',
                    'bank_guid',
                    'type',
                    'asset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'owner':
                        (str,),
                    'guid':
                        (str,),
                    'customer_guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'type':
                        (str,),
                    'asset':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'owner': 'owner',
                    'guid': 'guid',
                    'customer_guid': 'customer_guid',
                    'bank_guid': 'bank_guid',
                    'type': 'type',
                    'asset': 'asset',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'owner': 'query',
                    'guid': 'query',
                    'customer_guid': 'query',
                    'bank_guid': 'query',
                    'type': 'query',
                    'asset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_activity_limit_configurations_endpoint = _Endpoint(
            settings={
                'response_type': (InternalActivityLimitConfigurationList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/activity_limit_configurations',
                'operation_id': 'internal_list_activity_limit_configurations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'type',
                    'environment',
                    'guid',
                    'customer_guid',
                    'bank_guid',
                    'audience',
                    'country_code',
                    'activity',
                    'side',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'type':
                        (str,),
                    'environment':
                        (str,),
                    'guid':
                        (str,),
                    'customer_guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'audience':
                        (str,),
                    'country_code':
                        (str,),
                    'activity':
                        (str,),
                    'side':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'type': 'type',
                    'environment': 'environment',
                    'guid': 'guid',
                    'customer_guid': 'customer_guid',
                    'bank_guid': 'bank_guid',
                    'audience': 'audience',
                    'country_code': 'country_code',
                    'activity': 'activity',
                    'side': 'side',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'type': 'query',
                    'environment': 'query',
                    'guid': 'query',
                    'customer_guid': 'query',
                    'bank_guid': 'query',
                    'audience': 'query',
                    'country_code': 'query',
                    'activity': 'query',
                    'side': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_bank_account_services_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBankAccountServiceList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/bank_account_services',
                'operation_id': 'internal_list_bank_account_services',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'environment',
                    'guid',
                    'type',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'environment':
                        (str,),
                    'guid':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'environment': 'environment',
                    'guid': 'guid',
                    'type': 'type',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'environment': 'query',
                    'guid': 'query',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_banks_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBankList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/banks',
                'operation_id': 'internal_list_banks',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'type',
                    'organization_guid',
                    'bank_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'type':
                        (str,),
                    'organization_guid':
                        (str,),
                    'bank_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'type': 'type',
                    'organization_guid': 'organization_guid',
                    'bank_guid': 'bank_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'type': 'query',
                    'organization_guid': 'query',
                    'bank_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_crypto_asset_configurations_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCryptoAssetConfigurationList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/crypto_asset_configurations',
                'operation_id': 'internal_list_crypto_asset_configurations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'asset_code',
                    'bank_guid',
                    'deposits_enabled',
                    'environment',
                    'invoices_enabled',
                    'storage_enabled',
                    'type',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'asset_code':
                        (str,),
                    'bank_guid':
                        (str,),
                    'deposits_enabled':
                        (bool,),
                    'environment':
                        (str,),
                    'invoices_enabled':
                        (bool,),
                    'storage_enabled':
                        (bool,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'asset_code': 'asset_code',
                    'bank_guid': 'bank_guid',
                    'deposits_enabled': 'deposits_enabled',
                    'environment': 'environment',
                    'invoices_enabled': 'invoices_enabled',
                    'storage_enabled': 'storage_enabled',
                    'type': 'type',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'asset_code': 'query',
                    'bank_guid': 'query',
                    'deposits_enabled': 'query',
                    'environment': 'query',
                    'invoices_enabled': 'query',
                    'storage_enabled': 'query',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_customers_endpoint = _Endpoint(
            settings={
                'response_type': (CustomerList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/customers',
                'operation_id': 'internal_list_customers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'bank_guid',
                    'organization_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'organization_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'bank_guid': 'bank_guid',
                    'organization_guid': 'organization_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'bank_guid': 'query',
                    'organization_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_cybrid_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCybridAccountList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/cybrid_accounts',
                'operation_id': 'internal_list_cybrid_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'environment',
                    'type',
                    'asset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'environment':
                        (str,),
                    'type':
                        (str,),
                    'asset':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'environment': 'environment',
                    'type': 'type',
                    'asset': 'asset',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'environment': 'query',
                    'type': 'query',
                    'asset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_deposit_bank_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (DepositBankAccountList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/deposit_bank_accounts',
                'operation_id': 'internal_list_deposit_bank_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'bank_guid',
                    'customer_guid',
                    'label',
                    'unique_memo_id',
                    'type',
                    'parent_deposit_bank_account_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'customer_guid':
                        (str,),
                    'label':
                        (str,),
                    'unique_memo_id':
                        (str,),
                    'type':
                        (str,),
                    'parent_deposit_bank_account_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'bank_guid': 'bank_guid',
                    'customer_guid': 'customer_guid',
                    'label': 'label',
                    'unique_memo_id': 'unique_memo_id',
                    'type': 'type',
                    'parent_deposit_bank_account_guid': 'parent_deposit_bank_account_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'bank_guid': 'query',
                    'customer_guid': 'query',
                    'label': 'query',
                    'unique_memo_id': 'query',
                    'type': 'query',
                    'parent_deposit_bank_account_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_exchange_orders_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeOrderList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_orders',
                'operation_id': 'internal_list_exchange_orders',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'state',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'state':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'state': 'state',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'state': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_exchange_settlement_configurations_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementConfigurationList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_configurations',
                'operation_id': 'internal_list_exchange_settlement_configurations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'asset',
                    'exchange_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'asset':
                        (str,),
                    'exchange_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'asset': 'asset',
                    'exchange_guid': 'exchange_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'asset': 'query',
                    'exchange_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_exchange_settlement_payment_orders_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeSettlementPaymentOrderList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlement_payment_orders',
                'operation_id': 'internal_list_exchange_settlement_payment_orders',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'settlement_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'settlement_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'settlement_guid': 'settlement_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'settlement_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_exchanges_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchanges',
                'operation_id': 'internal_list_exchanges',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'provider',
                    'environment',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'provider':
                        (str,),
                    'environment':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'provider': 'provider',
                    'environment': 'environment',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'provider': 'query',
                    'environment': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_expected_payments_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExpectedPaymentList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/expected_payments',
                'operation_id': 'internal_list_expected_payments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'settlement_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'settlement_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'settlement_guid': 'settlement_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'settlement_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_external_bank_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalBankAccountList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_bank_accounts',
                'operation_id': 'internal_list_external_bank_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'asset',
                    'bank_guid',
                    'exchange_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'asset':
                        (str,),
                    'bank_guid':
                        (str,),
                    'exchange_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'asset': 'asset',
                    'bank_guid': 'bank_guid',
                    'exchange_guid': 'exchange_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'asset': 'query',
                    'bank_guid': 'query',
                    'exchange_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_external_wallets_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWalletList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallets',
                'operation_id': 'internal_list_external_wallets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'asset',
                    'exchange_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'asset':
                        (str,),
                    'exchange_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'asset': 'asset',
                    'exchange_guid': 'exchange_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'asset': 'query',
                    'exchange_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_fee_configurations_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFeeConfigurationList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/fee_configurations',
                'operation_id': 'internal_list_fee_configurations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'configuration_type',
                    'product_type',
                    'primary_asset_code',
                    'counter_asset_code',
                    'bank_guid',
                    'organization_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'configuration_type':
                        (str,),
                    'product_type':
                        (str,),
                    'primary_asset_code':
                        (str,),
                    'counter_asset_code':
                        (str,),
                    'bank_guid':
                        (str,),
                    'organization_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'configuration_type': 'configuration_type',
                    'product_type': 'product_type',
                    'primary_asset_code': 'primary_asset_code',
                    'counter_asset_code': 'counter_asset_code',
                    'bank_guid': 'bank_guid',
                    'organization_guid': 'organization_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'configuration_type': 'query',
                    'product_type': 'query',
                    'primary_asset_code': 'query',
                    'counter_asset_code': 'query',
                    'bank_guid': 'query',
                    'organization_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_fees_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFeeChargeList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/fees',
                'operation_id': 'internal_list_fees',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'state',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'state':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'state': 'state',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'state': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_internal_bank_accounts_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalBankAccountList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_bank_accounts',
                'operation_id': 'internal_list_internal_bank_accounts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'environment',
                    'asset',
                    'account_kind',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'environment':
                        (str,),
                    'asset':
                        (str,),
                    'account_kind':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'environment': 'environment',
                    'asset': 'asset',
                    'account_kind': 'account_kind',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'environment': 'query',
                    'asset': 'query',
                    'account_kind': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_internal_wallets_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalWalletList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_wallets',
                'operation_id': 'internal_list_internal_wallets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'owner',
                    'environment',
                    'guid',
                    'bank_guid',
                    'customer_guid',
                    'internal_wallet_group_guid',
                    'type',
                    'asset',
                    'account_kind',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'owner':
                        (str,),
                    'environment':
                        (str,),
                    'guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'customer_guid':
                        (str,),
                    'internal_wallet_group_guid':
                        (str,),
                    'type':
                        (str,),
                    'asset':
                        (str,),
                    'account_kind':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'owner': 'owner',
                    'environment': 'environment',
                    'guid': 'guid',
                    'bank_guid': 'bank_guid',
                    'customer_guid': 'customer_guid',
                    'internal_wallet_group_guid': 'internal_wallet_group_guid',
                    'type': 'type',
                    'asset': 'asset',
                    'account_kind': 'account_kind',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'owner': 'query',
                    'environment': 'query',
                    'guid': 'query',
                    'bank_guid': 'query',
                    'customer_guid': 'query',
                    'internal_wallet_group_guid': 'query',
                    'type': 'query',
                    'asset': 'query',
                    'account_kind': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_invoices_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalInvoiceList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/invoices',
                'operation_id': 'internal_list_invoices',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'bank_guid',
                    'customer_guid',
                    'account_guid',
                    'state',
                    'asset',
                    'environment',
                    'label',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'environment',
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('environment',): {

                        "SANDBOX": "sandbox",
                        "PRODUCTION": "production"
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'customer_guid':
                        (str,),
                    'account_guid':
                        (str,),
                    'state':
                        (str,),
                    'asset':
                        (str,),
                    'environment':
                        (str,),
                    'label':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'bank_guid': 'bank_guid',
                    'customer_guid': 'customer_guid',
                    'account_guid': 'account_guid',
                    'state': 'state',
                    'asset': 'asset',
                    'environment': 'environment',
                    'label': 'label',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'bank_guid': 'query',
                    'customer_guid': 'query',
                    'account_guid': 'query',
                    'state': 'query',
                    'asset': 'query',
                    'environment': 'query',
                    'label': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_reconciliations_endpoint = _Endpoint(
            settings={
                'response_type': (InternalReconciliationList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/reconciliations',
                'operation_id': 'internal_list_reconciliations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'category',
                    'confidence',
                    'direction',
                    'transfer_guid',
                    'transaction_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'category':
                        (str,),
                    'confidence':
                        (str,),
                    'direction':
                        (str,),
                    'transfer_guid':
                        (str,),
                    'transaction_id':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'category': 'category',
                    'confidence': 'confidence',
                    'direction': 'direction',
                    'transfer_guid': 'transfer_guid',
                    'transaction_id': 'transaction_id',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'category': 'query',
                    'confidence': 'query',
                    'direction': 'query',
                    'transfer_guid': 'query',
                    'transaction_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_trades_endpoint = _Endpoint(
            settings={
                'response_type': (TradeList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trades',
                'operation_id': 'internal_list_trades',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'guid',
                    'customer_guid',
                    'bank_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'guid':
                        (str,),
                    'customer_guid':
                        (str,),
                    'bank_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'guid': 'guid',
                    'customer_guid': 'customer_guid',
                    'bank_guid': 'bank_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'guid': 'query',
                    'customer_guid': 'query',
                    'bank_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_trading_symbol_configurations_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTradingSymbolConfigurationList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trading_symbol_configurations',
                'operation_id': 'internal_list_trading_symbol_configurations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'bank_guid',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'bank_guid':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'bank_guid': 'bank_guid',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'bank_guid': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_transactions_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransactionsList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transactions',
                'operation_id': 'internal_list_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment',
                    'account_guid',
                    'account_type',
                    'cursor',
                    'per_page',
                    'include_pii',
                    'created_at_gte',
                    'created_at_lt',
                ],
                'required': [
                    'environment',
                    'account_guid',
                    'account_type',
                ],
                'nullable': [
                    'cursor',
                ],
                'enum': [
                    'environment',
                    'account_type',
                ],
                'validation': [
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('environment',): {

                        "SANDBOX": "sandbox",
                        "PRODUCTION": "production"
                    },
                    ('account_type',): {

                        "WALLET": "internal_wallet",
                        "BANK_ACCOUNT": "internal_bank_account"
                    },
                },
                'openapi_types': {
                    'environment':
                        (str,),
                    'account_guid':
                        (str,),
                    'account_type':
                        (str,),
                    'cursor':
                        (str, none_type,),
                    'per_page':
                        (int,),
                    'include_pii':
                        (bool,),
                    'created_at_gte':
                        (str,),
                    'created_at_lt':
                        (str,),
                },
                'attribute_map': {
                    'environment': 'environment',
                    'account_guid': 'account_guid',
                    'account_type': 'account_type',
                    'cursor': 'cursor',
                    'per_page': 'per_page',
                    'include_pii': 'include_pii',
                    'created_at_gte': 'created_at_gte',
                    'created_at_lt': 'created_at_lt',
                },
                'location_map': {
                    'environment': 'query',
                    'account_guid': 'query',
                    'account_type': 'query',
                    'cursor': 'query',
                    'per_page': 'query',
                    'include_pii': 'query',
                    'created_at_gte': 'query',
                    'created_at_lt': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_transfers_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransferList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfers',
                'operation_id': 'internal_list_transfers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'asset',
                    'guid',
                    'transfer_type',
                    'customer_guid',
                    'bank_guid',
                    'account_guid',
                    'state',
                    'side',
                    'txn_hash',
                    'external_id',
                    'amount',
                    'estimated_amount',
                    'principal_source_account_guid',
                    'principal_destination_account_guid',
                    'created_at_gte',
                    'created_at_lt',
                    'updated_at_gte',
                    'updated_at_lt',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'asset':
                        (str,),
                    'guid':
                        (str,),
                    'transfer_type':
                        (str,),
                    'customer_guid':
                        (str,),
                    'bank_guid':
                        (str,),
                    'account_guid':
                        (str,),
                    'state':
                        (str,),
                    'side':
                        (str,),
                    'txn_hash':
                        (str,),
                    'external_id':
                        (str,),
                    'amount':
                        (int,),
                    'estimated_amount':
                        (int,),
                    'principal_source_account_guid':
                        (str,),
                    'principal_destination_account_guid':
                        (str,),
                    'created_at_gte':
                        (str,),
                    'created_at_lt':
                        (str,),
                    'updated_at_gte':
                        (str,),
                    'updated_at_lt':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'asset': 'asset',
                    'guid': 'guid',
                    'transfer_type': 'transfer_type',
                    'customer_guid': 'customer_guid',
                    'bank_guid': 'bank_guid',
                    'account_guid': 'account_guid',
                    'state': 'state',
                    'side': 'side',
                    'txn_hash': 'txn_hash',
                    'external_id': 'external_id',
                    'amount': 'amount',
                    'estimated_amount': 'estimated_amount',
                    'principal_source_account_guid': 'principal_source_account_guid',
                    'principal_destination_account_guid': 'principal_destination_account_guid',
                    'created_at_gte': 'created_at_gte',
                    'created_at_lt': 'created_at_lt',
                    'updated_at_gte': 'updated_at_gte',
                    'updated_at_lt': 'updated_at_lt',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'asset': 'query',
                    'guid': 'query',
                    'transfer_type': 'query',
                    'customer_guid': 'query',
                    'bank_guid': 'query',
                    'account_guid': 'query',
                    'state': 'query',
                    'side': 'query',
                    'txn_hash': 'query',
                    'external_id': 'query',
                    'amount': 'query',
                    'estimated_amount': 'query',
                    'principal_source_account_guid': 'query',
                    'principal_destination_account_guid': 'query',
                    'created_at_gte': 'query',
                    'created_at_lt': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lt': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_list_wallet_services_endpoint = _Endpoint(
            settings={
                'response_type': (InternalWalletServiceList,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/wallet_services',
                'operation_id': 'internal_list_wallet_services',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'environment',
                    'guid',
                    'type',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'environment':
                        (str,),
                    'guid':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'environment': 'environment',
                    'guid': 'guid',
                    'type': 'type',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'environment': 'query',
                    'guid': 'query',
                    'type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_patch_account_endpoint = _Endpoint(
            settings={
                'response_type': (Account,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/accounts/{account_guid}',
                'operation_id': 'internal_patch_account',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_guid',
                    'patch_internal_account',
                ],
                'required': [
                    'account_guid',
                    'patch_internal_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_guid':
                        (str,),
                    'patch_internal_account':
                        (PatchInternalAccount,),
                },
                'attribute_map': {
                    'account_guid': 'account_guid',
                },
                'location_map': {
                    'account_guid': 'path',
                    'patch_internal_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_activity_limit_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalActivityLimitConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/activity_limit_configurations/{guid}',
                'operation_id': 'internal_patch_activity_limit_configuration',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_activity_limit_configuration',
                ],
                'required': [
                    'guid',
                    'patch_internal_activity_limit_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_activity_limit_configuration':
                        (PatchInternalActivityLimitConfiguration,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_activity_limit_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_bank_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBank,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/banks/{bank_guid}',
                'operation_id': 'internal_patch_bank',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'bank_guid',
                    'patch_internal_bank',
                ],
                'required': [
                    'bank_guid',
                    'patch_internal_bank',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bank_guid':
                        (str,),
                    'patch_internal_bank':
                        (PatchInternalBank,),
                },
                'attribute_map': {
                    'bank_guid': 'bank_guid',
                },
                'location_map': {
                    'bank_guid': 'path',
                    'patch_internal_bank': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_bank_account_service_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBankAccountService,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/bank_account_services/{guid}',
                'operation_id': 'internal_patch_bank_account_service',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_bank_account_service',
                ],
                'required': [
                    'guid',
                    'patch_internal_bank_account_service',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_bank_account_service':
                        (PatchInternalBankAccountService,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_bank_account_service': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_business_detail_endpoint = _Endpoint(
            settings={
                'response_type': (InternalBusinessDetail,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/business_details/{guid}',
                'operation_id': 'internal_patch_business_detail',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_business_detail',
                ],
                'required': [
                    'guid',
                    'patch_internal_business_detail',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_business_detail':
                        (PatchInternalBusinessDetail,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_business_detail': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_counterparty_endpoint = _Endpoint(
            settings={
                'response_type': (Counterparty,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/counterparties/{counterparty_guid}',
                'operation_id': 'internal_patch_counterparty',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'counterparty_guid',
                    'patch_internal_counterparty',
                ],
                'required': [
                    'counterparty_guid',
                    'patch_internal_counterparty',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'counterparty_guid':
                        (str,),
                    'patch_internal_counterparty':
                        (PatchInternalCounterparty,),
                },
                'attribute_map': {
                    'counterparty_guid': 'counterparty_guid',
                },
                'location_map': {
                    'counterparty_guid': 'path',
                    'patch_internal_counterparty': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_crypto_asset_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCryptoAssetConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/crypto_asset_configurations/{guid}',
                'operation_id': 'internal_patch_crypto_asset_configuration',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_crypto_asset_configuration',
                ],
                'required': [
                    'guid',
                    'patch_internal_crypto_asset_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_crypto_asset_configuration':
                        (PatchInternalCryptoAssetConfiguration,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_crypto_asset_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_customer_endpoint = _Endpoint(
            settings={
                'response_type': (Customer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/customers/{customer_guid}',
                'operation_id': 'internal_patch_customer',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_guid',
                    'patch_internal_customer',
                ],
                'required': [
                    'customer_guid',
                    'patch_internal_customer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_guid':
                        (str,),
                    'patch_internal_customer':
                        (PatchInternalCustomer,),
                },
                'attribute_map': {
                    'customer_guid': 'customer_guid',
                },
                'location_map': {
                    'customer_guid': 'path',
                    'patch_internal_customer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_cybrid_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCybridAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/cybrid_accounts/{guid}',
                'operation_id': 'internal_patch_cybrid_account',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_cybrid_account',
                ],
                'required': [
                    'guid',
                    'patch_internal_cybrid_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_cybrid_account':
                        (PatchInternalCybridAccount,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_cybrid_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_deposit_address_endpoint = _Endpoint(
            settings={
                'response_type': (DepositAddress,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/deposit_addresses/{guid}',
                'operation_id': 'internal_patch_deposit_address',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_deposit_address',
                ],
                'required': [
                    'guid',
                    'patch_internal_deposit_address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_deposit_address':
                        (PatchInternalDepositAddress,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_deposit_address': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_deposit_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (DepositBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/deposit_bank_accounts/{deposit_bank_account_guid}',
                'operation_id': 'internal_patch_deposit_bank_account',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'deposit_bank_account_guid',
                    'patch_internal_deposit_bank_account',
                ],
                'required': [
                    'deposit_bank_account_guid',
                    'patch_internal_deposit_bank_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'deposit_bank_account_guid':
                        (str,),
                    'patch_internal_deposit_bank_account':
                        (PatchInternalDepositBankAccount,),
                },
                'attribute_map': {
                    'deposit_bank_account_guid': 'deposit_bank_account_guid',
                },
                'location_map': {
                    'deposit_bank_account_guid': 'path',
                    'patch_internal_deposit_bank_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_exchange_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_accounts/{guid}',
                'operation_id': 'internal_patch_exchange_account',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_exchange_account',
                ],
                'required': [
                    'guid',
                    'patch_internal_exchange_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_exchange_account':
                        (PatchInternalExchangeAccount,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_exchange_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_exchange_order_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExchangeOrder,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_orders/{guid}',
                'operation_id': 'internal_patch_exchange_order',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_exchange_order',
                ],
                'required': [
                    'guid',
                    'patch_internal_exchange_order',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_exchange_order':
                        (PatchInternalExchangeOrder,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_exchange_order': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_exchange_settlement_endpoint = _Endpoint(
            settings={
                'response_type': (InternalCreateExchangeSettlementApproval202Response,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/exchange_settlements/{exchange_settlement_guid}',
                'operation_id': 'internal_patch_exchange_settlement',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'exchange_settlement_guid',
                    'patch_internal_exchange_settlement',
                ],
                'required': [
                    'exchange_settlement_guid',
                    'patch_internal_exchange_settlement',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'exchange_settlement_guid':
                        (str,),
                    'patch_internal_exchange_settlement':
                        (PatchInternalExchangeSettlement,),
                },
                'attribute_map': {
                    'exchange_settlement_guid': 'exchange_settlement_guid',
                },
                'location_map': {
                    'exchange_settlement_guid': 'path',
                    'patch_internal_exchange_settlement': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_external_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_bank_accounts/{external_bank_account_guid}',
                'operation_id': 'internal_patch_external_bank_account',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_bank_account_guid',
                    'patch_internal_external_bank_account',
                ],
                'required': [
                    'external_bank_account_guid',
                    'patch_internal_external_bank_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_bank_account_guid':
                        (str,),
                    'patch_internal_external_bank_account':
                        (PatchInternalExternalBankAccount,),
                },
                'attribute_map': {
                    'external_bank_account_guid': 'external_bank_account_guid',
                },
                'location_map': {
                    'external_bank_account_guid': 'path',
                    'patch_internal_external_bank_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_external_wallet_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWallet,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallets/{external_wallet_guid}',
                'operation_id': 'internal_patch_external_wallet',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_wallet_guid',
                    'patch_internal_external_wallet',
                ],
                'required': [
                    'external_wallet_guid',
                    'patch_internal_external_wallet',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_wallet_guid':
                        (str,),
                    'patch_internal_external_wallet':
                        (PatchInternalExternalWallet,),
                },
                'attribute_map': {
                    'external_wallet_guid': 'external_wallet_guid',
                },
                'location_map': {
                    'external_wallet_guid': 'path',
                    'patch_internal_external_wallet': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_external_wallet_screening_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWalletScreening,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallet_screenings/{external_wallet_screening_guid}',
                'operation_id': 'internal_patch_external_wallet_screening',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_wallet_screening_guid',
                    'patch_internal_external_wallet_screening',
                ],
                'required': [
                    'external_wallet_screening_guid',
                    'patch_internal_external_wallet_screening',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_wallet_screening_guid':
                        (str,),
                    'patch_internal_external_wallet_screening':
                        (PatchInternalExternalWalletScreening,),
                },
                'attribute_map': {
                    'external_wallet_screening_guid': 'external_wallet_screening_guid',
                },
                'location_map': {
                    'external_wallet_screening_guid': 'path',
                    'patch_internal_external_wallet_screening': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_fee_endpoint = _Endpoint(
            settings={
                'response_type': (InternalFeeCharge,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/fees/{guid}',
                'operation_id': 'internal_patch_fee',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_fee_charge',
                ],
                'required': [
                    'guid',
                    'patch_internal_fee_charge',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_fee_charge':
                        (PatchInternalFeeCharge,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_fee_charge': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_files_endpoint = _Endpoint(
            settings={
                'response_type': (PlatformFile,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/files/{file_guid}',
                'operation_id': 'internal_patch_files',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_guid',
                    'patch_internal_file',
                ],
                'required': [
                    'file_guid',
                    'patch_internal_file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_guid':
                        (str,),
                    'patch_internal_file':
                        (PatchInternalFile,),
                },
                'attribute_map': {
                    'file_guid': 'file_guid',
                },
                'location_map': {
                    'file_guid': 'path',
                    'patch_internal_file': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_identity_verification_endpoint = _Endpoint(
            settings={
                'response_type': (IdentityVerification,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/identity_verifications/{identity_verification_guid}',
                'operation_id': 'internal_patch_identity_verification',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_verification_guid',
                    'patch_internal_identity_verification',
                ],
                'required': [
                    'identity_verification_guid',
                    'patch_internal_identity_verification',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'identity_verification_guid':
                        (str,),
                    'patch_internal_identity_verification':
                        (PatchInternalIdentityVerification,),
                },
                'attribute_map': {
                    'identity_verification_guid': 'identity_verification_guid',
                },
                'location_map': {
                    'identity_verification_guid': 'path',
                    'patch_internal_identity_verification': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_internal_bank_account_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalBankAccount,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_bank_accounts/{guid}',
                'operation_id': 'internal_patch_internal_bank_account',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_internal_bank_account',
                ],
                'required': [
                    'guid',
                    'patch_internal_internal_bank_account',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_internal_bank_account':
                        (PatchInternalInternalBankAccount,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_internal_bank_account': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_internal_wallet_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalWallet,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_wallets/{guid}',
                'operation_id': 'internal_patch_internal_wallet',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_internal_wallet',
                ],
                'required': [
                    'guid',
                    'patch_internal_internal_wallet',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_internal_wallet':
                        (PatchInternalInternalWallet,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_internal_wallet': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_internal_wallet_group_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInternalWalletGroup,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/internal_wallet_groups/{guid}',
                'operation_id': 'internal_patch_internal_wallet_group',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_internal_wallet_group',
                ],
                'required': [
                    'guid',
                    'patch_internal_internal_wallet_group',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_internal_wallet_group':
                        (PatchInternalInternalWalletGroup,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_internal_wallet_group': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_invoice_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInvoice,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/invoices/{invoice_guid}',
                'operation_id': 'internal_patch_invoice',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'invoice_guid',
                    'patch_internal_invoice',
                ],
                'required': [
                    'invoice_guid',
                    'patch_internal_invoice',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'invoice_guid':
                        (str,),
                    'patch_internal_invoice':
                        (PatchInternalInvoice,),
                },
                'attribute_map': {
                    'invoice_guid': 'invoice_guid',
                },
                'location_map': {
                    'invoice_guid': 'path',
                    'patch_internal_invoice': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_payment_instruction_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentInstruction,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/payment_instructions/{guid}',
                'operation_id': 'internal_patch_payment_instruction',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_payment_instruction',
                ],
                'required': [
                    'guid',
                    'patch_internal_payment_instruction',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_payment_instruction':
                        (PatchInternalPaymentInstruction,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_payment_instruction': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_person_detail_endpoint = _Endpoint(
            settings={
                'response_type': (InternalPersonDetail,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/person_details/{guid}',
                'operation_id': 'internal_patch_person_detail',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_person_detail',
                ],
                'required': [
                    'guid',
                    'patch_internal_person_detail',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_person_detail':
                        (PatchInternalPersonDetail,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_person_detail': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_trade_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTrade,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trades/{trade_guid}',
                'operation_id': 'internal_patch_trade',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'trade_guid',
                    'patch_internal_trade',
                ],
                'required': [
                    'trade_guid',
                    'patch_internal_trade',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'trade_guid':
                        (str,),
                    'patch_internal_trade':
                        (PatchInternalTrade,),
                },
                'attribute_map': {
                    'trade_guid': 'trade_guid',
                },
                'location_map': {
                    'trade_guid': 'path',
                    'patch_internal_trade': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_trading_symbol_configuration_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTradingSymbolConfiguration,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/trading_symbol_configurations/{guid}',
                'operation_id': 'internal_patch_trading_symbol_configuration',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_trading_symbol_configuration',
                ],
                'required': [
                    'guid',
                    'patch_internal_trading_symbol_configuration',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_trading_symbol_configuration':
                        (PatchInternalTradingSymbolConfiguration,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_trading_symbol_configuration': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransfer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfers/{transfer_guid}',
                'operation_id': 'internal_patch_transfer',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_guid',
                    'patch_internal_transfer',
                ],
                'required': [
                    'transfer_guid',
                    'patch_internal_transfer',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'transfer_guid':
                        (str,),
                    'patch_internal_transfer':
                        (PatchInternalTransfer,),
                },
                'attribute_map': {
                    'transfer_guid': 'transfer_guid',
                },
                'location_map': {
                    'transfer_guid': 'path',
                    'patch_internal_transfer': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_transfer_screening_endpoint = _Endpoint(
            settings={
                'response_type': (InternalTransferScreening,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfer_screenings/{transfer_screening_guid}',
                'operation_id': 'internal_patch_transfer_screening',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_screening_guid',
                    'patch_internal_transfer_screening',
                ],
                'required': [
                    'transfer_screening_guid',
                    'patch_internal_transfer_screening',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'transfer_screening_guid':
                        (str,),
                    'patch_internal_transfer_screening':
                        (PatchInternalTransferScreening,),
                },
                'attribute_map': {
                    'transfer_screening_guid': 'transfer_screening_guid',
                },
                'location_map': {
                    'transfer_screening_guid': 'path',
                    'patch_internal_transfer_screening': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_wallet_service_endpoint = _Endpoint(
            settings={
                'response_type': (InternalWalletService,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/wallet_services/{guid}',
                'operation_id': 'internal_patch_wallet_service',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'guid',
                    'patch_internal_wallet_service',
                ],
                'required': [
                    'guid',
                    'patch_internal_wallet_service',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'guid':
                        (str,),
                    'patch_internal_wallet_service':
                        (PatchInternalWalletService,),
                },
                'attribute_map': {
                    'guid': 'guid',
                },
                'location_map': {
                    'guid': 'path',
                    'patch_internal_wallet_service': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_patch_workflow_endpoint = _Endpoint(
            settings={
                'response_type': (Workflow,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/workflows/{workflow_guid}',
                'operation_id': 'internal_patch_workflow',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'workflow_guid',
                    'patch_internal_workflow',
                ],
                'required': [
                    'workflow_guid',
                    'patch_internal_workflow',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workflow_guid':
                        (str,),
                    'patch_internal_workflow':
                        (PatchInternalWorkflow,),
                },
                'attribute_map': {
                    'workflow_guid': 'workflow_guid',
                },
                'location_map': {
                    'workflow_guid': 'path',
                    'patch_internal_workflow': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_signal_external_wallet_screening_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExternalWalletScreening,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/external_wallet_screenings/{external_wallet_screening_guid}/signal',
                'operation_id': 'internal_signal_external_wallet_screening',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'external_wallet_screening_guid',
                    'post_signal_internal_external_wallet_screening',
                ],
                'required': [
                    'external_wallet_screening_guid',
                    'post_signal_internal_external_wallet_screening',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'external_wallet_screening_guid':
                        (str,),
                    'post_signal_internal_external_wallet_screening':
                        (PostSignalInternalExternalWalletScreening,),
                },
                'attribute_map': {
                    'external_wallet_screening_guid': 'external_wallet_screening_guid',
                },
                'location_map': {
                    'external_wallet_screening_guid': 'path',
                    'post_signal_internal_external_wallet_screening': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_signal_identity_verification_endpoint = _Endpoint(
            settings={
                'response_type': (IdentityVerification,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/identity_verifications/{identity_verification_guid}/signal',
                'operation_id': 'internal_signal_identity_verification',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_verification_guid',
                    'post_signal_internal_identity_verification',
                ],
                'required': [
                    'identity_verification_guid',
                    'post_signal_internal_identity_verification',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'identity_verification_guid':
                        (str,),
                    'post_signal_internal_identity_verification':
                        (PostSignalInternalIdentityVerification,),
                },
                'attribute_map': {
                    'identity_verification_guid': 'identity_verification_guid',
                },
                'location_map': {
                    'identity_verification_guid': 'path',
                    'post_signal_internal_identity_verification': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.internal_signal_invoice_endpoint = _Endpoint(
            settings={
                'response_type': (InternalInvoice,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/invoices/{invoice_guid}/signal',
                'operation_id': 'internal_signal_invoice',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'invoice_guid',
                ],
                'required': [
                    'invoice_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'invoice_guid':
                        (str,),
                },
                'attribute_map': {
                    'invoice_guid': 'invoice_guid',
                },
                'location_map': {
                    'invoice_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.internal_signal_transfer_endpoint = _Endpoint(
            settings={
                'response_type': (Transfer,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/transfers/{transfer_guid}/signal',
                'operation_id': 'internal_signal_transfer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_guid',
                ],
                'required': [
                    'transfer_guid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'transfer_guid':
                        (str,),
                },
                'attribute_map': {
                    'transfer_guid': 'transfer_guid',
                },
                'location_map': {
                    'transfer_guid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.patch_internal_execution_endpoint = _Endpoint(
            settings={
                'response_type': (InternalExecution,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/executions/{execution_guid}',
                'operation_id': 'patch_internal_execution',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'execution_guid',
                    'patch_internal_execution',
                ],
                'required': [
                    'execution_guid',
                    'patch_internal_execution',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'execution_guid':
                        (str,),
                    'patch_internal_execution':
                        (PatchInternalExecution,),
                },
                'attribute_map': {
                    'execution_guid': 'execution_guid',
                },
                'location_map': {
                    'execution_guid': 'path',
                    'patch_internal_execution': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.patch_internal_plan_endpoint = _Endpoint(
            settings={
                'response_type': (InternalPlan,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/plans/{plan_guid}',
                'operation_id': 'patch_internal_plan',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'plan_guid',
                    'patch_internal_plan',
                ],
                'required': [
                    'plan_guid',
                    'patch_internal_plan',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'plan_guid':
                        (str,),
                    'patch_internal_plan':
                        (PatchInternalPlan,),
                },
                'attribute_map': {
                    'plan_guid': 'plan_guid',
                },
                'location_map': {
                    'plan_guid': 'path',
                    'patch_internal_plan': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.patch_internal_stage_endpoint = _Endpoint(
            settings={
                'response_type': (InternalStage,),
                'auth': [
                    'BearerAuth',
                    'oauth2'
                ],
                'endpoint_path': '/api/internal/stages/{stage_guid}',
                'operation_id': 'patch_internal_stage',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'stage_guid',
                    'patch_internal_stage',
                ],
                'required': [
                    'stage_guid',
                    'patch_internal_stage',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'stage_guid':
                        (str,),
                    'patch_internal_stage':
                        (PatchInternalStage,),
                },
                'attribute_map': {
                    'stage_guid': 'stage_guid',
                },
                'location_map': {
                    'stage_guid': 'path',
                    'patch_internal_stage': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def internal_claim_exchange_settlement_payment_order(
        self,
        guid,
        post_internal_claim_exchange_settlement_payment_order,
        **kwargs
    ):
        """Claim Exchange Settlement Payment Order  # noqa: E501

        Claim an Exchange Settlement Payment Order.  Required scope: **internal:exchange_settlements:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_claim_exchange_settlement_payment_order(guid, post_internal_claim_exchange_settlement_payment_order, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the exchange settlement expected payment.
            post_internal_claim_exchange_settlement_payment_order (PostInternalClaimExchangeSettlementPaymentOrder):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementPaymentOrder
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['post_internal_claim_exchange_settlement_payment_order'] = \
            post_internal_claim_exchange_settlement_payment_order
        return self.internal_claim_exchange_settlement_payment_order_endpoint.call_with_http_info(**kwargs)

    def internal_claim_expected_payment(
        self,
        guid,
        post_internal_claim_expected_payment,
        **kwargs
    ):
        """Claim Expected Payment  # noqa: E501

        Claim an Expected Payments.  Required scope: **internal:exchange_settlements:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_claim_expected_payment(guid, post_internal_claim_expected_payment, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the expected payment.
            post_internal_claim_expected_payment (PostInternalClaimExpectedPayment):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExpectedPayment
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['post_internal_claim_expected_payment'] = \
            post_internal_claim_expected_payment
        return self.internal_claim_expected_payment_endpoint.call_with_http_info(**kwargs)

    def internal_create_account(
        self,
        internal_post_account,
        **kwargs
    ):
        """Create Account  # noqa: E501

        Creates an account.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_account(internal_post_account, async_req=True)
        >>> result = thread.get()

        Args:
            internal_post_account (InternalPostAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Account
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['internal_post_account'] = \
            internal_post_account
        return self.internal_create_account_endpoint.call_with_http_info(**kwargs)

    def internal_create_activity_limit_configuration(
        self,
        post_internal_activity_limit_configuration,
        **kwargs
    ):
        """Create ActivityLimitConfiguration  # noqa: E501

        Creates a transfer rail configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_activity_limit_configuration(post_internal_activity_limit_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_activity_limit_configuration (PostInternalActivityLimitConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalActivityLimitConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_activity_limit_configuration'] = \
            post_internal_activity_limit_configuration
        return self.internal_create_activity_limit_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_activity_report(
        self,
        post_internal_activity_report,
        **kwargs
    ):
        """Create Activity Report  # noqa: E501

        Create an Activity Report.  Required scope: **internal:reports:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_activity_report(post_internal_activity_report, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_activity_report (PostInternalActivityReport):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalActivityReport
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_activity_report'] = \
            post_internal_activity_report
        return self.internal_create_activity_report_endpoint.call_with_http_info(**kwargs)

    def internal_create_bank(
        self,
        post_internal_bank,
        **kwargs
    ):
        """Create Bank  # noqa: E501

        Create a bank.  Required scope: **internal:banks:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_bank(post_internal_bank, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_bank (PostInternalBank):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBank
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_bank'] = \
            post_internal_bank
        return self.internal_create_bank_endpoint.call_with_http_info(**kwargs)

    def internal_create_bank_account_service(
        self,
        post_internal_bank_account_service,
        **kwargs
    ):
        """Create BankAccountService  # noqa: E501

        Create an BankAccountService.  Required scope: **internal:bank_account_services:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_bank_account_service(post_internal_bank_account_service, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_bank_account_service (PostInternalBankAccountService):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBankAccountService
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_bank_account_service'] = \
            post_internal_bank_account_service
        return self.internal_create_bank_account_service_endpoint.call_with_http_info(**kwargs)

    def internal_create_compliance_decision(
        self,
        post_internal_compliance_decision,
        **kwargs
    ):
        """Create Compliance Decision  # noqa: E501

        Create an Compliance Decision.  Required scope: **internal:customers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_compliance_decision(post_internal_compliance_decision, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_compliance_decision (PostInternalComplianceDecision):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalComplianceDecision
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_compliance_decision'] = \
            post_internal_compliance_decision
        return self.internal_create_compliance_decision_endpoint.call_with_http_info(**kwargs)

    def internal_create_country_code_configuration(
        self,
        post_internal_country_code_configuration,
        **kwargs
    ):
        """Create CountryCodeConfiguration  # noqa: E501

        Creates a country code configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_country_code_configuration(post_internal_country_code_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_country_code_configuration (PostInternalCountryCodeConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCountryCodeConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_country_code_configuration'] = \
            post_internal_country_code_configuration
        return self.internal_create_country_code_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_crypto_asset_configuration(
        self,
        post_internal_crypto_asset_configuration,
        **kwargs
    ):
        """Create CryptoAssetConfiguration  # noqa: E501

        Creates a crypto asset configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_crypto_asset_configuration(post_internal_crypto_asset_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_crypto_asset_configuration (PostInternalCryptoAssetConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCryptoAssetConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_crypto_asset_configuration'] = \
            post_internal_crypto_asset_configuration
        return self.internal_create_crypto_asset_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_cybrid_account(
        self,
        post_internal_cybrid_account,
        **kwargs
    ):
        """Create CybridAccount  # noqa: E501

        Create a CybridAccount.  Required scope: **internal:cybrid_accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_cybrid_account(post_internal_cybrid_account, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_cybrid_account (PostInternalCybridAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCybridAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_cybrid_account'] = \
            post_internal_cybrid_account
        return self.internal_create_cybrid_account_endpoint.call_with_http_info(**kwargs)

    def internal_create_cybrid_gas_account_configuration(
        self,
        post_internal_cybrid_gas_account_configuration,
        **kwargs
    ):
        """Create CybridGasAccountConfiguration  # noqa: E501

        Creates a cybrid gas account configuration.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_cybrid_gas_account_configuration(post_internal_cybrid_gas_account_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_cybrid_gas_account_configuration (PostInternalCybridGasAccountConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCybridGasAccountConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_cybrid_gas_account_configuration'] = \
            post_internal_cybrid_gas_account_configuration
        return self.internal_create_cybrid_gas_account_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_deposit_bank_account(
        self,
        internal_post_deposit_bank_account,
        **kwargs
    ):
        """Create Deposit Bank Account  # noqa: E501

        Creates a deposit bank account.  Required scope: **internal:deposit_bank_accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_deposit_bank_account(internal_post_deposit_bank_account, async_req=True)
        >>> result = thread.get()

        Args:
            internal_post_deposit_bank_account (InternalPostDepositBankAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DepositBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['internal_post_deposit_bank_account'] = \
            internal_post_deposit_bank_account
        return self.internal_create_deposit_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange(
        self,
        post_internal_exchange,
        **kwargs
    ):
        """Create Exchange  # noqa: E501

        Create an Exchanges.  Required scope: **internal:exchanges:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange(post_internal_exchange, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange (PostInternalExchange):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchange
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange'] = \
            post_internal_exchange
        return self.internal_create_exchange_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_account(
        self,
        post_internal_exchange_account,
        **kwargs
    ):
        """Create ExchangeAccount  # noqa: E501

        Create an ExchangeAccount.  Required scope: **internal:exchange_accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_account(post_internal_exchange_account, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange_account (PostInternalExchangeAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange_account'] = \
            post_internal_exchange_account
        return self.internal_create_exchange_account_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_monitor(
        self,
        post_internal_exchange_monitor,
        **kwargs
    ):
        """Create ExchangeMonitor  # noqa: E501

        Creates a ExchangeMonitor.Required scope: **internal:exchange_monitors:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_monitor(post_internal_exchange_monitor, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange_monitor (PostInternalExchangeMonitor):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeMonitor
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange_monitor'] = \
            post_internal_exchange_monitor
        return self.internal_create_exchange_monitor_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_order(
        self,
        post_internal_exchange_order,
        **kwargs
    ):
        """Create ExchangeOrder  # noqa: E501

        Creates a ExchangeOrder.Required scope: **internal:exchange_orders:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_order(post_internal_exchange_order, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange_order (PostInternalExchangeOrder):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeOrder
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange_order'] = \
            post_internal_exchange_order
        return self.internal_create_exchange_order_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_settlement(
        self,
        post_internal_exchange_settlement,
        **kwargs
    ):
        """Create Exchange Settlement  # noqa: E501

        Create an Exchange Settlements.  Required scope: **internal:exchange_settlements:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_settlement(post_internal_exchange_settlement, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange_settlement (PostInternalExchangeSettlement):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlement
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange_settlement'] = \
            post_internal_exchange_settlement
        return self.internal_create_exchange_settlement_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_settlement_approval(
        self,
        guid,
        **kwargs
    ):
        """Create Exchange Settlement Approval  # noqa: E501

        Queue an Exchange Settlement Approval.  Required scope: **internal:exchange_settlements:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_settlement_approval(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the exchange settlement.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCreateExchangeSettlementApproval202Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_create_exchange_settlement_approval_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_settlement_completion(
        self,
        guid,
        **kwargs
    ):
        """Create Exchange Settlement Completion  # noqa: E501

        Queue an Exchange Settlement Completion.  Required scope: **internal:exchange_settlements:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_settlement_completion(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the exchange settlement.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCreateExchangeSettlementApproval202Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_create_exchange_settlement_completion_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_settlement_configuration(
        self,
        post_internal_exchange_settlement_configuration,
        **kwargs
    ):
        """Create ExchangeSettlementConfiguration  # noqa: E501

        Creates a configuration.  Required scope: **internal:exchanges:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_settlement_configuration(post_internal_exchange_settlement_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange_settlement_configuration (PostInternalExchangeSettlementConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange_settlement_configuration'] = \
            post_internal_exchange_settlement_configuration
        return self.internal_create_exchange_settlement_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_exchange_settlement_payment_order(
        self,
        post_internal_exchange_settlement_payment_order,
        **kwargs
    ):
        """Create Exchange Settlement Payment Order  # noqa: E501

        Create an Exchange Settlement Payment Orders.  Required scope: **internal:exchange_settlements:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_exchange_settlement_payment_order(post_internal_exchange_settlement_payment_order, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_exchange_settlement_payment_order (PostInternalExchangeSettlementPaymentOrder):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementPaymentOrder
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_exchange_settlement_payment_order'] = \
            post_internal_exchange_settlement_payment_order
        return self.internal_create_exchange_settlement_payment_order_endpoint.call_with_http_info(**kwargs)

    def internal_create_expected_payment(
        self,
        post_internal_expected_payment,
        **kwargs
    ):
        """Create Expected Payment  # noqa: E501

        Create an Expected Payments.  Required scope: **internal:exchange_settlements:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_expected_payment(post_internal_expected_payment, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_expected_payment (PostInternalExpectedPayment):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExpectedPayment
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_expected_payment'] = \
            post_internal_expected_payment
        return self.internal_create_expected_payment_endpoint.call_with_http_info(**kwargs)

    def internal_create_external_bank_account(
        self,
        post_internal_external_bank_account,
        **kwargs
    ):
        """Create ExternalBankAccount  # noqa: E501

        Create an ExternalBankAccount.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_external_bank_account(post_internal_external_bank_account, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_external_bank_account (PostInternalExternalBankAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_external_bank_account'] = \
            post_internal_external_bank_account
        return self.internal_create_external_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_create_external_wallet(
        self,
        post_internal_external_wallet,
        **kwargs
    ):
        """Create ExternalWallet  # noqa: E501

        Create an ExternalWallet.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_external_wallet(post_internal_external_wallet, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_external_wallet (PostInternalExternalWallet):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWallet
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_external_wallet'] = \
            post_internal_external_wallet
        return self.internal_create_external_wallet_endpoint.call_with_http_info(**kwargs)

    def internal_create_fee(
        self,
        post_internal_fee_charge,
        **kwargs
    ):
        """Create Fee  # noqa: E501

        Creates a Fee.Required scope: **internal:fees:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_fee(post_internal_fee_charge, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_fee_charge (PostInternalFeeCharge):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFeeCharge
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_fee_charge'] = \
            post_internal_fee_charge
        return self.internal_create_fee_endpoint.call_with_http_info(**kwargs)

    def internal_create_fee_configuration(
        self,
        internal_post_fee_configuration,
        **kwargs
    ):
        """Create FeeConfiguration  # noqa: E501

        Creates a fee configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_fee_configuration(internal_post_fee_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            internal_post_fee_configuration (InternalPostFeeConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFeeConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['internal_post_fee_configuration'] = \
            internal_post_fee_configuration
        return self.internal_create_fee_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_fiat_asset_configuration(
        self,
        post_internal_fiat_asset_configuration,
        **kwargs
    ):
        """Create FiatAssetConfiguration  # noqa: E501

        Creates a fiat asset configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_fiat_asset_configuration(post_internal_fiat_asset_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_fiat_asset_configuration (PostInternalFiatAssetConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFiatAssetConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_fiat_asset_configuration'] = \
            post_internal_fiat_asset_configuration
        return self.internal_create_fiat_asset_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_file(
        self,
        post_file,
        **kwargs
    ):
        """Create File  # noqa: E501

        Creates a file.  Required scope: **internal:files:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_file(post_file, async_req=True)
        >>> result = thread.get()

        Args:
            post_file (PostFile):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PlatformFile
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_file'] = \
            post_file
        return self.internal_create_file_endpoint.call_with_http_info(**kwargs)

    def internal_create_internal_bank_account(
        self,
        post_internal_internal_bank_account,
        **kwargs
    ):
        """Create InternalBankAccount  # noqa: E501

        Create an InternalBankAccount.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_internal_bank_account(post_internal_internal_bank_account, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_internal_bank_account (PostInternalInternalBankAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_internal_bank_account'] = \
            post_internal_internal_bank_account
        return self.internal_create_internal_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_create_internal_bank_account_configuration(
        self,
        post_internal_internal_bank_account_configuration,
        **kwargs
    ):
        """Create InternalBankAccountConfiguration  # noqa: E501

        Creates an internal bank account configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_internal_bank_account_configuration(post_internal_internal_bank_account_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_internal_bank_account_configuration (PostInternalInternalBankAccountConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalBankAccountConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_internal_bank_account_configuration'] = \
            post_internal_internal_bank_account_configuration
        return self.internal_create_internal_bank_account_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_internal_wallet(
        self,
        post_internal_internal_wallet,
        **kwargs
    ):
        """Create InternalWallet  # noqa: E501

        Create an InternalWallet.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_internal_wallet(post_internal_internal_wallet, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_internal_wallet (PostInternalInternalWallet):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalWallet
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_internal_wallet'] = \
            post_internal_internal_wallet
        return self.internal_create_internal_wallet_endpoint.call_with_http_info(**kwargs)

    def internal_create_internal_wallet_configuration(
        self,
        post_internal_internal_wallet_configuration,
        **kwargs
    ):
        """Create InternalWalletConfiguration  # noqa: E501

        Creates an internal wallet configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_internal_wallet_configuration(post_internal_internal_wallet_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_internal_wallet_configuration (PostInternalInternalWalletConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalWalletConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_internal_wallet_configuration'] = \
            post_internal_internal_wallet_configuration
        return self.internal_create_internal_wallet_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_payout_symbol_configuration(
        self,
        post_internal_payout_symbol_configuration,
        **kwargs
    ):
        """Create PayoutSymbolConfiguration  # noqa: E501

        Creates a payout symbol configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_payout_symbol_configuration(post_internal_payout_symbol_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_payout_symbol_configuration (PostInternalPayoutSymbolConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalPayoutSymbolConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_payout_symbol_configuration'] = \
            post_internal_payout_symbol_configuration
        return self.internal_create_payout_symbol_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_quote(
        self,
        internal_post_quote,
        **kwargs
    ):
        """Create InternalQuote  # noqa: E501

        Creates a quote.  Required scope: **internal:quotes:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_quote(internal_post_quote, async_req=True)
        >>> result = thread.get()

        Args:
            internal_post_quote (InternalPostQuote):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalQuote
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['internal_post_quote'] = \
            internal_post_quote
        return self.internal_create_quote_endpoint.call_with_http_info(**kwargs)

    def internal_create_reconciliation(
        self,
        post_internal_reconciliation,
        **kwargs
    ):
        """Create Reconciliation  # noqa: E501

        Creates a Reconciliation.Required scope: **internal:transfers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_reconciliation(post_internal_reconciliation, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_reconciliation (PostInternalReconciliation):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalReconciliation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_reconciliation'] = \
            post_internal_reconciliation
        return self.internal_create_reconciliation_endpoint.call_with_http_info(**kwargs)

    def internal_create_stage(
        self,
        post_internal_stage,
        **kwargs
    ):
        """Create Stage  # noqa: E501

        Create an Stage.  Required scope: **internal:plans:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_stage(post_internal_stage, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_stage (PostInternalStage):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalStage
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_stage'] = \
            post_internal_stage
        return self.internal_create_stage_endpoint.call_with_http_info(**kwargs)

    def internal_create_trade(
        self,
        post_internal_trade,
        **kwargs
    ):
        """Create Internal Trade  # noqa: E501

        Creates a trade.  Required scope: **internal:trades:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_trade(post_internal_trade, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_trade (PostInternalTrade):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTrade
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_trade'] = \
            post_internal_trade
        return self.internal_create_trade_endpoint.call_with_http_info(**kwargs)

    def internal_create_trading_symbol_configuration(
        self,
        post_internal_trading_symbol_configuration,
        **kwargs
    ):
        """Create TradingSymbolConfiguration  # noqa: E501

        Creates a trading symbol configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_trading_symbol_configuration(post_internal_trading_symbol_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_trading_symbol_configuration (PostInternalTradingSymbolConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTradingSymbolConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_trading_symbol_configuration'] = \
            post_internal_trading_symbol_configuration
        return self.internal_create_trading_symbol_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_transaction_monitor(
        self,
        post_internal_transaction_monitor,
        **kwargs
    ):
        """Create TransactionMonitor  # noqa: E501

        Creates a TransactionMonitor.Required scope: **internal:transaction_monitors:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_transaction_monitor(post_internal_transaction_monitor, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_transaction_monitor (PostInternalTransactionMonitor):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransactionMonitor
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_transaction_monitor'] = \
            post_internal_transaction_monitor
        return self.internal_create_transaction_monitor_endpoint.call_with_http_info(**kwargs)

    def internal_create_transfer(
        self,
        post_internal_transfer,
        **kwargs
    ):
        """Create Transfer  # noqa: E501

        Create an Transfer.  Required scope: **internal:transfers:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_transfer(post_internal_transfer, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_transfer (PostInternalTransfer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransfer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_transfer'] = \
            post_internal_transfer
        return self.internal_create_transfer_endpoint.call_with_http_info(**kwargs)

    def internal_create_transfer_rail_configuration(
        self,
        post_internal_transfer_rail_configuration,
        **kwargs
    ):
        """Create TransferRailConfiguration  # noqa: E501

        Creates a transfer rail configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_transfer_rail_configuration(post_internal_transfer_rail_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_transfer_rail_configuration (PostInternalTransferRailConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransferRailConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_transfer_rail_configuration'] = \
            post_internal_transfer_rail_configuration
        return self.internal_create_transfer_rail_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_create_transfer_screening(
        self,
        post_internal_transfer_screening,
        **kwargs
    ):
        """Create TransferScreening  # noqa: E501

        Create an TransferScreening.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_transfer_screening(post_internal_transfer_screening, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_transfer_screening (PostInternalTransferScreening):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransferScreening
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_transfer_screening'] = \
            post_internal_transfer_screening
        return self.internal_create_transfer_screening_endpoint.call_with_http_info(**kwargs)

    def internal_create_wallet_service(
        self,
        post_internal_wallet_service,
        **kwargs
    ):
        """Create WalletService  # noqa: E501

        Create an WalletService.  Required scope: **internal:wallet_services:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_create_wallet_service(post_internal_wallet_service, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_wallet_service (PostInternalWalletService):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalWalletService
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_wallet_service'] = \
            post_internal_wallet_service
        return self.internal_create_wallet_service_endpoint.call_with_http_info(**kwargs)

    def internal_crypto_funding_deposit_transfer(
        self,
        post_internal_crypto_funding_deposit_transfer,
        **kwargs
    ):
        """Create Crypto Funding Deposit Transfer  # noqa: E501

        Create a Crypto Funding Deposit Transfer.  Required scope: **internal:transfers:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_crypto_funding_deposit_transfer(post_internal_crypto_funding_deposit_transfer, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_crypto_funding_deposit_transfer (PostInternalCryptoFundingDepositTransfer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCryptoFundingDepositTransfer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_crypto_funding_deposit_transfer'] = \
            post_internal_crypto_funding_deposit_transfer
        return self.internal_crypto_funding_deposit_transfer_endpoint.call_with_http_info(**kwargs)

    def internal_delete_activity_limit_configuration(
        self,
        guid,
        **kwargs
    ):
        """Delete ActivityLimitConfiguration  # noqa: E501

        Deletes an activity limit configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_delete_activity_limit_configuration(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the activity limit configuration.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalActivityLimitConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_delete_activity_limit_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_delete_external_bank_account(
        self,
        external_bank_account_guid,
        **kwargs
    ):
        """Delete External Bank Account  # noqa: E501

        Deletes an external bank account.  Required scope: **internal:accounts:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_delete_external_bank_account(external_bank_account_guid, async_req=True)
        >>> result = thread.get()

        Args:
            external_bank_account_guid (str): Identifier for the external bank account.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_bank_account_guid'] = \
            external_bank_account_guid
        return self.internal_delete_external_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_funding_deposit_transfer(
        self,
        post_internal_funding_deposit_transfer,
        **kwargs
    ):
        """Create Funding Deposit Transfer  # noqa: E501

        Create a Funding Deposit Transfer.  Required scope: **internal:transfers:execute**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_funding_deposit_transfer(post_internal_funding_deposit_transfer, async_req=True)
        >>> result = thread.get()

        Args:
            post_internal_funding_deposit_transfer (PostInternalFundingDepositTransfer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFundingDepositTransfer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['post_internal_funding_deposit_transfer'] = \
            post_internal_funding_deposit_transfer
        return self.internal_funding_deposit_transfer_endpoint.call_with_http_info(**kwargs)

    def internal_get_bank(
        self,
        bank_guid,
        **kwargs
    ):
        """Get Bank  # noqa: E501

        Retrieves a bank.  Required scope: **internal:banks:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_bank(bank_guid, async_req=True)
        >>> result = thread.get()

        Args:
            bank_guid (str): Identifier for the bank.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBank
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['bank_guid'] = \
            bank_guid
        return self.internal_get_bank_endpoint.call_with_http_info(**kwargs)

    def internal_get_bank_account_service(
        self,
        bank_account_service_guid,
        **kwargs
    ):
        """Get BankAccountService  # noqa: E501

        Retrieves a bank_account service.  Required scope: **internal:bank_account_services:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_bank_account_service(bank_account_service_guid, async_req=True)
        >>> result = thread.get()

        Args:
            bank_account_service_guid (str): Identifier for the bank_account service.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBankAccountService
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['bank_account_service_guid'] = \
            bank_account_service_guid
        return self.internal_get_bank_account_service_endpoint.call_with_http_info(**kwargs)

    def internal_get_customer(
        self,
        customer_guid,
        **kwargs
    ):
        """Get Customer  # noqa: E501

        Retrieves a customer.  Required scope: **internal:customers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_customer(customer_guid, async_req=True)
        >>> result = thread.get()

        Args:
            customer_guid (str): Identifier for the customer.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Customer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['customer_guid'] = \
            customer_guid
        return self.internal_get_customer_endpoint.call_with_http_info(**kwargs)

    def internal_get_cybrid_account(
        self,
        account_guid,
        **kwargs
    ):
        """Get CybridAccount  # noqa: E501

        Get an CybridAccount.  Required scope: **internal:cybrid_accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_cybrid_account(account_guid, async_req=True)
        >>> result = thread.get()

        Args:
            account_guid (str): Identifier for the Cybrid account.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCybridAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['account_guid'] = \
            account_guid
        return self.internal_get_cybrid_account_endpoint.call_with_http_info(**kwargs)

    def internal_get_exchange(
        self,
        exchange_guid,
        **kwargs
    ):
        """Get Exchange  # noqa: E501

        Get an Exchange.  Required scope: **internal:exchanges:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_exchange(exchange_guid, async_req=True)
        >>> result = thread.get()

        Args:
            exchange_guid (str): Identifier for the exchange.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchange
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['exchange_guid'] = \
            exchange_guid
        return self.internal_get_exchange_endpoint.call_with_http_info(**kwargs)

    def internal_get_exchange_account(
        self,
        account_guid,
        **kwargs
    ):
        """Get ExchangeAccount  # noqa: E501

        Get an ExchangeAccount.  Required scope: **internal:exchange_accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_exchange_account(account_guid, async_req=True)
        >>> result = thread.get()

        Args:
            account_guid (str): Identifier for the bank.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['account_guid'] = \
            account_guid
        return self.internal_get_exchange_account_endpoint.call_with_http_info(**kwargs)

    def internal_get_exchange_settlement(
        self,
        guid,
        **kwargs
    ):
        """Get Exchange Settlement  # noqa: E501

        Get an Exchange Settlement.  Required scope: **internal:exchange_settlements:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_exchange_settlement(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the exchange settlement.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlement
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_get_exchange_settlement_endpoint.call_with_http_info(**kwargs)

    def internal_get_exchange_settlement_obligation(
        self,
        guid,
        **kwargs
    ):
        """Get Exchange Settlement Obligation  # noqa: E501

        Get an Exchange Settlement Obligation.  Required scope: **internal:exchange_settlements:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_exchange_settlement_obligation(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the exchange settlement obligation.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementObligation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_get_exchange_settlement_obligation_endpoint.call_with_http_info(**kwargs)

    def internal_get_exchange_settlement_payment_order(
        self,
        guid,
        **kwargs
    ):
        """Get Exchange Settlement Payment Order  # noqa: E501

        Get an Exchange Settlement Payment Order.  Required scope: **internal:exchange_settlements:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_exchange_settlement_payment_order(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the exchange settlement payment order.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementPaymentOrder
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_get_exchange_settlement_payment_order_endpoint.call_with_http_info(**kwargs)

    def internal_get_execution(
        self,
        execution_guid,
        **kwargs
    ):
        """Get Execution  # noqa: E501

        Retrieves a execution.  Required scope: **internal:executions:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_execution(execution_guid, async_req=True)
        >>> result = thread.get()

        Args:
            execution_guid (str): Identifier for the execution.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExecution
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['execution_guid'] = \
            execution_guid
        return self.internal_get_execution_endpoint.call_with_http_info(**kwargs)

    def internal_get_expected_payment(
        self,
        guid,
        **kwargs
    ):
        """Get Expected Payment  # noqa: E501

        Get an Expected Payment.  Required scope: **internal:exchange_settlements:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_expected_payment(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the expected payment.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExpectedPayment
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_get_expected_payment_endpoint.call_with_http_info(**kwargs)

    def internal_get_external_bank_account(
        self,
        external_bank_account_guid,
        **kwargs
    ):
        """Get ExternalBankAccount  # noqa: E501

        Retrieves an external bank account.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_external_bank_account(external_bank_account_guid, async_req=True)
        >>> result = thread.get()

        Args:
            external_bank_account_guid (str): Identifier for the external bank account.

        Keyword Args:
            force_balance_refresh (bool): Force the balance on the account to be updated.. [optional]
            include_balances (bool): Include account balances in the response.. [optional]
            include_pii (bool): Include account holder's PII in the response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_bank_account_guid'] = \
            external_bank_account_guid
        return self.internal_get_external_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_get_external_wallet(
        self,
        external_wallet_guid,
        **kwargs
    ):
        """Get ExternalWallet  # noqa: E501

        Retrieves an internal wallet.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_external_wallet(external_wallet_guid, async_req=True)
        >>> result = thread.get()

        Args:
            external_wallet_guid (str): Identifier for the internal wallet.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWallet
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_wallet_guid'] = \
            external_wallet_guid
        return self.internal_get_external_wallet_endpoint.call_with_http_info(**kwargs)

    def internal_get_external_wallet_screening(
        self,
        external_wallet_screening_guid,
        **kwargs
    ):
        """Get ExternalWalletScreening  # noqa: E501

        Retrieves an external wallet screening.  Required scope: **internal:external_wallet_screenings:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_external_wallet_screening(external_wallet_screening_guid, async_req=True)
        >>> result = thread.get()

        Args:
            external_wallet_screening_guid (str): Identifier for the external wallet screening.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWalletScreening
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_wallet_screening_guid'] = \
            external_wallet_screening_guid
        return self.internal_get_external_wallet_screening_endpoint.call_with_http_info(**kwargs)

    def internal_get_file(
        self,
        file_guid,
        **kwargs
    ):
        """Get File  # noqa: E501

        Retrieves an file.  Required scope: **internal:files:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_file(file_guid, async_req=True)
        >>> result = thread.get()

        Args:
            file_guid (str): Identifier for the file.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PlatformFile
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['file_guid'] = \
            file_guid
        return self.internal_get_file_endpoint.call_with_http_info(**kwargs)

    def internal_get_internal_bank_account(
        self,
        internal_bank_account_guid,
        **kwargs
    ):
        """Get InternalBankAccount  # noqa: E501

        Retrieves an internal bank account.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_internal_bank_account(internal_bank_account_guid, async_req=True)
        >>> result = thread.get()

        Args:
            internal_bank_account_guid (str): Identifier for the internal bank account.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['internal_bank_account_guid'] = \
            internal_bank_account_guid
        return self.internal_get_internal_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_get_internal_wallet(
        self,
        internal_wallet_guid,
        **kwargs
    ):
        """Get InternalWallet  # noqa: E501

        Retrieves an internal wallet.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_internal_wallet(internal_wallet_guid, async_req=True)
        >>> result = thread.get()

        Args:
            internal_wallet_guid (str): Identifier for the internal wallet.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalWallet
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['internal_wallet_guid'] = \
            internal_wallet_guid
        return self.internal_get_internal_wallet_endpoint.call_with_http_info(**kwargs)

    def internal_get_invoice(
        self,
        invoice_guid,
        **kwargs
    ):
        """Get Invoice  # noqa: E501

        Retrieves an invoice.  Required scope: **internal:invoices:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_invoice(invoice_guid, async_req=True)
        >>> result = thread.get()

        Args:
            invoice_guid (str): Identifier for the invoice.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInvoice
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['invoice_guid'] = \
            invoice_guid
        return self.internal_get_invoice_endpoint.call_with_http_info(**kwargs)

    def internal_get_plan(
        self,
        plan_guid,
        **kwargs
    ):
        """Get Plan  # noqa: E501

        Retrieves a plan.  Required scope: **internal:plans:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_plan(plan_guid, async_req=True)
        >>> result = thread.get()

        Args:
            plan_guid (str): Identifier for the plan.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalPlan
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['plan_guid'] = \
            plan_guid
        return self.internal_get_plan_endpoint.call_with_http_info(**kwargs)

    def internal_get_quote(
        self,
        quote_guid,
        **kwargs
    ):
        """Get Internal Quote  # noqa: E501

        Retrieves a quote.  Required scope: **internal:quotes:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_quote(quote_guid, async_req=True)
        >>> result = thread.get()

        Args:
            quote_guid (str): Identifier for the quote.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalQuote
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['quote_guid'] = \
            quote_guid
        return self.internal_get_quote_endpoint.call_with_http_info(**kwargs)

    def internal_get_reconciliation(
        self,
        guid,
        **kwargs
    ):
        """Get Reconciliation  # noqa: E501

        Retrieves a reconciliation.  Required scope: **internal:transfers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_reconciliation(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalReconciliation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_get_reconciliation_endpoint.call_with_http_info(**kwargs)

    def internal_get_trade(
        self,
        trade_guid,
        **kwargs
    ):
        """Get Internal Trade  # noqa: E501

        Retrieves a trade.  Required scope: **internal:trades:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_trade(trade_guid, async_req=True)
        >>> result = thread.get()

        Args:
            trade_guid (str): Identifier for the trade.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTrade
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['trade_guid'] = \
            trade_guid
        return self.internal_get_trade_endpoint.call_with_http_info(**kwargs)

    def internal_get_transfer(
        self,
        guid,
        **kwargs
    ):
        """Get Transfer  # noqa: E501

        Retrieves an internal transfer.  Required scope: **internal:transfers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_transfer(guid, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the internal transfer.

        Keyword Args:
            include_provider_info (bool): Include provider info in the response.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransfer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        return self.internal_get_transfer_endpoint.call_with_http_info(**kwargs)

    def internal_get_transfer_screening(
        self,
        transfer_screening_guid,
        **kwargs
    ):
        """Get TransferScreening  # noqa: E501

        Retrieves an transfer screening.  Required scope: **internal:transfer_screenings:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_transfer_screening(transfer_screening_guid, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_screening_guid (str): Identifier for the transfer screening.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransferScreening
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['transfer_screening_guid'] = \
            transfer_screening_guid
        return self.internal_get_transfer_screening_endpoint.call_with_http_info(**kwargs)

    def internal_get_wallet_service(
        self,
        wallet_service_guid,
        **kwargs
    ):
        """Get WalletService  # noqa: E501

        Retrieves a wallet service.  Required scope: **internal:wallet_services:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_get_wallet_service(wallet_service_guid, async_req=True)
        >>> result = thread.get()

        Args:
            wallet_service_guid (str): Identifier for the wallet service.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalWalletService
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['wallet_service_guid'] = \
            wallet_service_guid
        return self.internal_get_wallet_service_endpoint.call_with_http_info(**kwargs)

    def internal_list_accounts(
        self,
        **kwargs
    ):
        """List Accounts  # noqa: E501

        Retrieves a list of accounts.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): The page index to retrieve.. [optional]
            per_page (int): The number of entities per page to return.. [optional]
            owner (str): The owner of the entity.. [optional]
            guid (str): Comma separated account_guids to list accounts for.. [optional]
            customer_guid (str): Comma separated customer_guids to list accounts for.. [optional]
            bank_guid (str): Comma separated bank_guids to list accounts for.. [optional]
            type (str): Comma separated account types to list accounts for.. [optional]
            asset (str): Comma separated assets to list accounts for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            AccountList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_accounts_endpoint.call_with_http_info(**kwargs)

    def internal_list_activity_limit_configurations(
        self,
        **kwargs
    ):
        """List ActivityLimitConfigurations  # noqa: E501

        Retrieves a listing of activity limit configurations.  Required scope: **internal:banks:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_activity_limit_configurations(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            type (str): Comma separated configuration types to list activity limit configurations for.. [optional]
            environment (str): Comma separated environments to list activity limit configurations for. . [optional]
            guid (str): Comma separated guids to list activity limit configurations for.. [optional]
            customer_guid (str): Comma separated customer guids to list activity limit configurations for.. [optional]
            bank_guid (str): Comma separated bank guids to list activity limit configurations for.. [optional]
            audience (str): Comma separated audiences to list activity limit configurations for.. [optional]
            country_code (str): Comma separated country codes to list activity limit configurations for.. [optional]
            activity (str): Comma separated activity types to list activity limit configurations for.. [optional]
            side (str): Comma separated activity sides to list activity limit configurations for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalActivityLimitConfigurationList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_activity_limit_configurations_endpoint.call_with_http_info(**kwargs)

    def internal_list_bank_account_services(
        self,
        **kwargs
    ):
        """List BankAccountServices  # noqa: E501

        Retrieves a listing of bank_account services.  Required scope: **internal:bank_account_services:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_bank_account_services(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            environment (str): Comma separated environments to list bank_account services for.. [optional]
            guid (str): Comma separated guids to list bank_account services for.. [optional]
            type (str): Comma separated types to list bank_account services for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBankAccountServiceList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_bank_account_services_endpoint.call_with_http_info(**kwargs)

    def internal_list_banks(
        self,
        **kwargs
    ):
        """List Banks  # noqa: E501

        Retrieves a listing of banks.  Required scope: **internal:banks:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_banks(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): The page index to retrieve.. [optional]
            per_page (int): The number of entities per page to return.. [optional]
            guid (str): Comma separated bank_guids to list banks for.. [optional]
            type (str): Comma separated types to list banks for.. [optional]
            organization_guid (str): Organization guid to list banks for.. [optional]
            bank_guid (str): Bank guid to list banks for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBankList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_banks_endpoint.call_with_http_info(**kwargs)

    def internal_list_crypto_asset_configurations(
        self,
        **kwargs
    ):
        """List CryptoAssetConfiguration  # noqa: E501

        Retrieves a listing of CryptoAssetConfiguration.Required scope: **internal:banks:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_crypto_asset_configurations(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            guid (str): Comma separated guids to list resources for (max 100).. [optional]
            asset_code (str): Comma separated asset codes to list resources for (max 100).. [optional]
            bank_guid (str): Comma separated bank guids to list resources for (max 100).. [optional]
            deposits_enabled (bool): Filter resources with deposits enabled.. [optional]
            environment (str): Environment to list resources for.. [optional]
            invoices_enabled (bool): Filter resources with invoices enabled.. [optional]
            storage_enabled (bool): Filter resources with storage enabled.. [optional]
            type (str): Type of resources to list.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCryptoAssetConfigurationList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_crypto_asset_configurations_endpoint.call_with_http_info(**kwargs)

    def internal_list_customers(
        self,
        **kwargs
    ):
        """List Customers  # noqa: E501

        Retrieves a listing of Customers.  Required scope: **internal:customers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_customers(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            guid (str): Comma separated assets to list customers for.. [optional]
            bank_guid (str): Comma separated bank_guids to list customers for.. [optional]
            organization_guid (str): Comma separated organization_guids to list customers for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CustomerList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_customers_endpoint.call_with_http_info(**kwargs)

    def internal_list_cybrid_accounts(
        self,
        **kwargs
    ):
        """List CybridAccounts  # noqa: E501

        Retrieves a listing of Cybrid accounts.  Required scope: **internal:cybrid_accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_cybrid_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            environment (str): Comma separated environments to list wallets for.. [optional]
            type (str): Comma separated types to list wallets for.. [optional]
            asset (str): Comma separated assets to list wallets for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCybridAccountList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_cybrid_accounts_endpoint.call_with_http_info(**kwargs)

    def internal_list_deposit_bank_accounts(
        self,
        **kwargs
    ):
        """List Deposit Bank Accounts  # noqa: E501

        Retrieves a list of deposit bank accounts.  Required scope: **internal:deposit_bank_accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_deposit_bank_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): The page index to retrieve.. [optional]
            per_page (int): The number of entities per page to return.. [optional]
            guid (str): Comma separated guids to list deposit bank accounts for.. [optional]
            bank_guid (str): Comma separated bank_guids to list deposit bank accounts for.. [optional]
            customer_guid (str): Comma separated customer_guids to list deposit bank accounts for.. [optional]
            label (str): Comma separated labels to list deposit bank accounts for.. [optional]
            unique_memo_id (str): Comma separated unique memo ids to list deposit bank accounts for.. [optional]
            type (str): Comma separated types to list deposit bank accounts for.. [optional]
            parent_deposit_bank_account_guid (str): Comma separated guids for parent accounts to list deposit bank accounts for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DepositBankAccountList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_deposit_bank_accounts_endpoint.call_with_http_info(**kwargs)

    def internal_list_exchange_orders(
        self,
        **kwargs
    ):
        """List ExchangeOrder  # noqa: E501

        Retrieves a listing of ExchangeOrders.Required scope: **internal:exchange_orders:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_exchange_orders(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            guid (str): Comma separated guids to list resources for.. [optional]
            state (str): Comma separated states to list resources for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeOrderList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_exchange_orders_endpoint.call_with_http_info(**kwargs)

    def internal_list_exchange_settlement_configurations(
        self,
        **kwargs
    ):
        """List ExchangeSettlementConfigurations  # noqa: E501

        Retrieves a listing of configurations.  Required scope: **internal:exchanges:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_exchange_settlement_configurations(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            asset (str): Comma separated assets to list configurations for.. [optional]
            exchange_guid (str): Comma separated exchange_guids to list configurations for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementConfigurationList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_exchange_settlement_configurations_endpoint.call_with_http_info(**kwargs)

    def internal_list_exchange_settlement_payment_orders(
        self,
        **kwargs
    ):
        """List Exchange Settlement Payment Orders  # noqa: E501

        Retrieves a listing of exchange settlement payment orders.  Required scope: **internal:exchange_settlements:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_exchange_settlement_payment_orders(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            settlement_guid (str): Comma separated exchange settlements to list payments for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeSettlementPaymentOrderList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_exchange_settlement_payment_orders_endpoint.call_with_http_info(**kwargs)

    def internal_list_exchanges(
        self,
        **kwargs
    ):
        """List Exchanges  # noqa: E501

        Retrieves a listing of exchanges.  Required scope: **internal:exchanges:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_exchanges(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            provider (str): Comma separated providers to list exchanges for.. [optional]
            environment (str): Comma separated environments to list exchanges for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_exchanges_endpoint.call_with_http_info(**kwargs)

    def internal_list_expected_payments(
        self,
        **kwargs
    ):
        """List Expected Payments  # noqa: E501

        Retrieves a listing of expected payments.  Required scope: **internal:exchange_settlements:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_expected_payments(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            settlement_guid (str): Comma separated exchange settlements to list payments for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExpectedPaymentList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_expected_payments_endpoint.call_with_http_info(**kwargs)

    def internal_list_external_bank_accounts(
        self,
        **kwargs
    ):
        """List ExternalBankAccounts  # noqa: E501

        Retrieves a listing of external bank accounts.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_external_bank_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            asset (str): Comma separated assets to list bank accounts for.. [optional]
            bank_guid (str): Comma separated bank_guids to list bank accounts for.. [optional]
            exchange_guid (str): Comma separated exchange_guids to list bank accounts for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalBankAccountList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_external_bank_accounts_endpoint.call_with_http_info(**kwargs)

    def internal_list_external_wallets(
        self,
        **kwargs
    ):
        """List ExternalWallets  # noqa: E501

        Retrieves a listing of external wallets.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_external_wallets(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            asset (str): Comma separated assets to list wallets for.. [optional]
            exchange_guid (str): Comma separated exchange_guids to list wallets for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWalletList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_external_wallets_endpoint.call_with_http_info(**kwargs)

    def internal_list_fee_configurations(
        self,
        **kwargs
    ):
        """List FeeConfiguration  # noqa: E501

        Retrieves a listing of FeeConfiguration.Required scope: **internal:banks:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_fee_configurations(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            guid (str): Comma separated guids to list resources for (max 100).. [optional]
            configuration_type (str): Comma separated configuration types to list resources for.. [optional]
            product_type (str): Comma separated product types to list resources for.. [optional]
            primary_asset_code (str): Comma separated primary asset codes to list resources for.. [optional]
            counter_asset_code (str): Comma separated counter asset codes to list resources for.. [optional]
            bank_guid (str): Comma separated bank guids to list resources for.. [optional]
            organization_guid (str): Comma separated organization guids to list resources for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFeeConfigurationList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_fee_configurations_endpoint.call_with_http_info(**kwargs)

    def internal_list_fees(
        self,
        **kwargs
    ):
        """List Fees  # noqa: E501

        Retrieves a listing of Fees.Required scope: **internal:fees:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_fees(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            guid (str): Comma separated guids to list resources for.. [optional]
            state (str): Comma separated states to list resources for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFeeChargeList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_fees_endpoint.call_with_http_info(**kwargs)

    def internal_list_internal_bank_accounts(
        self,
        **kwargs
    ):
        """List InternalBankAccounts  # noqa: E501

        Retrieves a listing of internal bank accounts.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_internal_bank_accounts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            environment (str): Comma separated environments to list bank accounts for.. [optional]
            asset (str): Comma separated assets to list bank accounts for.. [optional]
            account_kind (str): Comma separated account kinds to list bank accounts for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalBankAccountList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_internal_bank_accounts_endpoint.call_with_http_info(**kwargs)

    def internal_list_internal_wallets(
        self,
        **kwargs
    ):
        """List InternalWallets  # noqa: E501

        Retrieves a listing of internal wallets.  Required scope: **internal:accounts:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_internal_wallets(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            owner (str): The owner of the entity.. [optional]
            environment (str): Comma separated environments to list wallets for.. [optional]
            guid (str): Comma separated guids to list wallets for.. [optional]
            bank_guid (str): Comma separated bank_guids to list wallets for.. [optional]
            customer_guid (str): Comma separated customer_guids to list wallets for.. [optional]
            internal_wallet_group_guid (str): Comma separated internal_wallet_group_guids to list wallets for.. [optional]
            type (str): Comma separated types to list wallets for.. [optional]
            asset (str): Comma separated assets to list wallets for.. [optional]
            account_kind (str): Comma separated account kinds to list wallets for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalWalletList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_internal_wallets_endpoint.call_with_http_info(**kwargs)

    def internal_list_invoices(
        self,
        **kwargs
    ):
        """List Invoices  # noqa: E501

        Retrieves a list of invoices.  Required scope: **internal:invoices:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_invoices(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): The page index to retrieve.. [optional]
            per_page (int): The number of entities per page to return.. [optional]
            guid (str): Comma separated guids to list invoices for.. [optional]
            bank_guid (str): Comma separated bank_guids to list invoices for.. [optional]
            customer_guid (str): Comma separated customer_guids to list invoices for.. [optional]
            account_guid (str): Comma separated account_guids to list invoices for.. [optional]
            state (str): Comma separated states to list invoices for.. [optional]
            asset (str): Comma separated assets to list invoices for.. [optional]
            environment (str): [optional]
            label (str): Comma separated labels to list invoices for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalInvoiceList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_invoices_endpoint.call_with_http_info(**kwargs)

    def internal_list_reconciliations(
        self,
        **kwargs
    ):
        """List Reconciliations  # noqa: E501

        Retrieves a listing of reconciliations.  Required scope: **internal:transfers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_reconciliations(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            category (str): Comma separated categories to list reconciliations for.. [optional]
            confidence (str): Comma separated confidences to list reconciliations for.. [optional]
            direction (str): Comma separated directions to list reconciliations for.. [optional]
            transfer_guid (str): Comma separated transfer_guids to list reconciliations for.. [optional]
            transaction_id (str): Comma separated transaction_ids to list reconciliations for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalReconciliationList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_reconciliations_endpoint.call_with_http_info(**kwargs)

    def internal_list_trades(
        self,
        **kwargs
    ):
        """List Trades  # noqa: E501

        Retrieves a list of trades.  Required scope: **internal:trades:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_trades(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): The page index to retrieve.. [optional]
            per_page (int): The number of entities per page to return.. [optional]
            guid (str): Comma separated trade_guids to list trades for.. [optional]
            customer_guid (str): Comma separated customer_guids to list trades for.. [optional]
            bank_guid (str): Comma separated bank_guids to list trades for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TradeList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_trades_endpoint.call_with_http_info(**kwargs)

    def internal_list_trading_symbol_configurations(
        self,
        **kwargs
    ):
        """List TradingSymbolConfigurations  # noqa: E501

        Retrieves a listing of trading symbol configurations.  Required scope: **internal:banks:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_trading_symbol_configurations(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            bank_guid (str): Comma separated bank guids to list trading symbol configurations for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTradingSymbolConfigurationList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_trading_symbol_configurations_endpoint.call_with_http_info(**kwargs)

    def internal_list_transactions(
        self,
        environment,
        account_guid,
        account_type,
        **kwargs
    ):
        """List Transactions  # noqa: E501

        Retrieves a listing of transactions.  Required scope: **internal:transfers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_transactions(environment, account_guid, account_type, async_req=True)
        >>> result = thread.get()

        Args:
            environment (str):
            account_guid (str):
            account_type (str):

        Keyword Args:
            cursor (str, none_type): [optional]
            per_page (int): [optional]
            include_pii (bool): Include PII in the response.. [optional]
            created_at_gte (str): Created at start date inclusive lower bound, ISO8601.. [optional]
            created_at_lt (str): Created at end date exclusive upper bound, ISO8601.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransactionsList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment'] = \
            environment
        kwargs['account_guid'] = \
            account_guid
        kwargs['account_type'] = \
            account_type
        return self.internal_list_transactions_endpoint.call_with_http_info(**kwargs)

    def internal_list_transfers(
        self,
        **kwargs
    ):
        """List Transfers  # noqa: E501

        Retrieves a listing of internal transfers.  Required scope: **internal:transfers:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_transfers(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            asset (str): Comma separated assets to list transfers for.. [optional]
            guid (str): Comma separated transfer_guids to list transfers for.. [optional]
            transfer_type (str): Comma separated transfer_types to list accounts for.. [optional]
            customer_guid (str): Comma separated customer_guids to list transfers for.. [optional]
            bank_guid (str): Comma separated bank_guids to list transfers for.. [optional]
            account_guid (str): Comma separated account_guids to list transfers for.. [optional]
            state (str): Comma separated states to list transfers for.. [optional]
            side (str): Comma separated sides to list transfers for.. [optional]
            txn_hash (str): Comma separated txn_hashes to list transfers for.. [optional]
            external_id (str): Comma separated external_ids to list transfers for.. [optional]
            amount (int): Amount in cents to list transfers for.. [optional]
            estimated_amount (int): Estimated amount in cents to list transfers for.. [optional]
            principal_source_account_guid (str): Comma separated principal_source_account_guids to list transfers for.. [optional]
            principal_destination_account_guid (str): Comma separated principal_destination_account_guids to list transfers for.. [optional]
            created_at_gte (str): Created at start date-time inclusive lower bound, ISO8601. [optional]
            created_at_lt (str): Created at end date-time exclusive upper bound, ISO8601.. [optional]
            updated_at_gte (str): Created at start date-time inclusive lower bound, ISO8601. [optional]
            updated_at_lt (str): Created at end date-time exclusive upper bound, ISO8601.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransferList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_transfers_endpoint.call_with_http_info(**kwargs)

    def internal_list_wallet_services(
        self,
        **kwargs
    ):
        """List WalletServices  # noqa: E501

        Retrieves a listing of wallet services.  Required scope: **internal:wallet_services:read**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_list_wallet_services(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): [optional]
            per_page (int): [optional]
            environment (str): Comma separated environments to list wallet services for.. [optional]
            guid (str): Comma separated guids to list wallet services for.. [optional]
            type (str): Comma separated types to list wallet services for.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalWalletServiceList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.internal_list_wallet_services_endpoint.call_with_http_info(**kwargs)

    def internal_patch_account(
        self,
        account_guid,
        patch_internal_account,
        **kwargs
    ):
        """Patch Account  # noqa: E501

        Patch an account.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_account(account_guid, patch_internal_account, async_req=True)
        >>> result = thread.get()

        Args:
            account_guid (str): Identifier for the account.
            patch_internal_account (PatchInternalAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Account
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['account_guid'] = \
            account_guid
        kwargs['patch_internal_account'] = \
            patch_internal_account
        return self.internal_patch_account_endpoint.call_with_http_info(**kwargs)

    def internal_patch_activity_limit_configuration(
        self,
        guid,
        patch_internal_activity_limit_configuration,
        **kwargs
    ):
        """Patch ActivityLimitConfiguration  # noqa: E501

        Updates an activity limit configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_activity_limit_configuration(guid, patch_internal_activity_limit_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the activity limit configuration.
            patch_internal_activity_limit_configuration (PatchInternalActivityLimitConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalActivityLimitConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_activity_limit_configuration'] = \
            patch_internal_activity_limit_configuration
        return self.internal_patch_activity_limit_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_patch_bank(
        self,
        bank_guid,
        patch_internal_bank,
        **kwargs
    ):
        """Patch Bank  # noqa: E501

        Update a bank.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_bank(bank_guid, patch_internal_bank, async_req=True)
        >>> result = thread.get()

        Args:
            bank_guid (str): Identifier for the bank.
            patch_internal_bank (PatchInternalBank):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBank
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['bank_guid'] = \
            bank_guid
        kwargs['patch_internal_bank'] = \
            patch_internal_bank
        return self.internal_patch_bank_endpoint.call_with_http_info(**kwargs)

    def internal_patch_bank_account_service(
        self,
        guid,
        patch_internal_bank_account_service,
        **kwargs
    ):
        """Patch Internal BankAccount  # noqa: E501

        Patch an internal bank_account.  Required scope: **internal:bank_account_services:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_bank_account_service(guid, patch_internal_bank_account_service, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_bank_account_service (PatchInternalBankAccountService):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBankAccountService
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_bank_account_service'] = \
            patch_internal_bank_account_service
        return self.internal_patch_bank_account_service_endpoint.call_with_http_info(**kwargs)

    def internal_patch_business_detail(
        self,
        guid,
        patch_internal_business_detail,
        **kwargs
    ):
        """Patch Business Details  # noqa: E501

        Patch a business details record.  Required scope: **internal:customers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_business_detail(guid, patch_internal_business_detail, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_business_detail (PatchInternalBusinessDetail):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalBusinessDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_business_detail'] = \
            patch_internal_business_detail
        return self.internal_patch_business_detail_endpoint.call_with_http_info(**kwargs)

    def internal_patch_counterparty(
        self,
        counterparty_guid,
        patch_internal_counterparty,
        **kwargs
    ):
        """Patch Counterparty  # noqa: E501

        Patch a counterparty.  Required scope: **internal:counterparties:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_counterparty(counterparty_guid, patch_internal_counterparty, async_req=True)
        >>> result = thread.get()

        Args:
            counterparty_guid (str): Identifier for the counterparty.
            patch_internal_counterparty (PatchInternalCounterparty):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Counterparty
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['counterparty_guid'] = \
            counterparty_guid
        kwargs['patch_internal_counterparty'] = \
            patch_internal_counterparty
        return self.internal_patch_counterparty_endpoint.call_with_http_info(**kwargs)

    def internal_patch_crypto_asset_configuration(
        self,
        guid,
        patch_internal_crypto_asset_configuration,
        **kwargs
    ):
        """Patch CryptoAssetConfiguration  # noqa: E501

        Updates a crypto asset configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_crypto_asset_configuration(guid, patch_internal_crypto_asset_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the crypto asset configuration.
            patch_internal_crypto_asset_configuration (PatchInternalCryptoAssetConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCryptoAssetConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_crypto_asset_configuration'] = \
            patch_internal_crypto_asset_configuration
        return self.internal_patch_crypto_asset_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_patch_customer(
        self,
        customer_guid,
        patch_internal_customer,
        **kwargs
    ):
        """Patch Customer  # noqa: E501

        Patch a customer.  Required scope: **internal:customers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_customer(customer_guid, patch_internal_customer, async_req=True)
        >>> result = thread.get()

        Args:
            customer_guid (str): Identifier for the customer.
            patch_internal_customer (PatchInternalCustomer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Customer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['customer_guid'] = \
            customer_guid
        kwargs['patch_internal_customer'] = \
            patch_internal_customer
        return self.internal_patch_customer_endpoint.call_with_http_info(**kwargs)

    def internal_patch_cybrid_account(
        self,
        guid,
        patch_internal_cybrid_account,
        **kwargs
    ):
        """Patch Cybrid Account  # noqa: E501

        Patch an cybrid account.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_cybrid_account(guid, patch_internal_cybrid_account, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_cybrid_account (PatchInternalCybridAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCybridAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_cybrid_account'] = \
            patch_internal_cybrid_account
        return self.internal_patch_cybrid_account_endpoint.call_with_http_info(**kwargs)

    def internal_patch_deposit_address(
        self,
        guid,
        patch_internal_deposit_address,
        **kwargs
    ):
        """Patch Deposit Address  # noqa: E501

        Patch an deposit address.  Required scope: **internal:deposit_addresses:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_deposit_address(guid, patch_internal_deposit_address, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_deposit_address (PatchInternalDepositAddress):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DepositAddress
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_deposit_address'] = \
            patch_internal_deposit_address
        return self.internal_patch_deposit_address_endpoint.call_with_http_info(**kwargs)

    def internal_patch_deposit_bank_account(
        self,
        deposit_bank_account_guid,
        patch_internal_deposit_bank_account,
        **kwargs
    ):
        """Patch DepositBankAccount  # noqa: E501

        Patch an deposit bank account.  Required scope: **internal:deposit_bank_accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_deposit_bank_account(deposit_bank_account_guid, patch_internal_deposit_bank_account, async_req=True)
        >>> result = thread.get()

        Args:
            deposit_bank_account_guid (str): Identifier for the deposit bank account.
            patch_internal_deposit_bank_account (PatchInternalDepositBankAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DepositBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['deposit_bank_account_guid'] = \
            deposit_bank_account_guid
        kwargs['patch_internal_deposit_bank_account'] = \
            patch_internal_deposit_bank_account
        return self.internal_patch_deposit_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_patch_exchange_account(
        self,
        guid,
        patch_internal_exchange_account,
        **kwargs
    ):
        """Patch Exchange Account  # noqa: E501

        Patch an exchange account.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_exchange_account(guid, patch_internal_exchange_account, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_exchange_account (PatchInternalExchangeAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_exchange_account'] = \
            patch_internal_exchange_account
        return self.internal_patch_exchange_account_endpoint.call_with_http_info(**kwargs)

    def internal_patch_exchange_order(
        self,
        guid,
        patch_internal_exchange_order,
        **kwargs
    ):
        """Patch ExchangeOrder  # noqa: E501

        Patches a ExchangeOrder.Required scope: **internal:exchange_orders:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_exchange_order(guid, patch_internal_exchange_order, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_exchange_order (PatchInternalExchangeOrder):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExchangeOrder
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_exchange_order'] = \
            patch_internal_exchange_order
        return self.internal_patch_exchange_order_endpoint.call_with_http_info(**kwargs)

    def internal_patch_exchange_settlement(
        self,
        exchange_settlement_guid,
        patch_internal_exchange_settlement,
        **kwargs
    ):
        """Patch Exchange Settlement  # noqa: E501

        Patch an exchange settlement verification.  Required scope: **internal:exchange_settlements:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_exchange_settlement(exchange_settlement_guid, patch_internal_exchange_settlement, async_req=True)
        >>> result = thread.get()

        Args:
            exchange_settlement_guid (str): Identifier for the exchange settlement.
            patch_internal_exchange_settlement (PatchInternalExchangeSettlement):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalCreateExchangeSettlementApproval202Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['exchange_settlement_guid'] = \
            exchange_settlement_guid
        kwargs['patch_internal_exchange_settlement'] = \
            patch_internal_exchange_settlement
        return self.internal_patch_exchange_settlement_endpoint.call_with_http_info(**kwargs)

    def internal_patch_external_bank_account(
        self,
        external_bank_account_guid,
        patch_internal_external_bank_account,
        **kwargs
    ):
        """Patch ExternalBankAccount  # noqa: E501

        Patch an external bank account.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_external_bank_account(external_bank_account_guid, patch_internal_external_bank_account, async_req=True)
        >>> result = thread.get()

        Args:
            external_bank_account_guid (str): Identifier for the external bank account.
            patch_internal_external_bank_account (PatchInternalExternalBankAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_bank_account_guid'] = \
            external_bank_account_guid
        kwargs['patch_internal_external_bank_account'] = \
            patch_internal_external_bank_account
        return self.internal_patch_external_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_patch_external_wallet(
        self,
        external_wallet_guid,
        patch_internal_external_wallet,
        **kwargs
    ):
        """Patch ExternalWallet  # noqa: E501

        Patch an transfer.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_external_wallet(external_wallet_guid, patch_internal_external_wallet, async_req=True)
        >>> result = thread.get()

        Args:
            external_wallet_guid (str): Identifier for the external wallet.
            patch_internal_external_wallet (PatchInternalExternalWallet):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWallet
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_wallet_guid'] = \
            external_wallet_guid
        kwargs['patch_internal_external_wallet'] = \
            patch_internal_external_wallet
        return self.internal_patch_external_wallet_endpoint.call_with_http_info(**kwargs)

    def internal_patch_external_wallet_screening(
        self,
        external_wallet_screening_guid,
        patch_internal_external_wallet_screening,
        **kwargs
    ):
        """Patch External Wallet Screening  # noqa: E501

        Patch an external wallet screening.  Required scope: **internal:external_wallet_screenings:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_external_wallet_screening(external_wallet_screening_guid, patch_internal_external_wallet_screening, async_req=True)
        >>> result = thread.get()

        Args:
            external_wallet_screening_guid (str): Identifier for the external wallet screening.
            patch_internal_external_wallet_screening (PatchInternalExternalWalletScreening):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWalletScreening
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_wallet_screening_guid'] = \
            external_wallet_screening_guid
        kwargs['patch_internal_external_wallet_screening'] = \
            patch_internal_external_wallet_screening
        return self.internal_patch_external_wallet_screening_endpoint.call_with_http_info(**kwargs)

    def internal_patch_fee(
        self,
        guid,
        patch_internal_fee_charge,
        **kwargs
    ):
        """Patch Fee  # noqa: E501

        Patches a Fee.Required scope: **internal:fees:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_fee(guid, patch_internal_fee_charge, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_fee_charge (PatchInternalFeeCharge):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalFeeCharge
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_fee_charge'] = \
            patch_internal_fee_charge
        return self.internal_patch_fee_endpoint.call_with_http_info(**kwargs)

    def internal_patch_files(
        self,
        file_guid,
        patch_internal_file,
        **kwargs
    ):
        """Patch Files  # noqa: E501

        Patch an file.  Required scope: **internal:files:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_files(file_guid, patch_internal_file, async_req=True)
        >>> result = thread.get()

        Args:
            file_guid (str): Identifier for the file.
            patch_internal_file (PatchInternalFile):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PlatformFile
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['file_guid'] = \
            file_guid
        kwargs['patch_internal_file'] = \
            patch_internal_file
        return self.internal_patch_files_endpoint.call_with_http_info(**kwargs)

    def internal_patch_identity_verification(
        self,
        identity_verification_guid,
        patch_internal_identity_verification,
        **kwargs
    ):
        """Patch Identity Verification  # noqa: E501

        Patch an identity verification.  Required scope: **internal:identity_verifications:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_identity_verification(identity_verification_guid, patch_internal_identity_verification, async_req=True)
        >>> result = thread.get()

        Args:
            identity_verification_guid (str): Identifier for the identity verification.
            patch_internal_identity_verification (PatchInternalIdentityVerification):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            IdentityVerification
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['identity_verification_guid'] = \
            identity_verification_guid
        kwargs['patch_internal_identity_verification'] = \
            patch_internal_identity_verification
        return self.internal_patch_identity_verification_endpoint.call_with_http_info(**kwargs)

    def internal_patch_internal_bank_account(
        self,
        guid,
        patch_internal_internal_bank_account,
        **kwargs
    ):
        """Patch Internal Bank Account  # noqa: E501

        Patch an internal bank account.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_internal_bank_account(guid, patch_internal_internal_bank_account, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_internal_bank_account (PatchInternalInternalBankAccount):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalBankAccount
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_internal_bank_account'] = \
            patch_internal_internal_bank_account
        return self.internal_patch_internal_bank_account_endpoint.call_with_http_info(**kwargs)

    def internal_patch_internal_wallet(
        self,
        guid,
        patch_internal_internal_wallet,
        **kwargs
    ):
        """Patch Internal Wallet  # noqa: E501

        Patch an internal wallet.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_internal_wallet(guid, patch_internal_internal_wallet, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_internal_wallet (PatchInternalInternalWallet):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalWallet
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_internal_wallet'] = \
            patch_internal_internal_wallet
        return self.internal_patch_internal_wallet_endpoint.call_with_http_info(**kwargs)

    def internal_patch_internal_wallet_group(
        self,
        guid,
        patch_internal_internal_wallet_group,
        **kwargs
    ):
        """Patch Internal Wallet  # noqa: E501

        Patch an internal wallet.  Required scope: **internal:accounts:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_internal_wallet_group(guid, patch_internal_internal_wallet_group, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_internal_wallet_group (PatchInternalInternalWalletGroup):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInternalWalletGroup
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_internal_wallet_group'] = \
            patch_internal_internal_wallet_group
        return self.internal_patch_internal_wallet_group_endpoint.call_with_http_info(**kwargs)

    def internal_patch_invoice(
        self,
        invoice_guid,
        patch_internal_invoice,
        **kwargs
    ):
        """Patch Invoice  # noqa: E501

        Patch an invoice.  Required scope: **internal:invoices:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_invoice(invoice_guid, patch_internal_invoice, async_req=True)
        >>> result = thread.get()

        Args:
            invoice_guid (str): Identifier for the invoice.
            patch_internal_invoice (PatchInternalInvoice):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInvoice
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['invoice_guid'] = \
            invoice_guid
        kwargs['patch_internal_invoice'] = \
            patch_internal_invoice
        return self.internal_patch_invoice_endpoint.call_with_http_info(**kwargs)

    def internal_patch_payment_instruction(
        self,
        guid,
        patch_internal_payment_instruction,
        **kwargs
    ):
        """Patch Payment Instruction  # noqa: E501

        Patch an payment instruction.  Required scope: **internal:invoices:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_payment_instruction(guid, patch_internal_payment_instruction, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_payment_instruction (PatchInternalPaymentInstruction):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PaymentInstruction
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_payment_instruction'] = \
            patch_internal_payment_instruction
        return self.internal_patch_payment_instruction_endpoint.call_with_http_info(**kwargs)

    def internal_patch_person_detail(
        self,
        guid,
        patch_internal_person_detail,
        **kwargs
    ):
        """Patch Person Details  # noqa: E501

        Patch a person details record.  Required scope: **internal:customers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_person_detail(guid, patch_internal_person_detail, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_person_detail (PatchInternalPersonDetail):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalPersonDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_person_detail'] = \
            patch_internal_person_detail
        return self.internal_patch_person_detail_endpoint.call_with_http_info(**kwargs)

    def internal_patch_trade(
        self,
        trade_guid,
        patch_internal_trade,
        **kwargs
    ):
        """Patch Trade  # noqa: E501

        Patch a trade.  Required scope: **internal:trades:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_trade(trade_guid, patch_internal_trade, async_req=True)
        >>> result = thread.get()

        Args:
            trade_guid (str): Identifier for the trade.
            patch_internal_trade (PatchInternalTrade):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTrade
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['trade_guid'] = \
            trade_guid
        kwargs['patch_internal_trade'] = \
            patch_internal_trade
        return self.internal_patch_trade_endpoint.call_with_http_info(**kwargs)

    def internal_patch_trading_symbol_configuration(
        self,
        guid,
        patch_internal_trading_symbol_configuration,
        **kwargs
    ):
        """Patch TradingSymbolConfiguration  # noqa: E501

        Updates an trading symbol configuration.  Required scope: **internal:banks:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_trading_symbol_configuration(guid, patch_internal_trading_symbol_configuration, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the trading symbol configuration.
            patch_internal_trading_symbol_configuration (PatchInternalTradingSymbolConfiguration):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTradingSymbolConfiguration
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_trading_symbol_configuration'] = \
            patch_internal_trading_symbol_configuration
        return self.internal_patch_trading_symbol_configuration_endpoint.call_with_http_info(**kwargs)

    def internal_patch_transfer(
        self,
        transfer_guid,
        patch_internal_transfer,
        **kwargs
    ):
        """Patch Transfer  # noqa: E501

        Patch an transfer.  Required scope: **internal:transfers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_transfer(transfer_guid, patch_internal_transfer, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_guid (str): Identifier for the transfer.
            patch_internal_transfer (PatchInternalTransfer):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransfer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['transfer_guid'] = \
            transfer_guid
        kwargs['patch_internal_transfer'] = \
            patch_internal_transfer
        return self.internal_patch_transfer_endpoint.call_with_http_info(**kwargs)

    def internal_patch_transfer_screening(
        self,
        transfer_screening_guid,
        patch_internal_transfer_screening,
        **kwargs
    ):
        """Patch External Wallet Screening  # noqa: E501

        Patch an transfer screening.  Required scope: **internal:transfer_screenings:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_transfer_screening(transfer_screening_guid, patch_internal_transfer_screening, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_screening_guid (str): Identifier for the transfer screening.
            patch_internal_transfer_screening (PatchInternalTransferScreening):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalTransferScreening
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['transfer_screening_guid'] = \
            transfer_screening_guid
        kwargs['patch_internal_transfer_screening'] = \
            patch_internal_transfer_screening
        return self.internal_patch_transfer_screening_endpoint.call_with_http_info(**kwargs)

    def internal_patch_wallet_service(
        self,
        guid,
        patch_internal_wallet_service,
        **kwargs
    ):
        """Patch Internal Wallet  # noqa: E501

        Patch an internal wallet.  Required scope: **internal:wallet_services:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_wallet_service(guid, patch_internal_wallet_service, async_req=True)
        >>> result = thread.get()

        Args:
            guid (str): Identifier for the resource.
            patch_internal_wallet_service (PatchInternalWalletService):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalWalletService
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['guid'] = \
            guid
        kwargs['patch_internal_wallet_service'] = \
            patch_internal_wallet_service
        return self.internal_patch_wallet_service_endpoint.call_with_http_info(**kwargs)

    def internal_patch_workflow(
        self,
        workflow_guid,
        patch_internal_workflow,
        **kwargs
    ):
        """Patch Workflow  # noqa: E501

        Patch an workflow.  Required scope: **internal:workflows:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_patch_workflow(workflow_guid, patch_internal_workflow, async_req=True)
        >>> result = thread.get()

        Args:
            workflow_guid (str): Identifier for the workflow.
            patch_internal_workflow (PatchInternalWorkflow):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Workflow
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['workflow_guid'] = \
            workflow_guid
        kwargs['patch_internal_workflow'] = \
            patch_internal_workflow
        return self.internal_patch_workflow_endpoint.call_with_http_info(**kwargs)

    def internal_signal_external_wallet_screening(
        self,
        external_wallet_screening_guid,
        post_signal_internal_external_wallet_screening,
        **kwargs
    ):
        """Signal External Wallet Screening  # noqa: E501

        Signal an external wallet screening with a outcome.  Required scope: **internal:external_wallet_screenings:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_signal_external_wallet_screening(external_wallet_screening_guid, post_signal_internal_external_wallet_screening, async_req=True)
        >>> result = thread.get()

        Args:
            external_wallet_screening_guid (str): Identifier for the external wallet screening.
            post_signal_internal_external_wallet_screening (PostSignalInternalExternalWalletScreening):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExternalWalletScreening
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['external_wallet_screening_guid'] = \
            external_wallet_screening_guid
        kwargs['post_signal_internal_external_wallet_screening'] = \
            post_signal_internal_external_wallet_screening
        return self.internal_signal_external_wallet_screening_endpoint.call_with_http_info(**kwargs)

    def internal_signal_identity_verification(
        self,
        identity_verification_guid,
        post_signal_internal_identity_verification,
        **kwargs
    ):
        """Signal Identity Verification  # noqa: E501

        Signal an identity verification with a decision.  Required scope: **internal:identity_verifications:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_signal_identity_verification(identity_verification_guid, post_signal_internal_identity_verification, async_req=True)
        >>> result = thread.get()

        Args:
            identity_verification_guid (str): Identifier for the identity verification.
            post_signal_internal_identity_verification (PostSignalInternalIdentityVerification):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            IdentityVerification
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['identity_verification_guid'] = \
            identity_verification_guid
        kwargs['post_signal_internal_identity_verification'] = \
            post_signal_internal_identity_verification
        return self.internal_signal_identity_verification_endpoint.call_with_http_info(**kwargs)

    def internal_signal_invoice(
        self,
        invoice_guid,
        **kwargs
    ):
        """Signal Invoice  # noqa: E501

        Signal an invoice to complete settlment.  Required scope: **internal:invoices:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_signal_invoice(invoice_guid, async_req=True)
        >>> result = thread.get()

        Args:
            invoice_guid (str): Identifier for the invoice.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalInvoice
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['invoice_guid'] = \
            invoice_guid
        return self.internal_signal_invoice_endpoint.call_with_http_info(**kwargs)

    def internal_signal_transfer(
        self,
        transfer_guid,
        **kwargs
    ):
        """Signal Transfer  # noqa: E501

        Signal an transfer to proceed.  Required scope: **internal:transfers:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.internal_signal_transfer(transfer_guid, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_guid (str): Identifier for the transfer.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Transfer
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['transfer_guid'] = \
            transfer_guid
        return self.internal_signal_transfer_endpoint.call_with_http_info(**kwargs)

    def patch_internal_execution(
        self,
        execution_guid,
        patch_internal_execution,
        **kwargs
    ):
        """Patch Execution  # noqa: E501

        Patch an execution verification.  Required scope: **internal:executions:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_internal_execution(execution_guid, patch_internal_execution, async_req=True)
        >>> result = thread.get()

        Args:
            execution_guid (str): Identifier for the execution.
            patch_internal_execution (PatchInternalExecution):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalExecution
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['execution_guid'] = \
            execution_guid
        kwargs['patch_internal_execution'] = \
            patch_internal_execution
        return self.patch_internal_execution_endpoint.call_with_http_info(**kwargs)

    def patch_internal_plan(
        self,
        plan_guid,
        patch_internal_plan,
        **kwargs
    ):
        """Patch Plan  # noqa: E501

        Patch an plan verification.  Required scope: **internal:plans:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_internal_plan(plan_guid, patch_internal_plan, async_req=True)
        >>> result = thread.get()

        Args:
            plan_guid (str): Identifier for the plan.
            patch_internal_plan (PatchInternalPlan):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalPlan
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['plan_guid'] = \
            plan_guid
        kwargs['patch_internal_plan'] = \
            patch_internal_plan
        return self.patch_internal_plan_endpoint.call_with_http_info(**kwargs)

    def patch_internal_stage(
        self,
        stage_guid,
        patch_internal_stage,
        **kwargs
    ):
        """Patch Stage  # noqa: E501

        Patch a stage.  Required scope: **internal:plans:write**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_internal_stage(stage_guid, patch_internal_stage, async_req=True)
        >>> result = thread.get()

        Args:
            stage_guid (str): Identifier for the stage.
            patch_internal_stage (PatchInternalStage):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InternalStage
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['stage_guid'] = \
            stage_guid
        kwargs['patch_internal_stage'] = \
            patch_internal_stage
        return self.patch_internal_stage_endpoint.call_with_http_info(**kwargs)

