from tkinter import *     # whole tkinter (GUI Package) is imported directly
from PIL import ImageTk,Image

def login():
    label6=Label(main,text="Login Session Started",fg="green")
    label6.place(x=500,y=500)

def register():
    global screen1
    screen1=Toplevel(main)
    screen1.title("Registration")
    screen1.geometry("400x200")

    global Email
    global password
    global Address
    global Email_entry
    global password_entry
    global Address_entry
    Email=StringVar()
    password=StringVar()
    Address=StringVar()

    label7=Label(screen1,text="E-mail:")
    label7.pack()

    Email_entry=Entry(screen1,textvariable=Email)
    Email_entry.pack()

    label8=Label(screen1, text="password:")
    label8.pack()

    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()

    label9=Label(screen1, text="Address:")
    label9.pack()

    Address_entry=Entry(screen1,textvariable=Address)
    Address_entry.pack()

    button2=Button(screen1,text="Register",width=10,height=1,command=register_user)
    button2.pack()


def register_user():
    Email_info=Email.get()
    password_info=password.get()
    Address_info=Address.get()

    label10=Label(screen1,text="Successfull Registration",fg="green")
    label10.pack()




main=Tk() # creates the window and put it into variable called main
main.geometry("900x700")
main.title('CSE233 Project')


# Read the Image
image = Image.open("Charity.png")
# Reszie the image using resize() method
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label0 = Label(image=img)
label0.image = img
label0.place(x=630, y=17)

label1=Label(main,text="Charity Organization",fg="light green",bg="dark green",font="Helvetica 30 bold italic")
label1.place(x=200, y=40)

label2=Label(main,text="Welcome to our charity, Please sign in with your E-mail and password.",font="Times 16")
label2.place(x=167, y=170)

label3=Label(main,text="E-mail:",font="Calibri 12")
label3.place(x=270, y=300)

entry0=Entry(main)
entry0.place(x=390, y=302)

label4=Label(main,text="Password:",font="Calibri 12")
label4.place(x=270, y=400)

entry1=Entry(main)
entry1.place(x=390, y=402)

button0=Button(main, text="Sign in", relief='solid',command=login)
button0.place(x=425, y=500)

label5=Label(main,text="Do not have an account? Register by clicking the Register button.")
label5.place(x=270, y=570)

button1=Button(main, text="Register", relief='solid',command=register)
button1.place(x=420, y=640)




main.mainloop()          #loops again and again in order for the window to be still open