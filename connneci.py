import mysql.connector

class cnnc:
    host="localhost"
    user="user"
    password="password"
    database="Agency"

    def __init__(self):
        self.db= mysql.connector.connect(
            host='localhost',
            user='root',
            password='tiger',
            database='Agency'
        )

    def insert(self):
        str = ""
        cur = self.db.cursor()
        cur.execute(str)
        cur.close()
