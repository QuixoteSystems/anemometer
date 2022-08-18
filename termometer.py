#!/usr/bin/python3

'''
    Clase del Sensor Termometro, crea el sensor, lo inicializa y lee los datos
'''

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


    def __init__(self, orig_name, pin):
        self.orig_name = orig_name
        self.sensor_name = "sensor_"+orig_name
        pin = "D"+pin
        print(pin)
        try:
            self.sensor_name = adafruit_dht.DHT22(pin=getattr(board, pin), use_pulseio=False)
            #temperature_int = dht22int.temperature
            #humidity_int = dht22int.humidity
            time.sleep(2)
        except RuntimeError as dht_error:
            print(f"Error de Conexion Sensor {orig_name}erior: {dht_error}")
            logger.error('Error de Conexion Sensor Interior: %s', dht_error)
        '''    
        try:
            self.sensor_exterior = adafruit_dht.DHT22(board.D21, use_pulseio=False)
            #temperature_ext = dht22ext.temperature
            #humidity_ext = dht22ext.humidity
            time.sleep(2)

        except RuntimeError as dht_error:
            print(f"Error de Conexion Sensor Exterior: {dht_error}")
            logger.error('Error de Conexion Sensor Exterior: %s', dht_error)
            
            #self.start_read(self.dht22int, self.dht22ext)
        
        #self.dht22ext = dht22ext
        #self.dht22int = dht22int
        '''

    def start_read(self):

        # Abrimos archivo donde escribiremos los datos
        data_file = open('/var/lib/prometheus/node-exporter/datos.prom','w', encoding = 'utf-8')

        try:
            # Controlamos si ha podido leer correctamente el sensor y lo intenta hasta que lo
            # consigue para que no de errores
            success = False
            while success is False:

                if success is False:
                    try:
                        temperature_int = self.sensor_name.temperature
                        humidity_int = self.sensor_name.humidity
                        success = True
                        logger.info(temperature_int)
                        logger.info(humidity_int)

                    except RuntimeError as dht_error:
                        print(f"Error de lectura del Sensor {self.orig_name}erior: {dht_error}")
                        # activar sólo para debug
                        logger.warning('Error de lectura del Sensor Interior: %s', dht_error)
                        
                if success is True:
                    temp_int = "{:.2f}".format(temperature_int)
                    data_file.write(f"{self.orig_name}_temp {temp_int}\n")
                    # activar sólo para debug
                    logger.info(f"Temperatura {self.orig_name}: %s", temp_int+"C")

                    hum_int = "{:.2f}".format(humidity_int)
                    data_file.write(f"{self.orig_name}_hum {hum_int}\n")
                time.sleep(2)

        except UnboundLocalError as dht_error:
            print(f"Sin datos del Sensor {self.orig_name}: {dht_error}")
            logger.warning('Sin datos del Sensor Interior: %s', dht_error)
            '''except AttributeError as dht_error:
            print(f"Error del Sensor {self.orig_name}: {dht_error}")
            logger.error('Error 1 del Sensor Interior: %s', dht_error)

            '''
        except RuntimeError as dht_error:
            print(f"Error del Sensor {self.orig_name}: {dht_error}")
            logger.error('Error 2 del Sensor interior: %s', dht_error)
        except TypeError as dht_error:
            print(f"Error del Sensor Interior: {dht_error}")
            logger.error('Error 3 del Sensor Interior: %s', dht_error)

            #print("Esperamos 30 segundos antes de volver a leer")
            #temperature_int = self.sensor_interior.temperature
            #humidity_int = self.sensor_interior.humidity
        '''        
        try:
            # Controlamos si ha podido leer correctamente el sensor y lo intenta hasta que lo
            # consigue para que no de errores
            success = False
            while success is False:

                if success is False:
                    try:
                        temperature_ext = self.sensor_exterior.temperature
                        humidity_ext = self.sensor_exterior.humidity
                        success = True

                    except RuntimeError as dht_error:
                        print(f"Error de lectura del Sensor Exterior: {dht_error}")
                        # activar sólo para debug
                        #logger.warning('Error de lectura del Sensor Exterior: %s', dht_error)

                        #print("Esperamos 30 segundos antes de volver a leer")
                        #time.sleep(30)
                        #temperature_ext = self.sensor_exterior.temperature
                        #humidity_ext = self.sensor_exterior.humidity

                if success is True:
                    temp_ext = "{:.2f}".format(temperature_ext)
                    data_file.write(f"exterior_temp {temp_ext}\n")

                    # activar sólo para debug
                    #logger.info("Temperatura Exterior: %s", temp_ext+"C")

                    hum_ext = "{:.2f}".format(humidity_ext)
                    data_file.write(f"exterior_hum {hum_ext}\n")
                time.sleep(2)

        except UnboundLocalError as dht_error:
            print(f"Sin datos del Sensor Exterior: {dht_error}")
            logger.warning('Sin datos del Sensor Exterior: %s', dht_error)
        except AttributeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")
            logger.error('Error 1 del Sensor Exterior: %s', dht_error)
        except RuntimeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")
            logger.error('Error 2 del Sensor Exterior: %s', dht_error)
        except TypeError as dht_error:
            print(f"Error del Sensor Exterior: {dht_error}")
            logger.error('Error 3 del Sensor Exterior: %s', dht_error)
        
        
        except RuntimeError as dht_error:
            print(f"Error de lectura del Sensor Exterior: {dht_error}")
            logger.warning('Error de lectura del Sensor Exterior: %s', dht_error)
            #print("Esperamos 30 segundos antes de volver a leer")
            time.sleep(30)
            #temperature_ext = self.sensor_exterior.temperature
            #humidity_ext = self.sensor_exterior.humidity
        '''
        

        #si queremos que muestre esto cada 5 segundos descomentar el while y el time.sleep

#print("Dia: "+ time.strftime("%d/%m/%y") + "  Hora: "+ time.strftime("%H:%M:%S"))
        #f.write("Fecha y Hora" + fecha_hora)
#print("Hora: "+ time.strftime("%H:%M:%S+0001"))

        # Cerramos el archivo
        data_file.close()

        #time.sleep(5)


