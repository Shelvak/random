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
from time import sleep
from datetime import datetime

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT
import pytesseract

class Retry(Exception):
    pass

def puts(msg):
    print(str(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ")) + msg)

def now():
    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    return datetime.timestamp(dt)

def connect():
    kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False, 'serialno': os.environ.get('SERIAL')}
    device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

    return [device, serialno]


class AutoKill():
    def __init__(self):
        self.device, self.serialno = connect()

        kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
        self.vc = ViewClient(self.device, self.serialno, **kwargs2)

        self.ataques = 0
        # argv will only be used for fuel from the moment
        # print(sys.argv)
        self.use_fuel = False # (len(sys.argv) == 1)
        self.home = None
        self.lastDonation = now()
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

        self.wait_and_help(self.attack_time, 'heal')
        # self.curar_y_esperar()
        if (now() - self.lastDonation) >= 9000: # 10 donations
            self.donate()

        self.help()

        if self.use_fuel:
            self.cargar_combustible()

        self.ataques += 1

        # Seguir atacando
        self.autokill()

    def atacar(self):
        self.home = self.home or self.get_current_coords()

        puts("Attacking...")
        ## Aca boton verde
        puts("Boton verde")
        self.device.touchDip(380.19, 582.86, 0)

        sleep(1)

        ## Confirmar busqueda
        puts("Confirmar busqueda")
        self.device.touchDip(367.24, 678.1, 0)
        sleep(2)
        # Click en bicho
        puts("Doble Click en bicho")
        self.device.touchDip(190.48, 303.24, 0)
        self.device.touchDip(190.48, 303.24, 0)
        sleep(1)

        coords = self.get_current_coords()

        # si no encontro una goma
        if coords is not None and self.home is not None and coords == self.home:
            puts("no se encontro monstruo")
            raise Retry()

        # Atacar al bicho
        self.device.touchDip(204.95, 491.43, 0)
        sleep(1)

        # Check if somebody is attacking
        print("Ahora viene el checkeo")
        # if len(set(['Cancelar', 'Cancel']) & set(self.take_screenshot((260, 980, 260+500, 980+120)))) > 0:
        #     self.device.touchDip(300, 1020, 0)
        #     return self.atacar()

        # Obtener tiempo de ataque
        try:
            self.attack_time = self.get_flew_time()
        except:
            raise Retry()

        # Maximo n minutos
        if self.attack_time > (3 * 60):
            raise Retry()

        # Click en formacion 2
        # self.device.touchDip(184.38, 137.14, 0)
        # sleep(0.5)

        # Confirmar ataque
        self.device.touchDip(364.95, 701.71, 0)
        self.attacking_until = now() + (self.attack_time * 2)
        sleep(2)

    def click_en_casa_o_mapa(self):
        puts("Click en casa o mapa")

        # Casa
        self.device.touchDip(42.67, 691.05, 0)
        sleep(3)

    def curar_y_esperar(self, retry=0):
        puts("Curando")
        # Click en + hospital
        self.device.touchDip(331.43, 409.14, 0)
        sleep(1)
        self.device.touchDip(331.43, 409.14, 0)
        sleep(2)
        # Confirmar
        heal_time = self.get_heal_time(retry)

        if (heal_time < self.attack_time):
            heal_time = self.attack_time

        self.device.touchDip(369.52, 695.62, 0)
        sleep(1)
        # Pedir ayuda
        self.device.touchDip(331.43, 409.14, 0)
        sleep(1)
        self.device.touchDip(331.43, 409.14, 0)
        self.wait_and_help(heal_time, 'heal')
        # Sacar los wachines
        self.device.touchDip(331.43, 409.14, 0)
        sleep(1)


    def cargar_combustible(self):
        puts("Checkeando combustible")
        # Click en parte de combustible
        self.device.touchDip(79.24, 45.71, 0)
        sleep(1)

        if (self.get_current_fuel() < 20):
            puts("Cargando combustible...")
            # Click en 1er usar
            self.device.touchDip(329.14, 285.71, 0)
            sleep(1)

            # Confirmar
            self.device.touchDip(207.24, 395.43, 0)
            sleep(1)

        # Click fuera del modal
        # self.device.touchDip(158.48, 91.43, 0)
        self.device.touchDip(161.52, 89.14, 0)
        sleep(1)

    def help(self):
        # Click en Alianza
        self.device.touchDip(321.52, 691.81, 0)
        sleep(1)
        # Click en Ayuda
        self.device.touchDip(220.38, 489.14, 0)
        sleep(2)

        # Click en Ayudar
        self.device.touchDip(219.43, 690.29, 0)
        sleep(1)
        # Click en Volver(a alianza)
        self.device.touchDip(41.14, 19.05, 0)
        sleep(1)
        # Click en Volver(a donde estaba)
        self.device.touchDip(24.38, 25.14, 0)
        sleep(1)

    def wait_and_help(self, time, kind):
        puts("Waiting " + str(time) + "s & helping")
        start = now()

        while (now() - start) < time:
            self.help()
            if (kind == 'heal' and self.attack_ready() and self.heal_ready()):
                return
            sleep(5)

    def attack_ready(self):
        return (now() >= self.attacking_until)

    def get_heal_time(self, retry):
        try:
            device, _serialno = connect()

            ss = device.takeSnapshot()
            raw_time = device.imageToData(
                ss.crop((747,1635,747+178, 1635+84)).convert("L") # cortar el tiempo y monocromear
            )['text'][-1]

            parts = list(map(lambda n: int(n), raw_time.split(':')))

            if len(parts) == 2:
                return parts[0] * 60 + parts[1]
            else:
                return parts[0]
        except:
            return self.attack_time

            # puts("Bombaso en curar...")
            # sleep(1)
            # self.device.press('BACK')
            # sleep(1)
            # self.device.press('BACK')
            # sleep(1)
            # self.device.press('BACK')
            # sleep(1)
            # # Click fuera del modal
            # self.device.touchDip(158.48, 91.43, 0)
            # return self.get_heal_time(retry + 1)

    def heal_ready(self):
        try:
            device, _serialno = connect()

            ss = device.takeSnapshot()
            results = device.imageToData(
                ss.crop((785,1307,785+121,1307+38)).convert("L") # cortar el tiempo y monocromear
            )['text']
            puts("curando", str(results))

            return len(list(filter(lambda e: (re.match(r"Cura", e)), results))) > 0
        except:
            return False

    def get_flew_time(self):
        device, _serialno = connect()

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
            return 100 # fake false condition

        try:
            device, _serialno = connect()

            ss = device.takeSnapshot()
            return int(
                device.imageToData(
                    ss.crop((633,533,633+130,533+70)).convert("L") # cortar el tiempo y monocromear
                )['text'][-1]
            )
        except:
            sleep(1)
            return self.get_current_fuel(retries + 1)


    def get_current_coords(self):
        try:
            coords = []
            values = self.take_screenshot((387,1585,387+250,1585+41))

            for r_v in values:
                try:
                    v = int(r_v)
                    coords.append(v)
                except:
                    pass

            puts("coords: " + str(coords))
            return coords

        except Exception as e:
            puts(str(e))
            return

    def take_screenshot(self, coords):
        device, _serialno = connect()

        ss = device.takeSnapshot()
        r = device.imageToData(ss.crop(coords).convert("L"))['text']
        puts("Agarramos el confirm?? resultado: " + str(r))
        return r

    def donate(self):
        puts("Donating...")
        # Click en Alianza
        self.device.touchDip(318.48, 694.1, 0)
        sleep(1)
        # Click en Tecnologia
        self.device.touchDip(200.38, 592.0, 0)
        sleep(1)
        # Click en primera tecnologia
        self.device.touchDip(240.0, 176.76, 0)
        sleep(0.5)
        # 4 clicks
        self.device.touchDip(81.52, 466.29, 0)
        sleep(0.5)
        self.device.touchDip(81.52, 466.29, 0)
        sleep(0.5)
        self.device.touchDip(81.52, 466.29, 0)
        sleep(0.5)
        self.device.touchDip(81.52, 466.29, 0)
        sleep(0.5)
        # Aceptar full donation
        # self.device.touchDip(156.95, 470.86, 0)
        self.device.touchDip(69.33, 404.57, 0)
        sleep(0.5)
        # Click fuera
        self.device.press('BACK')
        sleep(0.5)
        self.device.press('BACK')
        sleep(0.5)

        self.lastDonation = now()

def start():
    try:
        auto = AutoKill()
        auto.autokill()
    except Retry as e:
        auto.device.press('BACK')
        auto.device.press('BACK')
        sleep(1)
        auto.device.press('BACK')
        auto.device.press('BACK')
        # auto.device.touchDip(389.33, 38.86, 0)
        # auto.device.touchDip(161.52, 89.14, 0)
        auto.device.touchDip(158.48, 91.43, 0)
        auto.device.touchDip(158.48, 91.43, 0)
        auto.help()
        start()
    except Exception as e:
        puts("Bombaso")
        puts(str(e))
        sleep(60)
        auto.device.press('BACK')
        sleep(1)
        auto.device.press('BACK')
        auto.device.press('BACK')
        auto.device.touchDip(158.48, 91.43, 0)
        # auto.device.touchDip(389.33, 38.86, 0)
        # auto.device.touchDip(389.33, 38.86, 0)
        # auto.device.touchDip(161.52, 89.14, 0)
        # auto.device.touchDip(161.52, 89.14, 0)
        start()

if __name__ == "__main__":
    start()
