import map_pb2
import flask
import json 
from p_to_json import copy_pb_to_dict
from MapFactory import MapFactory

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    output = {}
    mappy = MapFactory().create_random_map(3)
    copy_pb_to_dict(output, mappy)
    return json.dumps(output)

if __name__ == '__main__':
    app.run(debug=True)