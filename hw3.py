import os
import json
from csv import DictReader


def get_path(file_name):
    """Глобальный путь к файлам"""
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV = get_path('books.csv')
JSON = get_path('users.json')
RESULT = get_path('result.json')


def read_csv():
    """Чтение и преобразование списка книг (удаление не нужных полей)"""
    global books
    books = []
    with open(CSV, newline='') as f:
        reader = DictReader(f)
        for book in reader:
            del book['Publisher']
            book['Pages'] = int(book['Pages'])
            books.append(book)
    return books


def read_json():
    """Чтение и преобразование списка пользователей (выборка только нужных полей)"""
    global users
    with open(JSON, "r") as f:
        users = []
        for user in json.load(f):
            users_list = {
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": []
            }
            users.append(users_list)


def distribute_book():
    """Раздача книг каждому пользователю"""
    for i, books in enumerate(read_csv()):
        users[i % len(users)]["books"].append(books)
    print(users)


def save_result():
    """Сохранение результата раздачи книг пользователям в формате JSON"""
    with open(RESULT, 'w') as fd:
        json.dump(users, fd, indent=4)


read_json()
distribute_book()
save_result()
