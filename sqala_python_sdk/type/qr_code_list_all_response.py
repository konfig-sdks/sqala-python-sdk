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

from sqala_python_sdk.type.qr_code_list_all_response_data import QrCodeListAllResponseData
from sqala_python_sdk.type.qr_code_list_all_response_paging import QrCodeListAllResponsePaging

class RequiredQrCodeListAllResponse(TypedDict):
    pass

class OptionalQrCodeListAllResponse(TypedDict, total=False):
    data: QrCodeListAllResponseData

    paging: QrCodeListAllResponsePaging

class QrCodeListAllResponse(RequiredQrCodeListAllResponse, OptionalQrCodeListAllResponse):
    pass
