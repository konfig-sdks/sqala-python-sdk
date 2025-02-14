# coding: utf-8

"""
    Developer API

    At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from sqala_python_sdk.paths.access_tokens.post import GenerateAccessToken
from sqala_python_sdk.apis.tags.token_api_raw import TokenApiRaw


class TokenApi(
    GenerateAccessToken,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TokenApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TokenApiRaw(api_client)
