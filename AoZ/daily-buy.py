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


# Almacen
device.touchDip(336.0, 275.81, 0)
# Venta de recursos
device.touchDip(289.52, 364.19, 0)
# Click en acero
device.touchDip(115.81, 512.76, 0)
# Click en mineral
device.touchDip(311.62, 508.19, 0)
# Click en casa/mapa 2 veces
device.touchDip(47.24, 679.62, 0)
time.sleep(1)
device.touchDip(47.24, 679.62, 0)
time.sleep(1)

# Entrar mercado negro
device.touchDip(268.95, 195.05, 0)
time.sleep(1)
device.touchDip(286.48, 276.57, 0)
time.sleep(1)
# Click en vender
device.touchDip(210.29, 229.33, 0)
# Vender trigo
device.touchDip(145.52, 341.33, 0)
# Vender petroleo
device.touchDip(344.38, 342.1, 0)
# Vender acero
device.touchDip(145.52, 458.67, 0)
# Vender mineral
device.touchDip(345.14, 454.86, 0)

# Comprar
# take screenshot y buscar "Insignia del Lider", "Cofre de Fragmento de oficial"
ss = device.takeSnapshot(reconnect=True)
raw = pytesseract.image_to_data(
    ss,
    output_type='dict', config='-l spa --psm 6'
)
texts = raw['text']
# Search for text Cofre multiple times in the raw['text'] array and iterate the index to check the next 2 words

Items_to_buy = [
    ['Cofre', 'de', 'Fragmento'],
    ['Insignia', 'de', 'Líder'],
    ['VIP', '(8', 'Hora)'],
    ['Combustible'],
]

for refresh in range(3):
    ss = device.takeSnapshot(reconnect=True)
    raw = pytesseract.image_to_data(ss, output_type='dict', config='-l spa --psm 6')

    for item in Items_to_buy:
        # Same item can be more than ones
        for item_idx in [i for i, x in enumerate(texts) if x == item[0]]:
            buy = True
            for i, word in enumerate(item):
                if texts[item_idx + i] != word:
                    buy = False
                    break
            if buy:
                print(f'Buying {item} at coords {raw["top"][item_idx]} {raw["left"][item_idx]}')
                device.touch(raw['left'][item_idx] + 320, raw['top'][item_idx] + 200, 0)
                time.sleep(1)
                # check screenshot "Confirma Comprar"
                device.touch(548.0, 1002.0, 0) # Confirmar
                time.sleep(1)
    # Only refresh twice
    if refresh < 2:
        # Click en refrescar:
        device.touchDip(358.1, 169.14, 0)
        time.sleep(0.5)
        # Confirmar
        device.touchDip(205.71, 393.14, 0)
        time.sleep(0.5)


# Tocar flecha de la izq
device.touchDip(7.62, 297.14, 0)

# ss = device.takeSnapshot(reconnect=True)
# raw = pytesseract.image_to_data(ss.convert("L"), output_type='dict', config='-l spa --psm 6')
# texts = raw['text']

# # Same item can be more than ones
# for pick in [i for i, x in enumerate(texts) if x == 'Recopilar']:
#     device.touch(raw['left'][pick], raw['top'][pick], 0)
#     time.sleep(0.5)


# Click en reclutamiento # poner numeros
device.touchDip(58.67, 167.62, 0) # Camp 1 993 1D
device.touchDip(131.81, 166.1, 0) # Camp 2 993 1D
device.touchDip(228.57, 169.14, 0) # Fab 1
device.touchDip(59.43, 249.9, 0)    # Fab 2
device.touchDip(140.95, 250.67, 0) # taller
device.touchDip(233.9, 247.62, 0) # Promocion

# Centro de mando
device.touchDip(227.05, 368.0, 0)
# Reclutamiento gratis
device.touchDip(113.52, 607.24, 0)
# Confirmar
device.touchDip(315.43, 629.33, 0)
# back
device.touchDip(30.48, 13.71, 0)





# NOTES:
# # Este es el tope del cuadrado
# device.touchDip(17.52, 384.0, 0)
# device.touch(46.0, 1004.0, 0)
# # Click en comprar dentro del cuadrado
# device.touchDip(145.52, 457.9, 0)
# device.touch(368.0, 1200.0, 0)
