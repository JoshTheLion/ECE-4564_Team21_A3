#!flask/bin/python
"""
ECE 4564 - Assignment 3 - Our API (Services Flask)

Before running, first make sure that the IP address you want to use is set for the parameters:
    SERVICE_IP = '0.0.0.0'
    SCRAPER_IP = '0.0.0.0'
(default values shown, be sure these assignments are consistent in both this file and scraper.py)

Run the Service API code with the simple command line format:
    $ python3 services.py

Once the flask instance is running, test connectivity from a separate terminal window with the command:
    $ curl -u admin:secret http://0.0.0.0:8081/Test/get_services_resource

Supports 4 cURL command formats:
    curl -u service_username:service_password http://127.0.0.1:8081/Marvel?story=36864
    curl -u service_username:service_password -d "user=scrape_user&pass=scrape_pass" http://127.0.0.1:3000/Weather/<city>
    curl -u service_username:service_password -d "user=scrape_user&pass=scrape_pass" http://127.0.0.1:3000/COVID/<state>
    curl -u service_username:service_password -d "user=scrape_user?pass=scrape_pass&new_user=user2&new_pass=pass2"
        -X POST http://127.0.0.1:3000/Update

Based on example code from a 4-part series of articles by Miguel Grinberg, at:
    https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
"""
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

from flask import session, flash, render_template
#from requests.auth import HTTPBasicAuth
import hashlib
import argparse
import json
import requests # To send+recieve HTTP GET/POST requests to/from the Scraper Flask and the Marvel API
import time

### Initialization ###
app = Flask(__name__)
auth = HTTPBasicAuth()

# Setting default values
SERVICE_IP = '0.0.0.0' #('0.0.0.0' or '127.0.0.1' for local testing, 'xxx.x.x.x' format for full online usage)
SERVICE_PORT = 8081

SCRAPER_IP = '0.0.0.0' #('0.0.0.0' or '127.0.0.1' for local testing, 'xxx.x.x.x' format for full online usage)
SCRAPER_PORT = 3000

apikey = '5fd57f8f0bc35903bab675fbfc99d9f7'
privatekey = 'b790475b329908ce985571a69040077fb8f54f8d'

service_username = 'admin'
service_password = 'secret'
#auth = HTTPBasicAuth()

### Authentication Routes ###
@auth.verify_password
def verify_password(username, password):
    if username == service_username:
        if password == service_password:
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
@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 405)
#============================================================#
# TODO: Finish adapting this section for our purposes
#============================================================#

### Service Module Utility Code ###
###
#api public key for marvel
#5fd57f8f0bc35903bab675fbfc99d9f7
#api private key for marvel
#b790475b329908ce985571a69040077fb8f54f8d
####
# request with auth=username, password
####
@app.route('/Marvel', methods = ['GET'])
@auth.login_required
def marvel():
    storyid = request.args['story']
    ts = str(int(time.time()))
    hashun = ts+privatekey+apikey
    marv = hashlib.md5(hashun.encode()).hexdigest()
    url = 'http://gateway.marvel.com/v1/public/stories/%s?ts=%s&apikey=%s&hash=%s'%( storyid, ts, apikey, marv)
    r = requests.get(url)
    finalresults = r.text
    return jsonify({'story': 'Here is the Marvel story description requested: %s' % finalresults})
####
# capture the sent username and password 
# and compare to whatever the login credentials saved
# into the python script
####



def do_admin_login():#pythonspot.com
    if request.form['password'] == 'secret' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return None
# end of function

def notFound(error):
    return make_response(jsonify({'error':'Not found'}), 404)
# end of function


### Request Routes ###

#one route
@app.route('/Weather/<string:city_name>', methods = ['POST'])
@auth.login_required
def weatherfunct(city_name):
    info = str(request.get_data()).split('&')
    print(info)
    user = info[0].split('=')
    userpassword = info[1].split('=')
    p = userpassword[1].split('\'')
    #URL = "http://127.0.0.1:5001/Weather/"+city_name
    URL = "http://" + str(SCRAPER_IP) +":" +str( SCRAPER_PORT) + "/Weather/"+city_name
    print(user[1])
    print(userpassword[0])
    print(URL)
    req = requests.get(URL, auth = (user[1], p[0]))
    result = req.text
    return result
# end of function

#the second route
@app.route('/COVID/<string:state_name>', methods = ['POST'])
@auth.login_required
def covid_func(state_name):
    info = str(request.get_data()).split('&')
    print(info)
    user = info[0].split('=')
    userpassword = info[1].split('=')
    p = userpassword[1].split('\'')
    print(user[1])
    print(p[0])
    URL = "http://" + str(SCRAPER_IP) +":" + str(SCRAPER_PORT) + "/COVID/"+ state_name
    print(URL)
    req = requests.get(URL, auth = (user[1], p[0]))
    print('Check')
    result = req.text
    return result
# end of function

# Echo service testing route #
@app.route('/Test/get_services_resource')
@auth.login_required
def get_services_resource():
    return jsonify({'response': 'Services Ping Test Success!'})
# end of function            


if __name__ == "__main__": # Run the Service Flask instance
    app.run(host=SERVICE_IP, port=SERVICE_PORT, debug=True)

