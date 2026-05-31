# Personal Assistant — консольний менеджер контактів і нотаток
Це консольний застосунок, який допомагає керувати контактами та нотатками, зберігати дані, виконувати пошук, редагування, сортування та отримувати нагадування про дні народження.

## ФУНКЦІОНАЛ
### Контакти
- Створення нових контактів
- Редагування телефонів та email-адрес
- Додавання або зміна дати народження
- Видалення контактів
- Перевірка унікальності email та телефону
- Пошук за ім’ям, телефоном або email
- Перегляд усіх контактів
- Нагадування про майбутні дні народження

### Нотатки
- Створення нотаток
- Редагування та видалення нотаток
- Пошук за текстом

### Теги
- Додавання, зміна та видалення тегів
- Пошук за тегами
- Сортування за тегами

### Збереження даних
Файли зберігаються у каталозі
```
/data/contacts.bin
/data/notes.bin
```
Дані зберігаються в бінарному форматі та серіалізуються/деріалізуються з використанням pickle
Про відсутності файлів даних створюються нові порожні
Дані зберігаються при виході з додатку (exit, close, Ctrl+C)

### Валідація
- Телефон — 10 цифр
- Email — перевірка формату
- Дата народження — формат DD.MM.YYYY

### Інтерфейс
- Кольоровий вивід (Colorama)
- Підказки для команд

### Пошук
- По контактах: частковий збіг у імені, телефоні або email
- По нотатках: Нотатки: пошук за текстом або тегами

### Системні вимоги
Python 3.10+
Пакет colorama
Рекомендовано використовувати віртуальне середовище

### Використання
1. Встановити залежності:
```
pip install -r requirements.txt
```
2. Запустити програму:
```
python main.py
```

### Встановлення як пакет (як опція)
```
pip install -e .
```

## КОМАНДИ ДЛЯ КОНТАКТІВ
Додавання контакту
```
add-contact [name] [phone] [email?]
```
Зміна телефону
```
change-phone [name] [old_phone] [new_phone]
```
Показати телефони
```
show-phone [name]
```
Робота з email
```
add-email [name] [email]
change-email [name] [old_email] [new_email]
delete-email [name] [email]
```
День народження
```
add-birthday [name] [DD.MM.YYYY]
show-birthday [name]
birthdays
```
Інші команди
```
show-all
delete-contact [name]
search [query]
```

КОМАНДИ ДЛЯ НОТАТОК
Створення нотатки
```
add-note [text] [#tag1 #tag2 ...]
```
Редагування нотатки
```
edit-note [note_id] [new_text]
Видалення нотатки
```
delete-note [note_id]
```
Пошук нотатки
```
find-note-by-id [note_id]
search-notes-by-text [text]
search-notes-by-tags [#tag1 #tag2]
```

КОМАНДИ ДЛЯ ДЕГІВ
```
add-tag-to-note [note_id] [#tag]
remove-tag-from-note [note_id] [#tag]
edit-tag-in-note [note_id] [old_tag] [new_tag]
sort-notes-by-tags
```

СИСТЕМНІ КОМАНДИ
```
help
exit
close
quit
```

ПРИКЛАД РОБОТИ
```
> add-contact Andrii 0123456789 andrii@email.com
Contact 'Andrii' added.

> add-email Andrii andrii@email.com
Email added.

> show-phone Andrii
Andrii: 1234567890

> add-birthday Andrii 12.04.1990
Birthday added for Andrii.

> birthdays
Upcoming birthdays:
 • Andrii — 01.01.1980

> exit
Good bye!
```