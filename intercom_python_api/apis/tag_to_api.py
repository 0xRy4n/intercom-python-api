import typing_extensions
import logging
from intercom_python_api.apis.tags import TagValues

try:
    from intercom_python_api.apis.tags.admins_api import AdminsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'AdminsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.articles_api import ArticlesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'ArticlesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.companies_api import CompaniesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'CompaniesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.contacts_api import ContactsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'ContactsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.conversations_api import ConversationsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'ConversationsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.data_attributes_api import DataAttributesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'DataAttributesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.data_events_api import DataEventsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'DataEventsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.data_export_api import DataExportApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'DataExportApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.help_center_api import HelpCenterApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'HelpCenterApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.messages_api import MessagesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'MessagesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.news_api import NewsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'NewsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.notes_api import NotesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'NotesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.segments_api import SegmentsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'SegmentsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.subscription_types_api import SubscriptionTypesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'SubscriptionTypesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.switch_api import SwitchApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'SwitchApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.tags_api import TagsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'TagsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.teams_api import TeamsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'TeamsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.ticket_type_attributes_api import TicketTypeAttributesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'TicketTypeAttributesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.ticket_types_api import TicketTypesApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'TicketTypesApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.tickets_api import TicketsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'TicketsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")
try:
    from intercom_python_api.apis.tags.visitors_api import VisitorsApi
except ModuleNotFoundError as e:
    logging.warn(f"Unable to import 'VisitorsApi'. \n - This is likely due to an incomplete or improper OpenAPI specification. \n - This API module will be unavailable.\n")


tag_dict = {}
try:
    tag_dict[TagValues.ADMINS] = AdminsApi
except:
    pass
try:
    tag_dict[TagValues.ARTICLES] = ArticlesApi
except:
    pass
try:
    tag_dict[TagValues.COMPANIES] = CompaniesApi
except:
    pass
try:
    tag_dict[TagValues.CONTACTS] = ContactsApi
except:
    pass
try:
    tag_dict[TagValues.CONVERSATIONS] = ConversationsApi
except:
    pass
try:
    tag_dict[TagValues.DATA_ATTRIBUTES] = DataAttributesApi
except:
    pass
try:
    tag_dict[TagValues.DATA_EVENTS] = DataEventsApi
except:
    pass
try:
    tag_dict[TagValues.DATA_EXPORT] = DataExportApi
except:
    pass
try:
    tag_dict[TagValues.HELP_CENTER] = HelpCenterApi
except:
    pass
try:
    tag_dict[TagValues.MESSAGES] = MessagesApi
except:
    pass
try:
    tag_dict[TagValues.NEWS] = NewsApi
except:
    pass
try:
    tag_dict[TagValues.NOTES] = NotesApi
except:
    pass
try:
    tag_dict[TagValues.SEGMENTS] = SegmentsApi
except:
    pass
try:
    tag_dict[TagValues.SUBSCRIPTION_TYPES] = SubscriptionTypesApi
except:
    pass
try:
    tag_dict[TagValues.SWITCH] = SwitchApi
except:
    pass
try:
    tag_dict[TagValues.TAGS] = TagsApi
except:
    pass
try:
    tag_dict[TagValues.TEAMS] = TeamsApi
except:
    pass
try:
    tag_dict[TagValues.TICKET_TYPE_ATTRIBUTES] = TicketTypeAttributesApi
except:
    pass
try:
    tag_dict[TagValues.TICKET_TYPES] = TicketTypesApi
except:
    pass
try:
    tag_dict[TagValues.TICKETS] = TicketsApi
except:
    pass
try:
    tag_dict[TagValues.VISITORS] = VisitorsApi
except:
    pass

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    tag_dict
)

tag_to_api = TagToApi(tag_dict)