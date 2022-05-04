"""
ТЕСТЫ

Maga 89995490719

>>> UserMessageTable(1)
таблица пользователя создана

"""
#>>> User('Maga', 89995490719)
import sqlite3
from sqlite3 import Error


#  СОЗДАЁМ ТАБЛИЦУ ПОЛЬЗОВАТЕЛЕЙ
with sqlite3.connect('database.db') as db:

    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS users(
    query = '''
    CREATE TABLE IF NOT EXISTS usersf(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT(50),
        Num TEXT(15))      
    """
    cursor.execute(query)
    cursor.execute("INSERT INTO usersf VALUES(1, 'John', 700 )")
    print(155)


#   СОЗДАЕМ ЛОГИКУ СОЗДАНИЯ - ПОИСКА id  в базе данных проверки создан ли пользователь
def User(Username='erik', Num=891234):
    Username = input ( "Name: " )
    Num = input ( "Num: " )

    try:
        db = sqlite3.connect ( "database.db" )
        cursor = db.cursor()

        cursor.execute("SELECT Num FROM users WHERE Num = ?", [Num])
        if cursor.fetchone() is None:
            values = [Username, Num]

            cursor.execute("INSERT INTO users(Username, Num) VALUES(?, ?)", values)
            db.commit()
            Id = Num
        else:
            Id = Num
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()



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
User()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
