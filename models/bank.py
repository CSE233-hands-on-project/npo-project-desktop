from . import dbconnection as db
from .abstractmodel import AbstractModel


class Bank(AbstractModel):
    def __init__(self):
        self.build()

    def build(self): pass

    def get_all_bank_names():

        return db.submit_query(f'SELECT name FROM banks')
