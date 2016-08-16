import flask
import redis 
import json

app = flask.Flask(__name__)


@app.route('/resource/<int:user_id>', methods=['GET'])
def home(user_id):
    amount = conn.get("user:" + str(user_id))
    return json.dumps({"id": user_id, "amount": int(amount)})


if __name__ == '__main__':
   conn = redis.StrictRedis(host = 'localhost', port=6379)  
   app.run(debug=True)