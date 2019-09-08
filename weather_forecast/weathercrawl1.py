#!/usr/bin/env python
from bs4 import BeautifulSoup              
import requests                            
from datetime import date
import pandas as pd

url = 'https://weather.com/en-IN/'
api_key="d522aa97197fd864d36b418f39ebb323"   #obtained from the source code itself.
date_def= date.today()                       #default date
choice_def="today"                           #default type of forecast

place=input("Enter place in details ie place:")         
date=input("Enter date in yyyy-mm-dd :")
print("Enter type of forecast you want :")                     
print("1.Today")
print("2.Hourly")
print("2.5-day")
print("3.10-day")
print("4.Weekend")
choice=input("Enter the type of weather forecasting : ")                                     

if date=="":
    date=date_def
if choice=="":
    choice=choice_def
if choice=="Today" or choice=="today":
    choice_enter=choice
elif choice=="Hourly" or choice=="hourly":
    choice_entered=choice
elif choice=="5-day" or choice=="5 day":
    choice_entered=choice
elif choice=="10-day" or choice=="10 day":
    choice_entered=choice
elif choice=="Weekend" or choice=="weekend":
    choice_entered=choice
elif choice=="Monthly" or choice=="monthly":
    choice_entered=choice

#obtaining the coordinates of the place
rr= requests.get("https://api.weather.com/v3/location/search?query="+ str(place)+"&locationType=city&language=en-IN&format=json&apiKey="+api_key)
info_place=rr.json()


def today(info):
    print("The current weather of " + str(info_place["location"]["address"][0]) + " is :-")
    print("  Co-ordinate - latitude :" + str(info_place["location"]["latitude"][0])+ " longitude :" + str(info_place["location"]["longitude"][0]))
    print("  Temperature :" + str(info["vt1observation"]["temperature"])+" deg C " +str(info["vt1observation"]["phrase"])+ " as of "+str(info["vt1observation"]["observationTime"]))
    print("  Feels like "+str(info["vt1observation"]["feelsLike"]) + " deg C" )
    print("  Dew point :"+str(info["vt1observation"]["dewPoint"])+ " deg")
    print("  Humidity :" +str(info["vt1observation"]["humidity"])+" %")
    print("  UV Index " +str(info["vt1observation"]["uvIndex"]) +" out of 10 which is "+str(info["vt1observation"]["uvDescription"]))
    print("  Wind :"+ str(info["vt1observation"]["windDirCompass"])+" " + str(info["vt1observation"]["windSpeed"])+ " km/hr")
    print("  Visibility :"+str(info["vt1observation"]["visibility"])+ " km")
    print("  Pressure: "+str(info["vt1observation"]["altimeter"])+"mb "+ str(info["vt1observation"]["barometerTrend"]))


def day5(info):
        print("Co-ordinate - latitude :" + str(info_place["location"]["latitude"][0])+ " longitude :" + str(info_place["location"]["longitude"][0]))
        print("Weather of "+str(info_place["location"]["address"][0])+" for the next 5 days are :-")
        for i in range(0,5):
            print(str(i+1)+"- "+info["vt1dailyForecast"]["dayOfWeek"][i])
            print("   Description : Day- "+str(info["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(info["vt1dailyForecast"]["night"]["phrase"][i]))
            print("   Temperature : Max- "+str(info["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(info["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
            print("   Precipitation : Day- "+str(info["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(info["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(info["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(info["vt1dailyForecast"]["day"]["precipType"][i]))
            print("   Wind : Day- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
            print("   Humidity : Day- "+str(info["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(info["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
            print("   UV Index : Day- "+str(info["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(info["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
            print("   Sunrise : "+str(info["vt1dailyForecast"]["sunrise"][i]))
            print("   SunSet : "+str(info["vt1dailyForecast"]["sunset"][i]))
            print("   Moon Phase : "+str(info["vt1dailyForecast"]["moonPhrase"][i]))
            print("   Moonrise : "+str(info["vt1dailyForecast"]["moonrise"][i]))
            print("   MoonSet : "+str(info["vt1dailyForecast"]["moonset"][i]))
            print(" ")
    
def day10(info):
        print("Co-ordinate - latitude :" + str(info_place["location"]["latitude"][0])+ " longitude :" + str(info_place["location"]["longitude"][0]))
        print("Weather of "+str(info_place["location"]["address"][0])+" for the next 10 days are :-")
        for i in range(0,10):
            print(str(i+1)+"- "+info["vt1dailyForecast"]["dayOfWeek"][i])
            print("   Description : Day- "+str(info["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(info["vt1dailyForecast"]["night"]["phrase"][i]))
            print("   Temperature : Max- "+str(info["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(info["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
            print("   Precipitation : Day- "+str(info["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(info["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(info["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(info["vt1dailyForecast"]["day"]["precipType"][i]))
            print("   Wind : Day- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
            print("   Humidity : Day- "+str(info["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(info["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
            print("   UV Index : Day- "+str(info["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(info["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
            print("   Sunrise : "+str(info["vt1dailyForecast"]["sunrise"][i]))
            print("   SunSet : "+str(info["vt1dailyForecast"]["sunset"][i]))
            print("   Moon Phase : "+str(info["vt1dailyForecast"]["moonPhrase"][i]))
            print("   Moonrise : "+str(info["vt1dailyForecast"]["moonrise"][i]))
            print("   MoonSet : "+str(info["vt1dailyForecast"]["moonset"][i]))
            print(" ")

def hourbyhour(info):
       
       url="https://weather.com/en-IN/weather/hourbyhour/l/"+str(info_place["location"]["placeId"][0])
       rr=requests.get(url)
       soup=BeautifulSoup(rr.text,'html.parser')
       table=soup.find('table',classname="twc-table")
       table_rows=table.find_all('tr')
       h=['']
       l =[]
       for th in soup.find_all('th'):
           h.append(th.text)
       for tr in table_rows:
               td = tr.find_all('td')
               row = [tr.text for tr in td]
               l.append(row)
       l.remove([])
       df=pd.DataFrame(data=l,columns=h)
       print(df)   

def weekend(info):
    
       print("Co-ordinate - latitude :" + str(info_place["location"]["latitude"][0])+ " longitude :" + str(info_place["location"]["longitude"][0]))
       print("Weather of "+str(info_place["location"]["address"][0])+" for the next 2 weekends are :-")
       j=0
       for i in range(0,15):
            if info["vt1dailyForecast"]["dayOfWeek"][i]=="Saturday":
                j+=1
                print(str(j)+"- "+ info["vt1dailyForecast"]["dayOfWeek"][i])
                print("   Description : Day- "+str(info["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(info["vt1dailyForecast"]["night"]["phrase"][i]))
                print("   Temperature : Max- "+str(info["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(info["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
                print("   Precipitation : Day- "+str(info["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(info["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(info["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(info["vt1dailyForecast"]["day"]["precipType"][i]))
                print("   Wind : Day- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
                print("   Humidity : Day- "+str(info["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(info["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
                print("   UV Index : Day- "+str(info["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(info["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
                print("   Sunrise : "+str(info["vt1dailyForecast"]["sunrise"][i]))
                print("   SunSet : "+str(info["vt1dailyForecast"]["sunset"][i]))
                print("   Moon Phase : "+str(info["vt1dailyForecast"]["moonPhrase"][i]))
                print("   Moonrise : "+str(info["vt1dailyForecast"]["moonrise"][i]))
                print("   MoonSet : "+str(info["vt1dailyForecast"]["moonset"][i]))
                print(" ")
            elif info["vt1dailyForecast"]["dayOfWeek"][i]=="Sunday":
                j+=1
                print(str(j)+"- "+ info["vt1dailyForecast"]["dayOfWeek"][i])
                print("   Description : Day- "+str(info["vt1dailyForecast"]["day"]["phrase"][i])+" ,Night- "+str(info["vt1dailyForecast"]["night"]["phrase"][i]))
                print("   Temperature : Max- "+str(info["vt1dailyForecast"]["day"]["temperature"][i])+" deg C, Min- "+str(info["vt1dailyForecast"]["night"]["temperature"][i])+ " deg C")
                print("   Precipitation : Day- "+str(info["vt1dailyForecast"]["day"]["precipPct"][i])+"% " +str(info["vt1dailyForecast"]["day"]["precipType"][i]) + " Night- "+str(info["vt1dailyForecast"]["night"]["precipPct"][i])+"% "+str(info["vt1dailyForecast"]["day"]["precipType"][i]))
                print("   Wind : Day- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["day"]["windSpeed"][i])+" km/hr ,Night- "+ str(info["vt1dailyForecast"]["day"]["windDirCompass"][i]) +str(info["vt1dailyForecast"]["night"]["windSpeed"][i])+" km/hr")
                print("   Humidity : Day- "+str(info["vt1dailyForecast"]["day"]["humidityPct"][i])+" % ,Night- "+str(info["vt1dailyForecast"]["night"]["humidityPct"][i])+" %")
                print("   UV Index : Day- "+str(info["vt1dailyForecast"]["day"]["uvIndex"][i])+" out of 10 ,Night- "+str(info["vt1dailyForecast"]["night"]["uvIndex"][i])+" out of 10")
                print("   Sunrise : "+str(info["vt1dailyForecast"]["sunrise"][i]))
                print("   SunSet : "+str(info["vt1dailyForecast"]["sunset"][i]))
                print("   Moon Phase : "+str(info["vt1dailyForecast"]["moonPhrase"][i]))
                print("   Moonrise : "+str(info["vt1dailyForecast"]["moonrise"][i]))
                print("   MoonSet : "+str(info["vt1dailyForecast"]["moonset"][i]))
                print(" ")



if __name__=="__main__":
    if choice=="Today" or choice=="today":
        resp= requests.get("https://api.weather.com/v2/turbo/vt1observation?apiKey="+api_key+"&format=json&geocode=" +str(info_place["location"]["latitude"][0]) + "," + str(info_place["location"]["longitude"][0]) + "&language=en-IN&units=m")
        info=resp.json()
        today(info)

    elif choice=='hourly' or choice=='Hourly':
             hourbyhour(info_place)
    
    else :
        response=requests.get("https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey="+api_key+"&format=json&geocode=" +str(info_place["location"]["latitude"][0]) + "," + str(info_place["location"]["longitude"][0]) + "&language=en-IN&units=m")
        info=response.json()
        if choice=="5-day" or choice=="5 day":
            day5(info)
        elif choice=="10-day" or choice=="10 day":
            day10(info)
        elif choice=="weekend" or choice=="Weekend":
            weekend(info)

#################################################################################################
