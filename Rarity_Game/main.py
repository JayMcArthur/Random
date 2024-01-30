from enum import Enum
from math import ceil, floor, log2
from random import randrange, random, randint
from copy import deepcopy as dc


class RarityTypes(Enum):
    # Name = Num   # Amount - Color           #Color Hex
    COMMON = 0  # __ 11 - Gray (Quartz)       #808080 // #525252
    UNCOMMON = 1  # _08 - Green (Emerald)     #009B77
    RARE = 2  # ____ 06 - Blue (Sapphire)     #0F52BA
    EPIC = 3  # ____ 05 - Purple (Taaffeite)  #6C3082
    LEGENDARY = 4  # 03 - Ruby                #9B111E
    MYTHIC = 5  # __ 02 - Gold                #D4AF37 // #876E1D
    DIVINE = 6  # __ 01 - Black Opal          #2C3241 // #424B61
    # EXOTIC
    # UNIQUE
    # ULTIMATE
    # Otherworldly
    # Ethereal


class ItemTypes(Enum):
    WEAPON = 0  # ____ Sword or somn
    HELMET = 1  # ____ Head
    BREASTPLATE = 2  # Chest
    PAILDRON = 3  # __ Shoulders
    REREBRACE = 4  # _ Upper Arms
    VAMBRACE = 5  # __ Lower Arms
    GAUNTLET = 6  # __ Hands
    CUISSES = 7  # ___ Thighs
    GREAVES = 8  # ___ Calves
    SAVATONS = 9  # __ Feet


class Rarity:
    def __init__(self, rtype: RarityTypes, level=0):
        self.type = rtype
        self.level = level


class ItemDrop:
    def __init__(self, rarity: Rarity, max_roll: int):
        self.rarity = rarity
        self.max_roll = max_roll


class Item:
    def __init__(self, itype: ItemTypes, stats: list[int]):
        self.type = itype



