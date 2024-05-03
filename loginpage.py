import firebase
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase import firebase
import tkinter as tk
import customtkinter
from customtkinter import CTk

# from components import singInFunc as snf
import os


os.system('cls')


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# from pages import signuptk , loginPage
root = customtkinter.CTk()
root.title("WeatherAPp")
root.geometry("280x300")
root.resizable(False, False)

# Create first page

page_one = tk.Frame(root)
page_one.grid(row=0, column=0, sticky="nsew")


# Login page
loginCTkFrame = tk.LabelFrame(
    page_one, text="Login /Signup", width=430, height=700, fg="green", bg="white")
loginCTkFrame.grid(row=0, column=1, sticky="nsew")


# signin CTkFrame
signinCTkFrame = customtkinter.CTkFrame(
    loginCTkFrame, fg_color='white', width=430, height=700)
signinCTkFrame.grid(row=0, column=0,  pady=20)


# creating singin
title = customtkinter.CTkLabel(
    signinCTkFrame, text='Login', font=('bold', 20), text_color='black')

title.grid(row=0, column=0, columnspan=2, pady=20)

name = customtkinter.CTkLabel(
    signinCTkFrame, text='Username', text_color='black')
name.grid(row=1, column=0)

name_entry = customtkinter.CTkEntry(signinCTkFrame)
name_entry.grid(row=1, column=1)


tk.Label(signinCTkFrame, text="", fg='white', bg='white').grid(row=2, column=0)
password = customtkinter.CTkLabel(
    signinCTkFrame, text='Password', text_color='black')
password.grid(row=3, column=0)

password_entry = customtkinter.CTkEntry(signinCTkFrame, show="*")
password_entry.grid(row=3, column=1)

tk.Label(signinCTkFrame, text="", fg='white', bg='white').grid(row=4, column=0)

email = customtkinter.CTkLabel(
    signinCTkFrame, text='Email', text_color='black')
email.grid(row=5, column=0)

email_entry = customtkinter.CTkEntry(signinCTkFrame)
email_entry.grid(row=5, column=1)

notify = tk.Label(signinCTkFrame, text="", fg='black', bg='white')
notify.grid(row=6, column=0)

# creating a new frame where singup and login button will be placed
buttonCTkFrame = customtkinter.CTkFrame(signinCTkFrame, fg_color='white')
buttonCTkFrame.grid(row=7, column=0, columnspan=2)


def check(name, password, id):

    doc_ref = db.collection("normal").document(id)
    doc = doc_ref.get().to_dict()
    print(f"Document data: {doc}")
    if doc != None:
        if doc["name"] == name and doc["password"] == password and doc["id"] == id:

            print("Login Successfull")
            page_one.destroy()

            notify.config(text="Login Successfull")





        else:
            print("Invalid Username/Password")
            notify.config(text="Invalid Username/Password")

    else:
        notify.config(text="Invalid Username/Password")

    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    return True



def signup(name, password, id):

    data = {
        "name": name,
        "password": password,
        "id": id
    }

    db.collection("normal").document(id).set(data)
    notify.config(text="signup successfully")
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    return True


# Buttons


button = customtkinter.CTkButton(buttonCTkFrame, text="SignIn", fg_color="teal", command=lambda: check(
    name_entry.get(), password_entry.get(), email_entry.get()))
button.grid(row=7, column=1)
button = customtkinter.CTkButton(buttonCTkFrame, text="SignUp", fg_color="teal", command=lambda: signup(
    name_entry.get(), password_entry.get(), email_entry.get()))
button.grid(row=7, column=3)


root.mainloop()
