import sqlite3
from Krmnd import Krmnd

#sakht yek database
connection = sqlite3.Connection('FirstDataBase.db')

#vared kardan dstoor dakhel database:
cursor = connection.cursor()

#neveshtan va sohbat ba database
cursor.execute('''CREATE TABLE IF NOT EXISTS Krmnd(
                first text,
                last text,
                pay integer

                )''')

def insert(emp):
    with connection:
        cursor.execute("INSERT INTO Krmnd VALUES (:first, :last, :pay)", (emp.first, emp.last, emp.pay))
        connection.commit()

def get_by_lastname(lastname):
    cursor.execute('SELECT * FROM Krmnd WHERE last = :last', ({'last' : lastname}))
    return cursor.fetchall()

Emp_1 = Krmnd('AmirHosein', 'Khodaparast', 900)
Emp_2 = Krmnd('Mahsa', 'Azizi', 400)



#cursor.execute("INSERT INTO Krmnd VALUES (:first, :last, :pay)", (Emp_1.first, Emp_1.last, Emp_1.pay))
#cursor.execute("INSERT INTO Krmnd VALUES (:first, :last, :pay)", (Emp_2.first, Emp_2.last, Emp_2.pay))

#zakhire dastoorat execute
#connection.commit()

#moshahede dastoorat neveshte shode:
#cursor.execute('SELECT * FROM Krmnd WHERE last = :last')
#print(cursor.fetchall())

#bastan dastoorant
connection.close()