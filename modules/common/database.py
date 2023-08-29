import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/home/bogdan/QA_Auto/Bohdan_Kernosenko_QA_Auto' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite3_selected_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite3_selected_Query)
        record = self.cursor.fetchall()
        print(record.format("Connected successfully. SQLite Database Version is: {record}"))