from . import dbconnection as db
from .usertypes import UserType
from .abstractmodel import AbstractModel
import hashlib  # For password hashing
import base64  # For encoding/decoding bytes


class User(AbstractModel):
    def __init__(self, username):

        # Basic initialzation: User with provided username
        self.username = username

    def exists(self):

        # Check if this user object exists by checking if its username exists in the database
        return db.submit_query('SELECT EXISTS(SELECT * FROM users WHERE username = %s)', (self.username, ))[0][0]

    def verify(self, password):

        # Fetch the salt used for hashing this user's password from the database
        salt = db.submit_query('SELECT salt FROM users WHERE username = %s', (self.username, ))[0][0]

        # Convert it into bytes
        saltbytes = base64.b64decode(salt.encode('utf-8'))

        # Then use it to hash the provided password
        passwordhashbytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), saltbytes, 1000000)

        # Then encode it in UTF-8 for comparison with that in database
        passwordhash = base64.b64encode(passwordhashbytes).decode('utf-8')

        # Return whether the resulting password hash matches the stored one or not
        return passwordhash == db.submit_query('SELECT pass FROM users WHERE username = %s', (self.username,))[0][0]

    def build(self):

        self.fullname = db.submit_query('SELECT fullname FROM users WHERE username = %s', (self.username,))[0][0]
        self.type = UserType(
            db.submit_query('SELECT usertypeid FROM users WHERE username = %s', (self.username,))[0][0]
        )
        # self.attributes = []
        # for option in self.type.options:  # TODO: create user attributes (create a sub-class Attribute???) from values
        #     self.attributes.append(
        #         db.submit_query(f'SELECT ')
        #     )
