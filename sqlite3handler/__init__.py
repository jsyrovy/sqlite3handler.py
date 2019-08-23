import sqlite3


class Database:
    def __init__(self, path):
        """Class for communication with SQLite3 database

        :param path: SQLite DB file path"""
        self._path = path
        self._conn = sqlite3.connect(path)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def path(self):
        return self._path

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def close(self):
        if self.connection:
            self.commit()
            self.cursor.close()
            self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, qry):
        self.cursor.execute(qry)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, qry):
        """Returns list with query result

        :param qry: SQL query string"""
        self.execute(qry)
        return self.fetchall()

    def qry_header(self, qry):
        self.execute(qry)
        return [s[0] for s in self.cursor.description]

    def table_header(self, table):
        return self.qry_header(f"SELECT * FROM {table};")
