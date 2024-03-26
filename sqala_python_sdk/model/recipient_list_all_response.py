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


class RecipientListAllResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['RecipientListAllResponseData']:
                return RecipientListAllResponseData
        
            @staticmethod
            def paging() -> typing.Type['RecipientListAllResponsePaging']:
                return RecipientListAllResponsePaging
            __annotations__ = {
                "data": data,
                "paging": paging,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'RecipientListAllResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> 'RecipientListAllResponsePaging': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "paging", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['RecipientListAllResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> typing.Union['RecipientListAllResponsePaging', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "paging", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['RecipientListAllResponseData', schemas.Unset] = schemas.unset,
        paging: typing.Union['RecipientListAllResponsePaging', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecipientListAllResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            paging=paging,
            _configuration=_configuration,
            **kwargs,
        )

from sqala_python_sdk.model.recipient_list_all_response_data import RecipientListAllResponseData
from sqala_python_sdk.model.recipient_list_all_response_paging import RecipientListAllResponsePaging
