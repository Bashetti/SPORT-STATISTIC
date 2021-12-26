import sqlite3
import typing

class WorkspaceData:

    def __init__(self):
        self.conn = sqlite3.connect('sportstatistic.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS signup1(username TEXT PRIMARY KEY,age REAL,"
                            "fname TEXT,mname TEXT,email TEXT,proat TEXT,aboutme TEXT,acheivements TEXT,password TEXT,"
                            "password1 TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS games(username TEXT,game TEXT,FOREIGN KEY(username) "
                            "REFERENCES signup1)")
        self.conn.commit()

    def add(self, table: str, data: typing.List[typing.Tuple]):
        table_data = self.cursor.execute(f"SELECT * FROM {table}")
        columns = [description[0] for description in table_data.description]
        sql_statement = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"
        self.cursor.executemany(sql_statement, data)
        self.conn.commit()

    def save(self, table: str, data: typing.List[typing.Tuple], username):
        self.cursor.execute(f"DELETE FROM {table} WHERE USERNAME = '{username}'")

        table_data = self.cursor.execute(f"SELECT * FROM {table}")
        columns = [description[0] for description in table_data.description]
        sql_statement = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"
        self.cursor.executemany(sql_statement, data)
        self.conn.commit()

    def get(self, table: str, username: str) -> typing.List[sqlite3.Row]:
        self.cursor.execute(f"SELECT * FROM {table} WHERE USERNAME='{username}'")
        data = self.cursor.fetchall()

        return data
