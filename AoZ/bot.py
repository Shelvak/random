#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time
from datetime import datetime

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT

HEAL_TIME = 120
ATTACK_TIME = 180
MIN_SLEEP_TIME = 0.8

def puts(msg):
    print(str(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ")) + msg)

def now():
    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    return datetime.timestamp(dt)


class Bot():
    def __init__(self):
        kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        self.device, self.serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

        kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
        self.vc = ViewClient(self.device, self.serialno, **kwargs2)

        self.attacks = 0
        # self.time = now()

    def autokill(self):
        puts("Atacando... Nº " + str(self.attacks))
        # Estando en la ciudad vamos al mapa
        self.home_or_map()

        # Buscar y attack
        self.attack()

        # Volver a la ciudad
        self.home_or_map()

        # Esperar a que llegue el ataque
        # self.vc.sleep(300)
        self.wait_and_help(ATTACK_TIME)

        self.heal_and_wait()

        self.help()

        if (self.need_to_refuel()):
            self.refuel()

        self.attacks += 1

        # Seguir atacando
        self.autokill()

    def attack(self):
        puts("Atacando...")
        ## Aca boton verde
        self.device.touchDip(380.19, 582.86, 0)

        self.vc.sleep(MIN_SLEEP_TIME)

        ## Confirmar busqueda
        self.device.touchDip(367.24, 678.1, 0)

        self.vc.sleep(3)

        # Click en bicho
        self.device.touchDip(209.52, 335.24, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(209.52, 335.24, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

        # Atacar
        self.device.touchDip(224.76, 486.86, 0)
        self.vc.sleep(2)

        # Click en formacion 2
        # self.device.touchDip(158.48, 35.81, 0)
        self.device.touchDip(184.38, 137.14, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

        # Confirmar
        # TODO: Leer time?
        self.device.touchDip(364.95, 701.71, 0)
        self.vc.sleep(2)

    def home_or_map(self):
        puts("Click en casa o mapa")

        # Casa
        self.device.touchDip(42.67, 691.05, 0)
        self.vc.sleep(3)

    def heal_and_wait(self):
        puts("Curando")
        # Click en + hospital
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(2)
        # Confirmar
        # TODO: Leer el time
        self.device.touchDip(369.52, 695.62, 0)
        self.vc.sleep(1)
        # Pedir ayuda
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)
        self.device.touchDip(331.43, 409.14, 0)
        # (5:42 minutos)
        self.wait_and_help(HEAL_TIME)
        # Sacar los wachines
        self.device.touchDip(331.43, 409.14, 0)
        self.vc.sleep(1)


    def refuel(self):
        puts("Cargando combustible")
        # Click en parte de combustible
        self.device.touchDip(79.24, 45.71, 0)

        self.vc.sleep(MIN_SLEEP_TIME)
        # Click en 1er usar
        self.device.touchDip(329.14, 285.71, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

        # Confirmar
        self.device.touchDip(207.24, 395.43, 0)
        self.vc.sleep(1)

        # Click fuera del modal
        self.device.touchDip(158.48, 91.43, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

    def need_to_refuel(self):
        if (self.skip_refuel):
            return False
        # ahora = now()

        # cada 1 hora, skippeamos junto con los attacks
        # if (ahora - self.time) > 3600 and (self.attacks % 2) == 0:
        #     puts(str(ahora) + " Pasaron 3 horas... reseteando")
        #     self.time = ahora
        #     self.attacks = 0
        #     return False

        # cada 3 attacks
        return ((self.attacks % 3) == 2)
            # return

        # return True

    def help(self):
        # Click en Alianza
        self.device.touchDip(321.52, 691.81, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # Click en Ayuda
        self.device.touchDip(232.38, 521.14, 0)
        self.vc.sleep(2)

        # Click en Ayudar
        self.device.touchDip(219.43, 690.29, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # Click en Volver(a alianza)
        self.device.touchDip(41.14, 19.05, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

        self.back()

    def wait_and_help(self, time):
        puts("Waiting " + str(time) + "s & helping")
        start = now()

        while (now() - start) < time:
            self.vc.sleep(5)
            self.help()

    def heal_zombie(self):
        # labo
        self.device.touchDip(161.52, 585.14, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # Sala de trat
        self.device.touchDip(163.81, 402.29, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # cura
        self.device.touchDip(53.33, 214.86, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # +1 cura
        self.device.touchDip(81.52, 686.48, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

        self.back()
        self.back()

    def back(self):
        # Click en Volver
        self.device.touchDip(24.38, 22.1, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

    def sell_in_merchant(self):
        # Muelle
        self.device.touchDip(275.05, 208.0, 0)
        self.vc.sleep(0.5)
        # Mercader
        self.device.touchDip(289.52, 287.24, 0)
        self.vc.sleep(0.5)
        # Vender
        self.device.touchDip(208.76, 277.33, 0)
        self.vc.sleep(0.5)

        # comida
        self.device.touchDip(144.76, 380.19, 0)
        self.vc.sleep(0.5)
        # Petro
        self.device.touchDip(348.19, 378.67, 0)
        self.vc.sleep(0.5)
        # acero
        self.device.touchDip(346.67, 377.9, 0)
        self.vc.sleep(0.5)
        # mineral
        self.device.touchDip(348.95, 493.71, 0)
        self.vc.sleep(0.5)

        self.back()

    def safe_click(self):
        self.device.touchDip(380.19, 42.67, 0)
        self.vc.sleep(0.2)

    def harvest(self):
        # Habilidad
        self.device.touchDip(378.67, 576.76, 0)
        # checkear tiempo
        # Seleccionar
        self.device.touchDip(60.19, 586.67, 0)
        # Usar
        self.device.touchDip(339.05, 347.43, 0)

    def donate(self):
        # Donar
        # Ir alianza
        self.device.touchDip(316.95, 700.19, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # Tecnologia
        self.device.touchDip(189.71, 618.67, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # seleccionar 1º
        self.device.touchDip(220.95, 205.71, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # donar
        self.device.touchDip(127.24, 465.52, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(127.24, 465.52, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(127.24, 465.52, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(127.24, 465.52, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # TODO: checkear el Desea donar?
        # coinfirmar donar todo
        self.device.touchDip(116.57, 400.76, 0)
        self.vc.sleep(MIN_SLEEP_TIME)

        self.back()
        self.back()
        self.back()
        # 32400 /

    def almacen(self):
        self.device.touchDip(347.43, 274.29, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(286.48, 368.76, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # 2x1 Acero
        # 10 veces
        self.device.touchDip(115.05, 515.81, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        # 2x2 Mineral
        # device.touchDip(306.29, 518.86, 0)

    def mostro_alianza(self):
        # Alianza
        self.device.touchDip(316.19, 691.05, 0)
        self.vc.sleep(0.5)
        # Bicho
        self.device.touchDip(210.29, 464.76, 0)
        self.vc.sleep(0.5)
        # de aca 2 veces
        self.device.touchDip(211.81, 294.86, 0)
        self.vc.sleep(0.5)
        # confirmar
        self.device.touchDip(335.24, 695.62, 0)
        self.vc.sleep(0.5)
        # salir
        self.device.touchDip(376.38, 150.86, 0)
        self.vc.sleep(0.5)
        # Confirmar
        self.device.touchDip(134.86, 392.38, 0)
        self.vc.sleep(6)
        # Vale
        self.device.touchDip(207.24, 554.67, 0)
        self.vc.sleep(0.5)

    def gather(self):
        # Verde
        self.device.touchDip(386.29, 578.29, 0)
        self.vc.sleep(0.5)
        # mina acero
        self.device.touchDip(170.67, 584.38, 0)
        self.vc.sleep(0.5)

        # ir
        self.device.touchDip(352.0, 676.57, 0)
        self.vc.sleep(0.5)

        # Click en recolectar
        self.device.touchDip(291.05, 328.38, 0)
        self.vc.sleep(0.5)
        self.device.touchDip(291.05, 328.38, 0)
        self.vc.sleep(0.5)

        # Swipe tropas al 100%
        self.device.dragDip((89.14, 698.67), (231.62, 697.14), 1000, 2, 0)
        self.vc.sleep(0.5)
        # Confirmar tropa
        self.device.touchDip(339.05, 696.38, 0)
        self.vc.sleep(1)

    def harvest_internal_mines(self):
        # Moverse para adentro
        self.device.dragDip((350.48, 532.57), (60.19, 307.05), 1000, 1, 0)
        self.vc.sleep(1)

        self.device.touchDip(141.71, 387.81, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(188.95, 419.05, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(236.95, 452.57, 0)
        self.vc.sleep(MIN_SLEEP_TIME)
        self.device.touchDip(284.19, 484.57, 0)
        self.vc.sleep(MIN_SLEEP_TIME)


    def get_time(self):
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

    def get_current_fuel(self):
        kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
        device, _serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

        ss = device.takeSnapshot()
        raw_time = device.imageToData(
            ss.crop((633,533,633+130,533+70)).convert("L") # cortar el tiempo y monocromear
        )['text'][-1]

        parts = list(map(lambda n: int(n), raw_time.split(':')))

        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        else:
            return parts[0]



# pasos
Confirmar si es que
mercader
almacen
gratis global
oficiales
recolectar minas internas
donar
bicho
ayudar
habilidad
# MAPA
recolectar x3

# SI es un rato antes de las 21
misiones diarias


# if __name__ == "__main__":
#     bot = Bot()
#     bot.autokill()
