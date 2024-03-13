from typing import Any
from . import BaseFilter


class PhoneNumbersFilter(BaseFilter):
    @staticmethod
    def filter(data: Any):
        new_data = []

        for row in data:
            if len(row["tel_br"]) != 0:
                row["tel_br"] = row["tel_br"].replace("\xa0", "/")
            new_data.append(row)

        return new_data
