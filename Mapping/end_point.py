from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import map_pb2
import json 
from p_to_json import copy_pb_to_dict
from MapFactory import MapRepository

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map/create', methods=['GET'])
def home():
    new_id = repo.create_random_map(3)
    return json.dumps({"id": new_id})

@socketio.on('move', namespace='/map')
def move(message):
    x_pos, y_pos, direction = message["data"].split(",")

    if direction == "left":
        x_pos, y_pos = int(x_pos) - 1, int(y_pos)    
    if direction == "right":
        x_pos, y_pos = int(x_pos) + 1, int(y_pos)    
    if direction == "down":
        x_pos, y_pos = int(x_pos), int(y_pos) - 1 
    if direction == "up":
        x_pos, y_pos = int(x_pos) - 1, int(y_pos) + 1
    square = map.rows[x_pos].cells[y_pos]
    output = {}
    copy_pb_to_dict(output, square)
       
    emit("my response", {"data": {"x_pos": x_pos, "y_pos": y_pos, "square": output}})

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    repo = MapRepository()
    id  = repo.create_random_map(4)
    map = repo.get_map(id)
    print(map)
    socketio.run(app)