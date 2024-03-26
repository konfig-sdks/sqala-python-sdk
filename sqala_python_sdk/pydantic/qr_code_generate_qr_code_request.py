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

from sqala_python_sdk.pydantic.qr_code_generate_qr_code_request_metadata import QrCodeGenerateQrCodeRequestMetadata
from sqala_python_sdk.pydantic.qr_code_generate_qr_code_request_payer import QrCodeGenerateQrCodeRequestPayer
from sqala_python_sdk.pydantic.qr_code_generate_qr_code_request_split import QrCodeGenerateQrCodeRequestSplit

class QrCodeGenerateQrCodeRequest(BaseModel):
    # Amount in cents to be paid.
    amount: int = Field(alias='amount')

    # Unique identifier for the object in your system.
    code: typing.Optional[str] = Field(None, alias='code')

    payer: typing.Optional[QrCodeGenerateQrCodeRequestPayer] = Field(None, alias='payer')

    split: typing.Optional[QrCodeGenerateQrCodeRequestSplit] = Field(None, alias='split')

    metadata: typing.Optional[QrCodeGenerateQrCodeRequestMetadata] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