RARITIES = [
    Rarity(RarityTypes.COMMON, 0),  # 00
    Rarity(RarityTypes.COMMON, 1),  # 01
    Rarity(RarityTypes.COMMON, 2),  # 02
    Rarity(RarityTypes.COMMON, 3),  # 03
    Rarity(RarityTypes.COMMON, 4),  # 04
    Rarity(RarityTypes.COMMON, 5),  # 05
    Rarity(RarityTypes.COMMON, 6),  # 06
    Rarity(RarityTypes.COMMON, 7),  # 07
    Rarity(RarityTypes.COMMON, 8),  # 08
    Rarity(RarityTypes.COMMON, 9),  # 09
    Rarity(RarityTypes.COMMON, 10),  # 10
    Rarity(RarityTypes.UNCOMMON, 1),  # 11
    Rarity(RarityTypes.UNCOMMON, 2),  # 12
    Rarity(RarityTypes.UNCOMMON, 3),  # 13
    Rarity(RarityTypes.UNCOMMON, 4),  # 14
    Rarity(RarityTypes.UNCOMMON, 5),  # 15
    Rarity(RarityTypes.UNCOMMON, 6),  # 16
    Rarity(RarityTypes.UNCOMMON, 7),  # 17
    Rarity(RarityTypes.UNCOMMON, 8),  # 18
    Rarity(RarityTypes.RARE, 1),  # 19
    Rarity(RarityTypes.RARE, 2),  # 20
    Rarity(RarityTypes.RARE, 3),  # 21
    Rarity(RarityTypes.RARE, 4),  # 22
    Rarity(RarityTypes.RARE, 5),  # 23
    Rarity(RarityTypes.RARE, 6),  # 24
    Rarity(RarityTypes.EPIC, 1),  # 25
    Rarity(RarityTypes.EPIC, 2),  # 26
    Rarity(RarityTypes.EPIC, 3),  # 27
    Rarity(RarityTypes.EPIC, 4),  # 28
    Rarity(RarityTypes.EPIC, 5),  # 29
    Rarity(RarityTypes.LEGENDARY, 1),  # 30
    Rarity(RarityTypes.LEGENDARY, 2),  # 31
    Rarity(RarityTypes.LEGENDARY, 3),  # 32
    Rarity(RarityTypes.MYTHIC, 1),  # 33
    Rarity(RarityTypes.MYTHIC, 2),  # 34
    Rarity(RarityTypes.DIVINE, 0)  # 35
]
# Total Drop = sum(1/x) where x is Items Drop Values
# Total Drop: 3.103032809523…809523
MAX_ROLL = [2995634920634, 3097968253968, 3102734920634, 3103007142857, 3103030476190, 3103032698412, 3103032809523]
# Drop Value = how many Common 0 an item is worth
# Drop Chance = 1/(Drop Value * Total Drop)
ITEM_DROPS = [
    # Rarity,                         Max Roll      # Drop Value, Drop Chance
    ItemDrop(RARITIES[0], 1000000000000),   # C0:       1 > 32.22% * 10^0
    ItemDrop(RARITIES[1], 1500000000000),   # C1:       2 > 16.11% * 10^0
    ItemDrop(RARITIES[2], 1833333333333),   # C2:       3 > 10.74% * 10^0
    ItemDrop(RARITIES[3], 2083333333333),   # C3:       4 > 80.56% * 10^-1
    ItemDrop(RARITIES[4], 2283333333333),   # C4:       5 > 64.40% * 10^-1
    ItemDrop(RARITIES[5], 2450000000000),   # C5:       6 > 53.71% * 10^-1
    ItemDrop(RARITIES[6], 2592857142857),   # C6:       7 > 46.03% * 10^-1
    ItemDrop(RARITIES[7], 2717857142857),   # C7:       8 > 40.28% * 10^-1
    ItemDrop(RARITIES[8], 2828968253968),   # C8:       9 > 35.80% * 10^-1
    ItemDrop(RARITIES[9], 2928968253968),   # C9:      10 > 32.22% * 10^-1
    ItemDrop(RARITIES[10], 2995634920634),  # C10:     15 > 21.48% * 10^-1
    ItemDrop(RARITIES[11], 3035624920634),  # U1:      25 > 12.89% * 10^-1
    ItemDrop(RARITIES[12], 3055634920634),  # U2:      50 > 64.45% * 10^-2
    ItemDrop(RARITIES[13], 3068968253968),  # U3:      75 > 42.96% * 10^-2
    ItemDrop(RARITIES[14], 3078968253968),  # U4:     100 > 32.22% * 10^-2
    ItemDrop(RARITIES[15], 3085634920634),  # U5:     150 > 21.48% * 10^-2
    ItemDrop(RARITIES[16], 3090634920634),  # U6:     200 > 16.11% * 10^-2
    ItemDrop(RARITIES[17], 3094634920634),  # U7:     250 > 12.89% * 10^-2
    ItemDrop(RARITIES[18], 3097968253968),  # U8:     300 > 10.74% * 10^-2
    ItemDrop(RARITIES[19], 3099968253968),  # R1:     500 > 64.45% * 10^-3
    ItemDrop(RARITIES[20], 3100968253968),  # R2:    1000 > 32.22% * 10^-3
    ItemDrop(RARITIES[21], 3101634920634),  # R3:    1500 > 21.48% * 10^-3
    ItemDrop(RARITIES[22], 3102134920634),  # R4:    2000 > 16.11% * 10^-3
    ItemDrop(RARITIES[23], 3102534920634),  # R5:    2500 > 12.89% * 10^-3
    ItemDrop(RARITIES[24], 3102734920634),  # R6:    5000 > 64.45% * 10^-4
    ItemDrop(RARITIES[25], 3102868253968),  # E1:    7500 > 42.96% * 10^-4
    ItemDrop(RARITIES[26], 3102934920634),  # E2:   15000 > 21.48% * 10^-4
    ItemDrop(RARITIES[27], 3102968253968),  # E3:   30000 > 10.74% * 10^-4
    ItemDrop(RARITIES[28], 3102990476190),  # E4:   45000 > 71.61% * 10^-5
    ItemDrop(RARITIES[29], 3103007142857),  # E5:   60000 > 53.71% * 10^-5
    ItemDrop(RARITIES[30], 3103020476190),  # L1:   75000 > 42.96% * 10^-5
    ItemDrop(RARITIES[31], 3103027142857),  # L2:  150000 > 21.48% * 10^-5
    ItemDrop(RARITIES[32], 3103030476190),  # L3:  300000 > 10.74% * 10^-5
    ItemDrop(RARITIES[33], 3103032142857),  # M1:  600000 > 53.71% * 10^-6
    ItemDrop(RARITIES[34], 3103032698412),  # M2: 1800000 > 17.90% * 10^-6
    ItemDrop(RARITIES[35], 3103032809523)   # D1: 9000000 > 35.80% * 10^-7
]
ITEM_WORTH = {
    RarityTypes.COMMON: {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 10,
        10: 15
    },
    RarityTypes.UNCOMMON: {
        1: 25,
        2: 50,
        3: 75,
        4: 100,
        5: 150,
        6: 200,
        7: 250,
        8: 300
    },
    RarityTypes.RARE: {
        1: 500,
        2: 1000,
        3: 1500,
        4: 2000,
        5: 2500,
        6: 5000
    },
    RarityTypes.EPIC: {
        1: 7500,
        2: 15000,
        3: 30000,
        4: 45000,
        5: 60000
    },
    RarityTypes.LEGENDARY: {
        1: 75000,
        2: 150000,
        3: 300000
    },
    RarityTypes.MYTHIC: {
        1: 600000,
        2: 1800000
    },
    RarityTypes.DIVINE: {
        0: 9000000
    }
}
# Average Drop Value: sum(Drop Value * Drop Chance) = 11.6015531287...
# Each line = (1/Total Drop) do to math canceling out
MERGE_COST = {
    RarityTypes.COMMON: {
        0: None,  # _______________________________ 00: Drops
        1: [[RARITIES[0], 2]],  # _________________ 01: C0 + C0
        2: [[RARITIES[1], 1], [RARITIES[0], 1]],  # 02: C1 + C0
        3: [[RARITIES[2], 1], [RARITIES[0], 1]],  # 03: C2 + C0
        4: [[RARITIES[3], 1], [RARITIES[0], 1]],  # 04: C3 + C0
        5: [[RARITIES[4], 1], [RARITIES[0], 1]],  # 05: C4 + C0
        6: [[RARITIES[5], 1], [RARITIES[0], 1]],  # 06: C5 + C0
        7: [[RARITIES[6], 1], [RARITIES[0], 1]],  # 07: C6 + C0
        8: [[RARITIES[7], 1], [RARITIES[0], 1]],  # 08: C7 + C0
        9: [[RARITIES[8], 1], [RARITIES[0], 1]],  # 09: C8 + C0
        10: [[RARITIES[9], 1], [RARITIES[4], 1]]  # 10: C9 + C4
    },
    RarityTypes.UNCOMMON: {
        1: [[RARITIES[10], 1], [RARITIES[9], 1]],  # 11: C10 + C9
        2: [[RARITIES[11], 2]],  # __________________ 12: U1 + U1
        3: [[RARITIES[12], 1], [RARITIES[11], 1]],  # 13: U2 + U1
        4: [[RARITIES[13], 1], [RARITIES[11], 1]],  # 14: U3 + U1
        5: [[RARITIES[14], 1], [RARITIES[12], 1]],  # 15: U4 + U2
        6: [[RARITIES[15], 1], [RARITIES[12], 1]],  # 16: U5 + U2
        7: [[RARITIES[16], 1], [RARITIES[12], 1]],  # 17: U6 + U2
        8: [[RARITIES[17], 1], [RARITIES[12], 1]]  # _18: U7 + U2
    },
    RarityTypes.RARE: {
        1: [[RARITIES[18], 1], [RARITIES[16], 1]],  # 19: U8 + U6
        2: [[RARITIES[19], 2]],  # __________________ 20: R1 + R1
        3: [[RARITIES[20], 1], [RARITIES[19], 1]],  # 21: R2 + R1
        4: [[RARITIES[21], 1], [RARITIES[19], 1]],  # 22: R3 + R1
        5: [[RARITIES[22], 1], [RARITIES[19], 1]],  # 23: R4 + R1
        6: [[RARITIES[23], 2]]  # ___________________ 24: R5 + R5
    },
    RarityTypes.EPIC: {
        1: [[RARITIES[24], 1], [RARITIES[23], 1]],  # 25: R6 + R5
        2: [[RARITIES[25], 2]],  # __________________ 26: E1 + E1
        3: [[RARITIES[26], 1], [RARITIES[25], 1]],  # 27: E2 + E2
        4: [[RARITIES[27], 1], [RARITIES[25], 1]],  # 28: E3 + E2
        5: [[RARITIES[28], 1], [RARITIES[25], 1]]  # _29: E4 + E2
    },
    RarityTypes.LEGENDARY: {
        1: [[RARITIES[29], 1], [RARITIES[25], 1]],  # 30: E5 + E2
        2: [[RARITIES[30], 2]],  # __________________ 31: L1 + L1
        3: [[RARITIES[31], 2]]  # ___________________ 32: L2 + L2
    },
    RarityTypes.MYTHIC: {
        1: [[RARITIES[32], 2]],  # 33: L3 + L3
        2: [[RARITIES[33], 3]]  # 34: M1 + M1 + M1
    },
    RarityTypes.DIVINE: {
        0: [[RARITIES[34], 5]]  # 35: M2 + M2 + M2 + M2 + M2
    }
}
ITEM_POWER = {
    # Default Power, Scaled Power, Gems
    RARITIES[0]: [1, 1, 0],
    RARITIES[1]: [5, 5, 0],
    RARITIES[2]: [10, 10, 0],
    RARITIES[3]: [20, 20, 0],
    RARITIES[4]: [30, 30, 0],
    RARITIES[5]: [40, 40, 0],
    RARITIES[6]: [50, 50, 0],
    RARITIES[7]: [60, 60, 0],
    RARITIES[8]: [70, 70, 0],
    RARITIES[9]: [80, 80, 0],
    RARITIES[10]: [90, 90, 0],
    RARITIES[11]: [110, 11, 1],
    RARITIES[12]: [220, 22, 1],
    RARITIES[13]: [330, 33, 1],
    RARITIES[14]: [440, 44, 1],
    RARITIES[15]: [550, 55, 1],
    RARITIES[16]: [660, 66, 1],
    RARITIES[17]: [770, 77, 1],
    RARITIES[18]: [880, 88, 1],
    RARITIES[19]: [1400, 14, 2],
    RARITIES[20]: [2800, 28, 2],
    RARITIES[21]: [4200, 42, 2],
    RARITIES[22]: [5700, 57, 2],
    RARITIES[23]: [7100, 71, 2],
    RARITIES[24]: [8500, 85, 2],
    RARITIES[25]: [16000, 16, 3],
    RARITIES[26]: [33000, 33, 3],
    RARITIES[27]: [50000, 50, 3],
    RARITIES[28]: [66000, 66, 3],
    RARITIES[29]: [83000, 83, 3],
    RARITIES[30]: [250000, 25, 4],
    RARITIES[31]: [500000, 50, 4],
    RARITIES[32]: [750000, 75, 4],
    RARITIES[33]: [3300000, 33, 5],
    RARITIES[34]: [6600000, 66, 5],
    RARITIES[35]: [99000000, 99, 6]
}


