import typing_extensions

from intercom_python_api.apis.tags import TagValues
from intercom_python_api.apis.tags.admins_api import AdminsApi
from intercom_python_api.apis.tags.articles_api import ArticlesApi
from intercom_python_api.apis.tags.companies_api import CompaniesApi
from intercom_python_api.apis.tags.contacts_api import ContactsApi
from intercom_python_api.apis.tags.conversations_api import ConversationsApi
from intercom_python_api.apis.tags.data_attributes_api import DataAttributesApi
from intercom_python_api.apis.tags.data_events_api import DataEventsApi
from intercom_python_api.apis.tags.data_export_api import DataExportApi
from intercom_python_api.apis.tags.help_center_api import HelpCenterApi
from intercom_python_api.apis.tags.messages_api import MessagesApi
from intercom_python_api.apis.tags.news_api import NewsApi
from intercom_python_api.apis.tags.notes_api import NotesApi
from intercom_python_api.apis.tags.segments_api import SegmentsApi
from intercom_python_api.apis.tags.subscription_types_api import SubscriptionTypesApi
from intercom_python_api.apis.tags.switch_api import SwitchApi
from intercom_python_api.apis.tags.tags_api import TagsApi
from intercom_python_api.apis.tags.teams_api import TeamsApi
#from intercom_python_api.apis.tags.ticket_type_attributes_api import TicketTypeAttributesApi
#from intercom_python_api.apis.tags.ticket_types_api import TicketTypesApi
from intercom_python_api.apis.tags.visitors_api import VisitorsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADMINS: AdminsApi,
        TagValues.ARTICLES: ArticlesApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.DATA_ATTRIBUTES: DataAttributesApi,
        TagValues.DATA_EVENTS: DataEventsApi,
        TagValues.DATA_EXPORT: DataExportApi,
        TagValues.HELP_CENTER: HelpCenterApi,
        TagValues.MESSAGES: MessagesApi,
        TagValues.NEWS: NewsApi,
        TagValues.NOTES: NotesApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.SUBSCRIPTION_TYPES: SubscriptionTypesApi,
        TagValues.SWITCH: SwitchApi,
        TagValues.TAGS: TagsApi,
        TagValues.TEAMS: TeamsApi,
        #TagValues.TICKET_TYPE_ATTRIBUTES: TicketTypeAttributesApi,
        #TagValues.TICKET_TYPES: TicketTypesApi,
        TagValues.VISITORS: VisitorsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADMINS: AdminsApi,
        TagValues.ARTICLES: ArticlesApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.CONVERSATIONS: ConversationsApi,
        TagValues.DATA_ATTRIBUTES: DataAttributesApi,
        TagValues.DATA_EVENTS: DataEventsApi,
        TagValues.DATA_EXPORT: DataExportApi,
        TagValues.HELP_CENTER: HelpCenterApi,
        TagValues.MESSAGES: MessagesApi,
        TagValues.NEWS: NewsApi,
        TagValues.NOTES: NotesApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.SUBSCRIPTION_TYPES: SubscriptionTypesApi,
        TagValues.SWITCH: SwitchApi,
        TagValues.TAGS: TagsApi,
        TagValues.TEAMS: TeamsApi,
        #TagValues.TICKET_TYPE_ATTRIBUTES: TicketTypeAttributesApi,
        #TagValues.TICKET_TYPES: TicketTypesApi,
        TagValues.VISITORS: VisitorsApi,
    }
)
