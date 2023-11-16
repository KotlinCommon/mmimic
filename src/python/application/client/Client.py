import requests
import json

from src.python.domain.message.ErrorMessage import ErrorMessage
from src.python.domain.response.Response import Response


class Client:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.bearerToken = None

    def send_request(self, method, endpoint, jsonData=None):
        """
         Sends an HTTP request and returns a Response object.
         """
        try:
            url = f"{self.baseUrl}{endpoint}"
            headers = {'Content-Type': 'application/json'}
            if jsonData:
                response = requests.request(method, url, data=json.dumps(jsonData), headers=headers)
            else:
                response = requests.request(method, url, headers=headers)
            response.raise_for_status()

            # Check the content type of the response
            contentType = response.headers.get('Content-Type', '')

            if 'application/json' in response.headers.get('Content-Type', ''):
                try:
                    return Response(value=response.json(), headers=response.headers)
                except json.JSONDecodeError:
                    return Response(value=None, error=ErrorMessage.TokenNotFound, headers=response.headers)
            else:
                return Response(value=response.text, headers=response.headers)

        except requests.HTTPError as http_err:
            return Response(value=None, error=str(http_err), headers=response.headers)
        except Exception as err:
            return Response(value=None, error=str(err), headers=response.headers)

    def get(self, endpoint):
        """Sends a GET request."""
        return self.send_request('GET', endpoint)

    def post(self, endpoint, jsonData):
        """Sends a POST request."""
        return self.send_request('POST', endpoint, jsonData)

    def put(self, endpoint, jsonData):
        """Sends a PUT request."""
        return self.send_request('PUT', endpoint, jsonData)
