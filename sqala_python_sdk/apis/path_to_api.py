import typing_extensions

from sqala_python_sdk.paths import PathValues
from sqala_python_sdk.apis.paths.access_tokens import AccessTokens
from sqala_python_sdk.apis.paths.pix_qrcode_payments import PixQrcodePayments
from sqala_python_sdk.apis.paths.pix_qrcode_payments_id import PixQrcodePaymentsId
from sqala_python_sdk.apis.paths.itp_payments import ItpPayments
from sqala_python_sdk.apis.paths.itp_payments_id import ItpPaymentsId
from sqala_python_sdk.apis.paths.bank_transfer_payments_bank_transfer_id import BankTransferPaymentsBankTransferId
from sqala_python_sdk.apis.paths.bank_transfer_payments import BankTransferPayments
from sqala_python_sdk.apis.paths.recipients import Recipients
from sqala_python_sdk.apis.paths.recipients_id import RecipientsId
from sqala_python_sdk.apis.paths.recipients_recipient_id_bank_accounts import RecipientsRecipientIdBankAccounts
from sqala_python_sdk.apis.paths.recipients_recipient_id_bank_accounts_bank_account_id import RecipientsRecipientIdBankAccountsBankAccountId
from sqala_python_sdk.apis.paths.recipients_recipient_id_withdrawals import RecipientsRecipientIdWithdrawals
from sqala_python_sdk.apis.paths.recipients_recipient_id_withdrawals_withdrawal_id import RecipientsRecipientIdWithdrawalsWithdrawalId
from sqala_python_sdk.apis.paths.recipients_recipient_id_balance import RecipientsRecipientIdBalance
from sqala_python_sdk.apis.paths.recipients_recipient_id_transactions import RecipientsRecipientIdTransactions
from sqala_python_sdk.apis.paths.webhooks_id_attempts import WebhooksIdAttempts
from sqala_python_sdk.apis.paths.webhooks_id import WebhooksId
from sqala_python_sdk.apis.paths.webhooks import Webhooks

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCESSTOKENS: AccessTokens,
        PathValues.PIXQRCODEPAYMENTS: PixQrcodePayments,
        PathValues.PIXQRCODEPAYMENTS_ID: PixQrcodePaymentsId,
        PathValues.ITPPAYMENTS: ItpPayments,
        PathValues.ITPPAYMENTS_ID: ItpPaymentsId,
        PathValues.BANKTRANSFERPAYMENTS_BANK_TRANSFER_ID: BankTransferPaymentsBankTransferId,
        PathValues.BANKTRANSFERPAYMENTS: BankTransferPayments,
        PathValues.RECIPIENTS: Recipients,
        PathValues.RECIPIENTS_ID: RecipientsId,
        PathValues.RECIPIENTS_RECIPIENT_ID_BANKACCOUNTS: RecipientsRecipientIdBankAccounts,
        PathValues.RECIPIENTS_RECIPIENT_ID_BANKACCOUNTS_BANK_ACCOUNT_ID: RecipientsRecipientIdBankAccountsBankAccountId,
        PathValues.RECIPIENTS_RECIPIENT_ID_WITHDRAWALS: RecipientsRecipientIdWithdrawals,
        PathValues.RECIPIENTS_RECIPIENT_ID_WITHDRAWALS_WITHDRAWAL_ID: RecipientsRecipientIdWithdrawalsWithdrawalId,
        PathValues.RECIPIENTS_RECIPIENT_ID_BALANCE: RecipientsRecipientIdBalance,
        PathValues.RECIPIENTS_RECIPIENT_ID_TRANSACTIONS: RecipientsRecipientIdTransactions,
        PathValues.WEBHOOKS_ID_ATTEMPTS: WebhooksIdAttempts,
        PathValues.WEBHOOKS_ID: WebhooksId,
        PathValues.WEBHOOKS: Webhooks,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCESSTOKENS: AccessTokens,
        PathValues.PIXQRCODEPAYMENTS: PixQrcodePayments,
        PathValues.PIXQRCODEPAYMENTS_ID: PixQrcodePaymentsId,
        PathValues.ITPPAYMENTS: ItpPayments,
        PathValues.ITPPAYMENTS_ID: ItpPaymentsId,
        PathValues.BANKTRANSFERPAYMENTS_BANK_TRANSFER_ID: BankTransferPaymentsBankTransferId,
        PathValues.BANKTRANSFERPAYMENTS: BankTransferPayments,
        PathValues.RECIPIENTS: Recipients,
        PathValues.RECIPIENTS_ID: RecipientsId,
        PathValues.RECIPIENTS_RECIPIENT_ID_BANKACCOUNTS: RecipientsRecipientIdBankAccounts,
        PathValues.RECIPIENTS_RECIPIENT_ID_BANKACCOUNTS_BANK_ACCOUNT_ID: RecipientsRecipientIdBankAccountsBankAccountId,
        PathValues.RECIPIENTS_RECIPIENT_ID_WITHDRAWALS: RecipientsRecipientIdWithdrawals,
        PathValues.RECIPIENTS_RECIPIENT_ID_WITHDRAWALS_WITHDRAWAL_ID: RecipientsRecipientIdWithdrawalsWithdrawalId,
        PathValues.RECIPIENTS_RECIPIENT_ID_BALANCE: RecipientsRecipientIdBalance,
        PathValues.RECIPIENTS_RECIPIENT_ID_TRANSACTIONS: RecipientsRecipientIdTransactions,
        PathValues.WEBHOOKS_ID_ATTEMPTS: WebhooksIdAttempts,
        PathValues.WEBHOOKS_ID: WebhooksId,
        PathValues.WEBHOOKS: Webhooks,
    }
)
