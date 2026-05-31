from datetime import datetime
from include.field import Field


class Birthday(Field):
    def __init__(self, value: str):
        try:
            dt = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(dt)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")