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

from sqala_python_sdk.type.itp_get_itp_response_metadata import ItpGetItpResponseMetadata
from sqala_python_sdk.type.itp_get_itp_response_payer import ItpGetItpResponsePayer
from sqala_python_sdk.type.itp_get_itp_response_split import ItpGetItpResponseSplit

class RequiredItpGetItpResponse(TypedDict):
    pass

class OptionalItpGetItpResponse(TypedDict, total=False):
    id: str

    code: str

    type: str

    amount: int

    paidAmount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    payload: str

    payer: ItpGetItpResponsePayer

    split: ItpGetItpResponseSplit

    status: str

    createdAt: str

    processedAt: str

    paidAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    failedAt: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    metadata: ItpGetItpResponseMetadata

class ItpGetItpResponse(RequiredItpGetItpResponse, OptionalItpGetItpResponse):
    pass
