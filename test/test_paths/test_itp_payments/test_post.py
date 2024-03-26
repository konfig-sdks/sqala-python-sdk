# coding: utf-8

"""
    Developer API

    At Sqala, we believe that everyone deserves access to financial services, and we are committed to providing secure and reliable payment solutions to clients who may have been overlooked by traditional financial institutions.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import sqala_python_sdk
from sqala_python_sdk.paths.itp_payments import post
from sqala_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestItpPayments(ApiTestMixin, unittest.TestCase):
    """
    ItpPayments unit test stubs
        Create an ITP
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
