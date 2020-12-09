#!flask/bin/python
"""
ECE 4564 - Assignment 3 - Our API

Run the Scraper code with the simple command line format:
    $ python3 scraper.py

Supports 3 HTTP `request` formats: ??? I'm just guessing at the format here...
    r = requests.get('https://api.website.com', auth=('user', 'pass'))

    r = requests.get('http://' + SCRAPER_IP + ':' + SCRAPER_PORT + '/Weather/<city>?user=' + {scrape_user} + '&pass=' + {scrape_pass})
    r = requests.get('http://' + SCRAPER_IP + ':' + SCRAPER_PORT + '/COVID/<state>?user=' + {scrape_user} + '&pass=' + {scrape_pass})
    r = requests.post('http://' + SCRAPER_IP + ':' + SCRAPER_PORT + '/Update?user=' + {scrape_user} + '&pass=' + {scrape_pass})

Based on example code from a 4-part series of articles by Miguel Grinberg, at:
    https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
and:
    https://realpython.com/beautiful-soup-web-scraper-python/
"""
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from flask_restful import reqparse
import requests  # To recieve+send HTTP POST/GET requests from/to the Service Flask and the Weather Data API

# Libraries to help scrape COVID data from:
# https://www.worldometers.info/coronavirus/country/us/
# Important: NOT using API requests for this one
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

### Initialization ###
app = Flask(__name__)
auth = HTTPBasicAuth()

# Setting default values
SERVICE_IP = '0.0.0.0'  # '127.0.0.1'  # NOTE: This is hardcoded as '127.0.0.1' so it can be tested locally
SERVICE_PORT = 8081  # 3000

SCRAPER_IP = '0.0.0.0'  # '127.0.0.1'  # NOTE: This is hardcoded as '127.0.0.1' so it can be tested locally
SCRAPER_PORT = 3000  # 8081

KEY_WEATHER = '81827b45a852dd349a8247994f2d47f5'

# Should there be any default users or passes for this instance, before new users
# are added via cURL command through Services API?
scrape_user = 'user1'
scrape_pass = 'pass1'
Users = {
        'username': 'admin',
        'password': 'secret'
}


# auth = HTTPBasicAuth()

### Authentication Routes ###
@auth.verify_password
def verify_password(username, password):
    # user = [user for user in Users if user['id'] == task_id]
    # if len(task) == 0:
    #    abort(404)
    # user = User.query.get(id)
    # if not user:
    #    abort(400)
    # return jsonify({'username': user.username})
    
    if username == scrape_user:
        if password == scrape_pass:
            print(username)
            print(password)
            return True
        return False
    return False


# end of function

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# ============================================================#
# TODO: Finish adapting this section for our purposes
# ============================================================#

@app.route('/Update', methods=['POST'])
@auth.login_required
def newuser():
    par = reqparse.RequestParser()
    par.add_argument('user')
    par.add_argument('pass')
    par.add_argument('new_arg')
    par.add_argument('new_user')
    args = par.parse_args()
    newperson = {args['new_user']: args['new_pass']}
    Users.update(newperson)
    return Users

# ============================================================#

@app.route('/Weather/<string:city>', methods=['GET'])
@auth.login_required
### Gathering Weather Data ###
def weather(city):
    # input city name here for testing
    city_name = 'Blacksburg'
    
    # gather weather data from API based on city
    URL = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + KEY_WEATHER  # pseudo website
    page = requests.get(URL).text
    
    # extract wanted fields from json object and print
    jsonText = json.loads(page)
    mainText = jsonText['main']
    
    print('location: ' + city_name + ', temperature: ' + str(mainText['temp']) + ', pressure: ' + str(
        mainText['pressure']) + ', humidity: ' + str(mainText['humidity']))
    # Send an HTTP GET request to the API for weather data
    # r = requests.get('https://api.github.com', auth=('user', 'pass'))
    r = requests.get(URL)  # TODO: Double-check the documentation on their website for the proper "query method" format
    
    print(r.status_code)
    print(r.headers['content-type'])
    
    # soup = BeautifulSoup(page.content, 'html.parser')
    # page = soup.find(id = 'ResulsContainer')
    return jsonify({'response': 'Weather for ' + city_name})


# end of function


### Gathering Covid Data ###
# input state name here
# state_name = 'Maine'

@app.route('/Covid/<string:state>', methods=['GET'])
@auth.login_required
def covid(state):
    # input state name here for testing
    state_name = 'Maine'
    print(state)
    URL2 = 'https//wwww.worldometer.info/coronavirus/country/us'
    pages = requests.get(URL2)
    soup = BeautifulSoup(pages.content, 'html.parser')
    result = soup.find(id='usa_table_countries_today')
    stateN = result.find('a', string=state)
    return jsonify({'state': state})


# end of function

# Echo service testing route #
@app.route('/Test/get_scraper_resource')
@auth.login_required
def get_scraper_resource():
    return jsonify({'response': 'Scraper Ping Test Success!'})


# end of function

if __name__ == "__main__":  # Run the Scraper Flask instance
    app.run(host=SCRAPER_IP, port=SCRAPER_PORT, debug=True)
