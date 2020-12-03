#!flask/bin/python
"""
ECE 4564 - Assignment 3 - Our API

Run the Service API code with the simple command line format:
    $ python3 service.py

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

import requests # To send+recieve HTTP GET/POST requests to/from the Scraper Flask and the Marvel API


### Initialization ###
app = Flask(__name__)

# Setting default values
SERVICE_IP = '127.0.0.1'  # NOTE: This is hardcoded as '127.0.0.1' so it can be tested locally
SERVICE_PORT = 3000

SCRAPER_IP = '127.0.0.1'  # NOTE: This is hardcoded as '127.0.0.1' so it can be tested locally
SCRAPER_PORT = 8081

KEY_MARVEL = '5fd57f8f0bc35903bab675fbfc99d9f7'
PRIVATE_KEY_MARVEL = 'b790475b329908ce985571a69040077fb8f54f8d'
TIME_STAMP = ''
service_username = 'admin'
service_password = 'secret'

auth = HTTPBasicAuth()

### Authentication Routes ###
@auth.verify_password
def verify_password(username, password):
    if username == service_username:
        if password == service_pass:
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

#============================================================#
# TODO: Finish adapting this section for our purposes
#============================================================#
@app.route('/api/users', methods=['POST'])
def new_user():
    # TODO: Send to Scraper Flask instance with Python requests #
    r = None
    #r = requests.post('http://' + SCRAPER_IP + ':' + SCRAPER_PORT + '/Update?user=' + {scrape_user} + '&pass=' + {scrape_pass})
    if not r:
        return ('failure')
    return ('success')
# end of function


@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})
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
def marvel():
    marv = KEY_MARVEL + PRIVATE_KEY_MARVEL + --
    marv_unecrypted = hashlib.md5(marv.encode())
    url = "https://gateway.marvel.com/v1/public/stories/36864?" + KEY_MARVEL
    print(url)
    r = requests.get(url, auth=('username', 'password'))
    finalresults = r.text
    return finalresults
####
# capture the sent username and password 
# and compare to whatever the login credentials saved
# into the python script
####
def dosomething():
    print(r.text)
    return None
# end of function

def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return dosomething() #the main method for serices?
# end of function

def do_admin_login():#pythonspot.com
    if request.form['password'] == 'secret' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return home()
# end of function

def notFound(error):
    return make_response(jsonify({'error':'Not found'}), 404)
# end of function


### Request Routes ###

#one route
@app.route('/Weather/<string:city>', methods = ['POST'])
def weatherfunct(city_name):
    info = str(requests.get_data().split('&'))
    print(info)
    user = info[0].split('=')
    userpassword = info[1].split('=')
    URL = "http://127.0.0.1:5001/Weather/"+city_name
    print(user[1])
    print(userpassword[0])
    print(URL)
    req = requests.get(URL, auth = (user[1], userpassword[0]))
    result = req.text
    return result
# end of function

#the second route
@app.route('/COVID/<string:state>', methods = ['POST'])
def decorated_func_2():
    info = str(requests.get_data().split('&'))
    print(info)
    user = info[0].split('=')
    userpassword = info[1].split('=')
    print(user[1])
    print(userpassword[0])
    print(URL)
    req = requests.get(URL, auth = (user[1], userpassword[0]))
    result = req.text
    return result
# end of function

###                   


if __name__ == '_main_': # Run the Service Flask instance
    app.run(debug=True, host='0.0.0', port=SERVICE_PORT)
