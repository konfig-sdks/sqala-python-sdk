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


class RecipientCreateRecipientRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "taxId",
            "name",
            "type",
        }
        
        class properties:
            name = schemas.StrSchema
            taxId = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "INDIVIDUAL": "INDIVIDUAL",
                        "COMPANY": "COMPANY",
                    }
                
                @schemas.classproperty
                def INDIVIDUAL(cls):
                    return cls("INDIVIDUAL")
                
                @schemas.classproperty
                def COMPANY(cls):
                    return cls("COMPANY")
            code = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['RecipientCreateRecipientRequestMetadata']:
                return RecipientCreateRecipientRequestMetadata
            __annotations__ = {
                "name": name,
                "taxId": taxId,
                "type": type,
                "code": code,
                "metadata": metadata,
            }
    
    taxId: MetaOapg.properties.taxId
    name: MetaOapg.properties.name
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'RecipientCreateRecipientRequestMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "taxId", "type", "code", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['RecipientCreateRecipientRequestMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "taxId", "type", "code", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        taxId: typing.Union[MetaOapg.properties.taxId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['RecipientCreateRecipientRequestMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecipientCreateRecipientRequest':
        return super().__new__(
            cls,
            *args,
            taxId=taxId,
            name=name,
            type=type,
            code=code,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from sqala_python_sdk.model.recipient_create_recipient_request_metadata import RecipientCreateRecipientRequestMetadata
