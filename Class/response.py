import json
from Helpers.constantes import REQUEST

class Response:

    def __init__(self, name: str, message: str = "", data: dict = []):
        self.name = name
        self.data = data
        self.message = message
        if not isinstance(self.data, list):
            self.data = [self.data]

    def create_response(self):

        response = {"status": REQUEST[self.name]["code"],
                    "message": REQUEST[self.name]["message"]
                    if self.message == "" else self.message,
                    "data": self.data if self.data else []}

        return response

    