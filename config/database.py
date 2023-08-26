import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='myapp'
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def execute_update(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()