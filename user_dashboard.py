from tkinter import *
from dbmanip import DatabaseConnector as dbc


def userproceed(fullname, usertypeid):

    dbconnection = dbc(host="localhost", port="3306", usr="root", db="npo_proj_mock")

    fn = fullname
    ut = dbconnection.submit_query(f'SELECT name FROM usertype WHERE id = {usertypeid}')[0][0]
    modules = dbconnection.submit_query(f'''
                                        SELECT displayname, pathnamecode
                                        FROM module
                                        WHERE id IN (SELECT module_id
                                                     FROM accessrule
                                                     WHERE usertype_id = {usertypeid})
                                        ''')

    dashboard = Tk()
    dashboard.resizable(FALSE, FALSE)
    dashboard.title('CSE233 Project - User Dashboard')
    welcome_label = Label(dashboard, text=f'Welcome, {ut}...', width=65); welcome_label.pack(pady=4)
    name_label = Label(dashboard, text=fn, font="Times 12 bold italic"); name_label.pack()
    msg_label = Label(dashboard, text="Please pick a module..."); msg_label.pack(pady=32)

    for module in modules:
        Button(dashboard, text=module[0], width=32, relief="groove",
               command=lambda filename=module[1]: exec(open(f'modules/{filename}.py').read())).pack(pady=4)

    def switch_to_login_panel():
        from login_panel import go_login; dashboard.destroy(); go_login()

    return_button = Button(dashboard, text="Back to login page", width=20, command=switch_to_login_panel)
    return_button.pack(pady=32)

    mainloop()  # infinite loop to keep window open


if __name__ == "__main__": userproceed("Dummy Student", 1)
