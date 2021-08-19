from . import dbconnection


class User:
    def __init__(self, username, password):

        record = (dbconnection.submit_query(f'SELECT * FROM users WHERE username = "{username}"'))

        if record:  # If there is a user record that has the provided username

            if record[0][3] == password:  # And if this user's password matches the provided password (3rd column)
                self.uid, self.fullname, self.usertypeid, self.password, self.username = record[0]
                self.usertype = dbconnection.submit_query(f'''
                                                          SELECT name FROM usertypes WHERE id = {self.usertypeid}
                                                          ''')[0][0]

                self.accessibleviews = dbconnection.submit_query(f'''
                                        SELECT *
                                        FROM views
                                        WHERE id IN (SELECT view_id
                                                     FROM viewmappings
                                                     WHERE usertype_id = {self.usertypeid})
                                        ''')
            else: raise ValueError("Password is incorrect")
        else: raise ValueError("Username does not exist")
