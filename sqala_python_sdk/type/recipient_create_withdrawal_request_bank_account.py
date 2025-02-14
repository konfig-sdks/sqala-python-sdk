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


class RequiredRecipientCreateWithdrawalRequestBankAccount(TypedDict):
    # The name of the person or business that owns the bank account.
    holderName: str

    # The tax ID of the account holder (CPF for individual account holders or CNPJ for businesses account holders).
    holderTaxId: str

    # The type of entity that holds the account. Can be INDIVIDUAL or COMPANY.
    holderType: str

    branchNumber: str

    accountNumber: str

    # The ID of the bank associated with the account.
    bankId: str

class OptionalRecipientCreateWithdrawalRequestBankAccount(TypedDict, total=False):
    # The type of bank account. Can be CHEKING or SAVINGS.
    type: str

class RecipientCreateWithdrawalRequestBankAccount(RequiredRecipientCreateWithdrawalRequestBankAccount, OptionalRecipientCreateWithdrawalRequestBankAccount):
    pass
