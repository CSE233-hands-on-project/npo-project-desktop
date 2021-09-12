from .abstracttoggleablecontroller import AbstractToggleableController
from views import placeholder


class AddSponsor(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)
