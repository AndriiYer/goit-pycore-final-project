import os
import pickle


DATA_DIR = "data"
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.bin")
NOTES_FILE = os.path.join(DATA_DIR, "notes.bin")


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def load_book(path, default_cls):
    if not os.path.exists(path):
        return default_cls()
    with open(path, "rb") as f:
        return pickle.load(f)


def save_book(path, obj):
    with open(path, "wb") as f:
        pickle.dump(obj, f)