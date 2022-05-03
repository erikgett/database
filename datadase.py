"""
ТЕСТЫ
>>> User('Maga', 89995490719)
Maga 89995490719

>>> UserMessageTable(1)
таблица пользователя создана

"""

import sqlite3

#  СОЗДАЁМ ТАБЛИЦУ ПОЛЬЗОВАТЕЛЕЙ
with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        number TEXT)        
    '''
    cursor.execute(query)


#   СОЗДАЕМ ЛОГИКУ СОЗДАНИЯ - ПОИСКА id  в базе данных проверки создан ли пользователь
def User(username='erik', usernumber=891234):
    try:
        db.cursor()
    except:
        pass


#   СОЗДАЕМ ДЛЯ ПОЛЬЗОВАТЕЛЯ ТАБЛИЦУ С ЕГО СООБЩЕНИЯМИ
def UserMessageTable(identifier):
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
