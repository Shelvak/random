#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2024-02-16 by Culebra v22.5.1
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


TAG = 'CULEBRA'
_s = 5
_v = '--verbose' in sys.argv
pid = os.getpid()


kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)


ruins_coords = {
    'mision_4': (320.76, 390.86, 0),
    'mision_3': (120.38, 357.33, 0),
    'mision_2': (317.71, 155.43, 0),
    'mision_1': (102.1, 134.1, 0),
}


for i in range(1, 5):
    # print(f'Empezando en {5-i} segundos')

    # Click en prosperidad
    device.touchDip(164.57, 3.81, 0)
    time.sleep(0.5)

    # Click en "Ir a ruinas"
    device.touchDip(230.1, 371.05, 0)
    time.sleep(2)

    # click en Explorar
    device.touchDip(259.05, 217.9, 0)
    time.sleep(1)

    # Click en nº mision
    device.touchDip(*ruins_coords['mision_' + str(i)])
    time.sleep(0.5)
    # confirmar exploracion
    if i == 1:
        device.touchDip(304.76, 597.33, 0)

    # drag para posicion
    device.dragDip((198.86, 529.52), (204.95, 238.48), 1000, 2, 0)
    time.sleep(0.5)

    # Click en mision x2
    device.touchDip(364.19, 680.38, 0)
    time.sleep(1)

    # Confirmar
    device.touchDip(350.48, 701.71, 0)
    time.sleep(0.5)


# Click en prosperidad
device.touchDip(164.57, 3.81, 0)
time.sleep(0.5)

# Click en "Ir a ruinas"
device.touchDip(230.1, 371.05, 0)
time.sleep(2)

# Click en juicio final
device.touchDip(149.33, 216.38, 0)
time.sleep(1)
# click confirmar
device.touchDip(350.48, 701.71, 0)
time.sleep(50)

for i in range(2):
    # Click en prosperidad
    device.touchDip(164.57, 3.81, 0)
    time.sleep(0.5)
    # Click en "Ir a ruinas"
    device.touchDip(230.1, 371.05, 0)
    time.sleep(2)
    # Click en agrupar
    device.touchDip(304.0, 307.05, 0)
    time.sleep(1)
    # Click en confirmar
    device.touchDip(350.48, 701.71, 0)
    time.sleep(1)
