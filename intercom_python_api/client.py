import time
import intercom_python_api
from pprint import pprint
from intercom_python_api.apis.tag_to_api import tag_to_api
from intercom_python_api.model.error import Error
from intercom_python_api.model.intercom_version import IntercomVersion


class Intercom:
    def __init__(self, api_token=None, host="https://api.intercom.io"):
        configuration = intercom_python_api.Configuration()
        configuration.access_token = api_token
        self.raw_api_client  = intercom_python_api.ApiClient(configuration)

        for value in tag_to_api.values():
            instance = value(self.raw_api_client)
            setattr(self, value.__name__, instance)





