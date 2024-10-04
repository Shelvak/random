#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2023-03-20 by Culebra v21.16.9
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

from time import sleep

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT


import argparse

parser = argparse.ArgumentParser(description="Opts", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--times", type=int, help="Times to use")
parser.add_argument("--use", type=str, help="Use N")
parser.add_argument("--second", action="store_true", help="Use 2nd item instead of 1st")
parser.add_argument("--delete", action="store_true", help="Delete input before use")
CONFIG = vars(parser.parse_args())




kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

vc = ViewClient(device, serialno, **kwargs2)

print(CONFIG)

def touch_number(device, n):
    match n:
        case 1:
            device.touchDip(56.38, 521.14, 0)
        case 2:
            device.touchDip(150.1, 523.43, 0)
        case 3:
            device.touchDip(258.29, 525.71, 0)
        case 4:
            device.touchDip(56.38, 583.14, 0)
        case 5:
            device.touchDip(155.43, 584.38, 0)
        case 6:
            device.touchDip(258.29, 591.24, 0)
        case 7:
            device.touchDip(52.57, 641.52, 0)
        case 8:
            device.touchDip(153.9, 644.57, 0)
        case 9:
            device.touchDip(256.76, 639.24, 0)
        case 0:
            device.touchDip(155.43, 697.14, 0)
        case _:
            raise ValueError("Invalid number")

for i in range(0, CONFIG['times'] or 10):
    # usar
    if CONFIG['second']:
        device.touchDip(350.48, 229.33, 0) # <= derecha
    else:
        device.touchDip(141.71, 229.33, 0) # <= izquierda
    sleep(0.5)

    # input
    device.touchDip(348.19, 381.71, 0)
    sleep(0.5)

    # Borrar
    if CONFIG['delete']:
        device.touchDip(361.14, 646.1, 0)

    for n in [*CONFIG['use']]:
        touch_number(device, int(n))
        sleep(0.5)

    # aceptar
    device.touchDip(355.81, 457.14, 0)
    sleep(0.5)

    # confirmar
    device.touchDip(212.57, 477.71, 0)
    sleep(2)

    # cerrar modal
    device.touchDip(207.24, 31.24, 0)
    sleep(0.5)
