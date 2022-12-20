def main_menu():
    print('\n1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход')
    return choice_main_menu()

def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные!')

def log_off():
    print('До свидания! До новых встреч!')

def load_success():
    print('Телефонная книга загружена!')

def save_success():
    print('Телефонная книга сохранена!')

def remove_success():
    print('Контакт удален!')

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]

def input_remove_contact():
    id = int(input('Введите ID контакта, который желаете удалить: '))
    return id

def find_contact():
    name = input('Ввдеите имя из телефонной книги: ')
    return name

def change_contact():
    id = int(input('Введите ID контакта, который желает изменить: '))
    return id
        