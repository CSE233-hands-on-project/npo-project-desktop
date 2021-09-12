from .abstracttoggleablecontroller import AbstractToggleableController
from views import placeholder


class ViewTeams(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class ManageTeams(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)


class CreateTeam(AbstractToggleableController):
    def __init__(self, toggler): super().__init__(toggler=toggler)
    def start(self): self.view = placeholder.View(parentcontroller=self)
