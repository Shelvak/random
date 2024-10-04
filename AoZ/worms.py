#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2023-08-18 by Culebra v22.5.1
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

# evento => ignorar => drag => (checkear texto) click en worms => + (por las dudas de nivel) => ir => Leer restantes de hoy => (ignorar) => ataque
# => desplegar

# Eventos
device.touchDip(28.19, 459.43, 0)
time.sleep(0.5)
# drag para buscarlo
device.dragDip((256.76, 645.33), (364.95, 304.0), 1000, 2, 0)
time.sleep(0.5)
# click en worms
device.touchDip(257.52, 591.24, 0)
time.sleep(0.5)
# click en +
device.touchDip(191.24, 640.76, 0)
time.sleep(0.5)
# click en ir
device.touchDip(222.48, 679.62, 0)
time.sleep(0.5)
# click en leer restantes de hoy
device.touchDip(374.86, 453.33, 0)
time.sleep(0.5)
# click en ataque
device.touchDip(368.76, 699.43, 0)
time.sleep(0.5)
