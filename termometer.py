import adafruit_dht
import time
from datetime import datetime
import board
import logging

# Create LOG file
# Current date and time
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
date= day+month+year

logging.basicConfig(filename=f'/home/siseda/git/weather-station/log/weather-station{date}.log', 
filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True)
#Let us Create an object
logger=logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)

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
        try:
            self.sensor_interior = adafruit_dht.DHT22(board.D17, use_pulseio=False)
            #temperature_int = dht22int.temperature
            #humidity_int = dht22int.humidity

        except RuntimeError as dht_error:
            print(f"Error de Conexion Sensor Interior: {dht_error}")
            logger.error('Error de Conexion Sensor Interior: %s', dht_error)
        try:
            self.sensor_exterior = adafruit_dht.DHT22(board.D21, use_pulseio=False)
            #temperature_ext = dht22ext.temperature
            #humidity_ext = dht22ext.humidity
        except RuntimeError as dht_error:
            print(f"Error de Conexion Sensor Exterior: {dht_error}")
            logger.error('Error de Conexion Sensor Exterior: %s', dht_error)
            
            #self.start_read(self.dht22int, self.dht22ext)
        
        #self.dht22ext = dht22ext
        #self.dht22int = dht22int


    def start_read(self):

        data_file = open ('/var/lib/prometheus/node-exporter/datos.prom','w', encoding = 'utf-8')

        try:
            temperature_int = self.sensor_interior.temperature
            humidity_int = self.sensor_interior.humidity

            temp_int = "{:.2f}".format(temperature_int)
            data_file.write(f"interior_temp {temp_int}\n")

            hum_int = "{:.2f}".format(humidity_int)
            data_file.write(f"interior_hum {hum_int}\n")

        except UnboundLocalError as dht_error:
            print(f"Sin datos del Sensor Interior: {dht_error}")
            logger.warning('Sin datos del Sensor Interior: %s', dht_error)
        except AttributeError as dht_error:
            print(f"Error del Sensor Interior: {dht_error}")
            logger.error('Error del Sensor Interior: %s', dht_error)
        except RuntimeError as dht_error:
            print(f"Error del Sensor Interior: {dht_error}")
            logger.error('Error del Sensor Interior: %s', dht_error)
        except TypeError as dht_error:
            print(f"Error del Sensor Interior: {dht_error}")
            logger.error('Error del Sensor Interior: %s', dht_error)
        '''
        except RuntimeError as dht_error:
            print(f"Error de lectura del Sensor Interior: {dht_error}")
            logger.warning('Error de lectura del Sensor Interior: %s', dht_error)
            time.sleep(30)
        '''
            #print("Esperamos 30 segundos antes de volver a leer")
            #temperature_int = self.sensor_interior.temperature
            #humidity_int = self.sensor_interior.humidity
            
        try:
            temperature_ext = self.sensor_exterior.temperature
            humidity_ext = self.sensor_exterior.humidity

        except RuntimeError as dht_error:
            print(f"Error de lectura del Sensor Exterior: {dht_error}")
            logger.warning('Error de lectura del Sensor Exterior: %s', dht_error)
            #print("Esperamos 30 segundos antes de volver a leer")
            time.sleep(30)
            #temperature_ext = self.sensor_exterior.temperature
            #humidity_ext = self.sensor_exterior.humidity

        fecha_hora = time.strftime("%c")

        #print(f"\n{fecha_hora}")

        # Abrimos archivo donde escribiremos los datos
        data_file = open ('/var/lib/prometheus/node-exporter/datos.prom','w', encoding = 'utf-8')
        #f.write('hola mundo')
        #f.close()

        #si queremos que muestre esto cada 5 segundos descomentar el while y el time.sleep

#print("Dia: "+ time.strftime("%d/%m/%y") + "  Hora: "+ time.strftime("%H:%M:%S"))
        #f.write("Fecha y Hora" + fecha_hora)
#print("Hora: "+ time.strftime("%H:%M:%S+0001"))


            #print(f"Humedad Interior= {hum_int} %")
        

        try:
            temp_ext = "{:.2f}".format(temperature_ext)
            data_file.write(f"exterior_temp {temp_ext}\n")

            #print(f"Temperatura Exterior= {temp_ext} C")

            hum_ext = "{:.2f}".format(humidity_ext)
            data_file.write(f"exterior_hum {hum_ext}\n")

            #print(f"Humedad Exterior= {hum_ext} %")

        except UnboundLocalError as dht_error:
            print(f"Sin datos del Sensor Exterior: {dht_error}")
            logger.warning('Sin datos del Sensor Exterior: %s', dht_error)
        except AttributeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")
            logger.error('Error del Sensor Exterior: %s', dht_error)
        except RuntimeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")
            logger.error('Error del Sensor Exterior: %s', dht_error)
        except TypeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")
            logger.error('Error del Sensor Exterior: %s', dht_error)

        # Cerramos el archivo
        data_file.close()

        #time.sleep(5)


