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

from sqala_python_sdk.pydantic.recipient_delete_bank_account_response_metadata import RecipientDeleteBankAccountResponseMetadata

class RecipientDeleteBankAccountResponse(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    code: typing.Optional[str] = Field(None, alias='code')

    holder_name: typing.Optional[str] = Field(None, alias='holderName')

    holder_tax_id: typing.Optional[str] = Field(None, alias='holderTaxId')

    holder_type: typing.Optional[str] = Field(None, alias='holderType')

    branch_number: typing.Optional[str] = Field(None, alias='branchNumber')

    account_number: typing.Optional[str] = Field(None, alias='accountNumber')

    bank_id: typing.Optional[str] = Field(None, alias='bankId')

    status: typing.Optional[str] = Field(None, alias='status')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[str] = Field(None, alias='deletedAt')

    metadata: typing.Optional[RecipientDeleteBankAccountResponseMetadata] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
