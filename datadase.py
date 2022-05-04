"""
ТЕСТЫ

Maga 89995490719
"""
#>>> User('Maga', 89995490719)
import sqlite3

#  СОЗДАЁМ ТАБЛИЦУ ПОЛЬЗОВАТЕЛЕЙ
with sqlite3.connect('database.db') as db:

    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT(50),
        Num TEXT(15))      
    """
    cursor.execute(query)


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
def UserMessageTable():
    TableName = ("Message_")
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = '''
        CREATE TABLE IF NOT EXISTS TableName (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Message TEXT,
            number TEXT)        
        '''
        cursor.execute (query)
    pass


User()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
