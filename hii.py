from configparser import ConfigParser
from tkinter import *
from tkinter import messagebox
import uuid
import pyrebase
import mysql.connector
import tkinter.messagebox as m
from operator import itemgetter

import requests

value=""
mainWindow = Tk()
mainWindow.title("tkinter")
mainWindow.geometry("400x400")

bigText = Label(text="Login and Registration", font="Verdana 20 bold")
bigText.place(x=30, y=30)


# def increment():
#     return value+1

dict={

}
def Register():



    registerWindow = Tk()
    registerWindow.title("Register")
    registerWindow.geometry("400x400")



    bigText = Label(text="Registration", font="verdana 20 bold")
    bigText.place(x=100, y=30)

    name = Label(registerWindow, text="Name")
    name.place(x=90, y=100)
    age = Label(registerWindow, text="Age")
    age.place(x=90, y=140)
    email = Label(registerWindow, text="Email")
    email.place(x=90, y=180)
    password = Label(registerWindow, text="Password")
    password.place(x=90, y=220)

    e1 = Entry(registerWindow)
    e1.place(x=180, y=100)
    e2 = Entry(registerWindow)
    e2.place(x=180, y=140)
    e3 = Entry(registerWindow)
    e3.place(x=180, y=180)
    e4 = Entry(registerWindow)
    e4.place(x=180, y=220)

    def clearEntryBox():
        e1.delete(first=0, last=100)
        e2.delete(first=0, last=100)
        e3.delete(first=0, last=100)
        e4.delete(first=0, last=100)

    def error():
        m.showerror(title="error", message="passwords not same")

    def insert():

        firebaseConfig = {
            "apiKey": "AIzaSyAcPvJ_aBZq5GCsYr3QPZuXabYa5y7UH2k",
            "authDomain": "weatherapp-f4c08.firebaseapp.com",
            "databaseURL": "https://weatherapp-f4c08-default-rtdb.asia-southeast1.firebasedatabase.app/",
            "projectId": "weatherapp-f4c08",
            "storageBucket": "weatherapp-f4c08.appspot.com",
            "messagingSenderId": "206893855577",
            "appId": "1:206893855577:web:e13059d667d0bbafa85248",
            "measurementId": "G-FKN03V3WRW"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()

        data = {"Name ": e1.get(), "Age ": e2.get(), "email ": e3.get(), "Passwd ": e4.get()}
        db.push(data)
        dict.get(e3)
        dict.get(e4)

        value=e1.get()
        db.child("users").child(f"User{ uuid.uuid4() }:").set(data)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        m.showinfo(title="Done", message="Account Created")
        registerWindow.destroy()

    register = Button(registerWindow, text="Register",
                      fg="green", command=insert)
    register.place(x=175, y=260)
    btnExit = Button(registerWindow, text="Exit", bg="red")
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
    password.place(x=100, y=180)

    e1 = Entry(loginWindow)
    e1.place(x=160, y=150)
    e2 = Entry(loginWindow)
    e2.place(x=160, y=180)

    def check():



        email = e1.get()
        password = e2.get()
        e = []
        p = []


        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p))
        k = len(res)
        i = 1
        while i < k:
            if res[i] == email and res2[i] == password:
                m.showinfo(title="Deo", message="Login Is Done")
                loginWindow.destroy()

                url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

                config_file = 'config.ini'
                config = ConfigParser()
                config.read(config_file)
                api_key = config['api_key']['key']

                def get_weather(city):

                    result = requests.get(url.format(city, api_key))
                    if result:

                        json = result.json()
                        city = json['name']
                        country = json['sys']['country']
                        temp_kelvin = json['main']['temp']
                        temp_centigrade = temp_kelvin - 273.15
                        temp_farhrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
                        weather = json['weather'][0]['main']
                        final = (city, country, temp_farhrenheit, temp_centigrade, weather)
                        return final
                    else:
                        return None

                def search():
                    city = city_text.get()
                    weather = get_weather(city)
                    if weather:
                        location_lbl['text'] = '{},{},{}'.format(weather[0], weather[1], weather[4])

                        temp_lbl['text'] = '{:.2f}°C,{:.2f}°F'.format(weather[3], weather[2])
                        weather_lbl['text'] = weather[4]
                    else:
                        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

                app = Tk()
                app.title = ("Weather App")
                app.geometry = ('700x350')
                frame = Frame(app, bg='light blue', height=500, width=925)

                city_text = StringVar()

                city_entry = Entry(app, textvariable=city_text, width=20, font=('bold', 20), bg='light blue')
                city_entry.pack()

                search_btn = Button(app, text="Search", width=14, command=search, font=('bold', 14), bg='grey')
                search_btn.pack()

                location_lbl = Label(app, text="", font=('bold', 20))
                location_lbl.pack()


                temp_lbl = Label(app, text="")
                temp_lbl.pack()

                weather_lbl = Label(app, text="")
                weather_lbl.pack()

                break
            i += 1
        else:
            m.showinfo(title="error", message="Some went wrong")

    login = Button(loginWindow, text="Login", fg="green", command=check)
    login.place(x=160, y=200)
    btnExit = Button(loginWindow, text="Exit", bg="red",
                     command=loginWindow.destroy)
    btnExit.place(x=350, y=350)

    mainWindow.destroy()
    loginWindow.mainloop()


goToLogin = Button(mainWindow, text="Login", fg="green",
                   font="verdana 10 bold", command=Login)
goToLogin.place(x=120, y=200)

goToRegister = Button(mainWindow, text="Register", fg="green",
                      font="verdana 10 bold", command=Register)
goToRegister.place(x=180, y=200)

btnExit = Button(mainWindow, text="Exit", bg="red", command=mainWindow.destroy)
btnExit.place(x=350, y=350)



url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']


def get_weather(city):

    result=requests.get(url.format(city,api_key))
    if result:

        json=result.json()
        city=json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_centigrade=temp_kelvin-273.15
        temp_farhrenheit=(temp_kelvin-273.15)*9/5+32
        weather=json['weather'][0]['main']
        final=(city,country,temp_farhrenheit,temp_centigrade,weather)
        return final
    else:
        return None





mainWindow.mainloop()
