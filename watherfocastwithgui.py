from tkinter import *
import requests
import json

mainwindow=Tk()

city=Text(mainwindow,height=1,width=10)
city.place(x=130,y=50)

def gettxtinput():
    cname=city.get('1.0','end-1c')
    link ='https://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&APPID=45f1870490dbbf547b2070675e33dd9e'%(cname)
    data=requests.get(url=link).text
    data_dict=json.loads(data)
    print(data_dict)
    showdata=Label(mainwindow,text=data_dict)
    showdata.place(x=20,y=150)
    

label=Label(mainwindow,text="Enter a city name").place(x=20,y=50)



btn=Button(mainwindow,text="click me",command=gettxtinput)
btn.place(x=120,y=120)


