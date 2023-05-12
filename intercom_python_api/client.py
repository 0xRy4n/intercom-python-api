import time
import intercom_python_api
from pprint import pprint
from intercom_python_api.apis.tag_to_api import tag_to_api
from intercom_python_api.configuration import Configuration
from intercom_python_api.api_client import ApiClient

class Intercom:
    def __init__(self, api_token=None, host="https://api.intercom.io"):
        config = Configuration()
        config.access_token = api_token
        self.raw_api_client = ApiClient(config)

        for value in tag_to_api.values():
            instance = value(self.raw_api_client)
            setattr(self, value.__name__, instance)
