import adafruit_dht
import time
import board


# GPIO17
#SENSOR_PIN17 = D17

# GPIO21
#SENSOR_PIN21 = D21

#dht22int = adafruit_dht.DHT22(SENSOR_PIN17, use_pulseio=False)
#dht22ext = adafruit_dht.DHT22(SENSOR_PIN21, use_pulseio=False)

dht22ext = adafruit_dht.DHT22(board.D21)
dht22int = adafruit_dht.DHT22(board.D17)

temperature_int = dht22int.temperature
humidity_int = dht22int.humidity

temperature_ext = dht22ext.temperature
humidity_ext = dht22ext.humidity

fechaHora = time.strftime("%c")

# Abrimos archivo donde escribiremos los datos
#f = open ('/var/lib/prometheus/node-exporter/datos.prom','w')
with open('/var/lib/prometheus/node-exporter/datos.prom','w', encoding = 'utf-8') as f:

#si queremos que muestre esto cada 5 segundos descomentar el while y el time.sleep
#while True:

        #print("Fecha y Hora" + fechaHora)
#print("Hora: "+ time.strftime("%H:%M:%S+0001"))
#print(f"------------------")
#print(f" Sensor Interior")
#print(f"------------------")
        while True:

                temperature_int = dht22int.temperature
                humidity_int = dht22int.humidity

                temperature_ext = dht22ext.temperature
                humidity_ext = dht22ext.humidity
                
                print(f"                  ")
                print("Dia: "+ time.strftime("%d/%m/%y") + "  Hora: "+ time.strftime("%H:%M:%S"))
                
                tempint = "{:.2f}".format(temperature_int)
                print(f"Temperatura Interior= " + tempint + " C")

                f.write("interior_temp "+ tempint + "\n")

                humint = "{:.2f}".format(humidity_int)
                print(f"Humedad Interior= "+ humint +" %")

                f.write("interior_hum "+ humint + "\n")

                tempext = "{:.2f}".format(temperature_ext)
                print(f"Temperatura Exterior= " + tempext + " C")

                f.write("exterior_temp "+ tempext + "\n")

                humext = "{:.2f}".format(humidity_ext)
                print(f"Humedad Exterior= "+ humext +" %")

                f.write("exterior_hum "+ humext + "\n")

                time.sleep(2)
# Cerramos el archivo
#f.close()
