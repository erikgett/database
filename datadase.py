"""
ТЕСТЫ
>>> NewUser('Maga', 89995490719)
Maga 89995490719
"""

import sqlite3

#  СОЗДАЁМ ВСЕ НЕОБХОДИМЫЕ ТАБЛИЧКИ
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
def User(Username='erik', Num=891234):
    print(Username, Num)
    try:
        db.cursor()
    except:
        pass


#   СОЗДАЕМ ДЛЯ ПОЛЬЗОВАТЕЛЯ ТАБЛИЦУ С ЕГО СООБЩЕНИЯМИ
def UserMessageTable():
    pass


NewUser()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
