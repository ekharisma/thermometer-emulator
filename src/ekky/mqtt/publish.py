from time import sleep, time
from src.ekky.mqtt import payload
import paho.mqtt.client as mqtt
import json

class Payload:
    def __init__(self, id:int, temperature:int, timestamp:str) -> None:
        self.id = id
        self.temperature = temperature
        self.timestamp = timestamp
        self.port = 1883
        self.topic = "challenge/payload"
        self.broker = "broker.hivemq.com"

    def to_protobuf(self):
        payload = {
            'id': self.id,
            'temperature': self.temperature,
            'timestamp': self.timestamp
        }
        return json.dumps(payload)

    def publish(self):
        client = mqtt.Client("Py1")
        print("Connecting to broker ", self.broker)
        client.connect(self.broker)
        sleep(4)
        client.disconnect()
