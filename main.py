import time
from src.ekky.mqtt import payload as data
from protobuf import payload_pb2
import sys

def populatePayload(payload, id:int, index:int):
    payload.id = id
    payload.temperature = data.get_temperature_value(index)
    payload.timestamp = data.get_time()


id = 0
while True:
    payload_proto = payload_pb2.Payloads()
    populatePayload(payload_proto.data.add(), id, id%10)
    serializedProtobuf = payload_proto.SerializeToString()
    print(serializedProtobuf)
    id += 1
    time.sleep(2)