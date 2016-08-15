import map_pb2
import flask
import json 
from p_to_json import copy_pb_to_dict


app = flask.Flask(__name__)

req = map_pb2.Cell()
req.terrain = map_pb2.GRASS
req.x_pos = 0
req.y_pos = 1

row = map_pb2.Row()
row.cells.extend([req])

mappy = map_pb2.Map()
mappy.rows.extend([row])

@app.route('/', methods=['GET'])
def home():
    output = {}
    copy_pb_to_dict(output, mappy)
    return json.dumps(output)

if __name__ == '__main__':
    app.run(debug=True)