import paho.mqtt.client as mqtt
discomindex = 0; H_value = 0; H_toggle = False; T_value = 0; T_toggle = False;
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print ("Conneted with result code " + str(rc))
    client.subscribe([('Environment/Humidity',2),('Environment/Temperature',2)])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global H_value, H_toggle, T_value, T_toggle
    # If recieved Humidity topic.
    if msg.topic == "Environment/Humidity":
        H_toggle = True
        H_value = float(msg.payload)
        print "Hum_Recieve " + str(H_value) + "%"
        H_value /= 100

    # else If recieved Temperature topic.
    elif msg.topic == "Environment/Temperature":
        T_toggle = True
        T_value = float(msg.payload)
        print "Tem_Recieve " + str(T_value) + "'C"
    
    # Caculate and Print the Discomprtable Index.
    if (H_toggle == True) and (T_toggle == True):
        print "-------------------------------------"
        discomindex = ((9.0/5.0)*T_value)-(0.55*(1-H_value)*((9.0/5.0)*T_value-26))+32
        print printIndex(discomindex)
        print "-------------------------------------"
        H_toggle = T_toggle = False
        H_value = T_value = 0
        #Reset Toggles value and value
        
def printIndex(Index):
    print "Discomfort Index is .. " + str(Index)
    if Index >= 80 :
        return  "Very High : Very Discomfort"
    elif (Index >= 75) and (Index < 80):
        return  "High : Harf Discomfort"
    elif (Index >= 68) and (Index < 75):
        return  "Normal : Starting feeling a Discomfort"
    elif (Index < 68):
        return  "Low : Feel Nice"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()
    
