#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2022-07-24 by Culebra v21.16.9
                      __    __    __    __
                     /  \  /  \  /  \  /  \
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
"""


import os
import re
import sys
import time

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT

def puts(msg):
    print(str(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ")) + msg)

# TAG = 'CULEBRA'
# _s = 5
# _v = '--verbose' in sys.argv
# pid = os.getpid()

from datetime import datetime
def now():
    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    return datetime.timestamp(dt)


class AutoKill():
    def __init__(self):
        kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        self.device, self.serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

        kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
        self.vc = ViewClient(self.device, self.serialno, **kwargs2)

        self.ataques = 0
        # self.tiempo = now()

    def autokill(self):
        puts("Atacando... Nº " + str(self.ataques))
        # Estando en la ciudad vamos al mapa
        self.click_en_casa_o_mapa()

        # Buscar y atacar
        self.atacar()

        # Volver a la ciudad
        self.click_en_casa_o_mapa()

        # Esperar a que llegue el ataque
        # self.vc.sleep(300)
        self.esperar_y_ayudar(300)

        self.curar_y_esperar()

        self.ayudar()

        if (self.necesita_combustible()):
            self.cargar_combustible()

        self.ataques += 1

        # Seguir atacando
        self.autokill()

    def atacar(self):
        puts("Atacando...")
        ## Aca boton verde
        self.device.touchDip(380.19, 582.86, 0)

        self.vc.sleep(1)

        ## Confirmar busqueda
        self.device.touchDip(367.24, 678.1, 0)

        self.vc.sleep(4)

        # Click en bicho
        self.device.touchDip(209.52, 335.24, 0)
        self.vc.sleep(1)
        self.device.touchDip(209.52, 335.24, 0)
        self.vc.sleep(1)

        # Atacar
        self.device.touchDip(224.76, 486.86, 0)

        self.vc.sleep(3)

        # Click en formacion 2
        # self.device.touchDip(158.48, 35.81, 0)
        self.device.touchDip(184.38, 137.14, 0)
        self.vc.sleep(1)

        # Confirmar
        # TODO: Leer tiempo?
        self.device.touchDip(364.95, 701.71, 0)

        self.vc.sleep(3)

    def click_en_casa_o_mapa(self):
        puts("Click en casa o mapa")

        # Casa
        self.device.touchDip(42.67, 691.05, 0)
        self.vc.sleep(3)

    def curar_y_esperar(self):
        puts("Curando")
        # Click en + hospital
        self.device.touchDip(331.43, 409.14, 0)
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(2)
        # Confirmar
        # TODO: Leer el tiempo
        self.device.touchDip(369.52, 695.62, 0)
        self.vc.sleep(2)
        # Pedir ayuda
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)
        self.device.touchDip(331.43, 409.14, 0)
        # (5:42 minutos)
        self.esperar_y_ayudar(340)
        # Sacar los wachines
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)


    def cargar_combustible(self):
        puts("Cargando combustible")
        # Click en parte de combustible
        self.device.touchDip(79.24, 45.71, 0)

        self.vc.sleep(1)
        # Click en 1er usar
        self.device.touchDip(329.14, 285.71, 0)
        self.vc.sleep(1)

        # Confirmar
        self.device.touchDip(207.24, 395.43, 0)
        self.vc.sleep(1)

        # Click fuera del modal
        self.device.touchDip(158.48, 91.43, 0)
        self.vc.sleep(1)

    def necesita_combustible(self):
        # ahora = now()

        # cada 1 hora, skippeamos junto con los ataques
        # if (ahora - self.tiempo) > 3600 and (self.ataques % 2) == 0:
        #     puts(str(ahora) + " Pasaron 3 horas... reseteando")
        #     self.tiempo = ahora
        #     self.ataques = 0
        #     return False

        # cada 3 ataques
        return ((self.ataques % 3) == 2)
            # return

        # return True

    def ayudar(self):
        # Click en Alianza
        self.device.touchDip(321.52, 691.81, 0)
        self.vc.sleep(1)
        # Click en Ayuda
        self.device.touchDip(232.38, 521.14, 0)
        self.vc.sleep(3)

        # Click en Ayudar
        self.device.touchDip(219.43, 690.29, 0)
        self.vc.sleep(1)
        # Click en Volver(a alianza)
        self.device.touchDip(41.14, 19.05, 0)
        self.vc.sleep(1)
        # Click en Volver(a donde estaba)
        self.device.touchDip(24.38, 25.14, 0)
        self.vc.sleep(1)

    def esperar_y_ayudar(self, tiempo):
        puts("Esperando " + str(tiempo) + "s y ayudando")
        start = now()

        while (now() - start) < tiempo:
            self.ayudar()
            self.vc.sleep(5)


if __name__ == "__main__":
    auto = AutoKill()
    auto.autokill()
