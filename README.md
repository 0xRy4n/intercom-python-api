<hr />
<h1>This package is deprecated and will no longer undergo development. Due to issues with the OpenAPI Specification of Intercom, it is difficult to generate a working client via code generation.<h1><h2>It has been succeeded by https://github.com/0xRy4n/intercom-python-sdk</h2>
<hr/>
<br /><br />
# Intercom Python API
<p style="text-align:center">

![Intercom Python API](https://i.imgur.com/rQooYPo.png)

</p>

This package provides a wrapper around the Intercom API in the form of a python client. It conforms to the OpenAPI specification files provided by Intercom.

This is an **unofficial** client and is in no way maintained by or directly affiliated to Intercom. 

This package was largely generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.9
- Package version: 1.2.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

Modifications to the Handlebars templates used to generate the client can be found in the `./templates` folder. The custom convienence interface can be found in the `./intercom_python_api/client.py` module.

The package is kept up-to-date to the most recent API version. To create an API client for a different spec, run:

`generate_api.sh <version_number>` `

The script will check the official Intercom repository for API spec you specify and generate a new client for it. Due to the fact Intecom's API specs are not 
fully self-consistent the spec will be modified to create more lenient validation rules. The modified spec will be saved as `spec.yaml`

For more information regarding the Intercom API, please visit [https://developers.intercom.com](https://developers.intercom.com)

## Requirements.

Python &gt;&#x3D;3.7

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/0xRy4n/intercom-python-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/0xRy4n/intercom-python-api.git`)

Then import the package:
```python
import intercom_python_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import intercom_python_api
```

## API Usage

### Parameters 
In order to avoid name collisions in parameter names provided in different locations, user inputs have been seperated into different dictionaries which can be passed in an API call:

- query_params
- path_params
- header_params
- cookie_params

### Endpoint Responses
All API calls / endpoint responses will a response object with three attributes:

- response: urllib3.HTTPResponse
- headers: typing.Union[Unset, TODO]
- body: typing.Union[Unset, Schema]

The body will of course contain the actual response payload from the API endpoint.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import intercom_python_api
from pprint import pprint
from intercom_python_api import Intercom
from intercom_python_api.model.activity_log_list import ActivityLogList
from intercom_python_api.model.admin import Admin
from intercom_python_api.model.admin_list import AdminList
from intercom_python_api.model.admin_with_app import AdminWithApp
from intercom_python_api.model.error import Error
from intercom_python_api.model.intercom_version import IntercomVersion

# Instantiate Intercom client object
intercom = Intercom(api_key='<YOUR API TOKEN>')

intercom_version = IntercomVersion("Unstable") # IntercomVersion |  (optional)

try:
    # Identify an admin
    api_response = intercom.AdminsApi.identify_admin(intercom_version=intercom_version)
    pprint(api_response)
