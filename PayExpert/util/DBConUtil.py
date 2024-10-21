import pyodbc
class DBConUtil:
    @staticmethod
    def getConnObj(connStr):
        conn = pyodbc.connect(connStr)
        return conn