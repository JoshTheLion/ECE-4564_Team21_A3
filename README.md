# ECE 4564: Team 21
# Assignment 3 - Our API

# Road Blocks 

Throughout this assignment, we encountered roadblocks that have become somewhat familiar this semester. Primarily, this was in the form of time constraints imposed by assignments from other classes and other commitments associated with Thanksgiving Break. As for the assignment itself, there was a large scope of requisite background material to know how to get started working, so much time was spent studying/reviewing the context of the assignment. Additionally, the new RESTful Flask tooling took time to become familiar with.

# External Libraries Used
  ## From service.py
- `import sys` : used for system exit 
- `import json` :  was a potential serialization alternative to Pickle
- `import hashlib` : used to hash the message data


  from flask import Flask, jsonify, abort, request, make_response, url_for
  from flask_httpauth import HTTPBasicAuth

  from flask import session, flash, render_template
  #from requests.auth import HTTPBasicAuth
  import hashlib
  import argparse
  import json
  import requests # To send+recieve HTTP GET/POST requests to/from the Scraper Flask and the Marvel API

  # From scraper.py
  from flask import Flask, jsonify, abort, request, make_response, url_for
  from flask_httpauth import HTTPBasicAuth

  import requests # To recieve+send HTTP POST/GET requests from/to the Service Flask and the Weather Data API

  # Libraries to help scrape COVID data from:
    https://www.worldometers.info/coronavirus/country/us/
    
  # Important: NOT using API requests for this one
  import json
  from bs4 import BeautifulSoup
  from urllib.request import Request, urlopen

# Team Members Contributions
- Marilyn contributed to the scraper.py gathering data for covid. Also help contribute and write the services.py file for marvel, covid, and weather.  
- Tyron contributed to ...
- Joshua contributed by organizing and communicating workflow plans, adding ~300 lines of structural code for team to build on, reorganizing, refactoring, and debugging code intermittently
