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


class RecipientDeleteBankAccountResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            code = schemas.StrSchema
            holderName = schemas.StrSchema
            holderTaxId = schemas.StrSchema
            holderType = schemas.StrSchema
            branchNumber = schemas.StrSchema
            accountNumber = schemas.StrSchema
            bankId = schemas.StrSchema
            status = schemas.StrSchema
            createdAt = schemas.StrSchema
            updatedAt = schemas.AnyTypeSchema
            deletedAt = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['RecipientDeleteBankAccountResponseMetadata']:
                return RecipientDeleteBankAccountResponseMetadata
            __annotations__ = {
                "id": id,
                "code": code,
                "holderName": holderName,
                "holderTaxId": holderTaxId,
                "holderType": holderType,
                "branchNumber": branchNumber,
                "accountNumber": accountNumber,
                "bankId": bankId,
                "status": status,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "deletedAt": deletedAt,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holderName"]) -> MetaOapg.properties.holderName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holderTaxId"]) -> MetaOapg.properties.holderTaxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holderType"]) -> MetaOapg.properties.holderType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branchNumber"]) -> MetaOapg.properties.branchNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNumber"]) -> MetaOapg.properties.accountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankId"]) -> MetaOapg.properties.bankId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletedAt"]) -> MetaOapg.properties.deletedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'RecipientDeleteBankAccountResponseMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "code", "holderName", "holderTaxId", "holderType", "branchNumber", "accountNumber", "bankId", "status", "createdAt", "updatedAt", "deletedAt", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holderName"]) -> typing.Union[MetaOapg.properties.holderName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holderTaxId"]) -> typing.Union[MetaOapg.properties.holderTaxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holderType"]) -> typing.Union[MetaOapg.properties.holderType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branchNumber"]) -> typing.Union[MetaOapg.properties.branchNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNumber"]) -> typing.Union[MetaOapg.properties.accountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankId"]) -> typing.Union[MetaOapg.properties.bankId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletedAt"]) -> typing.Union[MetaOapg.properties.deletedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['RecipientDeleteBankAccountResponseMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "code", "holderName", "holderTaxId", "holderType", "branchNumber", "accountNumber", "bankId", "status", "createdAt", "updatedAt", "deletedAt", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        holderName: typing.Union[MetaOapg.properties.holderName, str, schemas.Unset] = schemas.unset,
        holderTaxId: typing.Union[MetaOapg.properties.holderTaxId, str, schemas.Unset] = schemas.unset,
        holderType: typing.Union[MetaOapg.properties.holderType, str, schemas.Unset] = schemas.unset,
        branchNumber: typing.Union[MetaOapg.properties.branchNumber, str, schemas.Unset] = schemas.unset,
        accountNumber: typing.Union[MetaOapg.properties.accountNumber, str, schemas.Unset] = schemas.unset,
        bankId: typing.Union[MetaOapg.properties.bankId, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        deletedAt: typing.Union[MetaOapg.properties.deletedAt, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['RecipientDeleteBankAccountResponseMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecipientDeleteBankAccountResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            code=code,
            holderName=holderName,
            holderTaxId=holderTaxId,
            holderType=holderType,
            branchNumber=branchNumber,
            accountNumber=accountNumber,
            bankId=bankId,
            status=status,
            createdAt=createdAt,
            updatedAt=updatedAt,
            deletedAt=deletedAt,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from sqala_python_sdk.model.recipient_delete_bank_account_response_metadata import RecipientDeleteBankAccountResponseMetadata
