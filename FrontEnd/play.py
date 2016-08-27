from websocket import create_connection

while True:
    ws = create_connection("ws://192.168.0.10:8888/input")
    ws.send("Jake is Great 08")
    result = ws.recv()
    print(result)
    ws.close()