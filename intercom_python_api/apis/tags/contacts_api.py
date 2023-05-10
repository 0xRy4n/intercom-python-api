# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.contacts_id_archive.post import ArchiveContact
from intercom_python_api.paths.contacts_id_companies.post import AttachContactToACompany
from intercom_python_api.paths.contacts_contact_id_subscriptions.post import AttachSubscriptionTypeToContact
from intercom_python_api.paths.contacts_contact_id_tags.post import AttachTagToContact
from intercom_python_api.paths.contacts.post import CreateContact
from intercom_python_api.paths.contacts_id_notes.post import CreateNote
from intercom_python_api.paths.contacts_id.delete import DeleteContact
from intercom_python_api.paths.contacts_contact_id_subscriptions_id.delete import DetachSubscriptionTypeToContact
from intercom_python_api.paths.contacts_contact_id_tags_id.delete import DetachTagFromContact
from intercom_python_api.paths.contacts_contact_id_companies_id.delete import DettachContactFromACompany
from intercom_python_api.paths.companies_id_contacts.get import ListAttachedContacts
from intercom_python_api.paths.contacts_contact_id_companies.get import ListCompaniesForAContact
from intercom_python_api.paths.contacts.get import ListContacts
from intercom_python_api.paths.contacts_id_notes.get import ListNotes
from intercom_python_api.paths.contacts_contact_id_segments.get import ListSegmentsForAContact
from intercom_python_api.paths.contacts_contact_id_subscriptions.get import ListSubscriptionsForAContact
from intercom_python_api.paths.contacts_contact_id_tags.get import ListTagsForAContact
from intercom_python_api.paths.contacts_merge.post import MergeContact
from intercom_python_api.paths.contacts_search.post import SearchContacts
from intercom_python_api.paths.contacts_id.get import ShowContact
from intercom_python_api.paths.contacts_id_unarchive.post import UnarchiveContact
from intercom_python_api.paths.contacts_id.put import UpdateContact


class ContactsApi(
    ArchiveContact,
    AttachContactToACompany,
    AttachSubscriptionTypeToContact,
    AttachTagToContact,
    CreateContact,
    CreateNote,
    DeleteContact,
    DetachSubscriptionTypeToContact,
    DetachTagFromContact,
    DettachContactFromACompany,
    ListAttachedContacts,
    ListCompaniesForAContact,
    ListContacts,
    ListNotes,
    ListSegmentsForAContact,
    ListSubscriptionsForAContact,
    ListTagsForAContact,
    MergeContact,
    SearchContacts,
    ShowContact,
    UnarchiveContact,
    UpdateContact,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass