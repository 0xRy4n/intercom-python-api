# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import intercom_python_api
from intercom_python_api.paths.companies_id import delete  # noqa: E501
from intercom_python_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCompaniesId(ApiTestMixin, unittest.TestCase):
    """
    CompaniesId unit test stubs
        Delete a company  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
