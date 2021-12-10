from datetime import datetime
from time import sleep, time
from protobuf import payload_pb2
from paho.mqtt import client as mqtt

def read_temperature(index: int):
    temperature = [i for i in range(25, 35)]
    return temperature[index]


def read_timestamp():
    return datetime.now().isoformat()


def build_payload_pkg(id: int):
    payload_pkg = payload_pb2.Payload()
    payload_pkg.id = id
    payload_pkg.temperature = read_temperature(id % 10)
    payload_pkg.timestamp = read_timestamp()
    return payload_pkg


def on_connect(client, userdata, flags, rc):
    print("Connected!")

mqtt_conn = mqtt.Client()
mqtt_conn.on_connect = on_connect
mqtt_conn.connect("broker.hivemq.com")
mqtt_conn.loop_start()
id = 0
while True:
    payload_pkg = build_payload_pkg(id).SerializeToString()
    mqtt_conn.publish("iot/thermostat", payload_pkg)
    print("Data sent with id:", id)
    id += 1
    sleep(2)