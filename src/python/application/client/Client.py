import requests
import json

from src.python.domain.message.ErrorMessage import ErrorMessage
from src.python.domain.response.Response import Response


class Client:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.bearerToken = None

    def request(self, method, endpoint, jsonData=None):
        """
            Sends an HTTP request and returns a Response object.
            """
        response = None
        try:
            url = f"{self.baseUrl}{endpoint}"
            headers = {'Content-Type': 'application/json'}

            if self.bearerToken:
                headers['Authorization'] = self.bearerToken

            if jsonData:
                response = requests.request(method, url, data=json.dumps(jsonData), headers=headers)
            else:
                response = requests.request(method, url, headers=headers)
            response.raise_for_status()

            # Check the content type of the response
            contentType = response.headers.get('Content-Type', '')

            if 'application/json' in contentType:
                try:
                    return Response(value=response.json(), headers=response.headers)
                except json.JSONDecodeError:
                    return Response(value=None, error=ErrorMessage.TokenNotFound, headers=response.headers)
            else:
                return Response(value=response.text, headers=response.headers)

        except requests.HTTPError as httpErr:
            errorMessage = str(httpErr)
        except Exception as err:
            errorMessage = str(err)

        # Return error response
        headers = response.headers if response is not None else {}
        return Response(value=None, error=errorMessage, headers=headers)

    def get(self, endpoint, params=None):
        if params:
            endpoint += '?' + '&'.join([f"{key}={value}" for key, value in params.items()])
        return self.request('GET', endpoint)

    def post(self, endpoint, jsonData):
        """Sends a POST request."""
        return self.request('POST', endpoint, jsonData)

    def put(self, endpoint, jsonData):
        """Sends a PUT request."""
        return self.request('PUT', endpoint, jsonData)
