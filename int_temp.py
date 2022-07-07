import adafruit_dht
import time
import board


# GPIO17
#SENSOR_PIN17 = D17

# GPIO21
#SENSOR_PIN21 = D21

#dht22int = adafruit_dht.DHT22(SENSOR_PIN17, use_pulseio=False)
#dht22ext = adafruit_dht.DHT22(SENSOR_PIN21, use_pulseio=False)

dht22int = adafruit_dht.DHT22(board.D21)

temperatureInt = dht22int.temperature
humidityInt = dht22int.humidity


fechaHora = time.strftime("%c")

# Abrimos archivo donde escribiremos los datos
f = open ('/var/lib/prometheus/node-exporter/datos.prom','w')
#f.write('hola mundo')
#f.close()

#si queremos que muestre esto cada 5 segundos descomentar el while y el time.sleep
#while True:
print(f"                  ")
print("Dia: "+ time.strftime("%d/%m/%y") + "  Hora: "+ time.strftime("%H:%M:%S"))
        #print("Fecha y Hora" + fechaHora)
#print("Hora: "+ time.strftime("%H:%M:%S+0001"))
#print(f"------------------")
#print(f" Sensor Interior")
#print(f"------------------")

tempint = "{:.2f}".format(temperatureInt)
print(f"Temperatura Interior= " + tempint + " C")
# alternativa de impresion de la temperatura
#tempint = "{:.2f}".format(temperatureInt)
f.write("interior_temp "+ tempint + "\n")

humint = "{:.2f}".format(humidityInt)
#print(f"Humedad= "+ humint +" %")
#print(f"Humedad= "+ humint +" %")
f.write("interior_hum "+ humint + "\n")

#       time.sleep(5)
# Cerramos el archivo
f.close()
