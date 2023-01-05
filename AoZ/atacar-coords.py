#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2022-10-08 by Culebra v21.16.9
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

import argparse

parser = argparse.ArgumentParser(description="Opts", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--onlySpy", action="store_true", help="spy mode")
parser.add_argument("--changeCoords", action="store_true", help="Change Objective Coords")
parser.add_argument("--attackTime", type=int, help="AttackTime")
parser.add_argument("--repeat", type=int, help="Repeat attack")
parser.add_argument("--maxMarches", type=int, help="Max Marches")
parser.add_argument("--withFireworks", type=int, help="With Firewarks option")
parser.add_argument("--usePosition", type=bool, help="Use Position 6")
parser.add_argument("--times", type=int, help="Times to attack")
CONFIG = vars(parser.parse_args())

kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)

cities = {
    '752:472': 10,   ## SingleMalt
    '765:428': 3,   ## Stout
    '758:470': 3,   ## Scotch
    '746:470': 1,   ## Odiado
    '750:429': 10,   ## Apa
    '746:432': 10,   ## Cebada
    '736:464': 5,   ## Rot_is_back
    '718:448': 5,   ## Blended
    '771:445': 3,   ## Whiscardo
    '754:428': 3,   ## CanadianMalt
    '765:471': 5,   ## Shelaso
    '743:472': 5,   ## RotAntiBan
    '774:449': 3,   ## Irish
    '735:434': 3,   ## ELA_ForEver
    '769:470': 3,   ## Asado
    '744:469': 3,   ## Bourbon
    '772:447': 12,  ## Chopera
    '752:438': 0, ## Malta
    '777:447': 3, ## EscudroFM
    '774:451': 3, ## EscudroFM2
    '775:453': 3, ## EscudroFM3
    '758:432': 3,  ## MrT2
    '760:432': 3,  ## MrT1
    '759:434': 3  ## MrT3
}

attack_time = 0

def get_attack_time():
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


marches = 0
for coord, times in cities.items():
    if CONFIG['changeCoords'] or CONFIG['onlySpy']:
        print("Attacking " + coord)
        n1, n2 = coord.split(':')

        # Coords
        device.touchDip(177.52, 611.05, 0)
        time.sleep(0.3)
        # Coords 1
        device.touchDip(176.76, 348.19, 0)
        # device.press('KEYCODE_DEL')
        # device.press('KEYCODE_DEL')
        # device.press('KEYCODE_DEL')
        # Needed to find element
        vc.dump(window=-1)
        vc.findViewByIdOrRaise("id/no_id/3").setText(n1)

        # Coords 2
        device.touchDip(330.67, 358.86, 0)
        time.sleep(0.2)
        device.touchDip(330.67, 358.86, 0)
        # device.press('KEYCODE_DEL')
        # device.press('KEYCODE_DEL')
        # device.press('KEYCODE_DEL')
        # Needed to find element
        # vc.dump(window=-1)
        vc.findViewByIdOrRaise("id/no_id/3").setText(n2)

        # Accept
        device.touchDip(326.86, 349.71, 0)
        time.sleep(0.5)

        # Go
        device.touchDip(211.05, 425.9, 0)
        time.sleep(1)
        device.touchDip(201.9, 376.38, 0)

    if (CONFIG['onlySpy']):
        if (marches == (CONFIG['maxMarches'] or 3)):
            print("Waiting until: " + str(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ")))
            time.sleep(10)
            marches = 0

        # City
        device.touchDip(209.52, 342.86, 0)
        time.sleep(0.5)
        # Spy with fireworks
        if CONFIG['withFireworks'] != False:
            device.touchDip(208.0, 209.52, 0)
        else:
            device.touchDip(152.38, 230.1, 0)

        time.sleep(1)
        # Confirm friendly alliance
        ss = device.takeSnapshot(reconnect=True)
        text = device.imageToData(ss.crop((320, 1000, 320+400, 1000+100)))['text'][-1]
        print("Confirmar? :" + text)
        if text in ['Confirmar', 'Confirm']:
            device.touchDip(206.48, 405.33, 0)

        time.sleep(2)
        # Confirm
        device.touchDip(232.38, 515.81, 0)
        marches = marches + 1

    else:
        attack_time = CONFIG['attackTime'] or 0
        print(range(CONFIG['times'] or times))
        for i in range(CONFIG['times'] or times):
            print("Iterando times:" + str(i))
            for j in range(CONFIG['repeat'] or 1):
                print("Iterando Repeat:" + str(j))
                # City
                device.touchDip(204.95, 335.24, 0)
                time.sleep(0.5)
                # Attack
                # device.touchDip(265.9, 262.1, 0)
                device.touchDip(258.29, 224.76, 0)
                time.sleep(0.5)
                # Confirm just in case
                device.touchDip(206.48, 405.33, 0)
                time.sleep(2)
                # Troops 6
                if (CONFIG['usePosition'] != False):
                    device.touchDip(319.24, 144.0, 0)
                    time.sleep(1)

                if (attack_time == 0):
                    attack_time = (get_attack_time() * 2) + 2
                    print("Waiting " + str(attack_time ))

                # Confirm
                device.touchDip(359.62, 696.38, 0)
                time.sleep(0.5)
            time.sleep(attack_time)
        # if attackTime is present we only have 1 objective
        if (CONFIG['attackTime'] != None):
            break

    attack_time = 0
