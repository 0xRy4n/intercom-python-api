# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import intercom_python_api

try:
    from intercom_python_api.paths.conversations_id import get  # noqa: E501
except:
    get = None
    
from intercom_python_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestConversationsId(ApiTestMixin, unittest.TestCase):
    """
    ConversationsId unit test stubs
        Retrieve a conversation  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
