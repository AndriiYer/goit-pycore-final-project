from colorama import Fore, Style
from include.address_book import AddressBook
from include.contact_commands import *
from include.data import CONTACTS_FILE, NOTES_FILE, ensure_data_dir, load_book, save_book
from include.note_commands import *
from include.notes_book import NotesBook
from include.parser import parse_input, print_help


def run_cli():
    ensure_data_dir()
    book: AddressBook = load_book(CONTACTS_FILE, AddressBook)
    notes: NotesBook = load_book(NOTES_FILE, NotesBook)

    print(Fore.GREEN + "Personal Assistant started. Type 'help' for commands.")

    try:
        while True:
            line = input(Fore.YELLOW + ">> " + Style.RESET_ALL)
            command, args = parse_input(line)

            if command in ("exit", "close", "quit"):
                print("Good bye!")
                break
            elif command == "help":
                print_help()
            elif command == "add-contact":
                print(cmd_add_contact(args, book))
            elif command == "change-phone":
                print(cmd_change_phone(args, book))
            elif command == "show-phone":
                print(cmd_show_phone(args, book))
            elif command == "add-email":
                print(cmd_add_email(args, book))
            elif command == "change-email":
                print(cmd_change_email(args, book))
            elif command == "delete-email":
                print(cmd_delete_email(args, book))
            elif command == "add-birthday":
                print(cmd_add_birthday(args, book))
            elif command == "show-birthday":
                print(cmd_show_birthday(args, book))
            elif command == "birthdays":
                print(cmd_birthdays(args, book))
            elif command == "show-all":
                print(cmd_show_all(book))
            elif command == "delete-contact":
                print(cmd_delete_contact(args, book))
            elif command == "search":
                print(cmd_search(args, book))
            elif command == "add-note":
                print(cmd_add_note(args, notes))
            elif command == "edit-note":
                print(cmd_edit_note(args, notes))
            elif command == "delete-note":
                print(cmd_delete_note(args, notes))
            elif command == "find-note-by-id":
                print(cmd_find_note_by_id(args, notes))
            elif command == "show-all-notes":
                if not notes.data:
                    print("No notes.")
                else:
                    print("\n".join(str(n) for n in notes.values()))
            elif command == "search-notes-by-text":
                print(cmd_search_notes_by_text(args, notes))
            elif command == "search-notes-by-tags":
                print(cmd_search_notes_by_tags(args, notes))
            elif command == "add-tag-to-note":
                print(cmd_add_tag_to_note(args, notes))
            elif command == "remove-tag-from-note":
                print(cmd_remove_tag_from_note(args, notes))
            elif command == "edit-tag-in-note":
                print(cmd_edit_tag_in_note(args, notes))
            elif command == "sort-notes-by-tags":
                print(cmd_sort_notes_by_tags(args, notes))
            elif command == "":
                continue
            else:
                print(Fore.RED + "Unknown command. Type 'help'.")
    finally:
        save_book(CONTACTS_FILE, book)
        save_book(NOTES_FILE, notes)