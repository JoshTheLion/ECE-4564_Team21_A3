#!flask/bin/python
"""
ECE 4564 - Assignment 3 - Our API

Run the Service API code with the simple command line format:
    $ python3 service.py

Supports 4 cURL command formats:
    curl -u service_username:service_password http://127.0.0.1:8081/Marvel?story=36864
    curl -u service_username:service_password -d "user=scrape_user&pass=scrape_pass" http://127.0.0.1:3000/Weather/<city>
    curl -u service_username:service_password -d "user=scrape_user&pass=scrape_pass" http://127.0.0.1:3000/COVID/<state>
    curl -u service_user:service_pass -d "user=scrape_user?pass=scrape_pass&new_user=user2&new_pass=pass2"
        -X POST http://127.0.0.1:3000/Update

Based on example code from a 4-part series of articles by Miguel Grinberg, at:
    https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
"""
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

from flask import session, flash, render_template
from requests.auth import HTTPBasicAuth


### Initialization ###
app = Flask(__name__)

# Setting default values
SERVICE_IP = '127.0.0.1'  # NOTE: This is hardcoded as '127.0.0.1' so it can be tested locally
SERVICE_PORT = 3000

service_user = 'admin'
service_pass = 'secret'

KEY_MARVEL = '5fd57f8f0bc35903bab675fbfc99d9f7'

auth = HTTPBasicAuth()

### Authentication Routes ###
@auth.get_password
def get_password(password):
    if password == service_pass:
        return 'Success!'
    return None

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

### Service Module Utility Code ###
###
#api public key for marvel
#5fd57f8f0bc35903bab675fbfc99d9f7
####
# request with auth=username, password
####
url = "https://gateway.marvel.com/v1/public/stories/36864?apikey=5fd57f8f0bc35903bab675fbfc99d9f7"
r = request.get(url, auth=('username', 'password'))

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
@app.route('/example_1', methods = ['GET'])
def decorated_func_1
    print('Route 1 Requested')
    return None
# end of function

#the second route
@app.route('/example_2', methods = ['POST'])
def decorated_func_2
    print('Route 2 Requested')
    return None
# end of function


if __name__ == '_main_': #run the services
    app.run(debug=True, host='0.0.0', port=SERVICE_PORT)
