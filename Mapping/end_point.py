from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import map_pb2
import json 
from p_to_json import copy_pb_to_dict
from MapFactory import MapRepository
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def new_session():
     id = conn.incr("sessionid")
     conn.set("pos:{0}".format(str(id)), "0,0")
     map_id = repo.create_random_map(3)
     map = repo.get_map(map_id)
     conn.set("smap:{0}".format(id), map.SerializeToString())
     return id

def session_move(sessionid, direction):
    print("Here")
    print(conn.get("pos:{0}".format(str(sessionid))))
    x_pos, y_pos = conn.get("pos:{0}".format(str(sessionid))).decode('utf-8').split(",")
    if direction == "left":
        x_pos, y_pos = int(x_pos) - 1, int(y_pos)    
    if direction == "right":
        x_pos, y_pos = int(x_pos) + 1, int(y_pos)    
    if direction == "down":
        x_pos, y_pos = int(x_pos), int(y_pos) - 1 
    if direction == "up":
        x_pos, y_pos = int(x_pos) - 1, int(y_pos) + 1
    conn.set("pos:{0}".format(str(sessionid)), str(x_pos) + "," + str(y_pos))
    mappy_raw = conn.get("smap:{0}".format(str(sessionid)))
    mappy = map_pb2.Map()
    mappy.ParseFromString(mappy_raw)
    square = mappy.rows[x_pos].cells[y_pos]
    return square

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map/create', methods=['GET'])
def home():
    new_id = repo.create_random_map(3)
    return json.dumps({"id": new_id})

@socketio.on('move', namespace='/map')
def move(message):
    id, direction = message["data"].split(",")
    print(id ,direction)
    square = session_move(int(id), direction)
    output = {}
    copy_pb_to_dict(output, square)
       
    emit("my response", {"data": {"square": output}})

@socketio.on('connect', namespace='/map')
def test_connect():
    emit('my response', {'data': 'Connected', "session_id": new_session()})

@socketio.on('disconnect', namespace='/map')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    repo = MapRepository()
    conn = redis.StrictRedis(host = 'localhost', port=6379)  
    socketio.run(app)