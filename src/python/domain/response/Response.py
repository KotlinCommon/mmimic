class Response:
    def __init__(self, value, error=None):
        self.value = value
        self.error = error

    def is_success(self):
        return self.error is None

    def is_error(self):
        return self.error is not None
