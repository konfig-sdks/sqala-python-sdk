# coding: utf-8

"""
    Developer API

    At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from sqala_python_sdk.paths.webhooks_id.get import GetRaw
from sqala_python_sdk.paths.webhooks.get import ListAllRaw
from sqala_python_sdk.paths.webhooks_id_attempts.post import ResendAttemptRaw


class WebhookApiRaw(
    GetRaw,
    ListAllRaw,
    ResendAttemptRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
