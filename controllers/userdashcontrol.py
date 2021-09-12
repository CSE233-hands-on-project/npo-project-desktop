from models.users import User
from views.user_dashboard import UserDashboard
from .abstractcontroller import AbstractController


class UserDashboardController(AbstractController):
    def __init__(self, user: User):
        super().__init__()
        self.user = user

    def start(self):
        self.view = UserDashboard(self.user, self)
        self.view.launch()
        print(f"{self.user.fullname}'s dashboard has been launched")
        self.view.root.mainloop()
        print(f"{self.user.fullname}'s dashboard has been destroyed")
