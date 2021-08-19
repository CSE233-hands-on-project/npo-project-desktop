from tkinter import *     # whole tkinter (GUI Package) is imported directly
from PIL import ImageTk, Image

from models.user import User
from views import user_dashboard


def launch():

    root = Tk()  # creates the landing page (login panel in this case) and put it into variable called root
    root.title('CSE233 Project - Landing Page')

    # Image, title, and welcome text section
    image = Image.open("./assets/Charity.png")  # Read the Image
    resized_image = image.resize((100, 100))  # Resize the image using resize() method
    imgtk = ImageTk.PhotoImage(resized_image)  # Convert resized image to ImageTk
    img = Label(image=imgtk)  # Create label containing resized image
    title = Label(root, text="Charity Organization", fg="light green", bg="dark green", font="Helvetica 24 bold italic")
    descr1 = Label(root, text="Welcome to your organization management portal", font="Times 16")
    descr2 = Label(root, text="Please enter your username and password below", font="Calibri 12")

    title.grid(row=0, column=0, padx=40, pady=10, columnspan=2)  # Place title
    img.grid(row=0, column=2, padx=40, pady=10)  # Place image
    descr1.grid(row=1, column=0, pady=[20, 0], columnspan=3)  # Place description below them
    descr2.grid(row=2, column=0, pady=[0, 20], columnspan=3)  # Place description below them
    # End image, title, and welcome text section

    # Login form section
    def signin():
        sign_in_button.config(state="disabled")
        response_label.config(text="Loading...", fg="blue")

        if not username_entry.get() or not password_entry.get():
            response_label.config(text="Please fill the empty fields.", fg="red")
            sign_in_button.config(state="normal")

        else:
            try:
                user = User(username=username_entry.get(), password=password_entry.get())
                root.destroy(); user_dashboard.launch(user)
            except ValueError as e:
                response_label.config(text=str(e), fg="red")
                sign_in_button.config(state="normal")

    username_label = Label(root, text="Username:", font="Calibri 12")
    username_entry = Entry(root, width=70); username_entry.focus()
    password_label = Label(root, text="Password:", font="Calibri 12")
    password_entry = Entry(root, width=70, show="*")
    sign_in_button = Button(root, width=40, text="Sign in", font="Calibri 12", command=signin)
    response_label = Label(root, text="")

    username_label.grid(row=3, column=0, pady=5)
    username_entry.grid(row=3, column=1, padx=[0, 40], columnspan=2, sticky=E + W)
    password_label.grid(row=4, column=0, pady=5)
    password_entry.grid(row=4, column=1, padx=[0, 40], columnspan=2, sticky=E + W)
    sign_in_button.grid(row=5, column=0, pady=[20, 5], columnspan=3)
    response_label.grid(row=6, column=0, pady=[5, 20], columnspan=3)
    # End login form section

    root.bind("<Return>", lambda event: signin())
    root.eval('tk::PlaceWindow . center')  # Center the window
    root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())
    root.maxsize(root.winfo_reqwidth() * 2, root.winfo_reqheight() * 2)
    for i in range(root.grid_size()[1]): root.rowconfigure(i, weight=1)  # Make rows span full width
    for i in range(root.grid_size()[0]): root.columnconfigure(i, weight=1)  # Make columns span full height

    mainloop()  # infinite loop to keep window open
