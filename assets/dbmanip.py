import mysql.connector
from mysql.connector.cursor import CursorBase


class Connector:

    connection = None

    def __init__(self, host, port, db, usr, pwd=""):
        if Connector.connection is None:
            Connector.connection = mysql.connector.connect(host=host, port=port, database=db, user=usr, password=pwd)

    def submit_query(self, query, qparams='', echo=False):
        return_stmt = None
        c: CursorBase = Connector.connection.cursor(buffered=True)
        try:
            c.execute(query, qparams)
            Connector.connection.commit()  # TODO: Implement proper transaction handling
            return_stmt = c.fetchall()

        except Exception as e:
            if echo: print(f"\n\nException occurred: {e}\n\n")

        finally:
            if echo: print(f"\n\nReturn statement: {return_stmt}\n\n")
            return return_stmt

    def __del__(self):
        Connector.connection.close()
        Connector.connection = None

# Can use ".rollback()" to undo stuff
