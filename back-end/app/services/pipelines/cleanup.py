import json
from .pipes import Pipe
from ..filters.activities_filter import ActivitesFilter
from ..filters.coordinates_filter import CoordinatesFilter
from ..filters.phone_number_filter import PhoneNumbersFilter


def cleanup_pipeline() -> None:
    data = None
    with open("vinarii2.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    cleanup_pipe = Pipe(data)
    cleanup_pipe.add_filter(ActivitesFilter)
    cleanup_pipe.add_filter(CoordinatesFilter)
    cleanup_pipe.add_filter(PhoneNumbersFilter)
    cleanup_pipe.execute()

    return cleanup_pipe.data
