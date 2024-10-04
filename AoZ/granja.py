#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time

from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT


kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': True, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)

#confirmar el del dia
device.touchDip(248.38, 530.29, 0)
vc.sleep(1)

## Click en barra
device.touchDip(358.86, 40.38, 0)
vc.sleep(1)
device.touchDip(358.86, 40.38, 0)
vc.sleep(1)
device.touchDip(358.86, 40.38, 0)
vc.sleep(1)
device.touchDip(358.86, 40.38, 0)
vc.sleep(1)




        # Reclutar oficiales
        self.device.touchDip(68.57, 387.81, 0)
        # Reclutar blanco
        self.device.touchDip(110.48, 609.52, 0)
# Click para que se salga la animacion
self.device.touchDip(357.33, 508.19, 0)
self.device.touchDip(357.33, 508.19, 0)
# Confirmar
self.device.touchDip(309.33, 624.76, 0)

# Volver
device.touchDip(24.38, 22.1, 0)
vc.sleep(0.5)

 # Casa

device.touchDip(51.05, 694.1, 0)

# Moverme para adentro
device.dragDip((348.95, 528.0), (32.0, 468.57), 1000, 1, 0)
# click ayuda
        self.device.touchDip(137.9, 325.33, 0)
        A
# Recolectar mina de arriba
self.device.touchDip(309.33, 450.29, 0)
# Petroleo
        self.device.touchDip(139.43, 227.05, 0)
# Acero A
device.touchDip(125.71, 470.1, 0)
# Mineral
self.device.touchDip(354.29, 380.19, 0)





# Misiones diariasç
# Misiones
device.touchDip(121.14, 691.81, 0)
# Diaria
device.touchDip(125.71, 79.24, 0)
# 1
device.touchDip(47.24, 182.1, 0)
# click fuera
device.touchDip(384.0, 128.76, 0)
#2
device.touchDip(105.9, 183.62, 0)
# click fuera
device.touchDip(384.0, 128.76, 0)
# 3
device.touchDip(176.76, 179.05, 0)
# click fuera
device.touchDip(384.0, 128.76, 0)
# 4
device.touchDip(236.19, 182.86, 0)
# click fuera
device.touchDip(384.0, 128.76, 0)
# 5
device.touchDip(297.9, 183.62, 0)
# click fuera
device.touchDip(384.0, 128.76, 0)

# volver



# zombieç
# volver x2

# FALTA:
- Zombie elite
- Regalos de alianza
- Ver como puta hacemos el shake
- pasar de cuenta en cuenta

adb emu sensor set acceleration 100:100:100; sleep 1; adb emu sensor set acceleration 0:0:0
adb shell input keyevent 82