class Backpack:
    def __init__(self):
        self.items = {
            RarityTypes.COMMON: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0},
            RarityTypes.UNCOMMON: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0},
            RarityTypes.RARE: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0},
            RarityTypes.EPIC: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
            RarityTypes.LEGENDARY: {1: 0, 2: 0, 3: 0},
            RarityTypes.MYTHIC: {1: 0, 2: 0},
            RarityTypes.DIVINE: {0: 0}
        }
        self.loot_level = 0
        self.loot_counter = 0

    def merge(self):
        while self.merge_pass(RarityTypes.DIVINE, 0, 0):
            pass

    def merge_pass(self, w_rtype, w_level, w_log_level) -> bool:
        for [n_rarity, n_amount] in MERGE_COST[w_rtype][w_level]:
            n_rtype = n_rarity.type
            n_level = n_rarity.level
            while self.items[n_rtype][n_level] < n_amount:
                if n_rtype == RarityTypes.COMMON and n_level == 0:
                    return False
                # print(f'{"-"*w_log_level}Request {n_rtype} {n_level}')
                if not self.merge_pass(n_rtype, n_level, w_log_level + 1):
                    return False

        for [n_rarity, n_amount] in MERGE_COST[w_rtype][w_level]:
            n_rtype = n_rarity.type
            n_level = n_rarity.level
            self.items[n_rtype][n_level] -= n_amount
            if self.items[n_rtype][n_level] < 0:
                print('ERROR')
        self.items[w_rtype][w_level] += 1
        # print(f'{"-"*w_log_level}Made {w_rtype} {w_level}')
        return True

    def loot(self, n):
        # loot level 0 - 6: Max roll is highest roll for that rarity type
        # loot level 7+: Max roll is Divine with roll boosted +(35.80 * 10^-8)%
        # aka 7+ limits the roll space by 1 of a divine
        current_max_roll = MAX_ROLL[min(self.loot_level, 6)]
        for i in range(n):
            roll = randint(1, current_max_roll)
            for check in ITEM_DROPS:
                if roll <= check.max_roll:
                    self.items[check.rarity.type][check.rarity.level] += 1
                    break
        self.loot_counter += n
        # This Means loot level goes up like once a week
        while self.loot_counter >= 16000:
            self.loot_counter -= 16000
            self.loot_level += 1

    def get_loot_worth(self):
        worth = 0
        for rtype in self.items.keys():
            for level in self.items[rtype].keys():
                worth += ITEM_WORTH[rtype][level] * self.items[rtype][level]
        return worth

    def report_items(self, old):
        for rtype in self.items.keys():
            for level in self.items[rtype].keys():
                print(str(rtype)[12:], f'{level}:', old[rtype][level], '>', self.items[rtype][level])


