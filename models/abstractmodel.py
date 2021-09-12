from abc import ABC, abstractmethod
from . import dbconnection


class AbstractModel(ABC):
    def __init__(self): super().__init__()

    @classmethod
    def get_all_names(callingclass): return dbconnection.submit_query(
        f'SELECT name FROM {callingclass.__module__.removeprefix("models.")}'
    )  # Gets the module name (which corresponds to the table name) and queries it for its "name" column

    @abstractmethod
    def build(self): pass
