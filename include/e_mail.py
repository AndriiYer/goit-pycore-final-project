from include.field import Field


class Email(Field):
    def __init__(self, value: str):
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email format.")
        super().__init__(value)