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


class ItpListAllResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            code = schemas.StrSchema
            type = schemas.StrSchema
            amount = schemas.IntSchema
            paidAmount = schemas.AnyTypeSchema
            payload = schemas.StrSchema
        
            @staticmethod
            def payer() -> typing.Type['ItpListAllResponseDataItemPayer']:
                return ItpListAllResponseDataItemPayer
        
            @staticmethod
            def split() -> typing.Type['ItpListAllResponseDataItemSplit']:
                return ItpListAllResponseDataItemSplit
            status = schemas.StrSchema
            createdAt = schemas.StrSchema
            processedAt = schemas.StrSchema
            paidAt = schemas.AnyTypeSchema
            failedAt = schemas.AnyTypeSchema
        
            @staticmethod
            def metadata() -> typing.Type['ItpListAllResponseDataItemMetadata']:
                return ItpListAllResponseDataItemMetadata
            __annotations__ = {
                "id": id,
                "code": code,
                "type": type,
                "amount": amount,
                "paidAmount": paidAmount,
                "payload": payload,
                "payer": payer,
                "split": split,
                "status": status,
                "createdAt": createdAt,
                "processedAt": processedAt,
                "paidAt": paidAt,
                "failedAt": failedAt,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paidAmount"]) -> MetaOapg.properties.paidAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payer"]) -> 'ItpListAllResponseDataItemPayer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["split"]) -> 'ItpListAllResponseDataItemSplit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processedAt"]) -> MetaOapg.properties.processedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paidAt"]) -> MetaOapg.properties.paidAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failedAt"]) -> MetaOapg.properties.failedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'ItpListAllResponseDataItemMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "code", "type", "amount", "paidAmount", "payload", "payer", "split", "status", "createdAt", "processedAt", "paidAt", "failedAt", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paidAmount"]) -> typing.Union[MetaOapg.properties.paidAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> typing.Union[MetaOapg.properties.payload, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payer"]) -> typing.Union['ItpListAllResponseDataItemPayer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["split"]) -> typing.Union['ItpListAllResponseDataItemSplit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processedAt"]) -> typing.Union[MetaOapg.properties.processedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paidAt"]) -> typing.Union[MetaOapg.properties.paidAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failedAt"]) -> typing.Union[MetaOapg.properties.failedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['ItpListAllResponseDataItemMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "code", "type", "amount", "paidAmount", "payload", "payer", "split", "status", "createdAt", "processedAt", "paidAt", "failedAt", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        paidAmount: typing.Union[MetaOapg.properties.paidAmount, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        payload: typing.Union[MetaOapg.properties.payload, str, schemas.Unset] = schemas.unset,
        payer: typing.Union['ItpListAllResponseDataItemPayer', schemas.Unset] = schemas.unset,
        split: typing.Union['ItpListAllResponseDataItemSplit', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        processedAt: typing.Union[MetaOapg.properties.processedAt, str, schemas.Unset] = schemas.unset,
        paidAt: typing.Union[MetaOapg.properties.paidAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        failedAt: typing.Union[MetaOapg.properties.failedAt, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        metadata: typing.Union['ItpListAllResponseDataItemMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ItpListAllResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            code=code,
            type=type,
            amount=amount,
            paidAmount=paidAmount,
            payload=payload,
            payer=payer,
            split=split,
            status=status,
            createdAt=createdAt,
            processedAt=processedAt,
            paidAt=paidAt,
            failedAt=failedAt,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from sqala_python_sdk.model.itp_list_all_response_data_item_metadata import ItpListAllResponseDataItemMetadata
from sqala_python_sdk.model.itp_list_all_response_data_item_payer import ItpListAllResponseDataItemPayer
from sqala_python_sdk.model.itp_list_all_response_data_item_split import ItpListAllResponseDataItemSplit
