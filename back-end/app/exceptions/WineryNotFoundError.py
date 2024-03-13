class WineryNotFoundError(Exception):
    "Raise when winery with given id is not in the database"

    def __init__(self, winery_id) -> None:
        message = f"Winery with {winery_id} not found."
        super().__init__(message)
