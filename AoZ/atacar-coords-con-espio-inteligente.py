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
from datetime import datetime, timedelta
from pprint import pprint
import pytesseract
import argparse
import math
import os
import re
import sys
import time
from time import sleep

## Command Options
parser = argparse.ArgumentParser(description="Opts", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--onlySpy", action="store_true", help="spy mode")
parser.add_argument("--spyWithInfo", action="store_true", help="SpyWith info")
parser.add_argument("--changeCoords", action="store_true", help="Change Objective Coords")
parser.add_argument("--attackTime", type=int, help="AttackTime")
parser.add_argument("--repeat", type=int, help="Repeat attack")
parser.add_argument("--maxMarches", type=int, help="Max Marches")
parser.add_argument("--withFireworks", action="store_false", help="With Firewarks option")
parser.add_argument("--useFleet", action="store_true", help="Use Fleet Nº 6") # To be improved with custom fleet number
parser.add_argument("--times", type=int, help="Times to attack")
parser.add_argument("--cargo", type=int, help="Quantity of resources each fleet can handle")
parser.add_argument("--spyAndAttack", action="store_true", help="Spy and attack")
parser.add_argument("--onlyC15", action="store_true", help="Filter Only C15s")
parser.add_argument("--onlyC20", action="store_true", help="Filter Only C20s")
CONFIG = vars(parser.parse_args())

# pprint(CONFIG)

kwargs1 = {'verbose': False, 'ignoresecuredevice': False, 'ignoreversioncheck': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'startviewserver': True, 'autodump': False, 'ignoreuiautomatorkilled': True, 'compresseddump': True, 'useuiautomatorhelper': False, 'debug': {}}
vc = ViewClient(device, serialno, **kwargs2)

cities = {
    'Apa          ': { 'coords': [ '554','606'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Asado        ': { 'coords': [ '564','598'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Blended      ': { 'coords': [ '560','574'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Bourbon      ': { 'coords': [ '550','599'], 'times': 1, 'repeat': 1, 'C': 20 },
    'CanadianMalt ': { 'coords': [ '560','594'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Cebada       ': { 'coords': [ '546','561'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Chopera      ': { 'coords': [ '554','596'], 'times': 1, 'repeat': 1, 'C': 20 },
    'ELA_ForEver  ': { 'coords': [ '524','596'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Escudro2     ': { 'coords': [ '553','566'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Escudrofrm   ': { 'coords': [ '554','602'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Heiti        ': { 'coords': [ '556','598'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Hernan213    ': { 'coords': [ '562','600'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Irish        ': { 'coords': [ '560','606'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Kelua        ': { 'coords': [ '556','600'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Jarbow       ': { 'coords': [ '558','606'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Jinet        ': { 'coords': [ '554','596'], 'times': 1, 'repeat': 1, 'C': 20 },
    'MK           ': { 'coords': [ '554','594'], 'times': 1, 'repeat': 1, 'C': 15 },
    'Malta        ': { 'coords': [ '563','572'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Mati213      ': { 'coords': [ '562','598'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Odiado       ': { 'coords': [ '569','585'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Porron       ': { 'coords': [ '537','587'], 'times': 1, 'repeat': 1, 'C': 20 },
    'RAMP-F       ': { 'coords': [ '568','598'], 'times': 1, 'repeat': 1, 'C': 20 },
    'RotAntiBan   ': { 'coords': [ '560','604'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Rot_is_back  ': { 'coords': [ '537','571'], 'times': 1, 'repeat': 1, 'C': 20 },
    'RotseN       ': { 'coords': [ '554','594'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Scotch       ': { 'coords': [ '569','580'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Shelaso      ': { 'coords': [ '558','598'], 'times': 1, 'repeat': 1, 'C': 20 },
    'SingleMalt   ': { 'coords': [ '570','592'], 'times': 1, 'repeat': 1, 'C': 20 },
    # 'Stal         ': { 'coords': [ '556','602'], 'times': 1, 'repeat': 1, 'C': 20 }, <== hay que buscarla
    'Stout        ': { 'coords': [ '558','596'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Toto         ': { 'coords': [ '556','606'], 'times': 1, 'repeat': 1, 'C': 20 },
    'Whiscardo    ': { 'coords': [ '573','576'], 'times': 1, 'repeat': 1, 'C': 20 },
    'bastian2213  ': { 'coords': [ '552','598'], 'times': 1, 'repeat': 1, 'C': 20 },
    'herny2213    ': { 'coords': [ '547','541'], 'times': 1, 'repeat': 1, 'C': 20 },
    'martinssj    ': { 'coords': [ '553','570'], 'times': 1, 'repeat': 1, 'C': 20 },
}

# check if any city has the same coords than  other
duplicated_cities = []
for name, data in cities.items():
    for name2, data2 in cities.items():
        if name != name2 and data['coords'] == data2['coords']:
            duplicated_cities.add("{} - {}".format(name, name2))
            # sys.exit(1)

if duplicated_cities:
    print("Duplicated cities: {}".format(', '.join(duplicated_cities)))
    sys.exit(1)

def calc_needed_fleets(cargo, food, oil, steel = 0.0, ore = 0.0):
    # save resources
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

    print("Total resources:", total, cargo)
    return math.ceil(total / cargo)

def parse_time_to_seconds(raw_time):
    try:
        parts = list(map(lambda n: int(n), raw_time.split(':')))
        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        else:
            return parts[0]
    except:
        return 0

def parse_image(image, index = None):
    raw = pytesseract.image_to_data(
        image,
        output_type='dict', config='-l spa --psm 6'
    )

    if index is None:
        return raw

    data = list(filter(lambda n: n != '', raw['text']))

    try:
        return data[index]
    except:
        return

def spy_and_attack(device, name, data):
    # City
    device.touchDip(209.52, 342.86, 0)
    time.sleep(0.5)
    # Spy with fireworks
    if CONFIG['withFireworks']:
        device.touchDip(207.0, 209.52, 0)
    else:
        device.touchDip(152.38, 230.1, 0)
    # Spy with fireworks & presidency
    # device.touchDip(167.62, 218.67, 0)
    # device.touchDip(165.33, 224.0, 0)

    time.sleep(1)

    # Confirm friendly alliance
    ss = device.takeSnapshot(reconnect=True)
    text = parse_image(ss.crop((320, 1000, 320+400, 1000+100)), -1)
    if text in ['Confirmar', 'Confirm']:
        device.touchDip(206.48, 405.33, 0)

    time.sleep(2)
    # Take screenshot then click and then parse
    ss = device.takeSnapshot(reconnect=True)

    # Confirm
    device.touchDip(227.05, 513.52, 0)

    spy_time = parse_time_to_seconds(
        parse_image(ss.crop((440.0, 1210.0, 560.0, 1312.0)), -1) # sin espionaje
    )

    if spy_time == 0:
        spy_time = parse_time_to_seconds(
            parse_image(ss.crop((660.0, 1210.0, 780.0, 1312.0)), -1) # con espionaje
        )

    # click en reconocimiento
    print("Tiempo de espionaje: %s" % spy_time)
    sleep(spy_time + 8)

    # Click en mensajes
    device.touchDip(248.38, 700.19, 0)
    sleep(1)

    d = parse_image(device.takeSnapshot(reconnect=True))
    # print("Espionaje ")
    # pprint(d['text'])
    try:
        iE = d['text'].index('Espionaje')
    except:
        try:
            iE = d['text'].index('Esplonaje')
        except:
            try:
                iE = d['text'].index('espió')
            except:
                print(d['text'])
                raise

    device.touch(d['left'][iE] + d['width'][iE], d['top'][iE] + d['height'][iE], 0)
    sleep(2)

    # click en primer msj
    device.touch(550.0, 348.0, 0)
    sleep(2)
    ss = device.takeSnapshot(reconnect=True)
    r = parse_image(ss)
    iA = r['text'].index('Ahorrados') - 1
    iD = r['text'].index('Durabilidad')

    raw_resources = parse_image(ss.crop((
        device.display['width'] / 4, r['top'][iA] + r['height'][iA], device.display['width'] - (device.display['width'] / 4), r['top'][iD]
    )))['text']

    def parse_resources(raw_resources):
        resources = []
        for r in raw_resources:
            only_numbers = re.sub(r'\D', '', r)
            if only_numbers != '':
                resources.append(int(only_numbers))

        return resources

    resources = parse_resources(raw_resources)
    # calcular cantidad de tropas

    # drag para bajar y ver unidades
    device.drag((224, 1516), (250, 610), 1000, 2, 0)

    # Leer unidades
    ss = device.takeSnapshot(reconnect=True)
    u = parse_image(ss)
    try:
        ## SHould match "Total de Unidades"
        iU = u['text'].index('Unidades') # Sometimes that match tech units stats
        if u['text'][iU - 1] != 'de' and u['text'][iU - 2] != 'Total':
            iU = None
    except:
        iU = None
        print("%s Sin unidades", name)
        # return 0

    # Si no encuentra unidades seguimos
    if iU:
        height = device.display['height']

        try:
            print("261")
            iT = u['text'].index('Tecnología')
            height = u['top'][iT]
        except:
            try:
                print("266")
                iT = u['text'].index('Tecnologia')
                height = u['top'][iT]
            except:
                print("270")
                None

        print("Previo a crop: suma: {}, height: {}".format(u['top'][iU] + u['height'][iU], height))

        raw_troops = parse_image(
            ss.crop((0, u['top'][iU] + u['height'][iU], device.display['width'], height))
        )
        print("Tropas: {}".format(raw_troops['text']))

        def parse_troops(raw_troops):
            troops = []
            for raw_t in raw_troops:
                troop = re.sub(r'\W', '', raw_t)
                troop = re.sub(r'\d', '', troop).lower()
                # Troop names always have more than 5 chars
                if len(troop) > 4 and troop not in ['x', 'zombi', 'zombibioquímico', 'zombie', 'bioquimico', 'bioquímico']:
                    troops.append(troop)

            return list(set(troops))

        # print("Tropas:")
        troops = parse_troops(raw_troops['text'])
        pprint(troops)
        # pprint(troops)
        # print("Recursos:")
        # pprint(resources)
        if len(troops) > 0:
            return 0

    cargo = CONFIG['cargo'] or 2_000_000
    # pprint(calc_needed_fleets(cargo, *resources))
    return calc_needed_fleets(cargo, *resources)
    # return resources
    # return parse_troops(raw_troops)

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

running_fleets = []

def current_fleets():
    i = 0
    for f in running_fleets:
        if f > time.time():
            i = i + 1

    return i

marches = 0
for name, data in cities.items():
    try:
        if CONFIG['onlyC15'] and data['C'] != 15:
            continue
        if CONFIG['onlyC20'] and data['C'] != 20:
            continue

        c1, c2  = data['coords']
        times   = CONFIG['times'] or data['times']
        repeat  = CONFIG['repeat'] or data['repeat'] or 1

        times_to_attack = 0

        if CONFIG['changeCoords'] or CONFIG['onlySpy'] or CONFIG['spyAndAttack']:
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
            time.sleep(1)

            # Go
            device.touchDip(211.05, 425.9, 0)
            time.sleep(1)
            device.touchDip(201.9, 376.38, 0)

        if (CONFIG['spyAndAttack']):
            times_to_attack = spy_and_attack(device, name, data)
            # Salir de los mensajes
            device.press('BACK')
            sleep(1)
            device.press('BACK')
            sleep(1)
            device.press('BACK')
            sleep(1)

            if times_to_attack == 0:
                continue

            times = int(times_to_attack / repeat)
            if times == 0:
                times = 1
            print("Attacking {} times (with {} fleets) to {}".format(times, repeat, name))

        elif (CONFIG['onlySpy']):
            if (marches == (CONFIG['maxMarches'] or 3)):
                print("Waiting until: " + str(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ")))
                time.sleep(10)
                marches = 0

            # City
            device.touchDip(209.52, 342.86, 0)
            time.sleep(1)
            # Spy with fireworks
            if CONFIG['withFireworks']:
                device.touchDip(207.0, 209.52, 0)
            else:
                device.touchDip(152.38, 230.1, 0)
            # Spy with fireworks& presi
            # device.touchDip(165.33, 224.0, 0)

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
            continue # pass to the next loop iteration

        # attacking
        attack_time = CONFIG['attackTime'] or 0

        attacked = 0
        sleep_until = 0
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
                    attack_time = (get_attack_time() * 2) + 3
                    sleep_until = datetime.now() + timedelta(seconds=attack_time)
                    print("Waiting " + str(attack_time))

                if j == 0:
                    sleep_until = datetime.now() + timedelta(seconds=attack_time)

                # Confirm
                device.touchDip(359.62, 696.38, 0)
                time.sleep(0.5)

            sleep_secs = (sleep_until - datetime.now()).seconds
            # sleep until can be past
            if sleep_secs > 500:
                sleep_secs = 0
            time.sleep(sleep_secs)

        # if attackTime is present or changeCoords is not true, we only have 1 objective
        if (CONFIG['attackTime'] != None or CONFIG['changeCoords'] != True):
            break

        attack_time = 0
    except Exception as e:
        pprint(e)
        continue
