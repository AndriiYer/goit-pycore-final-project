from include.name import Name
from include.phone import Phone
from include.e_mail import Email
from include.birthday import Birthday

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.emails: list[Email] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str):
        if any(p.value == phone for p in self.phones):
            raise ValueError("Phone already exists for this contact.")
        self.phones.append(Phone(phone))

    def change_phone(self, old: str, new: str):
        for p in self.phones:
            if p.value == old:
                self.phones.remove(p)
                self.add_phone(new)
                return
        raise ValueError("Old phone not found.")

    def add_email(self, email: str):
        if any(e.value == email for e in self.emails):
            raise ValueError("Email already exists for this contact.")
        self.emails.append(Email(email))

    def change_email(self, old: str, new: str):
        for e in self.emails:
            if e.value == old:
                self.emails.remove(e)
                self.add_email(new)
                return
        raise ValueError("Old email not found.")

    def delete_email(self, email: str):
        for e in self.emails:
            if e.value == email:
                self.emails.remove(e)
                return
        raise ValueError("Email not found.")

    def set_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones) or "—"
        emails = ", ".join(e.value for e in self.emails) or "—"
        bday = str(self.birthday) if self.birthday else "—"
        return f"{self.name.value}: phones [{phones}], emails [{emails}], birthday [{bday}]"