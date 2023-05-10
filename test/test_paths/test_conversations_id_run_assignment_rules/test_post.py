# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import intercom_python_api
from intercom_python_api.paths.conversations_id_run_assignment_rules import post  # noqa: E501
from intercom_python_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestConversationsIdRunAssignmentRules(ApiTestMixin, unittest.TestCase):
    """
    ConversationsIdRunAssignmentRules unit test stubs
        Run Assignment Rules on a conversation  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
