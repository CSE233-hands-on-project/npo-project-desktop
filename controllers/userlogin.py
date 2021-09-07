from models.user import User
from views.signin_panel import SigninPanel
from .abstractcontroller import AbstractController
from .userdashcontrol import UserDashboardController


class UserLogin(AbstractController):

    def start(self):
        self.view = SigninPanel(self)
        self.view.launch()
        print("Sign-in panel has been launched")

    def attemptlogin(self, username, password):

        # Ensure that both fields are filled
        if not (username and password): raise ValueError("Please fill the empty fields.")

        # Create a basic user object with only the username
        user = User(username)

        # Check if a user with that username actually exists
        if user.exists():

            # If so, verify the input password
            if user.verify(password):

                # If valid, build it
                user.build()

                # Then destroy sign in panel
                self.view.root.destroy()
                print("Sign-in panel has been destroyed")

                # And launch the user's dashboard by starting its controller
                UserDashboardController(user).start()

                # When its controller is done, re-start
                self.start()

            # Otherwise, if password verification fails...
            else: raise ValueError("Password is incorrect")

        # Otherwise, if user does not exist...
        else: raise ValueError("Username does not exist")

    # def register():

    #     # Destroy sign in panel
    #     signin_panel.root.destroy()
    #     print("Sign-in panel has been destroyed")

    #     # Launch the donation panel by starting its controller
    #     userregister.start()

    #     # When done its controller is done, re-start
    #     start()
