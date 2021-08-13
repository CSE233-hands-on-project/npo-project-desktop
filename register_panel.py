from tkinter import *
from typing import List
from dbmanip import DatabaseConnector as dbc

w = 400
h = 300


def register():

    dbconnection = dbc(host="localhost", port="3306", usr="root", db="npo_proj_mock")

    form = Tk()
    form.resizable(FALSE, FALSE)
    form.title('CSE233 Project - Registration Form')
    form.geometry(f"{w}x{h}+{(form.winfo_screenwidth() - w) // 2}+{(form.winfo_screenheight() - h) // 2}")

    username_label = Label(form, text="Username:", width=10)
    username_entry = Entry(form, width=50)

    password_label = Label(form, text="Password:", width=10)
    password_entry = Entry(form, width=50, show="*")

    usertypes = dbconnection.submit_query(f'SELECT id, name FROM usertype')
    usertype_label = Label(form, text="Usertype:", width=10)
    usertype_lstbx = Listbox(form, width=50, height=len(usertypes))
    for usertype in usertypes: usertype_lstbx.insert(usertype[0], usertype[1])

    username_label.grid(row=0, column=0, pady=8); username_entry.grid(row=0, column=1, pady=8)
    password_label.grid(row=1, column=0, pady=8); password_entry.grid(row=1, column=1, pady=8)
    usertype_label.grid(row=2, column=0, pady=8); usertype_lstbx.grid(row=2, column=1, pady=8)
    request_submit_prompt = Label(form)

    def register_user():
        request_submit_prompt.config(text="Loading...", fg="blue")
        request_submit_prompt.grid(row=5, column=0, columnspan=2, pady=8)

        if not username_entry.get() or not password_entry.get() or not usertype_lstbx.curselection():
            request_submit_prompt.config(text="Please enter username, password, and select user type.", fg="red")

        else:
            dbconnection.submit_query(f'''
                                    INSERT INTO pendingregistration (fullname, usertypeid, password) VALUES (
                                    "{username_entry.get()}",
                                    {usertype_lstbx.curselection()[0]+1},
                                    "{password_entry.get()}"
                                    )''')  # user types are one-based, listbox indices are zero-based, hence the +1
            request_submit_prompt.config(text="Registration Request Submitted", fg="green")

    def switch_to_login_panel():
        from login_panel import go_login; form.destroy(); go_login()

    register_button = Button(form, text="Register", width=10, command=register_user)
    return_button = Button(form, text="Back to login page", width=20, command=switch_to_login_panel)

    register_button.grid(row=3, column=0, columnspan=2, pady=8)
    return_button.grid(row=4, column=0, columnspan=2)

    mainloop()  # infinite loop to keep window open


if __name__ == "__main__": register()