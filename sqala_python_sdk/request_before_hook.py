# coding: utf-8

"""
    Developer API

    At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import typing
from urllib3._collections import HTTPHeaderDict
from sqala_python_sdk.configuration import Configuration

def request_before_hook(
        resource_path: str,
        method: str,
        configuration: Configuration,
        path_template: str,
        headers: typing.Optional[HTTPHeaderDict] = None,
        body: typing.Any = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any
):
    pass