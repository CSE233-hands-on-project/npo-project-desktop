from . import dbconnection as db
from models.abstractmodel import AbstractModel


class Donor(AbstractModel):
    def __init__(self, uid):

        # Basic initialization with unique donor id
        self.uid = uid

    def exists(self):

        # Check if this donor object exists by checking if its uid exists in the database
        return db.submit_query(f'SELECT EXISTS(SELECT * FROM donors WHERE uid = "{self.uid}")')[0][0]

    def build(self):
        return super().build()