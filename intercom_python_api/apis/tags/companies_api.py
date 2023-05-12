# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.9
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.contacts_id_companies.post import AttachContactToACompany
from intercom_python_api.paths.companies.post import CreateOrUpdateCompany
from intercom_python_api.paths.companies_id.delete import DeleteCompany
from intercom_python_api.paths.contacts_contact_id_companies_id.delete import DettachContactFromACompany
from intercom_python_api.paths.companies_list.post import ListAllCompanies
from intercom_python_api.paths.companies_id_contacts.get import ListAttachedContacts
from intercom_python_api.paths.companies_id_segments.get import ListAttachedSegmentsForCompanies
from intercom_python_api.paths.contacts_contact_id_companies.get import ListCompaniesForAContact
from intercom_python_api.paths.companies_id.get import RetrieveACompanyById
from intercom_python_api.paths.companies.get import RetrieveCompany
from intercom_python_api.paths.companies_scroll.get import ScrollOverAllCompanies
from intercom_python_api.paths.companies_id.put import UpdateCompany


class CompaniesApi(
    AttachContactToACompany,
    CreateOrUpdateCompany,
    DeleteCompany,
    DettachContactFromACompany,
    ListAllCompanies,
    ListAttachedContacts,
    ListAttachedSegmentsForCompanies,
    ListCompaniesForAContact,
    RetrieveACompanyById,
    RetrieveCompany,
    ScrollOverAllCompanies,
    UpdateCompany,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
