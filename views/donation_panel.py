from tkinter import *  # TODO: replace * with only the used stuff

from .abstractview import AbstractView
from controllers import guestdonate


class DonationPanel(AbstractView):

    def launch(self):
        self.root.title('CSE233 Project - Donation Panel')
        self.root.resizable(False, False)

        self.show_entry()

        self.root.eval('tk::PlaceWindow . center')

    def show_entry(self):
        self.desc1 = Label(self.root, text="Thank you for wanting to donate!", font="Times 16")
        self.desc2 = Label(self.root, text="Have you donated before?", font="Calibri 12")

        self.choices_frame = Frame(self.root)
        self.yes_btn = Button(self.choices_frame, text="Yes", padx=32, pady=8,
                              bg="white", command=guestdonate.yes_btn_pressed)
        self.no_btn = Button(self.choices_frame, text="No", padx=32, pady=8,
                             bg="white", command=guestdonate.no_btn_pressed)
        self.yes_btn.grid(row=0, column=0, padx=2)
        self.no_btn.grid(row=0, column=1, padx=2)

        self.yes_frame = Frame(self.root)
        self.yes_label = Label(self.yes_frame, text="Please enter your donation profile ID")
        self.yes_entry = Entry(self.yes_frame)
        self.yes_submit = Button(self.yes_frame, text="Proceed", borderwidth=1, relief="groove", padx=16, pady=4,
                                 command=guestdonate.existing_donor_attempt_enter)
        self.yes_label.grid(row=0, column=0, columnspan=3)
        self.yes_entry.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.yes_submit.grid(row=1, column=2)

        self.no_frame = Frame(self.root)
        self.no_label = Label(self.no_frame, text="Please create a donation profile")
        self.no_submit = Button(self.no_frame, text="Proceed (WIP)", bg="white", borderwidth=1, padx=16, pady=4,
                                state="disabled")  # TODO: Implement donor profile creation
        self.no_label.grid(row=0, column=0, columnspan=3)
        self.no_submit.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.desc1.grid(row=self.r(), pady=[40, 0], padx=40)
        self.desc2.grid(row=self.r(), pady=[0, 20])
        self.choices_frame.grid(row=self.r(), pady=[0, 20])

    def hide_entry(self):
        self.desc1.grid_forget()
        self.desc2.grid_forget()
        self.choices_frame.grid_forget()
        self.yes_frame.grid_forget()
        self.no_frame.grid_forget()
        self.root.unbind("<Return>")

    def show_yes_response(self):
        self.yes_frame.grid(row=self.r(), pady=[0, 20], padx=50)
        self.yes_entry.focus()
        self.root.bind("<Return>", lambda event: guestdonate.existing_donor_attempt_enter())

    def hide_yes_response(self):
        self.yes_frame.grid_forget()

    def show_no_response(self):
        self.no_frame.grid(row=self.r(), pady=[10, 20], padx=50)
        self.no_submit.focus()
        self.root.bind("<Return>", lambda event: print("."))

    def hide_no_response(self):
        self.no_frame.grid_forget()

    def show_donation_profile_creator(self):
        pass

    def show_donation_menu(self, eventtypenames, pmnames):
        self.dm_event_label = Label(text="Choose an event to donate for:")
        self.dm_event_lstbx = Listbox(selectmode="single", height=len(eventtypenames), exportselection=0)
        for n in eventtypenames: self.dm_event_lstbx.insert("end", n[0])

        self.donationchoice = IntVar()
        self.donationchoice.set(3)

        self.dm_money_rdbtn = Radiobutton(text="Donate with money:", variable=self.donationchoice, value=1,
                                          command=guestdonate.setdonationtypechoice)

        self.dm_money_lstbx = Listbox(selectmode="single", height=len(pmnames), exportselection=0)
        for n in pmnames: self.dm_money_lstbx.insert("end", n[0])
        self.dm_money_lstbx.configure(state="disabled")

        self.dm_items_rdbtn = Radiobutton(text="Donate with items:", variable=self.donationchoice, value=2,
                                          command=guestdonate.setdonationtypechoice)

        self.dm_items_lstbx = Listbox(selectmode="single", height=3, exportselection=0)
        for n in ("item1", "item2", "item3"): self.dm_items_lstbx.insert("end", n)
        self.dm_items_lstbx.configure(state="disabled")

        self.go_btn = Button(text="Go", bg="white", command=guestdonate.pay)

        self.dm_event_label.grid(row=self.r(), column=0, columnspan=3, pady=[20, 0])
        self.dm_event_lstbx.grid(row=self.r(), column=1, pady=[8, 32], padx=32)
        self.dm_money_rdbtn.grid(row=self.r(), column=0)
        self.dm_items_rdbtn.grid(row=self.r() - 1, column=2)
        self.dm_money_lstbx.grid(row=self.r(), column=0, pady=[8, 32], padx=32)
        self.dm_items_lstbx.grid(row=self.r() - 1, column=2, pady=[8, 32], padx=32)
        self.go_btn.grid(row=self.r() - 1, column=1, sticky="nsew", pady=[0, 20])

        self.root.eval('tk::PlaceWindow . center')

    def hide_donation_menu(self):
        self.dm_event_label.grid_forget()
        self.dm_event_lstbx.grid_forget()
        self.dm_money_rdbtn.grid_forget()
        self.dm_items_rdbtn.grid_forget()
        self.dm_money_lstbx.grid_forget()
        self.dm_items_lstbx.grid_forget()
        self.go_btn.grid_forget()

    def show_payment_menu(self, paymentmethoddetails):

        formfields = []

        for d in paymentmethoddetails:

            Label(text=d[0], width=64).pack(padx=16, pady=[16, 0])
            if d[1] == "String" or d[1] == "Number" or d[1] == "MonthYear":
                e = Entry(width=32); e.pack(); formfields.append(e)

            elif "Listbox" in d[1]:
                listitems = guestdonate.get_all_names_of(d[1][d[1].find(":") + 1:])
                l = Listbox(height=len(listitems), width=32, exportselection=0)
                for i in listitems: l.insert("end", i[0])
                l.pack(); formfields.append(l)

        Button(text="Submit", pady=8, padx=16, command=lambda:
               guestdonate.succeed(formfields, paymentmethoddetails)
               ).pack(pady=[32, 16])

        self.root.eval('tk::PlaceWindow . center')
