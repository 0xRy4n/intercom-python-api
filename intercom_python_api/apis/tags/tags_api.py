# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.contacts_contact_id_tags.post import AttachTagToContact
from intercom_python_api.paths.conversations_conversation_id_tags.post import AttachTagToConversation
from intercom_python_api.paths.tags.post import CreateTag
from intercom_python_api.paths.tags_id.delete import DeleteTag
from intercom_python_api.paths.contacts_contact_id_tags_id.delete import DetachTagFromContact
from intercom_python_api.paths.conversations_conversation_id_tags_id.delete import DetachTagFromConversation
from intercom_python_api.paths.tags_id.get import FindTag
from intercom_python_api.paths.tags.get import ListTags
from intercom_python_api.paths.contacts_contact_id_tags.get import ListTagsForAContact


class TagsApi(
    AttachTagToContact,
    AttachTagToConversation,
    CreateTag,
    DeleteTag,
    DetachTagFromContact,
    DetachTagFromConversation,
    FindTag,
    ListTags,
    ListTagsForAContact,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass