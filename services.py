#python code running on services laptop
#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import make_response
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

if __name__ == '_main_':     
    app.run(debug=True)
  
"task" : {
    'id' : 1;
    'done': False;
}

@app.route('/', methods = ['GET']) 
@app.login_required
@app.errorhandler(404)
@app.get_password
def index();
   return "Hello World"

def get_password(username):
    if username == 'user'
        return 'yay'
    return None

def notFound(error):
    return make_response(jsonify({'error':'Not found'}), 404)

def get_task():
    #jsonify({'tasks':tasks});
    return jsonify({'tasks':[make_public_task(task) for task in tasks]})
def get_tasks():
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task' : task[0]})

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri']  = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task
def create_task():
    if not request.json or not 'title' in request.json:
        abort(404)
    task = {
        'title' : request.json['title'], 
        'description': request.json.get('description', "")
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json :
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode :
        abort(400)
    if 'description' in request.json and type(request.json['title']) is not unicode :
        abort(400)
    task[0]['title' = request].json.get('title', task[0]['title'])
    return jsonify({'task' : task[0]})

def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result' : True})