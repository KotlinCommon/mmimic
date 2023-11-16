import requests
import json

from src.python.domain.message.ErrorMessage import ErrorMessage
from src.python.domain.response.Response import Response


class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, method, endpoint, json_data=None):
        """
         Sends an HTTP request and returns a Response object.
         """
        try:
            url = f"{self.base_url}{endpoint}"
            headers = {'Content-Type': 'application/json'}
            if json_data:
                response = requests.request(method, url, data=json.dumps(json_data), headers=headers)
            else:
                response = requests.request(method, url, headers=headers)
            response.raise_for_status()

            # Check the content type of the response
            content_type = response.headers.get('Content-Type', '')

            if 'application/json' in content_type:
                # Process JSON response
                try:
                    return Response(response.json())
                except json.JSONDecodeError:
                    return Response(None, error="Invalid JSON response from server")
            else:
                # Process non-JSON response
                return Response(response.text)

        except requests.HTTPError as http_err:
            return Response(None, error=str(http_err))
        except Exception as err:
            return Response(None, error=str(err))

    def get(self, endpoint):
        """Sends a GET request."""
        return self.send_request('GET', endpoint)

    def post(self, endpoint, json_data):
        """Sends a POST request."""
        return self.send_request('POST', endpoint, json_data)

    def put(self, endpoint, json_data):
        """Sends a PUT request."""
        return self.send_request('PUT', endpoint, json_data)
