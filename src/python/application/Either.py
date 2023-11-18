class Either:
    def __init__(self, value, is_error=False):
        self.value = value
        self.is_error = is_error

    @classmethod
    def Success(cls, value):
        return cls(value, False)

    @classmethod
    def Failure(cls, value):
        return cls(value, True)

    def isSuccess(self):
        return not self.is_error

    def isFailure(self):
        return self.is_error
