# coding: utf-8

"""
    Developer API

    At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sqala_python_sdk import schemas  # noqa: F401


class QrCodeGetQrCodeByIdResponseMetadata(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['QrCodeGetQrCodeByIdResponseMetadataItem']:
            return QrCodeGetQrCodeByIdResponseMetadataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['QrCodeGetQrCodeByIdResponseMetadataItem'], typing.List['QrCodeGetQrCodeByIdResponseMetadataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'QrCodeGetQrCodeByIdResponseMetadata':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'QrCodeGetQrCodeByIdResponseMetadataItem':
        return super().__getitem__(i)

from sqala_python_sdk.model.qr_code_get_qr_code_by_id_response_metadata_item import QrCodeGetQrCodeByIdResponseMetadataItem
