import typing_extensions

from intercom_python_api.paths import PathValues
from intercom_python_api.apis.paths.me import Me
from intercom_python_api.apis.paths.admins_id_away import AdminsIdAway
from intercom_python_api.apis.paths.admins_activity_logs import AdminsActivityLogs
from intercom_python_api.apis.paths.admins import Admins
from intercom_python_api.apis.paths.admins_id import AdminsId
from intercom_python_api.apis.paths.articles import Articles
from intercom_python_api.apis.paths.articles_id import ArticlesId
from intercom_python_api.apis.paths.help_center_collections import HelpCenterCollections
from intercom_python_api.apis.paths.help_center_collections_id import HelpCenterCollectionsId
from intercom_python_api.apis.paths.companies import Companies
from intercom_python_api.apis.paths.companies_id import CompaniesId
from intercom_python_api.apis.paths.companies_id_contacts import CompaniesIdContacts
from intercom_python_api.apis.paths.companies_id_segments import CompaniesIdSegments
from intercom_python_api.apis.paths.companies_list import CompaniesList
from intercom_python_api.apis.paths.companies_scroll import CompaniesScroll
from intercom_python_api.apis.paths.contacts_id_companies import ContactsIdCompanies
from intercom_python_api.apis.paths.contacts_contact_id_companies_id import ContactsContactIdCompaniesId
from intercom_python_api.apis.paths.contacts_contact_id_companies import ContactsContactIdCompanies
from intercom_python_api.apis.paths.contacts_id_notes import ContactsIdNotes
from intercom_python_api.apis.paths.contacts_contact_id_segments import ContactsContactIdSegments
from intercom_python_api.apis.paths.contacts_contact_id_subscriptions import ContactsContactIdSubscriptions
from intercom_python_api.apis.paths.contacts_contact_id_subscriptions_id import ContactsContactIdSubscriptionsId
from intercom_python_api.apis.paths.contacts_contact_id_tags import ContactsContactIdTags
from intercom_python_api.apis.paths.contacts_contact_id_tags_id import ContactsContactIdTagsId
from intercom_python_api.apis.paths.contacts_id import ContactsId
from intercom_python_api.apis.paths.contacts_merge import ContactsMerge
from intercom_python_api.apis.paths.contacts_search import ContactsSearch
from intercom_python_api.apis.paths.contacts import Contacts
from intercom_python_api.apis.paths.contacts_id_archive import ContactsIdArchive
from intercom_python_api.apis.paths.contacts_id_unarchive import ContactsIdUnarchive
from intercom_python_api.apis.paths.conversations_conversation_id_tags import ConversationsConversationIdTags
from intercom_python_api.apis.paths.conversations_conversation_id_tags_id import ConversationsConversationIdTagsId
from intercom_python_api.apis.paths.conversations import Conversations
from intercom_python_api.apis.paths.conversations_id import ConversationsId
from intercom_python_api.apis.paths.conversations_search import ConversationsSearch
from intercom_python_api.apis.paths.conversations_id_reply import ConversationsIdReply
from intercom_python_api.apis.paths.conversations_id_parts import ConversationsIdParts
from intercom_python_api.apis.paths.conversations_id_run_assignment_rules import ConversationsIdRunAssignmentRules
from intercom_python_api.apis.paths.conversations_id_customers import ConversationsIdCustomers
from intercom_python_api.apis.paths.conversations_conversation_id_customers_contact_id import ConversationsConversationIdCustomersContactId
from intercom_python_api.apis.paths.conversations_redact import ConversationsRedact
from intercom_python_api.apis.paths.data_attributes import DataAttributes
from intercom_python_api.apis.paths.data_attributes_id import DataAttributesId
from intercom_python_api.apis.paths.events import Events
from intercom_python_api.apis.paths.events_summaries import EventsSummaries
from intercom_python_api.apis.paths.export_content_data import ExportContentData
from intercom_python_api.apis.paths.export_content_data_job_identifier import ExportContentDataJobIdentifier
from intercom_python_api.apis.paths.export_cancel_job_identifier import ExportCancelJobIdentifier
from intercom_python_api.apis.paths.download_content_data_job_identifier import DownloadContentDataJobIdentifier
from intercom_python_api.apis.paths.messages import Messages
from intercom_python_api.apis.paths.news_news_items import NewsNewsItems
from intercom_python_api.apis.paths.news_news_items_id import NewsNewsItemsId
from intercom_python_api.apis.paths.news_newsfeeds_id_items import NewsNewsfeedsIdItems
from intercom_python_api.apis.paths.news_newsfeeds import NewsNewsfeeds
from intercom_python_api.apis.paths.news_newsfeeds_id import NewsNewsfeedsId
from intercom_python_api.apis.paths.notes_id import NotesId
from intercom_python_api.apis.paths.segments import Segments
from intercom_python_api.apis.paths.segments_id import SegmentsId
from intercom_python_api.apis.paths.subscription_types import SubscriptionTypes
from intercom_python_api.apis.paths.phone_call_redirects import PhoneCallRedirects
from intercom_python_api.apis.paths.tags import Tags
from intercom_python_api.apis.paths.tags_id import TagsId
from intercom_python_api.apis.paths.teams import Teams
from intercom_python_api.apis.paths.teams_id import TeamsId
from intercom_python_api.apis.paths.ticket_types_ticket_type_id_attributes import TicketTypesTicketTypeIdAttributes
from intercom_python_api.apis.paths.ticket_types_ticket_type_id_attributes_id import TicketTypesTicketTypeIdAttributesId
from intercom_python_api.apis.paths.ticket_types import TicketTypes
from intercom_python_api.apis.paths.ticket_types_id import TicketTypesId
from intercom_python_api.apis.paths.tickets_ticket_id_reply import TicketsTicketIdReply
from intercom_python_api.apis.paths.tickets import Tickets
from intercom_python_api.apis.paths.tickets_id import TicketsId
from intercom_python_api.apis.paths.visitors import Visitors
from intercom_python_api.apis.paths.visitors_id import VisitorsId
from intercom_python_api.apis.paths.visitors_convert import VisitorsConvert

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ME: Me,
        PathValues.ADMINS_ID_AWAY: AdminsIdAway,
        PathValues.ADMINS_ACTIVITY_LOGS: AdminsActivityLogs,
        PathValues.ADMINS: Admins,
        PathValues.ADMINS_ID: AdminsId,
        PathValues.ARTICLES: Articles,
        PathValues.ARTICLES_ID: ArticlesId,
        PathValues.HELP_CENTER_COLLECTIONS: HelpCenterCollections,
        PathValues.HELP_CENTER_COLLECTIONS_ID: HelpCenterCollectionsId,
        PathValues.COMPANIES: Companies,
        PathValues.COMPANIES_ID: CompaniesId,
        PathValues.COMPANIES_ID_CONTACTS: CompaniesIdContacts,
        PathValues.COMPANIES_ID_SEGMENTS: CompaniesIdSegments,
        PathValues.COMPANIES_LIST: CompaniesList,
        PathValues.COMPANIES_SCROLL: CompaniesScroll,
        PathValues.CONTACTS_ID_COMPANIES: ContactsIdCompanies,
        PathValues.CONTACTS_CONTACT_ID_COMPANIES_ID: ContactsContactIdCompaniesId,
        PathValues.CONTACTS_CONTACT_ID_COMPANIES: ContactsContactIdCompanies,
        PathValues.CONTACTS_ID_NOTES: ContactsIdNotes,
        PathValues.CONTACTS_CONTACT_ID_SEGMENTS: ContactsContactIdSegments,
        PathValues.CONTACTS_CONTACT_ID_SUBSCRIPTIONS: ContactsContactIdSubscriptions,
        PathValues.CONTACTS_CONTACT_ID_SUBSCRIPTIONS_ID: ContactsContactIdSubscriptionsId,
        PathValues.CONTACTS_CONTACT_ID_TAGS: ContactsContactIdTags,
        PathValues.CONTACTS_CONTACT_ID_TAGS_ID: ContactsContactIdTagsId,
        PathValues.CONTACTS_ID: ContactsId,
        PathValues.CONTACTS_MERGE: ContactsMerge,
        PathValues.CONTACTS_SEARCH: ContactsSearch,
        PathValues.CONTACTS: Contacts,
        PathValues.CONTACTS_ID_ARCHIVE: ContactsIdArchive,
        PathValues.CONTACTS_ID_UNARCHIVE: ContactsIdUnarchive,
        PathValues.CONVERSATIONS_CONVERSATION_ID_TAGS: ConversationsConversationIdTags,
        PathValues.CONVERSATIONS_CONVERSATION_ID_TAGS_ID: ConversationsConversationIdTagsId,
        PathValues.CONVERSATIONS: Conversations,
        PathValues.CONVERSATIONS_ID: ConversationsId,
        PathValues.CONVERSATIONS_SEARCH: ConversationsSearch,
        PathValues.CONVERSATIONS_ID_REPLY: ConversationsIdReply,
        PathValues.CONVERSATIONS_ID_PARTS: ConversationsIdParts,
        PathValues.CONVERSATIONS_ID_RUN_ASSIGNMENT_RULES: ConversationsIdRunAssignmentRules,
        PathValues.CONVERSATIONS_ID_CUSTOMERS: ConversationsIdCustomers,
        PathValues.CONVERSATIONS_CONVERSATION_ID_CUSTOMERS_CONTACT_ID: ConversationsConversationIdCustomersContactId,
        PathValues.CONVERSATIONS_REDACT: ConversationsRedact,
        PathValues.DATA_ATTRIBUTES: DataAttributes,
        PathValues.DATA_ATTRIBUTES_ID: DataAttributesId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_SUMMARIES: EventsSummaries,
        PathValues.EXPORT_CONTENT_DATA: ExportContentData,
        PathValues.EXPORT_CONTENT_DATA_JOB_IDENTIFIER: ExportContentDataJobIdentifier,
        PathValues.EXPORT_CANCEL_JOB_IDENTIFIER: ExportCancelJobIdentifier,
        PathValues.DOWNLOAD_CONTENT_DATA_JOB_IDENTIFIER: DownloadContentDataJobIdentifier,
        PathValues.MESSAGES: Messages,
        PathValues.NEWS_NEWS_ITEMS: NewsNewsItems,
        PathValues.NEWS_NEWS_ITEMS_ID: NewsNewsItemsId,
        PathValues.NEWS_NEWSFEEDS_ID_ITEMS: NewsNewsfeedsIdItems,
        PathValues.NEWS_NEWSFEEDS: NewsNewsfeeds,
        PathValues.NEWS_NEWSFEEDS_ID: NewsNewsfeedsId,
        PathValues.NOTES_ID: NotesId,
        PathValues.SEGMENTS: Segments,
        PathValues.SEGMENTS_ID: SegmentsId,
        PathValues.SUBSCRIPTION_TYPES: SubscriptionTypes,
        PathValues.PHONE_CALL_REDIRECTS: PhoneCallRedirects,
        PathValues.TAGS: Tags,
        PathValues.TAGS_ID: TagsId,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TICKET_TYPES_TICKET_TYPE_ID_ATTRIBUTES: TicketTypesTicketTypeIdAttributes,
        PathValues.TICKET_TYPES_TICKET_TYPE_ID_ATTRIBUTES_ID: TicketTypesTicketTypeIdAttributesId,
        PathValues.TICKET_TYPES: TicketTypes,
        PathValues.TICKET_TYPES_ID: TicketTypesId,
        PathValues.TICKETS_TICKET_ID_REPLY: TicketsTicketIdReply,
        PathValues.TICKETS: Tickets,
        PathValues.TICKETS_ID: TicketsId,
        PathValues.VISITORS: Visitors,
        PathValues.VISITORS_ID: VisitorsId,
        PathValues.VISITORS_CONVERT: VisitorsConvert,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ME: Me,
        PathValues.ADMINS_ID_AWAY: AdminsIdAway,
        PathValues.ADMINS_ACTIVITY_LOGS: AdminsActivityLogs,
        PathValues.ADMINS: Admins,
        PathValues.ADMINS_ID: AdminsId,
        PathValues.ARTICLES: Articles,
        PathValues.ARTICLES_ID: ArticlesId,
        PathValues.HELP_CENTER_COLLECTIONS: HelpCenterCollections,
        PathValues.HELP_CENTER_COLLECTIONS_ID: HelpCenterCollectionsId,
        PathValues.COMPANIES: Companies,
        PathValues.COMPANIES_ID: CompaniesId,
        PathValues.COMPANIES_ID_CONTACTS: CompaniesIdContacts,
        PathValues.COMPANIES_ID_SEGMENTS: CompaniesIdSegments,
        PathValues.COMPANIES_LIST: CompaniesList,
        PathValues.COMPANIES_SCROLL: CompaniesScroll,
        PathValues.CONTACTS_ID_COMPANIES: ContactsIdCompanies,
        PathValues.CONTACTS_CONTACT_ID_COMPANIES_ID: ContactsContactIdCompaniesId,
        PathValues.CONTACTS_CONTACT_ID_COMPANIES: ContactsContactIdCompanies,
        PathValues.CONTACTS_ID_NOTES: ContactsIdNotes,
        PathValues.CONTACTS_CONTACT_ID_SEGMENTS: ContactsContactIdSegments,
        PathValues.CONTACTS_CONTACT_ID_SUBSCRIPTIONS: ContactsContactIdSubscriptions,
        PathValues.CONTACTS_CONTACT_ID_SUBSCRIPTIONS_ID: ContactsContactIdSubscriptionsId,
        PathValues.CONTACTS_CONTACT_ID_TAGS: ContactsContactIdTags,
        PathValues.CONTACTS_CONTACT_ID_TAGS_ID: ContactsContactIdTagsId,
        PathValues.CONTACTS_ID: ContactsId,
        PathValues.CONTACTS_MERGE: ContactsMerge,
        PathValues.CONTACTS_SEARCH: ContactsSearch,
        PathValues.CONTACTS: Contacts,
        PathValues.CONTACTS_ID_ARCHIVE: ContactsIdArchive,
        PathValues.CONTACTS_ID_UNARCHIVE: ContactsIdUnarchive,
        PathValues.CONVERSATIONS_CONVERSATION_ID_TAGS: ConversationsConversationIdTags,
        PathValues.CONVERSATIONS_CONVERSATION_ID_TAGS_ID: ConversationsConversationIdTagsId,
        PathValues.CONVERSATIONS: Conversations,
        PathValues.CONVERSATIONS_ID: ConversationsId,
        PathValues.CONVERSATIONS_SEARCH: ConversationsSearch,
        PathValues.CONVERSATIONS_ID_REPLY: ConversationsIdReply,
        PathValues.CONVERSATIONS_ID_PARTS: ConversationsIdParts,
        PathValues.CONVERSATIONS_ID_RUN_ASSIGNMENT_RULES: ConversationsIdRunAssignmentRules,
        PathValues.CONVERSATIONS_ID_CUSTOMERS: ConversationsIdCustomers,
        PathValues.CONVERSATIONS_CONVERSATION_ID_CUSTOMERS_CONTACT_ID: ConversationsConversationIdCustomersContactId,
        PathValues.CONVERSATIONS_REDACT: ConversationsRedact,
        PathValues.DATA_ATTRIBUTES: DataAttributes,
        PathValues.DATA_ATTRIBUTES_ID: DataAttributesId,
        PathValues.EVENTS: Events,
        PathValues.EVENTS_SUMMARIES: EventsSummaries,
        PathValues.EXPORT_CONTENT_DATA: ExportContentData,
        PathValues.EXPORT_CONTENT_DATA_JOB_IDENTIFIER: ExportContentDataJobIdentifier,
        PathValues.EXPORT_CANCEL_JOB_IDENTIFIER: ExportCancelJobIdentifier,
        PathValues.DOWNLOAD_CONTENT_DATA_JOB_IDENTIFIER: DownloadContentDataJobIdentifier,
        PathValues.MESSAGES: Messages,
        PathValues.NEWS_NEWS_ITEMS: NewsNewsItems,
        PathValues.NEWS_NEWS_ITEMS_ID: NewsNewsItemsId,
        PathValues.NEWS_NEWSFEEDS_ID_ITEMS: NewsNewsfeedsIdItems,
        PathValues.NEWS_NEWSFEEDS: NewsNewsfeeds,
        PathValues.NEWS_NEWSFEEDS_ID: NewsNewsfeedsId,
        PathValues.NOTES_ID: NotesId,
        PathValues.SEGMENTS: Segments,
        PathValues.SEGMENTS_ID: SegmentsId,
        PathValues.SUBSCRIPTION_TYPES: SubscriptionTypes,
        PathValues.PHONE_CALL_REDIRECTS: PhoneCallRedirects,
        PathValues.TAGS: Tags,
        PathValues.TAGS_ID: TagsId,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TICKET_TYPES_TICKET_TYPE_ID_ATTRIBUTES: TicketTypesTicketTypeIdAttributes,
        PathValues.TICKET_TYPES_TICKET_TYPE_ID_ATTRIBUTES_ID: TicketTypesTicketTypeIdAttributesId,
        PathValues.TICKET_TYPES: TicketTypes,
        PathValues.TICKET_TYPES_ID: TicketTypesId,
        PathValues.TICKETS_TICKET_ID_REPLY: TicketsTicketIdReply,
        PathValues.TICKETS: Tickets,
        PathValues.TICKETS_ID: TicketsId,
        PathValues.VISITORS: Visitors,
        PathValues.VISITORS_ID: VisitorsId,
        PathValues.VISITORS_CONVERT: VisitorsConvert,
    }
)
