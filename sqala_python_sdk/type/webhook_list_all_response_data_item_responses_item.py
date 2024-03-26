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


class RequiredWebhookListAllResponseDataItemResponsesItem(TypedDict):
    pass

class OptionalWebhookListAllResponseDataItemResponsesItem(TypedDict, total=False):
    code: int

    time: int

    at: str

class WebhookListAllResponseDataItemResponsesItem(RequiredWebhookListAllResponseDataItemResponsesItem, OptionalWebhookListAllResponseDataItemResponsesItem):
    pass
