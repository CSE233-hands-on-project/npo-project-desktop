from logging import exception
from models.donor import Donor
from models.eventtype import EventType
from models.paymentmethod import PaymentMethod
from models.__init__ import dbconnection as db
from views.donation_panel import DonationPanel

donation_panel = None


def start():
    global donation_panel
    donation_panel = DonationPanel()
    donation_panel.launch()
    donation_panel.root.mainloop()  # To keep the window open


def yes_btn_pressed():
    donation_panel.yes_btn.configure(bg="#d8ffd8", state="disabled", relief="sunken")
    donation_panel.no_btn.configure(bg="white", state="normal", relief="raised")
    donation_panel.hide_no_response()
    donation_panel.show_yes_response()


def no_btn_pressed():
    donation_panel.no_btn.configure(bg="#ffd8d8", state="disabled", relief="sunken")
    donation_panel.yes_btn.configure(bg="white", state="normal", relief="raised")
    donation_panel.hide_yes_response()
    donation_panel.show_no_response()


def existing_donor_attempt_enter():
    if not donation_panel.yes_entry.get():
        donation_panel.yes_label.configure(fg="red", text="Please enter your donation profile ID")
    else:
        donor = Donor(donation_panel.yes_entry.get())
        if donor.exists():
            donation_panel.hide_entry()
            donation_panel.show_donation_menu(EventType.get_all_event_type_names(),
                                              PaymentMethod.get_all_pm_names())
        else:
            donation_panel.yes_label.configure(fg="red", text="The ID you've entered doesn't exist")


def setdonationtypechoice():
    if donation_panel.donationchoice.get() == 1:
        donation_panel.dm_money_lstbx.configure(state="normal")
        donation_panel.dm_items_lstbx.selection_clear(0, "end")
        donation_panel.dm_items_lstbx.configure(state="disabled")
    elif donation_panel.donationchoice.get() == 2:
        donation_panel.dm_items_lstbx.configure(state="normal")
        donation_panel.dm_money_lstbx.selection_clear(0, "end")
        donation_panel.dm_money_lstbx.configure(state="disabled")
    else:
        donation_panel.dm_items_lstbx.selection_clear(0, "end")
        donation_panel.dm_money_lstbx.selection_clear(0, "end")
        donation_panel.dm_items_lstbx.configure(state="disabled")
        donation_panel.dm_money_lstbx.configure(state="disabled")


def pay():
    paymentmethodid = donation_panel.dm_money_lstbx.curselection()[0] + 1
    paymentmethod = PaymentMethod()
    paymentmethoddetails = paymentmethod.build(paymentmethodid)
    donation_panel.hide_donation_menu()
    donation_panel.show_payment_menu(paymentmethoddetails)


def get_all_names_of(arg):
    return db.submit_query(f"SELECT name FROM {arg}")


def succeed(fields, paymentmethoddetails):

    import re

    values = []

    for i in range(len(paymentmethoddetails)):

        if paymentmethoddetails[i][1] == "String" and re.fullmatch("[a-zA-Z ]+", fields[i].get()):
            values.append(fields[i].get())

        elif paymentmethoddetails[i][1] == "Number" and re.fullmatch("[0-9]+", fields[i].get()):
            values.append(int(fields[i].get()))

        elif paymentmethoddetails[i][1] == "MonthYear" and re.fullmatch("[0-3][0-9]\/[0-9][0-9]", fields[i].get()):
            values.append(fields[i].get())

        elif "Listbox" in paymentmethoddetails[i][1] and fields[i].curselection():
            values.append(fields[i].curselection()[0])

        else: break

    else: print(values)  # TODO: Insert values into db instead of printing values (simple)
