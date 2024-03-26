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

from sqala_python_sdk.type.webhook_list_all_response_data_item_data import WebhookListAllResponseDataItemData
from sqala_python_sdk.type.webhook_list_all_response_data_item_object import WebhookListAllResponseDataItemObject
from sqala_python_sdk.type.webhook_list_all_response_data_item_responses import WebhookListAllResponseDataItemResponses

class RequiredWebhookListAllResponseDataItem(TypedDict):
    pass

class OptionalWebhookListAllResponseDataItem(TypedDict, total=False):
    responses: WebhookListAllResponseDataItemResponses

    id: str

    event: str

    object: WebhookListAllResponseDataItemObject

    signature: str

    data: WebhookListAllResponseDataItemData

    status: str

    createdAt: str

    queuedAt: str

    deliveredAt: str

    failedAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    lastAttemptAt: str

    nextAttemptAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    endpointId: str

    organizationId: str

class WebhookListAllResponseDataItem(RequiredWebhookListAllResponseDataItem, OptionalWebhookListAllResponseDataItem):
    pass
