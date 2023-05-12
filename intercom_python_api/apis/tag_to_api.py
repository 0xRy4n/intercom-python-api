import typing_extensions
import warnings

from intercom_python_api.apis.tags import TagValues
try:
    from intercom_python_api.apis.tags.admins_api import AdminsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'AdminsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.articles_api import ArticlesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'ArticlesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.companies_api import CompaniesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'CompaniesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.contacts_api import ContactsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'ContactsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.conversations_api import ConversationsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'ConversationsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.data_attributes_api import DataAttributesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'DataAttributesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.data_events_api import DataEventsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'DataEventsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.data_export_api import DataExportApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'DataExportApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.help_center_api import HelpCenterApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'HelpCenterApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.messages_api import MessagesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'MessagesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.news_api import NewsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'NewsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.notes_api import NotesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'NotesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.segments_api import SegmentsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'SegmentsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.subscription_types_api import SubscriptionTypesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'SubscriptionTypesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.switch_api import SwitchApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'SwitchApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.tags_api import TagsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'TagsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.teams_api import TeamsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'TeamsApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.ticket_type_attributes_api import TicketTypeAttributesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'TicketTypeAttributesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.ticket_types_api import TicketTypesApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'TicketTypesApi'. Got error: {e}",
        RuntimeWarning
    )
try:
    from intercom_python_api.apis.tags.visitors_api import VisitorsApi
except ModuleNotFoundError as e:
    warnings.warn(
        f"Unable to import 'VisitorsApi'. Got error: {e}",
        RuntimeWarning
    )

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
        TagValues.TICKET_TYPE_ATTRIBUTES: TicketTypeAttributesApi,
        TagValues.TICKET_TYPES: TicketTypesApi,
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
        TagValues.TICKET_TYPE_ATTRIBUTES: TicketTypeAttributesApi,
        TagValues.TICKET_TYPES: TicketTypesApi,
        TagValues.VISITORS: VisitorsApi,
    }
)