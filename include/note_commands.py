from colorama import Fore
from include.input_error import input_error
from include.notes_book import NotesBook


@input_error
def cmd_add_note(args, notes: NotesBook):
    if not args:
        raise ValueError("Text is required.")
    # text до першого тега
    tags = [a for a in args if a.startswith("#")]
    text_parts = [a for a in args if not a.startswith("#")]
    text = " ".join(text_parts)
    note = notes.add_note(text, tags)
    return Fore.GREEN + f"Note added with id {note.id}"


@input_error
def cmd_edit_note(args, notes: NotesBook):
    note_id = args[0]
    new_text = " ".join(args[1:])
    note = notes.find_by_id(note_id)
    if not note:
        raise KeyError
    note.text = new_text
    return Fore.GREEN + "Note updated."


@input_error
def cmd_delete_note(args, notes: NotesBook):
    note_id = args[0]
    if not notes.find_by_id(note_id):
        raise KeyError
    notes.delete(note_id)
    return Fore.GREEN + "Note deleted."


@input_error
def cmd_find_note_by_id(args, notes: NotesBook):
    note_id = args[0]
    note = notes.find_by_id(note_id)
    if not note:
        raise KeyError
    return str(note)


@input_error
def cmd_search_notes_by_text(args, notes: NotesBook):
    text = " ".join(args)
    res = notes.search_by_text(text)
    if not res:
        return "No notes found."
    return "\n".join(str(n) for n in res)


@input_error
def cmd_search_notes_by_tags(args, notes: NotesBook):
    tags = args
    res = notes.search_by_tags(tags)
    if not res:
        return "No notes found."
    return "\n".join(str(n) for n in res)


@input_error
def cmd_add_tag_to_note(args, notes: NotesBook):
    note_id, tag = args
    note = notes.find_by_id(note_id)
    if not note:
        raise KeyError
    if tag not in note.tags:
        note.tags.append(tag)
    return Fore.GREEN + "Tag added."


@input_error
def cmd_remove_tag_from_note(args, notes: NotesBook):
    note_id, tag = args
    note = notes.find_by_id(note_id)
    if not note:
        raise KeyError
    if tag in note.tags:
        note.tags.remove(tag)
    return Fore.GREEN + "Tag removed."


@input_error
def cmd_edit_tag_in_note(args, notes: NotesBook):
    note_id, old_tag, new_tag = args
    note = notes.find_by_id(note_id)
    if not note:
        raise KeyError
    if old_tag not in note.tags:
        raise ValueError("Old tag not found.")
    note.tags = [new_tag if t == old_tag else t for t in note.tags]
    return Fore.GREEN + "Tag updated."


def cmd_sort_notes_by_tags(args, notes: NotesBook):
    sorted_notes = notes.sort_by_tags()
    if not sorted_notes:
        return "No notes."
    return "\n".join(str(n) for n in sorted_notes)
