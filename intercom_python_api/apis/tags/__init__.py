# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from intercom_python_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ADMINS = "Admins"
    ARTICLES = "Articles"
    COMPANIES = "Companies"
    CONTACTS = "Contacts"
    CONVERSATIONS = "Conversations"
    DATA_ATTRIBUTES = "Data Attributes"
    DATA_EVENTS = "Data Events"
    DATA_EXPORT = "Data Export"
    HELP_CENTER = "Help Center"
    MESSAGES = "Messages"
    NEWS = "News"
    NOTES = "Notes"
    SEGMENTS = "Segments"
    SUBSCRIPTION_TYPES = "Subscription Types"
    SWITCH = "Switch"
    TAGS = "Tags"
    TEAMS = "Teams"
    TICKET_TYPE_ATTRIBUTES = "Ticket Type Attributes"
    TICKET_TYPES = "Ticket Types"
    TICKETS = "Tickets"
    VISITORS = "Visitors"
