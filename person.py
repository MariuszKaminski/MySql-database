import os
import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='mario',
    password='123password',
    database='testdatabase'
    )

cur = db.cursor()



cur.execute('SELECT * FROM person')

for x in cur:
    print(x)

#db.commit()

#db.close()