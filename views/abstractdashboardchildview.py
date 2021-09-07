from .abstractview import AbstractView
from tkinter import Tk


class AbstractDashboardChildView(AbstractView):
    def __init__(self, parentcontroller):
        super().__init__(parentcontroller, startwith__init__=False)

    def toggle(self):
        if self.root:
            self.root.destroy()
            self.root = None
        else:
            self.root = Tk()
            self.launch()
            # The WM_DELETE_WINDOW protocol is used to handle response to pressing "X" on the window
            self.root.protocol("WM_DELETE_WINDOW", self.parentcontroller.toggle)
