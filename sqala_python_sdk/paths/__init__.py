# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sqala_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCESSTOKENS = "/access-tokens"
    PIXQRCODEPAYMENTS = "/pix-qrcode-payments"
    PIXQRCODEPAYMENTS_ID = "/pix-qrcode-payments/{id}"
    ITPPAYMENTS = "/itp-payments"
    ITPPAYMENTS_ID = "/itp-payments/{id}"
    BANKTRANSFERPAYMENTS_BANK_TRANSFER_ID = "/bank-transfer-payments/{bankTransferId}"
    BANKTRANSFERPAYMENTS = "/bank-transfer-payments"
    RECIPIENTS = "/recipients"
    RECIPIENTS_ID = "/recipients/{id}"
    RECIPIENTS_RECIPIENT_ID_BANKACCOUNTS = "/recipients/{recipientId}/bank-accounts"
    RECIPIENTS_RECIPIENT_ID_BANKACCOUNTS_BANK_ACCOUNT_ID = "/recipients/{recipientId}/bank-accounts/{bankAccountId}"
    RECIPIENTS_RECIPIENT_ID_WITHDRAWALS = "/recipients/{recipientId}/withdrawals"
    RECIPIENTS_RECIPIENT_ID_WITHDRAWALS_WITHDRAWAL_ID = "/recipients/{recipientId}/withdrawals/{withdrawalId}"
    RECIPIENTS_RECIPIENT_ID_BALANCE = "/recipients/{recipientId}/balance"
    RECIPIENTS_RECIPIENT_ID_TRANSACTIONS = "/recipients/{recipientId}/transactions"
    WEBHOOKS_ID_ATTEMPTS = "/webhooks/{id}/attempts"
    WEBHOOKS_ID = "/webhooks/{id}"
    WEBHOOKS = "/webhooks"