class Player:
    def __init__(self):
        self.defense = 0
        self.shield = 0
        self.armor = 0
        self.max_hp = 0
        self.health = 0
        self.regen = 0
        self.leach = 0
        self.attack = 0
        self.speed = 0
        self.poison = 0
        self.timer = 0
        self.inflicted_poison = 0
        self.used_shield = 0


def fight(p1, p2, finals=False) -> int:
    world_timer = 0
    p1.health = p1.max_hp
    p1.timer = 0
    p1.inflicted_poison = 0
    p1.used_shield = 0
    p2.health = p2.max_hp
    p2.timer = 0
    p2.inflicted_poison = 0
    p2.used_shield = 0
    while p1.health > 0 and p2.health > 0:
        p1.timer += (100 + p1.speed) / 100
        p2.timer += (100 + p2.speed) / 100
        world_timer += 1
        if p1.timer >= 100:
            # print(f'Player 1 Attacks')
            p1.timer = p1.timer % 100
            if p2.shield > p2.used_shield:
                p2.used_shield += ceil(2 * log2(p1.attack))
                # p2.inflicted_poison += p1.poison
                # print(f'- Hit Shield')
            else:
                attack = p1.attack
                attack = max(0, attack - p2.defense)
                # print(f'- Leaches {min(p1.max_hp, p1.health + min(p1.leach, attack)) - p1.health}')
                p1.health = min(p1.max_hp, p1.health + min(p1.leach, attack))
                attack = ceil(attack * (100 - p2.armor) / 100)
                p2.health -= attack
                # print(f'- Did {attack} damage')
                p2.inflicted_poison += p1.poison

        if p2.timer >= 100:
            p2.timer = p2.timer % 100
            # print(f'Player 2 Attacks')
            if p1.shield > p1.used_shield:
                p1.used_shield += ceil(2 * log2(p2.attack))
                # p1.inflicted_poison += p2.poison
                # print(f'- Hit Shield')
            else:
                attack = p2.attack
                attack = max(0, attack - p1.defense)
                # print(f'- Leaches {min(p2.max_hp, p2.health + min(p2.leach, attack)) - p2.health}')
                p2.health = min(p2.max_hp, p2.health + min(p2.leach, attack))
                attack = ceil(attack * (100 - p1.armor) / 100)
                p1.health -= attack
                # print(f'- Did {attack} damage')
                p1.inflicted_poison += p2.poison

        if world_timer >= 100:
            world_timer = world_timer % 100
            heal_amount = p1.regen
            if heal_amount >= p1.inflicted_poison:
                heal_amount -= p1.inflicted_poison
                # print(f'P1 Regens {min(p1.max_hp, p1.health + heal_amount) - p1.health}')
                p1.health = min(p1.max_hp, p1.health + heal_amount)
            else:
                p1.inflicted_poison -= heal_amount
                # print(f'P1 takes {p1.inflicted_poison} Poison')
                p1.health -= p1.inflicted_poison

            heal_amount = p2.regen
            if heal_amount >= p2.inflicted_poison:
                heal_amount -= p2.inflicted_poison
                # print(f'P2 Regens {min(p2.max_hp, p2.health + heal_amount) - p2.health}')
                p2.health = min(p2.max_hp, p2.health + heal_amount)
            else:
                p2.inflicted_poison -= heal_amount
                # print(f'P2 takes {p2.inflicted_poison} Poison')
                p2.health -= p2.inflicted_poison
    if p1.health > p2.health:
        if finals:
            print(f'One Win')
        return 1
    if finals:
        print(f'Two Win')
    return 2


