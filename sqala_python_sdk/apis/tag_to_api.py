import typing_extensions

from sqala_python_sdk.apis.tags import TagValues
from sqala_python_sdk.apis.tags.recipient_api import RecipientApi
from sqala_python_sdk.apis.tags.webhook_api import WebhookApi
from sqala_python_sdk.apis.tags.itp_api import ITPApi
from sqala_python_sdk.apis.tags.qr_code_api import QRCodeApi
from sqala_python_sdk.apis.tags.bank_transfer_api import BankTransferApi
from sqala_python_sdk.apis.tags.token_api import TokenApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.RECIPIENT: RecipientApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.ITP: ITPApi,
        TagValues.QRCODE: QRCodeApi,
        TagValues.BANK_TRANSFER: BankTransferApi,
        TagValues.TOKEN: TokenApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.RECIPIENT: RecipientApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.ITP: ITPApi,
        TagValues.QRCODE: QRCodeApi,
        TagValues.BANK_TRANSFER: BankTransferApi,
        TagValues.TOKEN: TokenApi,
    }
)
