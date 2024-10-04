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

for i in range(1, 150):
    # usar
    device.touchDip(138.67, 220.19, 0)
    vc.sleep(1)
    # Click en input
    device.touchDip(348.19, 381.71, 0)
    vc.sleep(1)
    # 9
    #device.touchDip(260.57, 645.33, 0)
    device.touchDip(275.05, 638.48, 0)
    vc.sleep(1)
    # aceptar
    device.touchDip(355.81, 457.14, 0)
    # device.touchDip(371.81, 463.24, 0)
    vc.sleep(1)
    # usar
    device.touchDip(212.57, 477.71, 0)
    # device.touchDip(352.76, 458.67, 0)
    vc.sleep(3)
    # Click fuera
    device.touchDip(207.24, 31.24, 0)
    vc.sleep(1)
