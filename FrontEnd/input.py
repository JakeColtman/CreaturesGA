from kafka import KafkaProducer, KafkaClient, KafkaConsumer
from tornado import websocket, httpserver, web, ioloop
import socket

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
consumer = KafkaConsumer('Game', bootstrap_servers=['0.0.0.0:9092'])
client = KafkaClient('0.0.0.0:9092')
client.ensure_topic_exists('Game')


def message_generator():
    for message in consumer:
        yield message.value


gens = message_generator()


class InputSocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print(message)
        producer.send("Game", message.encode("utf-8"))
        self.write_message(u"Jake magnanimously acknowledges your request")

    def check_origin(self, origin):
        return True

    def on_close(self):
        print("WebSocket closed")


class OutputSocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        msg = next(gens)
        self.write_message(msg)

    def check_origin(self, origin):
        return True

    def on_close(self):
        print("WebSocket closed")


app = web.Application([
    (r'/input', InputSocket),
    (r'/output', OutputSocket)
])

if __name__ == '__main__':
    server = httpserver.HTTPServer(app)
    server.listen(8888, address="0.0.0.0")
    myIP = socket.gethostbyname(socket.gethostname())
    ioloop.IOLoop.instance().start()
