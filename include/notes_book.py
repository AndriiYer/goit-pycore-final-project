from collections import UserDict
from include.note import Note
from include.record import Record


class NotesBook(UserDict):
    def add_note(self, text: str, tags: list[str]):
        note = Note(text, tags)
        self.data[note.id] = note
        return note

    def find_by_id(self, note_id: str) -> Note | None:
        return self.data.get(note_id)

    def delete(self, note_id: str):
        if note_id in self.data:
            del self.data[note_id]

    def search_by_text(self, text: str):
        q = text.lower()
        return [n for n in self.data.values() if q in n.text.lower()]

    def search_by_tags(self, tags: list[str]):
        tags_set = set(tags)
        return [n for n in self.data.values() if tags_set.issubset(set(n.tags))]

    def sort_by_tags(self):
        return sorted(self.data.values(), key=lambda n: ", ".join(n.tags))