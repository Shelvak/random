#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013-2022  Diego Torres Milano
Created on 2023-03-30 by Culebra v21.16.9
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
com_camelgames_aoz___id_unitySurfaceView = vc.findViewByIdOrRaise("com.camelgames.aoz:id/unitySurfaceView")
com_camelgames_aoz___id_unitySurfaceView = vc.findViewWithContentDescriptionOrRaise(u'''Game view''')

device.touchDip(157.71, 397.71, 0)
vc.sleep(5)
vc.dump(window=-1)

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
com_camelgames_aoz___id_unitySurfaceView = vc.findViewByIdOrRaise("com.camelgames.aoz:id/unitySurfaceView")
com_camelgames_aoz___id_unitySurfaceView = vc.findViewWithContentDescriptionOrRaise(u'''Game view''')

vc.sleep(_s)
