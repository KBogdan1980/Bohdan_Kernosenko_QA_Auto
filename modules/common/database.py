import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/home/bohdan/Bohdan_Kernosenko_QA_Auto' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite3_selected_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite3_selected_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
        #print(record.format("Connected successfully. SQLite Database Version is: {record}"))
        #https://youtu.be/6HLK7kiSukA

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record