from . import dbconnection as db
from .abstractmodel import AbstractModel


class PaymentMethod(AbstractModel):
    def __init__(self, id):
        self.id = id
        self.build()

    def build(self):
        self.options = db.submit_query('''
                                SELECT name, type
                                FROM paymentoptions
                                WHERE id IN (
                                    SELECT optionid
                                    FROM paymentmethodoptions
                                    WHERE methodid = %s)
                                ''', (self.id,))
