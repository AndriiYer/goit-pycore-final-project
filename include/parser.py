from colorama import Fore


def parse_input(line: str):
    parts = line.strip().split()
    if not parts:
        return "", []
    return parts[0], parts[1:]


def print_help():
    print(Fore.CYAN + "Available commands:")
    print(" add-contact [name] [phone] [email?]")
    print(" change-phone [name] [old_phone] [new_phone]")
    print(" show-phone [name]")
    print(" add-email [name] [email]")
    print(" change-email [name] [old_email] [new_email]")
    print(" delete-email [name] [email]")
    print(" add-birthday [name] [DD.MM.YYYY]")
    print(" show-birthday [name]")
    print(" birthdays")
    print(" show-all")
    print(" delete-contact [name]")
    print(" search [query]")
    print(" add-note [text] [#tag1 #tag2 ...]")
    print(" edit-note [note_id] [new_text]")
    print(" delete-note [note_id]")
    print(" find-note-by-id [note_id]")
    print(" show-all-notes")
    print(" search-notes-by-text [text]")
    print(" search-notes-by-tags [#tag1 #tag2]")
    print(" add-tag-to-note [note_id] [#tag]")
    print(" remove-tag-from-note [note_id] [#tag]")
    print(" edit-tag-in-note [note_id] [old_tag] [new_tag]")
    print(" sort-notes-by-tags")
    print(" help")
    print(" exit | close | quit")