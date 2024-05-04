"""
Client automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .users_tag import UsersTag
from .databases_tag import DatabasesTag

class Client(sdkgen.ClientAbstract):
    def __init__(self, base_url: str, credentials: sdkgen.CredentialsInterface):
        super().__init__(base_url, credentials)

    def users(self) -> UsersTag:
        return UsersTag(
            self.http_client,
            self.parser
        )

    def databases(self) -> DatabasesTag:
        return DatabasesTag(
            self.http_client,
            self.parser
        )



    @staticmethod
    def build(token: str):
        return Client("https://api.notion.com", sdkgen.HttpBearer(token))
