from tkinter import *     # whole tkinter (GUI Package) is imported directly
from PIL import ImageTk, Image

from register_panel import register
from user_dashboard import userproceed
from dbmanip import DatabaseConnector as dbc


def go_login():

    dbconnection = dbc(host="localhost", port="3306", usr="root", db="npo_proj_mock")

    def login():
        login_button.config(state="disabled")
        response_label = Label(root, text="Loading...", fg="blue")
        response_label.place(x=w // 2.5, y=h // 1.5, width=w // 5)
        record = (dbconnection.submit_query(f'SELECT * FROM user WHERE fullname = "{username_entry.get()}"'))

        if not username_entry.get() or not password_entry.get():
            response_label.config(text="Please fill the empty fields.", fg="red")
            login_button.config(state="normal")

        elif record:
            if record[0][3] == password_entry.get(): root.destroy(); userproceed(record[0][1], record[0][2])
            else: response_label.config(text="Incorrect password.", fg="red"); login_button.config(state="normal")

        else:
            response_label.config(text="User does not exist.", fg="red")
            login_button.config(state="normal")

    root = Tk()  # creates the landing page (login panel in this case) and put it into variable called root
    root.resizable(FALSE, FALSE)
    root.title('CSE233 Project - Landing Page')
    w = root.winfo_screenwidth() // 2; h = root.winfo_screenheight() // 3 * 2
    root.geometry(f"{w}x{h}+{(root.winfo_screenwidth() - w)//2}+{(root.winfo_screenheight() - h)//2}")

    # Image, title, and welcome text section
    image = Image.open("Charity.png")  # Read the Image
    resized_image = image.resize((100, 100))  # Resize the image using resize() method
    imgtk = ImageTk.PhotoImage(resized_image)  # Convert resized image to ImageTk
    img = Label(image=imgtk)  # Create label containing resized image
    title = Label(root, text="Charity Organization", fg="light green", bg="dark green", font="Helvetica 30 bold italic")
    descr = Label(root, text="Welcome to our charity, please sign in with your email and password.", font="Times 16")
    img.place(x=w // 1.45, y=h // 20)  # Place image on window
    title.place(x=w // 5, y=h // 12.5)  # Place title before it
    descr.place(x=w // 5, y=h // 5)  # Place description below them
    # End image, title, and welcome text section

    # Login form section
    username_label = Label(root, text="Username:", font="Calibri 12"); username_entry = Entry(root)
    password_label = Label(root, text="Password:", font="Calibri 12"); password_entry = Entry(root, show="*")
    login_button = Button(root, text="Sign in", command=login)
    username_label.place(x=w // 3, y=h // 2.5); username_entry.place(x=w // 2.3, y=h // 2.5, width=w // 4)
    password_label.place(x=w // 3, y=h // 2); password_entry.place(x=w // 2.3, y=h // 2, width=w // 4)
    login_button.place(x=w // 2.5, y=h // 1.75, width=w // 5)
    # End login form section

    # Registeration alternative section
    def switch_to_register_panel():
        root.destroy(); register()

    reg_label = Label(root, text="Do not have an account? Register by clicking the Register button.")
    reg_button = Button(root, text="Register", command=switch_to_register_panel)
    reg_label.place(x=w // 4, y=h // 1.2, width=w // 2)
    reg_button.place(x=w // 4, y=h // 1.1, width=w // 2)
    # End registeration alternative section

    mainloop()  # infinite loop to keep window open


if __name__ == "__main__": go_login()
