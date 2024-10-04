from pprint import pprint
def calc_milonga(cargo, food, oil, steel = 0.0, ore = 0.0):
    w_food = 750000
    w_oil = 750000
    w_steal = 70000
    w_ore = 60000

    total = 0

    if (food <= w_food):
        food = 0

    if (oil <= w_oil):
        oil = 0

    if (steel <= w_steal):
        steel = 0

    if (ore <= w_ore):
        ore = 0

    total = food + oil + steel * 5.5 + ore * 12.5

    pprint("After ore: %f" % (total))

    fp = food / total
    op = oil / total
    sp = steel * 5.5 / total
    rp = ore * 12.5 / total

    pprint("fp: %f, op: %f, sp: %f, rp: %f" % (fp, op, sp, rp))

    if rp > 0.01:
        return cargo / (ore * rp )

    return round(cargo / (steel * sp))
