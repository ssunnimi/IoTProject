import paho.mqtt.client as mqtt
import random
import time

mqttc = mqtt.Client("Tem_pub")

mqttc.connect("127.0.0.1", 1883)


while 1:
    Tem = random.randrange(20,35)
    mqttc.publish("Environment/Temperature", Tem)
    print "Temperature = " + str(Tem) + "'"
    time.sleep(2)

mqttc.loop(2)    





