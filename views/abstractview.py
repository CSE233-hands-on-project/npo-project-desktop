from abc import ABC, abstractmethod
from tkinter import Tk


class AbstractView(ABC):
    def __init__(self):
        # First, create the basic window to be created for any view
        # This basic window will be the "root" of control for the view
        self.root = Tk()
        super().__init__()

    @abstractmethod
    def launch(self): pass

    # The following functions return the number of columns and rows in the grid of this window respectively
    # They can be used to dynamically add rows or columns to the window
    # To add an item to a new row, use row=r(), since r() will return the number of rows
    # ---- For example if you have 3 rows already, r() returns 3, so row=3 means row #4 (0-based indexing)
    # To add an item to the previous row, use row=r() - 1
    # Likewise for columns
    def c(self): return self.root.grid_size()[0]
    def r(self): return self.root.grid_size()[1]
