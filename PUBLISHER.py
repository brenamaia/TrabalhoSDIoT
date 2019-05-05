#coding:utf-8
import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("teste/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print( str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("m15.cloudmqtt.com", 10729, 5)
client.username_pw_set("rhdzbmfs", "ECvfT0nxtyab")

#client.loop_forever()
client.loop_start()
time.sleep(3)

while True:
	try:
		a = input("Para ativar o sensor, digite '1' \n")

		if(a == 1):
			v = "ligar"
			print ("Sensor Ativado!")
			client.publish("teste", v)
		time.sleep(1)
	except KeyboardInterrupt:
		client.loop_stop()
		client.disconnect()



    






