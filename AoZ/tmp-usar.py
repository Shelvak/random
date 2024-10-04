#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2023-07-21 by Culebra v22.5.1
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


for i in range(65):
    device.touchDip(143.24, 424.38, 0)
    vc.sleep(1)

    device.touchDip(341.33, 377.9, 0)
    vc.sleep(1)

    device.touchDip(60.19, 525.71, 0)
    vc.sleep(1)

    device.touchDip(327.62, 326.86, 0)
    vc.sleep(1)

    device.touchDip(216.38, 489.14, 0)
    vc.sleep(1)

    device.touchDip(401.52, 318.48, 0)
    vc.sleep(1)
