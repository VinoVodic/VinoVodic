class InvalidInputError(Exception):
    "Raised when given inputs don't match the expected inputs"

    def __init__(self, location):
        message = f"Got incorrect input for the given request.\nCheck all the required fields and their data type.\nThe exception was thrown in {location}"
        super().__init__(message)