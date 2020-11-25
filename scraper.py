#python code running on scraper laptop
#first what is a scrapper? its getting/scrapping data from the internet
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

URL = "https://somewebsite.com/stuff" #pseudo website
page = requests.get(URL)
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
page = soup.find(id = 'ResulsContainer') #parentheses may not be right