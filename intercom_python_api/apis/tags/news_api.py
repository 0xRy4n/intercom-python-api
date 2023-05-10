# coding: utf-8

"""
    Intercom API

    The intercom API reference.  # noqa: E501

    The version of the OpenAPI document: 2.8
    Generated by: https://openapi-generator.tech
"""

from intercom_python_api.paths.news_news_items.post import CreateNewsItem
from intercom_python_api.paths.news_news_items_id.delete import DeleteNewsItem
from intercom_python_api.paths.news_newsfeeds_id_items.get import ListLiveNewsfeedItems
from intercom_python_api.paths.news_news_items.get import ListNewsItems
from intercom_python_api.paths.news_newsfeeds.get import ListNewsfeeds
from intercom_python_api.paths.news_news_items_id.get import RetrieveNewsItem
from intercom_python_api.paths.news_newsfeeds_id.get import RetrieveNewsfeed
from intercom_python_api.paths.news_news_items_id.put import UpdateNewsItem


class NewsApi(
    CreateNewsItem,
    DeleteNewsItem,
    ListLiveNewsfeedItems,
    ListNewsItems,
    ListNewsfeeds,
    RetrieveNewsItem,
    RetrieveNewsfeed,
    UpdateNewsItem,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass