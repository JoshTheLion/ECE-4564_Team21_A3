#python code running on scraper laptop
#first what is a scrapper? its getting/scrapping data from the internet
import requests
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
#input city name here
city_name = 'Blacksburg'
#scrape weather data from api based on city
URL = 'http://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=81827b45a852dd349a8247994f2d47f5' #pseudo website
page = requests.get(URL).text
soup = BeautifulSoup(page, 'html.parser')

#extract wanted fields from json object and print
jsonText = json.loads(soup.text)
mainText = jsonText['main']
print('location: '+ city_name+', temperature: '+ str(mainText['temp'])+', pressure: '+ str(mainText['pressure'])+', humidity: '+str(mainText['humidity']))


#soup = BeautifulSoup(page.content, 'html.parser')
#page = soup.find(id = 'ResulsContainer')
