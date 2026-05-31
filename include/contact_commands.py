from colorama import Fore
from include.input_error import input_error
from include.address_book import AddressBook
from include.record import Record

@input_error
def cmd_add_contact(args, book: AddressBook):
    name = args[0]
    phone = args[1] if len(args) > 1 else None
    email = args[2] if len(args) > 2 else None

    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        msg = "Contact added."
    else:
        msg = "Contact updated."

    if phone:
        record.add_phone(phone)
    if email:
        record.add_email(email)
    return Fore.GREEN + msg


@input_error
def cmd_change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    rec = book.find(name)
    if not rec:
        raise KeyError
    rec.change_phone(old_phone, new_phone)
    return Fore.GREEN + "Phone changed."


@input_error
def cmd_show_phone(args, book: AddressBook):
    name = args[0]
    rec = book.find(name)
    if not rec:
        raise KeyError
    phones = ", ".join(p.value for p in rec.phones) or "—"
    return f"{name}: {phones}"


@input_error
def cmd_add_email(args, book: AddressBook):
    name, email = args
    rec = book.find(name)
    if not rec:
        raise KeyError
    rec.add_email(email)
    return Fore.GREEN + "Email added."


@input_error
def cmd_change_email(args, book: AddressBook):
    name, old_email, new_email = args
    rec = book.find(name)
    if not rec:
        raise KeyError
    rec.change_email(old_email, new_email)
    return Fore.GREEN + "Email changed."


@input_error
def cmd_delete_email(args, book: AddressBook):
    name, email = args
    rec = book.find(name)
    if not rec:
        raise KeyError
    rec.delete_email(email)
    return Fore.GREEN + "Email deleted."


@input_error
def cmd_add_birthday(args, book: AddressBook):
    name, date_str = args
    rec = book.find(name)
    if not rec:
        raise KeyError
    rec.set_birthday(date_str)
    return Fore.GREEN + "Birthday set."


@input_error
def cmd_show_birthday(args, book: AddressBook):
    name = args[0]
    rec = book.find(name)
    if not rec:
        raise KeyError
    if not rec.birthday:
        return "No birthday."
    return f"{name}: {rec.birthday}"


@input_error
def cmd_birthdays(args, book: AddressBook):
    upcoming = book.upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    lines = ["Upcoming birthdays:"]
    for name, date_ in upcoming:
        lines.append(f" • {name} — {date_.strftime('%d.%m.%Y')}")
    return "\n".join(lines)


def cmd_show_all(book: AddressBook):
    if not book.data:
        return "No contacts."
    return "\n".join(str(r) for r in book.values())


@input_error
def cmd_delete_contact(args, book: AddressBook):
    name = args[0]
    if not book.find(name):
        raise KeyError
    book.delete(name)
    return Fore.GREEN + "Contact deleted."


@input_error
def cmd_search(args, book: AddressBook):
    query = " ".join(args)
    res = book.search(query)
    if not res:
        return "No matches."
    return "\n".join(str(r) for r in res)
