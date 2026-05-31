from collections import UserDict
from datetime import datetime, timedelta
from include.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def search(self, query: str):
        res = []
        q = query.lower()
        for rec in self.data.values():
            if q in rec.name.value.lower():
                res.append(rec)
                continue
            if any(q in p.value for p in rec.phones):
                res.append(rec)
                continue
            if any(q in e.value.lower() for e in rec.emails):
                res.append(rec)
                continue
        return res

    def upcoming_birthdays(self, days: int = 7):
        today = datetime.today().date()
        end = today + timedelta(days=days)
        result = []
        for rec in self.data.values():
            if not rec.birthday:
                continue
            bday = rec.birthday.value.date().replace(year=today.year)
            if today <= bday <= end:
                result.append((rec.name.value, bday))
        return result