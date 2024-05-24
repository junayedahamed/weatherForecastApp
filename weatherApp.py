import tkinter
from  tkinter import *
from tkinter import messagebox
from configparser import ConfigParser

import app
import requests




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
        condition=icon(weather)
        final=(city,country,temp_farhrenheit,temp_centigrade,weather,condition)
        return final
    else:
        return None

# add animation for different weather conditions
# def weather_icon(weather):


def icon(weather):

    if weather == 'Haze':

        photo = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\02n@2x.png')
        return photo
    elif weather == 'Cloudy':
        photo1 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\04n@2x.png')
        return photo1
    elif weather == 'Clouds':
        photo1 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\04n@2x.png')
        return photo1
    elif weather == 'Clear':
        photo2 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\01d@2x.png')
        return photo2
    elif weather == 'Drizzle':
        photo3 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\10d@2x.png')

        return photo3
    elif weather == 'Rain':
        photo3 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\09n@2x.png')

        return photo3
    elif weather == 'Snow':
        photo4 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\13d@2x.png')


        return photo4
    elif weather == 'Thunderstorm':
        photo5 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\11n@2x.png')

        return photo5
    elif weather=='Windy':
        photo6 = PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\50d@2x.png')
        return photo6
    else:
        return '🤷‍♂️'



def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location_lbl['text']='{},{},{}'.format(weather[0],weather[1],weather[4])



        temp_lbl['text']='{:.2f}°C\n,{:.2f}°F\n'.format(weather[3],weather[2])
        weather_lbl['text']=weather[4]
        weather_l=weather[5]

        pht=Label(image=weather_l)
        pht.pack()
        pht.image=weather_l







    else:
        messagebox.showerror('Error','Cannot find city {}'.format(city))

app=Tk()
app.title=("Weather App")
app.geometry=('900x800')
frame=Frame(app,bg='light blue')
frame.pack()

city_text=StringVar()
location_lbl=Label(app,text="",font=('bold',20))
location_lbl.pack()
city_entry=Entry(app,textvariable=city_text,width=20,font=('bold',20),bg='light blue')
city_entry.pack()

search_btn=Button(app,text="Search",width=14,command=search,font=('bold',14),bg='grey')
search_btn.pack()



temp_lbl=Label(app,text="",)
temp_lbl.pack()

location_lbl=Label(app,text="",font=('bold',20))


location_lbl.pack()
weather_lbl=Label(app,text="Search City in the box",height=8,font=("bold",10))
weather_l=Label()
weather_l.pack()
weather_lbl.pack()



app.mainloop()


