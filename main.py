#!/usr/bin/python3

import sys
import time

from anemometer import Anemometer
from termometer import Termometer

if __name__ == "__main__":
    anemometer = Anemometer()
    termometer = Termometer()

    ## Inicio lecturas de datos de anemometro y termometros
    anemometer.start_read()
    termometer.start_read()

    ## Espera de 3 segundos recopilando los primeros datos
    time.sleep(3)
    count = 0

    """
    Anulamos la lectura continua para que eso lo realice crontab
    """

    ## Muestro constantemente los datos recopilados para probar, calibrar o debug
    while True:
        try:
            anemometer.start_read()
            termometer.start_read()
            ## Cuando ha tomado 5 lecturas devuelve y resetea contadores
            ## para indicar que comienza una nueva medición.
            count += 1
            #print('Contador:', count)
            if (count % 5) == 0:
                #print(anemometer.get_all_datas())
                anemometer.debug()
            else:
                anemometer.debug()
        except KeyboardInterrupt:
            anemometer.stop_read()
            sys.exit(0)
        time.sleep(10)
    
    # Ejecutamos una vez la lectura
    #anemometer.debug()