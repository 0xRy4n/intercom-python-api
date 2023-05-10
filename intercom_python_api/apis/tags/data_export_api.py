# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.export_cancel_job_identifier.post import CancelDataExport
from intercom_python_api.paths.export_content_data.post import CreateDataExport
from intercom_python_api.paths.download_content_data_job_identifier.get import DownloadDataExport
from intercom_python_api.paths.export_content_data_job_identifier.get import GetDataExport


class DataExportApi(
    CancelDataExport,
    CreateDataExport,
    DownloadDataExport,
    GetDataExport,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
