import mysql.connector


class Connector:

    def __init__(self, host, port, db, usr, pwd=""):
        self.connection = mysql.connector.connect(host=host, port=port, database=db, user=usr, password=pwd)

    def submit_query(self, query, echo=False):
        return_stmt = None
        c = self.connection.cursor(buffered=True)
        try:
            c.execute(query)
            self.connection.commit()  # TODO: Implement proper transaction handling
            return_stmt = c.fetchall()

        except Exception as e:
            if echo: print(f"\n\nException occurred: {e}\n\n")

        finally:
            if echo: print(f"\n\nReturn statement: {return_stmt}\n\n")
            return return_stmt

    def __del__(self):
        self.connection.close()

# Can use ".rollback()" to undo stuff
