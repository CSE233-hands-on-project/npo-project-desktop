# Need to start application from this directory as the root of the package hierarchy
from controllers.userlogin import UserLogin
from tkinter import mainloop

UserLogin().start()
print("Main loop starting now...")
mainloop()
print("Main loop has been terminated")
