import paho.mqtt.client as mqtt

broker_address="192.168.1.80" #Dirección Ip de la raspberry
broker_port= 1883
client = mqtt.Client("dispensador1") #creación del cliente
client.connect(broker_address, broker_port) #Conectar servidor
topic = "casa/sala/dispensador"

client.publish(topic, payload=1)
client.publish(topic, payload=2)
client.publish(topic, payload=3)
client.publish(topic, payload=4)
client.publish(topic, payload=5)
client.publish(topic, payload=6)


-----------------------------------------------------------------
import paho.mqtt.client as mqtt
import time

broker_address="192.168.1.80" #Dirección Ip de la raspberry
broker_port= 1883
client = mqtt.Client("disp1") #creación del cliente
client.connect(broker_address, broker_port) #Conectar servidor
topic = "casa/sala/dispensador" #topico a publicar

print("Led pinD4")
  client.publish(topic, payload="1" qos=0, retain=False)
  time.sleep(3)

print("Mover servo")
  client.publish(topic, payload="2" qos=0, retain=False)
  time.sleep(3)

print("Led pinD4")
  client.publish(topic, payload="3" qos=0, retain=False)
  time.sleep(3)

print("Led pinD4")
  client.publish(topic, payload="4" qos=0, retain=False)
  time.sleep(3)



  -----------------------------------------------------------------
import paho.mqtt.client as mqtt
import time

broker_address="192.168.1.80" #Dirección Ip de la raspberry
broker_port= 1883
client = mqtt.Client("disp1") #creación del cliente
client.connect(broker_address, broker_port) #Conectar servidor
topic = "casa/sala/dispensador" #topico a publicar

print("Led pinD4")
  client.publish(topic, payload="1" qos=0, retain=False)
  time.sleep(3)

print("Mover servo")
  client.publish(topic, payload="2" qos=0, retain=False)
  time.sleep(3)

print("Led pinD4")
  client.publish(topic, payload="3" qos=0, retain=False)
  time.sleep(3)

print("Led pinD4")
  client.publish(topic, payload="4" qos=0, retain=False)
  time.sleep(3)