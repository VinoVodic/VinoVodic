class UserHasNoPermission(Exception):
    def __init__(self, user, location):
        message = f"User ({user}) has no permission to do the following task.\nThe exception was thrown in {location}"
        super().__init__(message)