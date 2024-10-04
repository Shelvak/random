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

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT


TAG = 'CULEBRA'
_s = 5
_v = '--verbose' in sys.argv
pid = os.getpid()


kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)

for item in range(5):
    device.touchDip(201.9, 376.38, 0)
    time.sleep(0.5)

    device.touchDip(265.9, 262.1, 0)
    time.sleep(2)
    device.touchDip(319.24, 144.0, 0)
    time.sleep(1)
    device.touchDip(359.62, 696.38, 0)
    time.sleep(133)
