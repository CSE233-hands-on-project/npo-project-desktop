from models.user import User
from views.signin_panel import SigninPanel
from views import user_dashboard # TODO: make it from views.user_dashboard import UserDashboard
from controllers import guestdonate

signin_panel = None

def start():
    global signin_panel
    signin_panel = SigninPanel()
    signin_panel.launch()
    signin_panel.root.mainloop()  # To keep the window open


def attempt(username, password):

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
            signin_panel.root.destroy()

            # And launch the user's dashboard
            user_dashboard.launch(user)  # TODO: Call a fellow controller instead

        # Otherwise, if password verification fails...
        else: raise ValueError("Password is incorrect")

    # Otherwise, if user does not exist...
    else: raise ValueError("Username does not exist")

def donate():

    signin_panel.root.destroy()
    guestdonate.start()
    start() # (re)start actually, once the donate controller is done