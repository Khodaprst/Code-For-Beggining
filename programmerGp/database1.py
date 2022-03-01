import sqlite3
from Karmand import Karmand
from tabulate import tabulate

# this is my connection (data base)
# conn
DataBase = sqlite3.connect('My_DataBase.db')

#c
kursor = DataBase.cursor()
kursor.execute('''CREATE TABLE IF NOT EXISTS Karmand
            (
            first text,
            last text, 
            pay integer
            )
''')

def insert_emp(emp):
    with DataBase:
        kursor.execute("""INSERT INTO Karmand VALUES (:first, :last, :pay)""", {'first' : emp.first, 'last' :emp.last, 'pay' : emp.pay})
    
def get_emp_by_lastname(lastname):
    kursor.execute("""SELECT * FROM Karmand where last = :last""", ({'last' : lastname}))
    return kursor.fetchall()

def get_all_emp():
    kursor.execute("""SELECT * FROM Karmand """)
    return kursor.fetchall()

def update_pay(emp, pay) :
    with DataBase:
        kursor.execute("""UPDATE Karmand SET pay = :pay
                        where first = :first AND last = :last""",
                        {'first' : emp.first, 'last' : emp.last, 'pay' : pay})

def remove_emp(emp):
    with DataBase:
        kursor.execute("""DELETE from Karmand where first = :first AND last = :last""",
                        {'first': emp.first, 'last': emp.last})


#kursor.execute("INSERT INTO Karmand VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.pay))
#DataBase.commit()

#kursor.execute("INSERT INTO Karmand VALUES (:first, :last, :pay)", {'first' : emp2.first, 'last' :emp2.last, 'pay' : emp2.pay})
#DataBase.commit()

emp1 = Karmand('AmirHosein', 'Moalemi', 700)
emp2 = Karmand('Mhmd', 'Golzar', 600)
emp3 = Karmand('Reza', 'Javan', 400)
emp4 = Karmand('Elnaz', 'Shakerdoost', 500)

#insert_emp(emp1)
#insert_emp(emp2)
#insert_emp(emp3)
#insert_emp(emp4)

remove_emp(emp4)
EmpHa = get_all_emp()
print(tabulate(EmpHa))


DataBase.close()