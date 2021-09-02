from . import dbconnection as db
from models.abstractmodel import AbstractModel


class PaymentMethod(AbstractModel):
    def __init__(self): pass

    def build(self, id):

        return db.submit_query(f'''
                                SELECT name, type
                                FROM paymentoptions
                                WHERE id IN (
                                    SELECT optionid
                                    FROM paymentmethodoptions
                                    WHERE methodid = {id})
                                ''')

    def get_all_pm_names():

        return db.submit_query(f'SELECT name FROM paymentmethods')
