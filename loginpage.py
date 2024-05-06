import firebase
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from tkinter import *
import tkinter as tk
import customtkinter


# from components import singInFunc as snf
import os



os.system('cls')


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# from pages import signuptk , loginPage
root = customtkinter.CTk()
root.title("WeatherAPP")
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

            # print("Login Successfull")
            page_one.destroy()





        else:
            print("Invalid Username/Password")
            notify.config(text="Invalid Username/Password")

    else:
        notify.config(text="Invalid Username/Password")

    # name_entry.delete(0, tk.END)
    # password_entry.delete(0, tk.END)
    # email_entry.delete(0, tk.END)

    #
    # from tkinter import messagebox
    # from configparser import ConfigParser
    #
    # import app
    # import requests
    # #
    # url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    #
    # config_file = 'config.ini'
    # config = ConfigParser()
    # config.read(config_file)
    # api_key = config['api_key']['key']
    #
    # def get_weather(city):
    #
    #     result = requests.get(url.format(city, api_key))
    #     if result:
    #
    #         json = result.json()
    #         city = json['name']
    #         country = json['sys']['country']
    #         temp_kelvin = json['main']['temp']
    #         temp_centigrade = temp_kelvin - 273.15
    #         temp_farhrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
    #         weather = json['weather'][0]['main']
    #         final = (city, country, temp_farhrenheit, temp_centigrade, weather)
    #         return final
    #     else:
    #         return None
    #
    # def search():
    #     city = city_text.get()
    #     weather = get_weather(city)
    #     if weather:
    #         location_lbl['text'] = '{},{},{}'.format(weather[0], weather[1], weather[4])
    #
    #         temp_lbl['text'] = '{:.2f}°C\n,{:.2f}°F\n'.format(weather[3], weather[2])
    #         weather_lbl['text'] = weather[4]
    #     else:
    #         messagebox.showerror('Error', 'Cannot find city {}'.format(city))
    #
    # app = Tk()
    # app.title = ("Weather App")
    # app.geometry = ('900x800')
    # frame = Frame(app, bg='light blue', height=850, width=925)
    #
    # city_text = StringVar()
    # location_lbl = Label(app, text="", font=('bold', 20))
    # location_lbl.pack()
    # city_entry = Entry(app, textvariable=city_text, width=20, font=('bold', 20), bg='light blue')
    # city_entry.pack()
    #
    # search_btn = Button(app, text="Search", width=14, command=search, font=('bold', 14), bg='grey')
    # search_btn.pack()
    #
    # #
    # # img=PhotoImage(file='')
    # # Image = Label(app, image = img)
    # # img.place(x=20,y=20)
    # #
    # # Image.pack()
    #
    # temp_lbl = Label(app, text="", )
    # temp_lbl.pack()
    #
    # location_lbl = Label(app, text="", font=('bold', 20))
    #
    # location_lbl.pack()
    # weather_lbl = Label(app, text="Search City in the box", height=8, font=("bold", 10))
    # weather_lbl.pack()
    #
    # app.mainloop()

    return True



def signup(name, password, id):

    data = {
        "name": name,
        "password": password,
        "id": id
    }

    db.collection("normal").document(id).set(data)
    notify.config(text="signup successfully")


    return True


# Buttons


button = customtkinter.CTkButton(buttonCTkFrame, text="SignIn", fg_color="teal", command=lambda: check(
    name_entry.get(), password_entry.get(), email_entry.get()))
button.grid(row=7, column=1)
button = customtkinter.CTkButton(buttonCTkFrame, text="SignUp", fg_color="teal", command=lambda: signup(
    name_entry.get(), password_entry.get(), email_entry.get()))
button.grid(row=7, column=3)


root.mainloop()

