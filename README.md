# ECE 4564: Team 21
# Assignment 3 - Our API

# Road Blocks 

Throughout this assignment, we encountered roadblocks that have become somewhat familiar this semester. Primarily, this was in the form of time constraints imposed by assignments from other classes and other commitments associated with Thanksgiving Break. As for the assignment itself, there was a large scope of requisite background material to know how to get started working, so much time was spent studying/reviewing the context of the assignment. Additionally, the new RESTful Flask tooling took time to become familiar with.

# External Libraries Used
  ## From server.py
- `import sys` : used for system exit 
- `import json` :  was a potential serialization alternative to Pickle
- `import socket` : used to help with socket connections
- `import tweepy as twp` : used to help extract and listen to tweets
- `import hashlib` : used to hash the message data
- `import pickle` : used to help stream serialized data
- `from tweepy.streaming import StreamListener` : help assit with twitter portion
- `from cryptography.fernet import Fernet` : used to help encode and decode
- `import wolframalpha as wolf`: help with api for wolframaplha

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

  # Insert the names of other python files here as imports
  - `import IBM_Watson_TTS` : used for audio
  - `from ServerKeys import api_id` : used to extract api key
  - `import ClientKeys` : used to extract client key

  # Importing consumer key, consumer secret, access token, access secret. These help with twitter API
  - `ckey = ClientKeys.Twitter_API_key`
  - `csecret = ClientKeys.Twitter_API_secret`
  - `atoken = ClientKeys.Twitter_access_token`
  - `asecret = ClientKeys.Twitter_access_secret`

# Team Members Contributions
- Marilyn contributed to ...
- Tyron contributed to ...
- Joshua contributed by organizing and communicating workflow plans, adding ~300 lines of structural code for team to build on, reorganizing, refactoring, and debugging code intermittently
