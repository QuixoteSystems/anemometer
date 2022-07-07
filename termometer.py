import adafruit_dht
import time
import board


class Termometer():
    """
    Esta clase representa un sensor que envia pulsos digitales a un pin GPIO
    conociendo de esta forma las vueltas completas que realiza.

    Mediante el metodo generateWind() se actualizaran los valores de la clase
    calculando y limpiándolos.
    De esta forma queda el modelo para el anemómetro separado de las peticiones
    en tiempo pudiendo pedirse cada una en intervalos distintos se calculará
    siempre la direncia de tiempo dinamicamente.

    La clase quedara siempre tomando datos y se podrán calcular en cualquier
    momento usando para ello los datos recopilados desde la última vez.
    """
    def __init__(self):
        self.connect()

    def connect(self):
        try:
            dht22int = adafruit_dht.DHT22(board.D17)
            temperature_int = dht22int.temperature
            humidity_int = dht22int.humidity

        except RuntimeError as dht_error:
            print(f"Error del Sensor Interior: {dht_error}")
        try:
            dht22ext = adafruit_dht.DHT22(board.D21)
            temperature_ext = dht22ext.temperature
            humidity_ext = dht22ext.humidity
        except RuntimeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")

        def __init__(self, dht22int, dht22ext):
            self.dht22int = dht22int
            self.dht22ext = dht22ext
            self.temperature_int = dht22int.temperature
            self.humidity_int = dht22int.humidity
            self.temperature_ext = dht22ext.temperature
            self.humidity_ext = dht22ext.humidity


    def start_read(self):

        fecha_hora = time.strftime("%c")

        # Abrimos archivo donde escribiremos los datos
        f = open ('/var/lib/prometheus/node-exporter/datos.prom','w')
        #f.write('hola mundo')
        #f.close()

        #si queremos que muestre esto cada 5 segundos descomentar el while y el time.sleep
        while True:
#print(f"                  ")
#print("Dia: "+ time.strftime("%d/%m/%y") + "  Hora: "+ time.strftime("%H:%M:%S"))
                f.write("Fecha y Hora" + fecha_hora)
#print("Hora: "+ time.strftime("%H:%M:%S+0001"))
#print(f"------------------")
#print(f" Sensor Interior")
#print(f"------------------")

                temp_int = "{:.2f}".format(self.temperature_int)
                f.write("interior_temp "+ temp_int + "\n")

                hum_int = "{:.2f}".format(self.humidity_int)
                f.write("interior_hum "+ hum_int + "\n")
#print(f"Temperatura Interior= " + tempint + " C")
# alternativa de impresion de la temperatura
#tempint = "{:.2f}".format(temperatureInt)

#print(f"Humedad= "+ humint +" %")
#print(f"Humedad= "+ humint +" %")


#print(f"                  ")
#print(f"------------------")
#print(f" Sensor Exterior")
#print(f"------------------")

                temp_ext = "{:.2f}".format(self.temperature_ext)
                f.write("exterior_temp "+ temp_ext + "\n")

                hum_ext = "{:.2f}".format(self.humidity_ext)
                f.write("exterior_hum "+ hum_ext + "\n")
                #print(f"Temperatura Exterior= " + tempext + " C")

                #print(f"Humedad= "+ humext +" %")
                f.close()

        #print(f"------------------")
        #print(f"                  ")
                time.sleep(5)
# Cerramos el archivo

