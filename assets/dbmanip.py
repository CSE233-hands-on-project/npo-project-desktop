import mysql.connector
import mysql.connector


class Connector:

    def __init__(self, host, port, db, usr, pwd=""):
        self.connection = mysql.connector.connect(host=host, port=port, database=db, user=usr, password=pwd)

    def submit_query(self, query):
        return_stmt = None
        c = self.connection.cursor(buffered=True)
        try:
            c.execute(query)
            self.connection.commit()  # TODO: Implement proper transaction handling
            return_stmt = c.fetchall()
        except Exception as e: return_stmt = e;  # For logging exceptions
        finally: return return_stmt

    def __del__(self):
        self.connection.close()

# TODO: replace python-mysql-connector with django's own connection module IF will use django's db stuff
# Can use ".rollback()" to undo stuff
