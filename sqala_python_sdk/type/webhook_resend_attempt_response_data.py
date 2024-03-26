# coding: utf-8

"""
    Developer API

    At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from sqala_python_sdk.type.webhook_resend_attempt_response_data_destination import WebhookResendAttemptResponseDataDestination
from sqala_python_sdk.type.webhook_resend_attempt_response_data_payer import WebhookResendAttemptResponseDataPayer
from sqala_python_sdk.type.webhook_resend_attempt_response_data_source import WebhookResendAttemptResponseDataSource
from sqala_python_sdk.type.webhook_resend_attempt_response_data_split import WebhookResendAttemptResponseDataSplit

class RequiredWebhookResendAttemptResponseData(TypedDict):
    pass

class OptionalWebhookResendAttemptResponseData(TypedDict, total=False):
    id: str

    code: str

    transactionId: str

    amount: int

    paidAmount: int

    method: str

    status: str

    createdAt: str

    processedAt: str

    paidAt: str

    failedAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    split: WebhookResendAttemptResponseDataSplit

    payer: WebhookResendAttemptResponseDataPayer

    source: WebhookResendAttemptResponseDataSource

    destination: WebhookResendAttemptResponseDataDestination

class WebhookResendAttemptResponseData(RequiredWebhookResendAttemptResponseData, OptionalWebhookResendAttemptResponseData):
    pass
