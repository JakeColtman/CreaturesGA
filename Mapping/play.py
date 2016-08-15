import map_pb2
import flask
import json 
from p_to_json import copy_pb_to_dict
from MapFactory import MapRepository

app = flask.Flask(__name__)


@app.route('/map/create', methods=['GET'])
def home():
    new_id = repo.create_random_map(3)
    return json.dumps({"id": new_id})

@app.route("/map/get/<int:map_id>", methods = ["GET"])
def get_map(map_id):
    output = {}
    mappy = repo.get_map(map_id)
    copy_pb_to_dict(output, mappy)
    return json.dumps(output)

@app.route('/river', methods=['GET'])
def river():
    output = {}
    mappy = MapRepository().create_river_map()
    copy_pb_to_dict(output, mappy)
    return json.dumps(output)

if __name__ == '__main__':
   repo = MapRepository()
   app.run(debug=True)