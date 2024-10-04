#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2024-01-21 by Culebra v22.5.1
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

vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(56.38, 521.14, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

vc.sleep(_s)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(150.1, 523.43, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(258.29, 525.71, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

vc.sleep(_s)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(155.43, 584.38, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(258.29, 591.24, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

vc.sleep(_s)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(52.57, 641.52, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(153.9, 644.57, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

vc.sleep(_s)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(256.76, 639.24, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

device.touchDip(155.43, 697.14, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

vc.sleep(_s)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
no_id2 = vc.findViewByIdOrRaise("id/no_id/2")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")

