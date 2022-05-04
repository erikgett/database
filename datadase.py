"""
ТЕСТЫ
>>> User('Maga', 89995490719)
Maga 89995490719

>>> UserMessageTable(1)
таблица пользователя создана

"""

import sqlite3
from sqlite3 import Error


#  СОЗДАЁМ ТАБЛИЦУ ПОЛЬЗОВАТЕЛЕЙ
with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS usersf(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        number TEXT)        
    '''
    cursor.execute(query)
    cursor.execute("INSERT INTO usersf VALUES(1, 'John', 700 )")
    print(155)


#   СОЗДАЕМ ЛОГИКУ СОЗДАНИЯ - ПОИСКА id  в базе данных проверки создан ли пользователь
def User(username='erik', usernumber=891234):
    try:
        db.cursor()
    except:
        pass


#   СОЗДАЕМ ДЛЯ ПОЛЬЗОВАТЕЛЯ ТАБЛИЦУ С ЕГО СООБЩЕНИЯМИ
def UserMessageTable(identifier =15, sms = '234'):
    print(identifier)
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    query ='CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTOINCREMENT, name text)'
    cursor.execute(query)
    db.commit()
    db.close()

UserMessageTable()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
