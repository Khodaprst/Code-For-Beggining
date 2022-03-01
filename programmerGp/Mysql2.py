import mysql.connector
mybd = mysql.connector.connect(
    host = 'localhost'
    user = 'root'
    password = 'Bokhoresh'
)

#print(mybd)

c = mydb.cursor()
c.execute('SHOW DATABASES')
for db in c:
    print(db)


    