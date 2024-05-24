from tkinter import *

root = Tk()
root.title("Weather App")
root.geometry("900x800")
photo=PhotoImage(file=r'C:\Users\AC\Desktop\weatherApp\weatherIcons\02d@2x.png')
photo_label=Label(image=photo)
photo_label.pack()
root.mainloop()

