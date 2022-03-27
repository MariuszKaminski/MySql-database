
import mysql.connector
import pymysql

db = mysql.connector.connect(
    host='127.0.0.1',
    user='mario',
    password='123password',
    database='foodbank'
    )

cur = db.cursor(pymysql.cursors.DictCursor)



cur.execute(""" CREATE TABLE items(
    itemid int AUTO_INCREMENT,
    categoryid int,
    name VARCHAR(50),    
    quantity int,
    unitid VARCHAR(5),
    PRIMARY KEY (itemid),
    FOREIGN KEY (categoryid) REFERENCES categories(categoryid),
    FOREIGN KEY (unitid) REFERENCES units(unitid)
    ) """)

db.commit()

db.close()