from tkinter import Label
from .abstractdashboardchildview import AbstractDashboardChildView


class View(AbstractDashboardChildView):

    def launch(self):
        Label(self.root, text=str(self.parentcontroller)).pack(pady=128, padx=32)
