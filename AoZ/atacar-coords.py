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


from com.dtmilano.android.viewclient import ViewClient, KEY_EVENT
from datetime import datetime
from pprint import pprint
import argparse
import os
import re
import sys
import time

## Command Options
parser = argparse.ArgumentParser(description="Opts", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--onlySpy", action="store_true", help="spy mode")
parser.add_argument("--changeCoords", action="store_true", help="Change Objective Coords")
parser.add_argument("--attackTime", type=int, help="AttackTime")
parser.add_argument("--repeat", type=int, help="Repeat attack")
parser.add_argument("--maxMarches", type=int, help="Max Marches")
parser.add_argument("--withFireworks", type=int, help="With Firewarks option")
parser.add_argument("--useFleet", type=bool, help="Use Fleet Nº 6") # To be improved with custom fleet number
parser.add_argument("--times", type=int, help="Times to attack")
CONFIG = vars(parser.parse_args())

pprint(CONFIG)

kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)

cities = {
    'Rot_is_back':   { 'coords': ['679', '553'], 'repeat': 1, 'times': 1, 'C': 15},
    'Blended':       { 'coords': ['669', '551'], 'repeat': 4, 'times': 2, 'C': 15},
    'Whiscardo':     { 'coords': ['672', '541'], 'repeat': 4, 'times': 2, 'C': 15},
    'CanadianMalt':  { 'coords': ['671', '553'], 'repeat': 4, 'times': 2, 'C': 15},
    'Shelaso':       { 'coords': ['671', '557'], 'repeat': 4, 'times': 2, 'C': 15},
    'RotAntiBan':    { 'coords': ['671', '551'], 'repeat': 4, 'times': 2, 'C': 15},
    'Irish':         { 'coords': ['673', '553'], 'repeat': 4, 'times': 2, 'C': 15},
    'ELA_ForEver':   { 'coords': ['674', '558'], 'repeat': 4, 'times': 2, 'C': 15},
    'Bourbon':       { 'coords': ['667', '555'], 'repeat': 4, 'times': 2, 'C': 15},
    'Asado':         { 'coords': ['673', '551'], 'repeat': 4, 'times': 2, 'C': 15},
    'Escudrofrm':    { 'coords': ['666', '576'], 'repeat': 4, 'times': 1, 'C': 15},
    'Escudro2':      { 'coords': ['666', '578'], 'repeat': 4, 'times': 2, 'C': 15},
    'Escudro3':      { 'coords': ['672', '574'], 'repeat': 4, 'times': 2, 'C': 15},
    'SingleMalt':    { 'coords': ['641', '546'], 'repeat': 4, 'times': 2, 'C': 20},
    'Stout':         { 'coords': ['641', '548'], 'repeat': 4, 'times': 2, 'C': 20},
    'Scotch':        { 'coords': ['641', '544'], 'repeat': 4, 'times': 2, 'C': 20},
    'Odiado':        { 'coords': ['641', '550'], 'repeat': 4, 'times': 2, 'C': 20},
    'Apa':           { 'coords': ['643', '581'], 'repeat': 1, 'times': 1, 'C': 20},
    'Cebada':        { 'coords': ['643', '579'], 'repeat': 4, 'times': 2, 'C': 20},
    'Chopera':       { 'coords': ['655', '555'], 'repeat': 4, 'times': 1, 'C': 20},
    'Malta':         { 'coords': ['654', '579'], 'repeat': 4, 'times': 4, 'C': 20},
    'Porron':        { 'coords': ['655', '553'], 'repeat': 4, 'times': 1, 'C': 20},
    # 'Escudro PPal':  { 'coords': ['662', '580'], 'repeat': 4, 'times': 2, 'C': 20},
    'Ashoka':        { 'coords': ['638', '569'], 'repeat': 4, 'times': 2, 'C': 20},
    'Jarbow':        { 'coords': ['636', '557'], 'repeat': 2, 'times': 1, 'C': 20},
    'Heiti':         { 'coords': ['636', '555'], 'repeat': 1, 'times': 1, 'C': 20},
    'Stal':          { 'coords': ['638', '557'], 'repeat': 3, 'times': 1, 'C': 20},
    'Mati213':       { 'coords': ['639', '542'], 'repeat': 1, 'times': 1, 'C': 20},
    'Jinet':         { 'coords': ['637', '538'], 'repeat': 4, 'times': 1, 'C': 15},
    'herny2213':     { 'coords': ['639', '540'], 'repeat': 1, 'times': 1, 'C': 20},
    'bastian2213':   { 'coords': ['641', '538'], 'repeat': 4, 'times': 1, 'C': 15},
    'Hernan213':     { 'coords': ['639', '538'], 'repeat': 2, 'times': 1, 'C': 20},
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
for name, data in cities.items():
    c1, c2  = data['coords']
    times   = CONFIG['times'] or data['times']
    repeat  = CONFIG['repeat'] or data['repeat'] or 1

    if CONFIG['changeCoords'] or CONFIG['onlySpy']:
        print('Sending to ' + name)

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
        vc.findViewByIdOrRaise("id/no_id/3").setText(c1)

        # Coords 2
        device.touchDip(330.67, 358.86, 0)
        time.sleep(0.2)
        device.touchDip(330.67, 358.86, 0)
        vc.findViewByIdOrRaise("id/no_id/3").setText(c2)

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
            device.touchDip(207.0, 209.52, 0)
        else:
            device.touchDip(152.38, 230.1, 0)

        time.sleep(1)
        # Confirm friendly alliance
        ss = device.takeSnapshot(reconnect=True)
        text = device.imageToData(ss.crop((320, 1000, 320+400, 1000+100)))['text'][-1]
        if text in ['Confirmar', 'Confirm']:
            device.touchDip(206.48, 405.33, 0)

        time.sleep(2)
        # Confirm
        device.touchDip(232.38, 515.81, 0)
        marches = marches + 1

    else:
        attack_time = CONFIG['attackTime'] or 0

        for i in range(times):
            print("Sending " + str(i + 1) +  " time...")

            for j in range(repeat):
                # City
                device.touchDip(204.95, 335.24, 0)
                time.sleep(0.5)
                # Attack
                # device.touchDip(265.9, 262.1, 0)
                device.touchDip(258.29, 224.76, 0)
                time.sleep(0.5)
                # Confirm just in case (first time)
                if (j == 0):
                    device.touchDip(206.48, 405.33, 0)
                    time.sleep(2)
                else:
                    time.sleep(1)

                # Troops 6
                if (CONFIG['useFleet'] != False):
                    # device.touchDip(319.24, 144.0, 0)
                    device.touchDip(320.0, 119.62, 0)
                    time.sleep(1)

                if (attack_time == 0):
                    attack_time = (get_attack_time() * 2) + 2
                    print("Waiting " + str(attack_time))

                # Confirm
                device.touchDip(359.62, 696.38, 0)
                time.sleep(0.5)
            time.sleep(attack_time)
        # if attackTime is present we only have 1 objective
        if (CONFIG['attackTime'] != None):
            break

    attack_time = 0


def calc_milonga(cargo, food, oil, steel = 0.0, ore = 0.0):
    w_food = 750000
    w_oil = 750000
    w_steal = 70000
    w_ore = 60000

    total = 0

    if (food > w_food):
        total = total + (food - w_oil)

    if (oil > w_oil):
        total = total + (oil - w_oil)

    if (steel > w_steal):
        total = total + (steel - w_steal) * 5.5

    if (ore > w_ore):
        total = total + (ore - w_ore) * 12.5

    fp = foor / total
    op = oil / total
    sp = steel / total
    rp = ore / total

    if rp > 0.01:
        return ore * rp / cargo

    return steel * sp / cargo


def espiar_y_atacar():
    # coordenadas
    # espiar
    # leer tiempo
    ss = device.takeSnapshot(reconnect=True)
    spy_time = parse_time_to_seconds(
        device.imageToData(ss.crop((440.0, 1210.0, 560.0, 1312.0))) # sin espionaje
    )

    if spy_time == 0:
        spy_time = parse_time_to_seconds(
            device.imageToData(ss.crop((660.0, 1210.0, 780.0, 1312.0))) # con espionaje
        )
    # click en reconocimiento
    sleep(spy_time)

    # Click en mensajes
    device.touchDip(248.38, 700.19, 0)
    sleep(0.5)
    ss = device.takeSnapshot(reconnect=True)
    d = device.imageToData(ss)
    iE = d['text'].index('Espionaje')
    device.touch(d['left'][iE] + d['width'][iE], d['top'][iE] + d['height'][iE], 0)
    sleep(0.5)
    # click en primer msj
    device.touch(806.0, 640.0, 0)
    sleep(0.5)
    ss = device.takeSnapshot(reconnect=True)
    e = device.imageToData(ss)
    iA = e['text'].index('Ahorrados') - 1
    iD = e['text'].index('Durabilidad')

    recursos = device.imageToData(ss.crop((
        device.display['width'] / 4, d['top'][iA] + d['height'][iA], device.display['width'] - (device.display['width'] / 4), d['top'][iD]
    )))
    # calcular cantidad de tropas

    # drag para bajar y ver unidades
    device.drag((224, 1516), (250, 580), 1000, 2, 0)

    # Leer unidades
    ss = device.takeSnapshot(reconnect=True)
    u = device.imageToData(ss)
    iU = u['text'].index('Unidades')
    height = device.display['height']

    try:
        iT = u['text'].index('Tecnología')
        height = u['top'][iT]
    except:
        try:
            iT = u['text'].index('Tecnologia')
            height = u['top'][iT]
        except:
            None

    raw_troops = pytesseract.image_to_data(
        ss.crop((0, u['top'][iU] + u['height'][iU], device.display['width'], height)),
        output_type='dict', config='-l spa --psm 6'
    )['text']

    def parse_troops(raw_troops):
        troops = []
        for troop in raw_troops:
            if len(troop) > 5:
                troops.append(troop)

        return troops

    return parse_troops(raw_troops)
