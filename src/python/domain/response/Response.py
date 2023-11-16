class Response:
    def __init__(self, value, error=None, headers=None):
        self.value = value
        self.error = error
        self.headers = headers

    def is_success(self):
        return self.error is None

    def is_error(self):
        return self.error is not None
