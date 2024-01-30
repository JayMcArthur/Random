import math as m


def multi_arb(_arb_num_a, _arb_num_b):
    if _arb_num_a > _arb_num_b:
        ten_place_a = m.floor(_arb_num_a)
        ten_place_b = m.floor(_arb_num_b)
        actual_num_a = (_arb_num_a - ten_place_a) * 10
        actual_num_b = (_arb_num_b - ten_place_b) * 10
    else:
        ten_place_a = m.floor(_arb_num_b)
        ten_place_b = m.floor(_arb_num_a)
        actual_num_a = (_arb_num_b - ten_place_a) * 10
        actual_num_b = (_arb_num_a - ten_place_b) * 10
    new_num = actual_num_a * actual_num_b
    while new_num > 10:
        new_num /= 10
        ten_place_a += 1
    new_num /= 10
    new_num += ten_place_a + ten_place_b
    return new_num


def power_arb(_arb_num, _power):
    ten_place = m.floor(_arb_num)
    actual_num = (_arb_num - ten_place) * 10

    working_power = m.floor(dec_to_arb(_power))

    working_num = dec_to_arb(m.pow(actual_num, (_power / (10 ** working_power))))
    new_num = working_num

    for i in range((10 ** working_power)-1, 0, -1):
        new_num = multi_arb(new_num, working_num)

    ten_place *= _power

    return ten_place + new_num


def dec_to_arb(_dec_num):
    ten_place = m.floor(m.log(m.floor(_dec_num), 10)) + 1
    return ten_place - 1 + (_dec_num / (m.pow(10,ten_place)))


def arb_to_dec(_arb_num):
    ten_place = m.floor(_arb_num)
    _arb_num -= ten_place
    _arb_num *= 10 ** (ten_place + 1)
    return _arb_num


# Calculates Module Tier in Myriad
def test(k):
    loop_tier = k - 1
    b_boost = 2.4
    gps = 1
    while loop_tier > 0:
        if loop_tier % 2 == 0:
            loop_tier /= 2
            b_boost *= b_boost
            if loop_tier == 1:
                gps *= b_boost
                break
        else:
            loop_tier -= 1
            gps *= b_boost
    print(m.floor(gps) + k - 1)