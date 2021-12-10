import paho.mqtt.client as mqtt
from protobuf import payload_pb2

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("iot/thermostat")
    print("==========================")

def on_message(client, user_data, message):
    payload_pkg = payload_pb2.Payload()
    payload = message.payload
    payload_pkg.ParseFromString(payload)
    print(f"id: {payload_pkg.id}")
    print(f"temperature: {payload_pkg.temperature}")
    print(f"timestamp: {payload_pkg.timestamp}")

mqtt_conn = mqtt.Client()
mqtt_conn.on_connect = on_connect
mqtt_conn.on_message = on_message
mqtt_conn.connect("broker.hivemq.com")
mqtt_conn.loop_forever()
