import paho.mqtt.client as mqtt
import random
import time

mqttc = mqtt.Client("Hum_pub")

mqttc.connect("127.0.0.1", 1883)


while 1:
    Hum = random.randrange(30,95)
    mqttc.publish("Environment/Humidity", Hum)
    print "Humidity = " + str(Hum) + "%"
    time.sleep(2)

mqttc.loop(2)    
