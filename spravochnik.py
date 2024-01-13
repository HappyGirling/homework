# Функция для добавления новой записи в справочник
def add_entry(phone_book, first_name, last_name, patronymic, phone_number):
    phone_book.append({
        "Фамилия": last_name,
        "Имя": first_name,
        "Отчество": patronymic,
        "Номер телефона": phone_number
    })

# Функция для сохранения справочника в текстовый файл
def save_to_file(phone_book, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phone_book:
            file.write(f"{entry['Фамилия']} {entry['Имя']} {entry['Отчество']} {entry['Номер телефона']}\n")

# Функция для вывода всех данных из справочника
def print_phone_book(phone_book):
    for entry in phone_book:
        print(f"{entry['Фамилия']} {entry['Имя']} {entry['Отчество']} {entry['Номер телефона']}")

# Функция для поиска записи по одной из характеристик
def search_entry(phone_book, search_query):
    results = [entry for entry in phone_book if search_query in entry.values()]
    return results

# Функция для импорта данных из файла
def import_from_file(filename):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                phone_book.append({
                    "Фамилия": parts[0],
                    "Имя": parts[1],
                    "Отчество": parts[2],
                    "Номер телефона": parts[3]
                })
    return phone_book

def copy_line_to_another_file(source_filename, target_filename, line_number):
    with open(source_filename, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()
        
    if 1 <= line_number <= len(lines):
        with open(target_filename, 'a', encoding='utf-8') as target_file:
            target_file.write(lines[line_number - 1])
        print(f"Строка {line_number} была успешно скопирована из {source_filename} в {target_filename}.")
    else:
        print(f"Ошибка: в файле нет строки с номером {line_number}.")