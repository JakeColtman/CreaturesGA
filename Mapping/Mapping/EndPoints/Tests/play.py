import asyncio
import websockets
from websocket import create_connection
from Mapping.move_pb2 import Movement, LEFT, RIGHT, UP, DOWN

move = Movement()
move.direction = UP
move.slug = 1

parsed = Movement()
parsed.ParseFromString(move.SerializeToString())
print(parsed)
ws = create_connection('ws://localhost:5000')
print(move.SerializeToString())
ws.send(move.SerializeToString())
result = ws.recv()
print(result)
