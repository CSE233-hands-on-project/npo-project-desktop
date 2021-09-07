from . import dbconnection as db
from .abstractmodel import AbstractModel


class EventType(AbstractModel):
    def __init__(self): 
        self.build()

    def build(self): pass

    def get_all_event_type_names():

        return db.submit_query(f'SELECT name FROM eventtypes')
