import paho.mqtt.client as mqtt
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("myhome/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
#    file_ = open('motiondata.csv', 'a')
#    st_dt = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
#    st = st_dt + "\t " + msg.topic + "\t" + str(msg.payload) + "\n"
#    file_.write(st)
#    file_.close()
    print(st)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.78", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
