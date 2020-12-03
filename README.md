# ECE 4564: Team 21
# Assignment 3 - Our API

# Road Blocks 

Throughout this assignment, we encountered roadblocks that have become somewhat familiar this semester. Primarily, this was in the form of time constraints imposed by assignments from other classes and other commitments associated with Thanksgiving Break. As for the assignment itself, there was a large scope of requisite background material to know how to get started working, so much time was spent studying/reviewing the context of the assignment. Additionally, the new RESTful Flask tooling took time to become familiar with.

# External Libraries Used
  ### From server.py
- `from flask import Flask` : used to make web application

- `from flask_httpauth import HTTPBasicAuth` : used to get password and username in service.py

- `import hashlib` : used for encryption of marvel
- `import argparse` : used in service
- `import json` : used in service.py
- `import requests` : to send+recieve HTTP GET/POST requests to/from the Scraper Flask and the Marvel API

  ### From scraper.py
  
- `from flask_httpauth import HTTPBasicAuth` : used for username and password
- `import requests` :  to recieve+send HTTP POST/GET requests from/to the Service Flask and the Weather Data API

  ### Libraries to help scrape COVID data from:
    https://www.worldometers.info/coronavirus/country/us/
    
- `import json` : Library to help parse COVID data
- `from bs4 import BeautifulSoup` : Library to help scrape COVID data
- `from urllib.request import` : Libraries to help scrape COVID data

# Team Members Contributions
- Marilyn contributed to the scraper.py gathering data for covid. Also help contribute and write the services.py file for marvel, covid, and weather.
- Tyron contributed to the scraper.py gathering data for the weather by city.
- Joshua contributed by organizing and communicating workflow plans, adding ~300 lines of structural code for team to build on, reorganizing, refactoring, and debugging code intermittently
