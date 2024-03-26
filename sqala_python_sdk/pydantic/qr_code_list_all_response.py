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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sqala_python_sdk.pydantic.qr_code_list_all_response_data import QrCodeListAllResponseData
from sqala_python_sdk.pydantic.qr_code_list_all_response_paging import QrCodeListAllResponsePaging

class QrCodeListAllResponse(BaseModel):
    data: typing.Optional[QrCodeListAllResponseData] = Field(None, alias='data')

    paging: typing.Optional[QrCodeListAllResponsePaging] = Field(None, alias='paging')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