except intercom_python_api.ApiException as e:
    print("Exception when calling AdminsApi->identify_admin: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.intercom.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminsApi* | [**identify_admin**](docs/apis/tags/AdminsApi.md#identify_admin) | **get** /me | Identify an admin
*AdminsApi* | [**list_activity_logs**](docs/apis/tags/AdminsApi.md#list_activity_logs) | **get** /admins/activity_logs | List all activity logs
*AdminsApi* | [**list_admins**](docs/apis/tags/AdminsApi.md#list_admins) | **get** /admins | List all admins
*AdminsApi* | [**retrieve_admin**](docs/apis/tags/AdminsApi.md#retrieve_admin) | **get** /admins/{id} | Retrieve an admin
*AdminsApi* | [**set_away_admin**](docs/apis/tags/AdminsApi.md#set_away_admin) | **put** /admins/{id}/away | Set an admin to away
*ArticlesApi* | [**create_article**](docs/apis/tags/ArticlesApi.md#create_article) | **post** /articles | Create an article
*ArticlesApi* | [**delete_article**](docs/apis/tags/ArticlesApi.md#delete_article) | **delete** /articles/{id} | Delete an article
*ArticlesApi* | [**list_articles**](docs/apis/tags/ArticlesApi.md#list_articles) | **get** /articles | List all articles
*ArticlesApi* | [**retrieve_article**](docs/apis/tags/ArticlesApi.md#retrieve_article) | **get** /articles/{id} | Retrieve an article
*ArticlesApi* | [**update_article**](docs/apis/tags/ArticlesApi.md#update_article) | **put** /articles/{id} | Update an article
*CompaniesApi* | [**attach_contact_to_a_company**](docs/apis/tags/CompaniesApi.md#attach_contact_to_a_company) | **post** /contacts/{id}/companies | Attach a Contact to a Company
*CompaniesApi* | [**create_or_update_company**](docs/apis/tags/CompaniesApi.md#create_or_update_company) | **post** /companies | Create or Update a company
*CompaniesApi* | [**delete_company**](docs/apis/tags/CompaniesApi.md#delete_company) | **delete** /companies/{id} | Delete a company
*CompaniesApi* | [**dettach_contact_from_a_company**](docs/apis/tags/CompaniesApi.md#dettach_contact_from_a_company) | **delete** /contacts/{contact_id}/companies/{id} | Detach a contact from a company
*CompaniesApi* | [**list_all_companies**](docs/apis/tags/CompaniesApi.md#list_all_companies) | **post** /companies/list | List all companies
*CompaniesApi* | [**list_attached_contacts**](docs/apis/tags/CompaniesApi.md#list_attached_contacts) | **get** /companies/{id}/contacts | List attached contacts
*CompaniesApi* | [**list_attached_segments_for_companies**](docs/apis/tags/CompaniesApi.md#list_attached_segments_for_companies) | **get** /companies/{id}/segments | List attached segments for companies
*CompaniesApi* | [**list_companies_for_a_contact**](docs/apis/tags/CompaniesApi.md#list_companies_for_a_contact) | **get** /contacts/{contact_id}/companies | List attached companies for contact
*CompaniesApi* | [**retrieve_a_company_by_id**](docs/apis/tags/CompaniesApi.md#retrieve_a_company_by_id) | **get** /companies/{id} | Retrieve a company by ID
*CompaniesApi* | [**retrieve_company**](docs/apis/tags/CompaniesApi.md#retrieve_company) | **get** /companies | Retrieve a company
*CompaniesApi* | [**scroll_over_all_companies**](docs/apis/tags/CompaniesApi.md#scroll_over_all_companies) | **get** /companies/scroll | Scroll over all companies
*CompaniesApi* | [**update_company**](docs/apis/tags/CompaniesApi.md#update_company) | **put** /companies/{id} | Update a company
*ContactsApi* | [**archive_contact**](docs/apis/tags/ContactsApi.md#archive_contact) | **post** /contacts/{id}/archive | Archive contact
*ContactsApi* | [**attach_contact_to_a_company**](docs/apis/tags/ContactsApi.md#attach_contact_to_a_company) | **post** /contacts/{id}/companies | Attach a Contact to a Company
*ContactsApi* | [**attach_subscription_type_to_contact**](docs/apis/tags/ContactsApi.md#attach_subscription_type_to_contact) | **post** /contacts/{contact_id}/subscriptions | Add subscription to a contact
*ContactsApi* | [**attach_tag_to_contact**](docs/apis/tags/ContactsApi.md#attach_tag_to_contact) | **post** /contacts/{contact_id}/tags | Add tag to a contact
*ContactsApi* | [**create_contact**](docs/apis/tags/ContactsApi.md#create_contact) | **post** /contacts | Create contact
*ContactsApi* | [**create_note**](docs/apis/tags/ContactsApi.md#create_note) | **post** /contacts/{id}/notes | Create a note
*ContactsApi* | [**delete_contact**](docs/apis/tags/ContactsApi.md#delete_contact) | **delete** /contacts/{id} | Delete a contact
*ContactsApi* | [**detach_subscription_type_to_contact**](docs/apis/tags/ContactsApi.md#detach_subscription_type_to_contact) | **delete** /contacts/{contact_id}/subscriptions/{id} | Remove subscription from a contact
*ContactsApi* | [**detach_tag_from_contact**](docs/apis/tags/ContactsApi.md#detach_tag_from_contact) | **delete** /contacts/{contact_id}/tags/{id} | Remove tag from a contact
*ContactsApi* | [**dettach_contact_from_a_company**](docs/apis/tags/ContactsApi.md#dettach_contact_from_a_company) | **delete** /contacts/{contact_id}/companies/{id} | Detach a contact from a company
*ContactsApi* | [**list_attached_contacts**](docs/apis/tags/ContactsApi.md#list_attached_contacts) | **get** /companies/{id}/contacts | List attached contacts
*ContactsApi* | [**list_companies_for_a_contact**](docs/apis/tags/ContactsApi.md#list_companies_for_a_contact) | **get** /contacts/{contact_id}/companies | List attached companies for contact
*ContactsApi* | [**list_contacts**](docs/apis/tags/ContactsApi.md#list_contacts) | **get** /contacts | List all contacts
*ContactsApi* | [**list_notes**](docs/apis/tags/ContactsApi.md#list_notes) | **get** /contacts/{id}/notes | List all notes
*ContactsApi* | [**list_segments_for_a_contact**](docs/apis/tags/ContactsApi.md#list_segments_for_a_contact) | **get** /contacts/{contact_id}/segments | List attached segments for contact
*ContactsApi* | [**list_subscriptions_for_a_contact**](docs/apis/tags/ContactsApi.md#list_subscriptions_for_a_contact) | **get** /contacts/{contact_id}/subscriptions | List subscriptions for a contact
*ContactsApi* | [**list_tags_for_a_contact**](docs/apis/tags/ContactsApi.md#list_tags_for_a_contact) | **get** /contacts/{contact_id}/tags | List tags attached to a contact
*ContactsApi* | [**merge_contact**](docs/apis/tags/ContactsApi.md#merge_contact) | **post** /contacts/merge | Merge a lead and a user
*ContactsApi* | [**search_contacts**](docs/apis/tags/ContactsApi.md#search_contacts) | **post** /contacts/search | Search contacts
*ContactsApi* | [**show_contact**](docs/apis/tags/ContactsApi.md#show_contact) | **get** /contacts/{id} | Get a contact
*ContactsApi* | [**unarchive_contact**](docs/apis/tags/ContactsApi.md#unarchive_contact) | **post** /contacts/{id}/unarchive | Unarchive contact
*ContactsApi* | [**update_contact**](docs/apis/tags/ContactsApi.md#update_contact) | **put** /contacts/{id} | Update a contact
*ConversationsApi* | [**attach_contact_to_conversation**](docs/apis/tags/ConversationsApi.md#attach_contact_to_conversation) | **post** /conversations/{id}/customers | Attach a contact to a conversation
*ConversationsApi* | [**attach_tag_to_conversation**](docs/apis/tags/ConversationsApi.md#attach_tag_to_conversation) | **post** /conversations/{conversation_id}/tags | Add tag to a conversation
*ConversationsApi* | [**auto_assign_conversation**](docs/apis/tags/ConversationsApi.md#auto_assign_conversation) | **post** /conversations/{id}/run_assignment_rules | Run Assignment Rules on a conversation
*ConversationsApi* | [**create_conversation**](docs/apis/tags/ConversationsApi.md#create_conversation) | **post** /conversations | Creates a conversation
*ConversationsApi* | [**detach_contact_from_conversation**](docs/apis/tags/ConversationsApi.md#detach_contact_from_conversation) | **delete** /conversations/{conversation_id}/customers/{contact_id} | Detach a contact from a group conversation
*ConversationsApi* | [**detach_tag_from_conversation**](docs/apis/tags/ConversationsApi.md#detach_tag_from_conversation) | **delete** /conversations/{conversation_id}/tags/{id} | Remove tag from a conversation
*ConversationsApi* | [**list_conversations**](docs/apis/tags/ConversationsApi.md#list_conversations) | **get** /conversations | List all conversations
*ConversationsApi* | [**manage_conversation**](docs/apis/tags/ConversationsApi.md#manage_conversation) | **post** /conversations/{id}/parts | Manage a conversation
*ConversationsApi* | [**redact_conversation**](docs/apis/tags/ConversationsApi.md#redact_conversation) | **post** /conversations/redact | Redact a conversation part
*ConversationsApi* | [**reply_conversation**](docs/apis/tags/ConversationsApi.md#reply_conversation) | **post** /conversations/{id}/reply | Reply to a conversation
*ConversationsApi* | [**retrieve_conversation**](docs/apis/tags/ConversationsApi.md#retrieve_conversation) | **get** /conversations/{id} | Retrieve a conversation
*ConversationsApi* | [**search_conversations**](docs/apis/tags/ConversationsApi.md#search_conversations) | **post** /conversations/search | Search conversations
*ConversationsApi* | [**update_conversation**](docs/apis/tags/ConversationsApi.md#update_conversation) | **put** /conversations/{id} | Update a conversation
*DataAttributesApi* | [**create_data_attribute**](docs/apis/tags/DataAttributesApi.md#create_data_attribute) | **post** /data_attributes | Create a data attribute
*DataAttributesApi* | [**lis_data_attributes**](docs/apis/tags/DataAttributesApi.md#lis_data_attributes) | **get** /data_attributes | List all data attributes
*DataAttributesApi* | [**update_data_attribute**](docs/apis/tags/DataAttributesApi.md#update_data_attribute) | **put** /data_attributes/{id} | Update a data attribute
*DataEventsApi* | [**create_data_event**](docs/apis/tags/DataEventsApi.md#create_data_event) | **post** /events | Submit a data event
*DataEventsApi* | [**data_event_summaries**](docs/apis/tags/DataEventsApi.md#data_event_summaries) | **post** /events/summaries | Create event summaries
*DataEventsApi* | [**lis_data_events**](docs/apis/tags/DataEventsApi.md#lis_data_events) | **get** /events | List all data events
*DataExportApi* | [**cancel_data_export**](docs/apis/tags/DataExportApi.md#cancel_data_export) | **post** /export/cancel/{job_identifier} | Cancel content data export
*DataExportApi* | [**create_data_export**](docs/apis/tags/DataExportApi.md#create_data_export) | **post** /export/content/data | Create content data export
*DataExportApi* | [**download_data_export**](docs/apis/tags/DataExportApi.md#download_data_export) | **get** /download/content/data/{job_identifier} | Download content data export
*DataExportApi* | [**get_data_export**](docs/apis/tags/DataExportApi.md#get_data_export) | **get** /export/content/data/{job_identifier} | Show content data export
*HelpCenterApi* | [**create_collection**](docs/apis/tags/HelpCenterApi.md#create_collection) | **post** /help_center/collections | Create a collection
*HelpCenterApi* | [**create_section**](docs/apis/tags/HelpCenterApi.md#create_section) | **post** /help_center/sections | Create a section
*HelpCenterApi* | [**delete_collection**](docs/apis/tags/HelpCenterApi.md#delete_collection) | **delete** /help_center/collections/{id} | Delete a collection
*HelpCenterApi* | [**delete_section**](docs/apis/tags/HelpCenterApi.md#delete_section) | **delete** /help_center/sections/{id} | Delete a section
*HelpCenterApi* | [**list_all_collections**](docs/apis/tags/HelpCenterApi.md#list_all_collections) | **get** /help_center/collections | List all collections
*HelpCenterApi* | [**list_all_sections**](docs/apis/tags/HelpCenterApi.md#list_all_sections) | **get** /help_center/sections | List all sections
*HelpCenterApi* | [**retrieve_collection**](docs/apis/tags/HelpCenterApi.md#retrieve_collection) | **get** /help_center/collections/{id} | Retrieve a collection
*HelpCenterApi* | [**retrieve_section**](docs/apis/tags/HelpCenterApi.md#retrieve_section) | **get** /help_center/sections/{id} | Retrieve a section
*HelpCenterApi* | [**update_collection**](docs/apis/tags/HelpCenterApi.md#update_collection) | **put** /help_center/collections/{id} | Update a collection
*HelpCenterApi* | [**update_section**](docs/apis/tags/HelpCenterApi.md#update_section) | **put** /help_center/sections/{id} | Update a section
*MessagesApi* | [**create_message**](docs/apis/tags/MessagesApi.md#create_message) | **post** /messages | Create a message
*NewsApi* | [**create_news_item**](docs/apis/tags/NewsApi.md#create_news_item) | **post** /news/news_items | Create a news item
*NewsApi* | [**delete_news_item**](docs/apis/tags/NewsApi.md#delete_news_item) | **delete** /news/news_items/{id} | Delete a news item
*NewsApi* | [**list_live_newsfeed_items**](docs/apis/tags/NewsApi.md#list_live_newsfeed_items) | **get** /news/newsfeeds/{id}/items | List all live newsfeed items
*NewsApi* | [**list_news_items**](docs/apis/tags/NewsApi.md#list_news_items) | **get** /news/news_items | List all news items
*NewsApi* | [**list_newsfeeds**](docs/apis/tags/NewsApi.md#list_newsfeeds) | **get** /news/newsfeeds | List all newsfeeds
*NewsApi* | [**retrieve_news_item**](docs/apis/tags/NewsApi.md#retrieve_news_item) | **get** /news/news_items/{id} | Retrieve a news item
*NewsApi* | [**retrieve_newsfeed**](docs/apis/tags/NewsApi.md#retrieve_newsfeed) | **get** /news/newsfeeds/{id} | Retrieve a newsfeed
*NewsApi* | [**update_news_item**](docs/apis/tags/NewsApi.md#update_news_item) | **put** /news/news_items/{id} | Update a news item
*NotesApi* | [**create_note**](docs/apis/tags/NotesApi.md#create_note) | **post** /contacts/{id}/notes | Create a note
*NotesApi* | [**list_notes**](docs/apis/tags/NotesApi.md#list_notes) | **get** /contacts/{id}/notes | List all notes
*NotesApi* | [**retrieve_note**](docs/apis/tags/NotesApi.md#retrieve_note) | **get** /notes/{id} | Retrieve a note
*SegmentsApi* | [**list_segments**](docs/apis/tags/SegmentsApi.md#list_segments) | **get** /segments | List all segments
*SegmentsApi* | [**list_segments_for_a_contact**](docs/apis/tags/SegmentsApi.md#list_segments_for_a_contact) | **get** /contacts/{contact_id}/segments | List attached segments for contact
*SegmentsApi* | [**retrieve_segment**](docs/apis/tags/SegmentsApi.md#retrieve_segment) | **get** /segments/{id} | Retrieve a segment
*SubscriptionTypesApi* | [**attach_subscription_type_to_contact**](docs/apis/tags/SubscriptionTypesApi.md#attach_subscription_type_to_contact) | **post** /contacts/{contact_id}/subscriptions | Add subscription to a contact
*SubscriptionTypesApi* | [**detach_subscription_type_to_contact**](docs/apis/tags/SubscriptionTypesApi.md#detach_subscription_type_to_contact) | **delete** /contacts/{contact_id}/subscriptions/{id} | Remove subscription from a contact
*SubscriptionTypesApi* | [**list_subscription_types**](docs/apis/tags/SubscriptionTypesApi.md#list_subscription_types) | **get** /subscription_types | List subscription types
*SubscriptionTypesApi* | [**list_subscriptions_for_a_contact**](docs/apis/tags/SubscriptionTypesApi.md#list_subscriptions_for_a_contact) | **get** /contacts/{contact_id}/subscriptions | List subscriptions for a contact
*SwitchApi* | [**create_phone_switch**](docs/apis/tags/SwitchApi.md#create_phone_switch) | **post** /phone_call_redirects | Create a phone Switch
*TagsApi* | [**attach_tag_to_contact**](docs/apis/tags/TagsApi.md#attach_tag_to_contact) | **post** /contacts/{contact_id}/tags | Add tag to a contact
*TagsApi* | [**attach_tag_to_conversation**](docs/apis/tags/TagsApi.md#attach_tag_to_conversation) | **post** /conversations/{conversation_id}/tags | Add tag to a conversation
*TagsApi* | [**create_tag**](docs/apis/tags/TagsApi.md#create_tag) | **post** /tags | Create or update a tag, Tag or untag companies, Tag contacts
*TagsApi* | [**delete_tag**](docs/apis/tags/TagsApi.md#delete_tag) | **delete** /tags/{id} | Delete tag
*TagsApi* | [**detach_tag_from_contact**](docs/apis/tags/TagsApi.md#detach_tag_from_contact) | **delete** /contacts/{contact_id}/tags/{id} | Remove tag from a contact
*TagsApi* | [**detach_tag_from_conversation**](docs/apis/tags/TagsApi.md#detach_tag_from_conversation) | **delete** /conversations/{conversation_id}/tags/{id} | Remove tag from a conversation
*TagsApi* | [**find_tag**](docs/apis/tags/TagsApi.md#find_tag) | **get** /tags/{id} | Find a specific tag
*TagsApi* | [**list_tags**](docs/apis/tags/TagsApi.md#list_tags) | **get** /tags | List all tags
*TagsApi* | [**list_tags_for_a_contact**](docs/apis/tags/TagsApi.md#list_tags_for_a_contact) | **get** /contacts/{contact_id}/tags | List tags attached to a contact
*TeamsApi* | [**list_teams**](docs/apis/tags/TeamsApi.md#list_teams) | **get** /teams | List all teams
*TeamsApi* | [**retrieve_team**](docs/apis/tags/TeamsApi.md#retrieve_team) | **get** /teams/{id} | Retrieve a team
*TicketTypeAttributesApi* | [**create_ticket_type_attribute**](docs/apis/tags/TicketTypeAttributesApi.md#create_ticket_type_attribute) | **post** /ticket_types/{ticket_type_id}/attributes | Create a new attribute for a ticket type
*TicketTypeAttributesApi* | [**update_ticket_type_attribute**](docs/apis/tags/TicketTypeAttributesApi.md#update_ticket_type_attribute) | **put** /ticket_types/{ticket_type_id}/attributes/{id} | Update an existing attribute for a ticket type
*TicketTypesApi* | [**ticket_types_get**](docs/apis/tags/TicketTypesApi.md#ticket_types_get) | **get** /ticket_types | List all ticket types
*TicketTypesApi* | [**ticket_types_id_get**](docs/apis/tags/TicketTypesApi.md#ticket_types_id_get) | **get** /ticket_types/{id} | Retrieve a ticket type
*TicketTypesApi* | [**ticket_types_id_put**](docs/apis/tags/TicketTypesApi.md#ticket_types_id_put) | **put** /ticket_types/{id} | Update a ticket type
*TicketTypesApi* | [**ticket_types_post**](docs/apis/tags/TicketTypesApi.md#ticket_types_post) | **post** /ticket_types | Create a ticket type
*TicketsApi* | [**tickets_id_get**](docs/apis/tags/TicketsApi.md#tickets_id_get) | **get** /tickets/{id} | Retrieve a ticket
*TicketsApi* | [**tickets_id_put**](docs/apis/tags/TicketsApi.md#tickets_id_put) | **put** /tickets/{id} | Update a ticket
*TicketsApi* | [**tickets_post**](docs/apis/tags/TicketsApi.md#tickets_post) | **post** /tickets | Create a ticket
*TicketsApi* | [**tickets_ticket_id_reply_post**](docs/apis/tags/TicketsApi.md#tickets_ticket_id_reply_post) | **post** /tickets/{ticket_id}/reply | Create a ticket reply
*VisitorsApi* | [**convert_visitor**](docs/apis/tags/VisitorsApi.md#convert_visitor) | **post** /visitors/convert | Convert a visitor
*VisitorsApi* | [**delete_visitor**](docs/apis/tags/VisitorsApi.md#delete_visitor) | **delete** /visitors/{id} | Delete a visitor
*VisitorsApi* | [**retrieve_visitor**](docs/apis/tags/VisitorsApi.md#retrieve_visitor) | **get** /visitors/{id} | Retrieve a visitor with ID
*VisitorsApi* | [**retrieve_visitor_with_user_id**](docs/apis/tags/VisitorsApi.md#retrieve_visitor_with_user_id) | **get** /visitors | Retrieve a visitor with User ID
*VisitorsApi* | [**update_visitor**](docs/apis/tags/VisitorsApi.md#update_visitor) | **put** /visitors | Update a visitor

## Documentation For Models

 - [ActivityLog](docs/models/ActivityLog.md)
 - [ActivityLogList](docs/models/ActivityLogList.md)
 - [AddressableList](docs/models/AddressableList.md)
 - [Admin](docs/models/Admin.md)
 - [AdminList](docs/models/AdminList.md)
 - [AdminPriorityLevel](docs/models/AdminPriorityLevel.md)
 - [AdminReplyConversationRequest](docs/models/AdminReplyConversationRequest.md)
 - [AdminWithApp](docs/models/AdminWithApp.md)
 - [App](docs/models/App.md)
 - [Article](docs/models/Article.md)
 - [ArticleContent](docs/models/ArticleContent.md)
 - [ArticleList](docs/models/ArticleList.md)
 - [ArticleStatistics](docs/models/ArticleStatistics.md)
 - [ArticleTranslatedContent](docs/models/ArticleTranslatedContent.md)
 - [AssignConversationRequest](docs/models/AssignConversationRequest.md)
 - [AttachContactToConversationRequest](docs/models/AttachContactToConversationRequest.md)
 - [CloseConversationRequest](docs/models/CloseConversationRequest.md)
 - [Collection](docs/models/Collection.md)
 - [CollectionList](docs/models/CollectionList.md)
 - [Company](docs/models/Company.md)
 - [CompanyAttachedContacts](docs/models/CompanyAttachedContacts.md)
 - [CompanyAttachedSegments](docs/models/CompanyAttachedSegments.md)
 - [CompanyList](docs/models/CompanyList.md)
 - [CompanyScroll](docs/models/CompanyScroll.md)
 - [Contact](docs/models/Contact.md)
 - [ContactAttachedCompanies](docs/models/ContactAttachedCompanies.md)
 - [ContactCompanies](docs/models/ContactCompanies.md)
 - [ContactList](docs/models/ContactList.md)
 - [ContactLocation](docs/models/ContactLocation.md)
 - [ContactNotes](docs/models/ContactNotes.md)
 - [ContactReplyConversationRequest](docs/models/ContactReplyConversationRequest.md)
 - [ContactSegments](docs/models/ContactSegments.md)
 - [ContactSocialProfiles](docs/models/ContactSocialProfiles.md)
 - [ContactSubscriptionTypes](docs/models/ContactSubscriptionTypes.md)
 - [ContactTags](docs/models/ContactTags.md)
 - [Conversation](docs/models/Conversation.md)
 - [ConversationContacts](docs/models/ConversationContacts.md)
 - [ConversationFirstContactReply](docs/models/ConversationFirstContactReply.md)
 - [ConversationList](docs/models/ConversationList.md)
 - [ConversationPart](docs/models/ConversationPart.md)
 - [ConversationPartAuthor](docs/models/ConversationPartAuthor.md)
 - [ConversationParts](docs/models/ConversationParts.md)
 - [ConversationRating](docs/models/ConversationRating.md)
 - [ConversationSource](docs/models/ConversationSource.md)
 - [ConversationStatistics](docs/models/ConversationStatistics.md)
 - [ConversationTeammates](docs/models/ConversationTeammates.md)
 - [ConvertVisitorRequest](docs/models/ConvertVisitorRequest.md)
 - [CreateArticleRequest](docs/models/CreateArticleRequest.md)
 - [CreateCollectionRequest](docs/models/CreateCollectionRequest.md)
 - [CreateContactRequest](docs/models/CreateContactRequest.md)
 - [CreateConversationRequest](docs/models/CreateConversationRequest.md)
 - [CreateDataAttributeRequest](docs/models/CreateDataAttributeRequest.md)
 - [CreateDataEventRequest](docs/models/CreateDataEventRequest.md)
 - [CreateDataEventSummariesRequest](docs/models/CreateDataEventSummariesRequest.md)
 - [CreateDataExportsRequest](docs/models/CreateDataExportsRequest.md)
 - [CreateMessageRequest](docs/models/CreateMessageRequest.md)
 - [CreateOrUpdateCompanyRequest](docs/models/CreateOrUpdateCompanyRequest.md)
 - [CreateOrUpdateTagRequest](docs/models/CreateOrUpdateTagRequest.md)
 - [CreatePhoneSwitchRequest](docs/models/CreatePhoneSwitchRequest.md)
 - [CreateSectionRequest](docs/models/CreateSectionRequest.md)
 - [CreateTicketReplyRequest](docs/models/CreateTicketReplyRequest.md)
 - [CreateTicketRequest](docs/models/CreateTicketRequest.md)
 - [CreateTicketTypeAttributeRequest](docs/models/CreateTicketTypeAttributeRequest.md)
 - [CreateTicketTypeRequest](docs/models/CreateTicketTypeRequest.md)
 - [CursorPages](docs/models/CursorPages.md)
 - [CustomAttributes](docs/models/CustomAttributes.md)
 - [CustomObjectInstance](docs/models/CustomObjectInstance.md)
 - [CustomerRequest](docs/models/CustomerRequest.md)
 - [DataAttribute](docs/models/DataAttribute.md)
 - [DataAttributeList](docs/models/DataAttributeList.md)
 - [DataEvent](docs/models/DataEvent.md)
 - [DataEventList](docs/models/DataEventList.md)
 - [DataEventSummary](docs/models/DataEventSummary.md)
 - [DataEventSummaryItem](docs/models/DataEventSummaryItem.md)
 - [DataExport](docs/models/DataExport.md)
 - [DataExportCsv](docs/models/DataExportCsv.md)
 - [DeletedArticleObject](docs/models/DeletedArticleObject.md)
 - [DeletedCollectionObject](docs/models/DeletedCollectionObject.md)
 - [DeletedCompanyObject](docs/models/DeletedCompanyObject.md)
 - [DeletedObject](docs/models/DeletedObject.md)
 - [DeletedSectionObject](docs/models/DeletedSectionObject.md)
 - [DetachContactFromConversationRequest](docs/models/DetachContactFromConversationRequest.md)
 - [Error](docs/models/Error.md)
 - [FileAttribute](docs/models/FileAttribute.md)
 - [GroupContent](docs/models/GroupContent.md)
 - [GroupTranslatedContent](docs/models/GroupTranslatedContent.md)
 - [IntercomVersion](docs/models/IntercomVersion.md)
 - [MergeContactsRequest](docs/models/MergeContactsRequest.md)
 - [Message](docs/models/Message.md)
 - [MultipleFilterSearchRequest](docs/models/MultipleFilterSearchRequest.md)
 - [NewsItem](docs/models/NewsItem.md)
 - [NewsItemRequest](docs/models/NewsItemRequest.md)
 - [Newsfeed](docs/models/Newsfeed.md)
 - [NewsfeedAssignment](docs/models/NewsfeedAssignment.md)
 - [Note](docs/models/Note.md)
 - [NoteList](docs/models/NoteList.md)
 - [OpenConversationRequest](docs/models/OpenConversationRequest.md)
 - [PagesLink](docs/models/PagesLink.md)
 - [PaginatedResponse](docs/models/PaginatedResponse.md)
 - [PartAttachment](docs/models/PartAttachment.md)
 - [PhoneSwitch](docs/models/PhoneSwitch.md)
 - [RedactConversationRequest](docs/models/RedactConversationRequest.md)
 - [Reference](docs/models/Reference.md)
 - [ReplyConversationRequest](docs/models/ReplyConversationRequest.md)
 - [SearchRequest](docs/models/SearchRequest.md)
 - [Section](docs/models/Section.md)
 - [SectionList](docs/models/SectionList.md)
 - [Segment](docs/models/Segment.md)
 - [SegmentList](docs/models/SegmentList.md)
 - [SingleFilterSearchRequest](docs/models/SingleFilterSearchRequest.md)
 - [SlaApplied](docs/models/SlaApplied.md)
 - [SnoozeConversationRequest](docs/models/SnoozeConversationRequest.md)
 - [SocialProfile](docs/models/SocialProfile.md)
 - [StartingAfterPaging](docs/models/StartingAfterPaging.md)
 - [SubscriptionType](docs/models/SubscriptionType.md)
 - [SubscriptionTypeList](docs/models/SubscriptionTypeList.md)
 - [Tag](docs/models/Tag.md)
 - [TagCompanyRequest](docs/models/TagCompanyRequest.md)
 - [TagList](docs/models/TagList.md)
 - [TagMultipleUsersRequest](docs/models/TagMultipleUsersRequest.md)
 - [Tags](docs/models/Tags.md)
 - [Team](docs/models/Team.md)
 - [TeamList](docs/models/TeamList.md)
 - [TeamPriorityLevel](docs/models/TeamPriorityLevel.md)
 - [Ticket](docs/models/Ticket.md)
 - [TicketContacts](docs/models/TicketContacts.md)
 - [TicketCustomAttributes](docs/models/TicketCustomAttributes.md)
 - [TicketNote](docs/models/TicketNote.md)
 - [TicketPart](docs/models/TicketPart.md)
 - [TicketPartAuthor](docs/models/TicketPartAuthor.md)
 - [TicketParts](docs/models/TicketParts.md)
 - [TicketRequestCustomAttributes](docs/models/TicketRequestCustomAttributes.md)
 - [TicketType](docs/models/TicketType.md)
 - [TicketTypeAttribute](docs/models/TicketTypeAttribute.md)
 - [TicketTypeAttributeList](docs/models/TicketTypeAttributeList.md)
 - [TicketTypeList](docs/models/TicketTypeList.md)
 - [Translation](docs/models/Translation.md)
 - [UntagCompanyRequest](docs/models/UntagCompanyRequest.md)
 - [UpdateArticleRequest](docs/models/UpdateArticleRequest.md)
 - [UpdateCollectionRequest](docs/models/UpdateCollectionRequest.md)
 - [UpdateContactRequest](docs/models/UpdateContactRequest.md)
 - [UpdateConversationRequest](docs/models/UpdateConversationRequest.md)
 - [UpdateDataAttributeRequest](docs/models/UpdateDataAttributeRequest.md)
 - [UpdateSectionRequest](docs/models/UpdateSectionRequest.md)
 - [UpdateTicketRequest](docs/models/UpdateTicketRequest.md)
 - [UpdateTicketTypeAttributeRequest](docs/models/UpdateTicketTypeAttributeRequest.md)
 - [UpdateTicketTypeRequest](docs/models/UpdateTicketTypeRequest.md)
 - [UpdateVisitorRequest](docs/models/UpdateVisitorRequest.md)
 - [Visitor](docs/models/Visitor.md)
 - [VisitorDeletedObject](docs/models/VisitorDeletedObject.md)