def create_player() -> Player:
    values = [random() for _ in range(9)]
    the_sum = sum(values)
    a = Player()
    a.defense = floor(values[0] / the_sum * (99 + 99))
    a.shield = floor(values[1] / the_sum * (99 + 99))
    a.armor = floor(values[2] / the_sum * (99 + 99))
    a.max_hp = 100 + floor(values[3] / the_sum * (99 + 99))
    a.regen = floor(values[4] / the_sum * (99 + 99))
    a.leach = floor(values[5] / the_sum * (99 + 99))
    a.attack = 1 + floor(values[6] / the_sum * (99 + 99))
    a.speed = floor(values[7] / the_sum * (99 + 99))
    a.poison = floor(values[8] / the_sum * (99 + 99))
    return a


def tournament():
    one = create_player()
    two = create_player()
    thr = create_player()
    fou = create_player()

    for i in range(100):
        result = fight(one, two)
        result2 = fight(thr, fou)
        if result == 1:
            two = create_player()
        else:
            one = create_player()
        if result2 == 1:
            fou = create_player()
        else:
            thr = create_player()

    print(f'Final 4')
    print(f'One vs Four')
    result = fight(one, fou, True)
    print(f'Two vs Three')
    result2 = fight(two, thr, True)
    print(f'Finals')
    if result == 1 and result2 == 1:
        fight(one, two, True)
    elif result == 1 and result2 == 2:
        fight(one, thr, True)
    elif result == 2 and result2 == 1:
        fight(fou, two, True)
    else:
        fight(fou, thr, True)


def main() -> None:
    B = Backpack()
    while True:
        action = input('Actions')
        if action == 'm':
            print('Worth:', B.get_loot_worth())
            hold = dc(B.items)
            B.merge()
            B.report_items(hold)
            print('Worth:', B.get_loot_worth())
            pass
        elif action == 'e':
            break
        elif int(action) > 0:
            B.loot(int(action))
