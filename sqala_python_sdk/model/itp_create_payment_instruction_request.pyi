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


class ItpCreatePaymentInstructionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "payer",
        }
        
        class properties:
            amount = schemas.Int32Schema
        
            @staticmethod
            def payer() -> typing.Type['ItpCreatePaymentInstructionRequestPayer']:
                return ItpCreatePaymentInstructionRequestPayer
            code = schemas.StrSchema
        
            @staticmethod
            def split() -> typing.Type['ItpCreatePaymentInstructionRequestSplit']:
                return ItpCreatePaymentInstructionRequestSplit
        
            @staticmethod
            def metadata() -> typing.Type['ItpCreatePaymentInstructionRequestMetadata']:
                return ItpCreatePaymentInstructionRequestMetadata
            __annotations__ = {
                "amount": amount,
                "payer": payer,
                "code": code,
                "split": split,
                "metadata": metadata,
            }
    
    amount: MetaOapg.properties.amount
    payer: 'ItpCreatePaymentInstructionRequestPayer'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payer"]) -> 'ItpCreatePaymentInstructionRequestPayer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["split"]) -> 'ItpCreatePaymentInstructionRequestSplit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'ItpCreatePaymentInstructionRequestMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "payer", "code", "split", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payer"]) -> 'ItpCreatePaymentInstructionRequestPayer': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["split"]) -> typing.Union['ItpCreatePaymentInstructionRequestSplit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['ItpCreatePaymentInstructionRequestMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "payer", "code", "split", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        payer: 'ItpCreatePaymentInstructionRequestPayer',
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        split: typing.Union['ItpCreatePaymentInstructionRequestSplit', schemas.Unset] = schemas.unset,
        metadata: typing.Union['ItpCreatePaymentInstructionRequestMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ItpCreatePaymentInstructionRequest':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            payer=payer,
            code=code,
            split=split,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from sqala_python_sdk.model.itp_create_payment_instruction_request_metadata import ItpCreatePaymentInstructionRequestMetadata
from sqala_python_sdk.model.itp_create_payment_instruction_request_payer import ItpCreatePaymentInstructionRequestPayer
from sqala_python_sdk.model.itp_create_payment_instruction_request_split import ItpCreatePaymentInstructionRequestSplit
