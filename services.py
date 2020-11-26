#python code running on services laptop
#!flask/bin/python

from flask import Flask, flash, render_template, abort
from flask import jsonify
from flask import request
from flask import make_response
from flask import session
from requests.auth import HTTPBasicAuth
#api public key for marvel
#5fd57f8f0bc35903bab675fbfc99d9f7
####
# request with auth=username, password
####
url = "https://gateway.marvel.com/v1/public/stories/36864?apikey=5fd57f8f0bc35903bab675fbfc99d9f7"
r = request.get(url, auth=('username', 'password'))

app = Flask(__name__)

if __name__ == '_main_':
    #run the services   
    app.run(debug=True, host='0.0.0', port=5000)
#one route    
@app.route('/', methods = ['GET'])
#the second route
@app.route('/login', methods= ['POST'])
####
# capture the sent username and password 
# and compare to whatever the login credentials saved
# into the python script
####
def do_admin_login():#pythonspot.com
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return home()

def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return dosomething() #the main method for serices

def notFound(error):
    return make_response(jsonify({'error':'Not found'}), 404)

def dosomething():
    print(r.text)
    return None
