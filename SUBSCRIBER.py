import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

ctrl = "a"

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("teste/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print( str(msg.payload))
    
    if(str(msg.payload) == "ligar"):
        if __name__ == '__main__':
             
            try:
                GPIO.setup(23,GPIO.OUT)
                start = time.time()
                while ((time.time() - start) < 10):
                    dist = distance()
                    if(dist < 3000):
                        print "Movimento detectado"
                        GPIO.output(23,GPIO.HIGH)
                    print ("Measured Distance = %.1f cm" % dist)
                    time.sleep(1)
                    GPIO.output(23,GPIO.LOW)
            except KeyboardInterrupt:
                GPIO.cleanup()    
    
    else:
        GPIO.cleanup()
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("m15.cloudmqtt.com", 10729, 5)
client.username_pw_set("rhdzbmfs", "ECvfT0nxtyab")

client.loop_forever()




