from paho.mqtt import client

class Payload:
    def __init__(self, id:int, temperature:int, timestamp:str) -> None:
        self.id = 0
        self.temperature = temperature
        self.timestamp = timestamp
        self.port = 1883
        self.topic = "challenge/payload"

    def to_protobuf():
        pass

    def publish():
        pass
