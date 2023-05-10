# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from intercom_python_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ME = "/me"
    ADMINS_ID_AWAY = "/admins/{id}/away"
    ADMINS_ACTIVITY_LOGS = "/admins/activity_logs"
    ADMINS = "/admins"
    ADMINS_ID = "/admins/{id}"
    ARTICLES = "/articles"
    ARTICLES_ID = "/articles/{id}"
    HELP_CENTER_COLLECTIONS = "/help_center/collections"
    HELP_CENTER_COLLECTIONS_ID = "/help_center/collections/{id}"
    HELP_CENTER_SECTIONS = "/help_center/sections"
    HELP_CENTER_SECTIONS_ID = "/help_center/sections/{id}"
    COMPANIES = "/companies"
    COMPANIES_ID = "/companies/{id}"
    COMPANIES_ID_CONTACTS = "/companies/{id}/contacts"
    COMPANIES_ID_SEGMENTS = "/companies/{id}/segments"
    COMPANIES_LIST = "/companies/list"
    COMPANIES_SCROLL = "/companies/scroll"
    CONTACTS_ID_COMPANIES = "/contacts/{id}/companies"
    CONTACTS_CONTACT_ID_COMPANIES_ID = "/contacts/{contact_id}/companies/{id}"
    CONTACTS_CONTACT_ID_COMPANIES = "/contacts/{contact_id}/companies"
    CONTACTS_ID_NOTES = "/contacts/{id}/notes"
    CONTACTS_CONTACT_ID_SEGMENTS = "/contacts/{contact_id}/segments"
    CONTACTS_CONTACT_ID_SUBSCRIPTIONS = "/contacts/{contact_id}/subscriptions"
    CONTACTS_CONTACT_ID_SUBSCRIPTIONS_ID = "/contacts/{contact_id}/subscriptions/{id}"
    CONTACTS_CONTACT_ID_TAGS = "/contacts/{contact_id}/tags"
    CONTACTS_CONTACT_ID_TAGS_ID = "/contacts/{contact_id}/tags/{id}"
    CONTACTS_ID = "/contacts/{id}"
    CONTACTS_MERGE = "/contacts/merge"
    CONTACTS_SEARCH = "/contacts/search"
    CONTACTS = "/contacts"
    CONTACTS_ID_ARCHIVE = "/contacts/{id}/archive"
    CONTACTS_ID_UNARCHIVE = "/contacts/{id}/unarchive"
    CONVERSATIONS_CONVERSATION_ID_TAGS = "/conversations/{conversation_id}/tags"
    CONVERSATIONS_CONVERSATION_ID_TAGS_ID = "/conversations/{conversation_id}/tags/{id}"
    CONVERSATIONS = "/conversations"
    CONVERSATIONS_ID = "/conversations/{id}"
    CONVERSATIONS_SEARCH = "/conversations/search"
    CONVERSATIONS_ID_REPLY = "/conversations/{id}/reply"
    CONVERSATIONS_ID_PARTS = "/conversations/{id}/parts"
    CONVERSATIONS_ID_RUN_ASSIGNMENT_RULES = "/conversations/{id}/run_assignment_rules"
    CONVERSATIONS_ID_CUSTOMERS = "/conversations/{id}/customers"
    CONVERSATIONS_CONVERSATION_ID_CUSTOMERS_CONTACT_ID = "/conversations/{conversation_id}/customers/{contact_id}"
    CONVERSATIONS_REDACT = "/conversations/redact"
    DATA_ATTRIBUTES = "/data_attributes"
    DATA_ATTRIBUTES_ID = "/data_attributes/{id}"
    EVENTS = "/events"
    EVENTS_SUMMARIES = "/events/summaries"
    EXPORT_CONTENT_DATA = "/export/content/data"
    EXPORT_CONTENT_DATA_JOB_IDENTIFIER = "/export/content/data/{job_identifier}"
    EXPORT_CANCEL_JOB_IDENTIFIER = "/export/cancel/{job_identifier}"
    DOWNLOAD_CONTENT_DATA_JOB_IDENTIFIER = "/download/content/data/{job_identifier}"
    MESSAGES = "/messages"
    NEWS_NEWS_ITEMS = "/news/news_items"
    NEWS_NEWS_ITEMS_ID = "/news/news_items/{id}"
    NEWS_NEWSFEEDS_ID_ITEMS = "/news/newsfeeds/{id}/items"
    NEWS_NEWSFEEDS = "/news/newsfeeds"
    NEWS_NEWSFEEDS_ID = "/news/newsfeeds/{id}"
    NOTES_ID = "/notes/{id}"
    SEGMENTS = "/segments"
    SEGMENTS_ID = "/segments/{id}"
    SUBSCRIPTION_TYPES = "/subscription_types"
    PHONE_CALL_REDIRECTS = "/phone_call_redirects"
    TAGS = "/tags"
    TAGS_ID = "/tags/{id}"
    TEAMS = "/teams"
    TEAMS_ID = "/teams/{id}"
    VISITORS = "/visitors"
    VISITORS_ID = "/visitors/{id}"
    VISITORS_CONVERT = "/visitors/convert"