import uuid


class Note:
    def __init__(self, text: str, tags: list[str] | None = None):
        self.id = str(uuid.uuid4())[:8]
        self.text = text
        self.tags = tags or []

    def __str__(self):
        tags = " ".join(self.tags) if self.tags else "—"
        return f"[{self.id}] {self.text}  ({tags})"