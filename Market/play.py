from message_pb2 import Message
from Market.commodities_pb2 import Commodity
from kafka import KafkaProducer

comm = Message()
comm.trade.user_a_id = 1
comm.trade.user_b_id = 2
comm.trade.commodity_id = 1
comm.trade.amount = 100

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

producer.send("resource", comm.SerializeToString())