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
from datetime import datetime

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT

def puts(msg):
    print(str(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ")) + msg)

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
        # argv will only be used for fuel from the moment
        self.use_fuel = (len(sys.argv) == 1)
        # self.time = now()

    def autokill(self):
        puts("Attacking... Nº " + str(self.ataques))
        # Estando en la ciudad vamos al mapa
        self.click_en_casa_o_mapa()

        # Buscar y atacar
        self.atacar()

        # Volver a la ciudad
        self.click_en_casa_o_mapa()

        # Esperar a que llegue el ataque
        self.wait_and_help(self.attack_time, 'attack')

        self.curar_y_esperar()

        self.help()

        if self.use_fuel:
            self.cargar_combustible()

        self.ataques += 1

        # Seguir atacando
        self.autokill()

    def atacar(self):
        puts("Attacking...")
        ## Aca boton verde
        self.device.touchDip(380.19, 582.86, 0)

        self.vc.sleep(1)

        ## Confirmar busqueda
        self.device.touchDip(367.24, 678.1, 0)

        self.vc.sleep(3)

        # Click en bicho
        self.device.touchDip(209.52, 335.24, 0)
        self.vc.sleep(1)
        self.device.touchDip(209.52, 335.24, 0)
        self.vc.sleep(1)

        # Atacar
        self.device.touchDip(224.76, 486.86, 0)
        self.vc.sleep(2)

        # Click en formacion 2
        # self.device.touchDip(158.48, 35.81, 0)
        self.device.touchDip(184.38, 137.14, 0)
        self.vc.sleep(1)

        # Confirmar
        self.attack_time = self.get_flew_time()
        self.device.touchDip(364.95, 701.71, 0)
        self.attacking_until = now() + (self.attack_time * 2)
        self.vc.sleep(2)

    def click_en_casa_o_mapa(self):
        puts("Click en casa o mapa")

        # Casa
        self.device.touchDip(42.67, 691.05, 0)
        self.vc.sleep(3)

    def curar_y_esperar(self):
        puts("Curando")
        # Click en + hospital
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(2)
        # Confirmar
        heal_time = self.get_heal_time()

        if (heal_time < self.attack_time):
            heal_time = self.attack_time

        self.device.touchDip(369.52, 695.62, 0)
        self.vc.sleep(1)
        # Pedir ayuda
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)
        self.device.touchDip(331.43, 409.14, 0)
        self.wait_and_help(heal_time, 'heal')
        # Sacar los wachines
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)


    def cargar_combustible(self):
        puts("Checkeando combustible")
        # Click en parte de combustible
        self.device.touchDip(79.24, 45.71, 0)
        self.vc.sleep(1)

        if (self.get_current_fuel() < 20):
            puts("Cargando combustible...")
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
        # if (ahora - self.time) > 3600 and (self.ataques % 2) == 0:
        #     puts(str(ahora) + " Pasaron 3 horas... reseteando")
        #     self.time = ahora
        #     self.ataques = 0
        #     return False

        # cada 3 ataques
        return ((self.ataques % 3) == 2)
            # return

        # return True

    def help(self):
        # Click en Alianza
        self.device.touchDip(321.52, 691.81, 0)
        self.vc.sleep(1)
        # Click en Ayuda
        self.device.touchDip(232.38, 521.14, 0)
        self.vc.sleep(2)

        # Click en Ayudar
        self.device.touchDip(219.43, 690.29, 0)
        self.vc.sleep(1)
        # Click en Volver(a alianza)
        self.device.touchDip(41.14, 19.05, 0)
        self.vc.sleep(1)
        # Click en Volver(a donde estaba)
        self.device.touchDip(24.38, 25.14, 0)
        self.vc.sleep(1)

    def wait_and_help(self, time, kind):
        puts("Waiting " + str(time) + "s & helping")
        start = now()

        while (now() - start) < time:
            self.help()
            if (kind == 'heal' and self.attack_ready() and self.heal_ready()):
                return
            self.vc.sleep(5)

    def attack_ready(self):
        return (now() >= self.attacking_until)

    def get_heal_time(self):
        kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        device, _serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

        ss = device.takeSnapshot()
        raw_time = device.imageToData(
            ss.crop((747,1635,747+178, 1635+84)).convert("L") # cortar el tiempo y monocromear
        )['text'][-1]

        parts = list(map(lambda n: int(n), raw_time.split(':')))

        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        else:
            return parts[0]

    def heal_ready(self):
        kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        device, _serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

        ss = device.takeSnapshot()
        results = device.imageToData(
            ss.crop((704,1210,704+271,1210+157)).convert("L") # cortar el tiempo y monocromear
        )['text']

        return 'Curacion' not in results

    def get_flew_time(self):
        kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        device, _serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

        ss = device.takeSnapshot()
        raw_time = device.imageToData(
            ss.crop((698,1698,698+328,1798)).convert("L") # cortar el tiempo y monocromear
        )['text'][-1]

        parts = list(map(lambda n: int(n), raw_time.split(':')))

        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        else:
            return parts[0]

    def get_current_fuel(self, retries = 0):
        if retries > 2:
            return False

        try:
            kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
            device, _serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

            ss = device.takeSnapshot()
            return int(
                device.imageToData(
                    ss.crop((633,533,633+130,533+70)).convert("L") # cortar el tiempo y monocromear
                )['text'][-1]
            )
        except:
            self.vc.sleep(1)
            return self.get_current_fuel(retries + 1)


if __name__ == "__main__":
    auto = AutoKill()
    auto.autokill()
