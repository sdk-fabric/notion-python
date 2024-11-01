"""
DatabaseTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .database import Database

class DatabaseTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get(self, database_id: str) -> Database:
        """
        Retrieves a database object — information that describes the structure and columns of a database — for a provided database ID. The response adheres to any limits to an integration’s capabilities.
        """
        try:
            path_params = {}
            path_params['database_id'] = database_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url('/v1/databases/:database_id', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = Database.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



