
from tkinter import *

import tkinter.messagebox as m


mainWindow = Tk()
mainWindow.title("tkinter")
mainWindow.geometry("400x400")

bigText = Label(text="Login and Registration",font="Verdana 20 bold")
bigText.place(x=30,y=30)

def Register():
    registerWindow = Tk()
    registerWindow.title("Register")
    registerWindow.geometry("400x400")


    bigText = Label(text="Registration",font="verdana 20 bold")
    bigText.place(x=100,y=30)

    name = Label(registerWindow,text="Name")
    name.place(x=90,y=100)
    age = Label(registerWindow, text="Age")
    age.place(x=90,y=140)
    email = Label(registerWindow, text="Email")
    email.place(x=90,y=180)
    password = Label(registerWindow, text="Password")
    password.place(x=90,y=220)

    e1 = Entry(registerWindow)
    e1.place(x=180,y=100)
    e2 = Entry(registerWindow)
    e2.place(x=180, y=140)
    e3 = Entry(registerWindow)
    e3.place(x=180, y=180)
    e4 = Entry(registerWindow)
    e4.place(x=180, y=220)

    def clearEntryBox():
        e1.delete(first=0,last=100)
        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)
        e4.delete(first=0,last=100)
    def error():
        m.showerror(title="error",message="passwords not same")

    def insert():
        insert = ("insert into register (name,age,email,password) values(%s,%s,%s,%s)")
        values = [e1.get(),e2.get(),e3.get(),e4.get()]
        if e3.get() :
            m.showinfo(title="Done",message="Account Created")
        else:
            error()
    register = Button(registerWindow,text="Register",fg="green",command=insert)
    register.place(x=175,y=260)
    btnExit = Button(registerWindow, text="Exit", bg="red", command=registerWindow.destroy)
    btnExit.place(x=350, y=350)

def Login():
    loginWindow = Tk()
    loginWindow.title("Login")
    loginWindow.geometry("400x400")



    bigText = Label(text="Login", font="verdana 20 bold")
    bigText.place(x=140, y=30)

    emai = Label(loginWindow, text="Email")
    emai.place(x=100, y=150)
    password = Label(loginWindow, text="Password")
    password.place(x=100,y=180)

    e1 = Entry(loginWindow)
    e1.place(x=160,y=150)
    e2 = Entry(loginWindow)
    e2.place(x=160,y=180)

    login = Button(loginWindow, text="Login", fg="green")
    login.place(x=160, y=200)
    btnExit = Button(loginWindow, text="Exit", bg="red", command=loginWindow.destroy)
    btnExit.place(x=350, y=350)

    mainWindow.destroy()
    loginWindow.mainloop()

goToLogin = Button(mainWindow,text="Login",fg="green",font="verdana 10 bold",command=Login)
goToLogin.place(x=120,y=200)

goToRegister = Button(mainWindow,text="Register",fg="green",font="verdana 10 bold",command=Register)
goToRegister.place(x=180,y=200)

btnExit = Button(mainWindow,text="Exit",bg="red",command=mainWindow.destroy)
btnExit.place(x=350,y=350)

mainWindow.mainloop()