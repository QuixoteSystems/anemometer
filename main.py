#!/usr/bin/python3

import sys
import time
import logging

from anemometer import Anemometer
from termometer import Termometer


def start_log():
    # Create LOG file
    # si no se pone un archivo valido va directamente a /var/log/syslog
    logging.basicConfig(filename=f'/home/siseda/git/weather-stationlog/weather-station{date}.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', force=True)

    #Let us Create an object
    logger=logging.getLogger('server_logger')
    logger.setLevel(logging.DEBUG)

    # Initial Log
    logger.info('Weather Station main.py script started')


    
def read_sensors(*args):
    while True:
        #try:
        anemometer.start_read()
        termometer.start_read()

            ## Cuando ha tomado 5 lecturas devuelve y resetea contadores
            ## para indicar que comienza una nueva medición.
            #count += 1
            #print('Contador:', count)
            #if (count % 5) == 0:
                #print(anemometer.get_all_datas())
                #anemometer.debug()
            #else:
                #anemometer.debug()
        #except KeyboardInterrupt:
            #anemometer.stop_read()
            #sys.exit(0)
        time.sleep(30)

if __name__ == "__main__":
    
    start_log()

    anemometer = Anemometer()
    termometer = Termometer()

    read_sensors(anemometer, termometer)

    ## Inicio lecturas de datos de anemometro y termometros
    #anemometer.start_read()
    #termometer.start_read()

    ## Espera de 3 segundos recopilando los primeros datos
    #time.sleep(3)
    #count = 0

    ## Muestro constantemente los datos recopilados para probar, calibrar o debug
    
    
    # Ejecutamos una vez la lectura
    #anemometer.debug()