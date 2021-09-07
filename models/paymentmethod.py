from . import dbconnection as db
from .abstractmodel import AbstractModel


class PaymentMethod(AbstractModel):
    def __init__(self, id):
        self.id = id
        self.build()

    def build(self):
        self.options = db.submit_query(f'''
                                SELECT name, type
                                FROM paymentoptions
                                WHERE id IN (
                                    SELECT optionid
                                    FROM paymentmethodoptions
                                    WHERE methodid = {self.id})
                                ''')

    def get_all_pm_names():

        return db.submit_query(f'SELECT name FROM paymentmethods')
