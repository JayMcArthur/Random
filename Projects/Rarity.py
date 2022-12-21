from enum import Enum
from random import randint


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    # EXOTIC = 3
    EPIC = 3
    LEGENDARY = 4
    MYTHIC = 5
    # UNIQUE
    # ULTIMATE = 6
    # Otherworldly
    # Ethereal
    DIVINE = 6


MAX_ROLL = 310303280952
RARITY_DROP = [
    [0, [Rarity.COMMON, 0]],
    [100000000000, [Rarity.COMMON, 1]],
    [150000000000, [Rarity.COMMON, 2]],
    [183333333333, [Rarity.COMMON, 3]],
    [208333333333, [Rarity.COMMON, 4]],
    [228333333333, [Rarity.COMMON, 5]],
    [245000000000, [Rarity.COMMON, 6]],
    [259285714286, [Rarity.COMMON, 7]],
    [271785714286, [Rarity.COMMON, 8]],
    [282896825397, [Rarity.COMMON, 9]],
    [292896825397, [Rarity.COMMON, 10]],
    [299563492063, [Rarity.UNCOMMON, 1]],
    [303562492063, [Rarity.UNCOMMON, 2]],
    [305563492063, [Rarity.UNCOMMON, 3]],
    [306896825397, [Rarity.UNCOMMON, 4]],
    [307896825397, [Rarity.UNCOMMON, 5]],
    [308563492063, [Rarity.UNCOMMON, 6]],
    [309063492063, [Rarity.UNCOMMON, 7]],
    [309463492063, [Rarity.UNCOMMON, 8]],
    [309796825397, [Rarity.RARE, 1]],
    [309996825397, [Rarity.RARE, 2]],
    [310096825397, [Rarity.RARE, 3]],
    [310163492063, [Rarity.RARE, 4]],
    [310213492063, [Rarity.RARE, 5]],
    [310253492063, [Rarity.RARE, 6]],
    [310273492063, [Rarity.EPIC, 1]],
    [310286825397, [Rarity.EPIC, 2]],
    [310293492063, [Rarity.EPIC, 3]],
    [310296825397, [Rarity.EPIC, 4]],
    [310299047619, [Rarity.EPIC, 5]],
    [310300714286, [Rarity.LEGENDARY, 1]],
    [310302047619, [Rarity.LEGENDARY, 2]],
    [310302714286, [Rarity.LEGENDARY, 3]],
    [310303047619, [Rarity.MYTHIC, 1]],
    [310303214286, [Rarity.MYTHIC, 2]],
    [310303269841, [Rarity.DIVINE, 0]]
]
MERGE_COST = {
    Rarity.COMMON: {
        0: None,
        1: [[Rarity.COMMON, 0, 2]],
        2: [[Rarity.COMMON, 1, 1], [Rarity.COMMON, 0, 1]],
        3: [[Rarity.COMMON, 2, 1], [Rarity.COMMON, 0, 1]],
        4: [[Rarity.COMMON, 3, 1], [Rarity.COMMON, 0, 1]],
        5: [[Rarity.COMMON, 4, 1], [Rarity.COMMON, 0, 1]],
        6: [[Rarity.COMMON, 5, 1], [Rarity.COMMON, 0, 1]],
        7: [[Rarity.COMMON, 6, 1], [Rarity.COMMON, 0, 1]],
        8: [[Rarity.COMMON, 7, 1], [Rarity.COMMON, 0, 1]],
        9: [[Rarity.COMMON, 8, 1], [Rarity.COMMON, 0, 1]],
        10: [[Rarity.COMMON, 9, 1], [Rarity.COMMON, 4, 1]]
    },
    Rarity.UNCOMMON: {
        1: [[Rarity.COMMON, 10, 1], [Rarity.COMMON, 9, 1]],
        2: [[Rarity.UNCOMMON, 1, 2]],
        3: [[Rarity.UNCOMMON, 2, 1], [Rarity.UNCOMMON, 1, 1]],
        4: [[Rarity.UNCOMMON, 3, 1], [Rarity.UNCOMMON, 1, 1]],
        5: [[Rarity.UNCOMMON, 4, 1], [Rarity.UNCOMMON, 2, 1]],
        6: [[Rarity.UNCOMMON, 5, 1], [Rarity.UNCOMMON, 2, 1]],
        7: [[Rarity.UNCOMMON, 6, 1], [Rarity.UNCOMMON, 2, 1]],
        8: [[Rarity.UNCOMMON, 7, 1], [Rarity.UNCOMMON, 2, 1]]
    },
    Rarity.RARE: {
        1: [[Rarity.UNCOMMON, 8, 1], [Rarity.UNCOMMON, 6, 1]],
        2: [[Rarity.RARE, 1, 2]],
        3: [[Rarity.RARE, 2, 1], [Rarity.RARE, 1, 1]],
        4: [[Rarity.RARE, 3, 1], [Rarity.RARE, 1, 1]],
        5: [[Rarity.RARE, 4, 1], [Rarity.RARE, 1, 1]],
        6: [[Rarity.RARE, 5, 2]]
    },
    Rarity.EPIC: {
        1: [[Rarity.RARE, 6, 1], [Rarity.RARE, 5, 1]],
        2: [[Rarity.EPIC, 1, 2]],
        3: [[Rarity.EPIC, 2, 1], [Rarity.EPIC, 1, 1]],
        4: [[Rarity.EPIC, 3, 1], [Rarity.EPIC, 1, 1]],
        5: [[Rarity.EPIC, 4, 1], [Rarity.EPIC, 1, 1]]
    },
    Rarity.LEGENDARY: {
        1: [[Rarity.EPIC, 5, 1], [Rarity.EPIC, 1, 1]],
        2: [[Rarity.LEGENDARY, 1, 2]],
        3: [[Rarity.LEGENDARY, 2, 2]]
    },
    Rarity.MYTHIC: {
        1: [[Rarity.LEGENDARY, 3, 2]],
        2: [[Rarity.MYTHIC, 1, 3]]
    },
    Rarity.DIVINE: {
        0: [[Rarity.MYTHIC, 2, 5]]
    }
}

# RARITY # ---- DEFAULT P - SCALED - ABILITIES
# COMMON 1 ---- 00 000 001 - 01 - 0
# COMMON 2 ---- 00 000 002 - 02 - 0
# COMMON 3 ---- 00 000 003 - 03 - 0
# COMMON 4 ---- 00 000 004 - 04 - 0
# COMMON 5 ---- 00 000 005 - 05 - 0
# COMMON 6 ---- 00 000 006 - 06 - 0
# COMMON 7 ---- 00 000 007 - 07 - 0
# COMMON 8 ---- 00 000 008 - 08 - 0
# COMMON 9 ---- 00 000 009 - 09 - 0
# COMMON 10 --- 00 000 010 - 10 - 0
# UNCOMMON 1 -- 00 000 110 - 11 - 1
# UNCOMMON 2 -- 00 000 220 - 22 - 1
# UNCOMMON 3 -- 00 000 330 - 33 - 1
# UNCOMMON 4 -- 00 000 440 - 44 - 1
# UNCOMMON 5 -- 00 000 550 - 55 - 1
# UNCOMMON 6 -- 00 000 660 - 66 - 1
# UNCOMMON 7 -- 00 000 770 - 77 - 1
# UNCOMMON 8 -- 00 000 880 - 88 - 1
# RARE 1 ------ 00 001 400 - 14 - 2
# RARE 2 ------ 00 002 800 - 28 - 2
# RARE 3 ------ 00 004 200 - 42 - 2
# RARE 4 ------ 00 005 700 - 57 - 2
# RARE 5 ------ 00 007 100 - 71 - 2
# RARE 6 ------ 00 008 500 - 85 - 2
# EPIC 1 ------ 00 016 000 - 16 - 3
# EPIC 2 ------ 00 033 000 - 33 - 3
# EPIC 3 ------ 00 050 000 - 50 - 3
# EPIC 4 ------ 00 066 000 - 66 - 3
# EPIC 5 ------ 00 083 000 - 83 - 3
# LEGENDARY 1 - 00 250 000 - 25 - 4
# LEGENDARY 2 - 00 500 000 - 50 - 4
# LEGENDARY 3 - 00 750 000 - 75 - 4
# MYTHIC 1 ---- 03 300 000 - 33 - 5
# MYTHIC 2 ---- 06 600 000 - 66 - 5
# DIVINE 0 ---- 99 000 000 - 99 - 6

# ITEM TYPES
# WEAPON
# ARMOR

# STAT TYPES
# Health Points
# Magic Points?
# Damage
# Crit Chance
# Defense
# Speed
# # Attack Speed
# # Dodge Change
#
# Intelligence
# # Spell Damage
# # Spell Resist

# Enchantments ?
# HEALTH POINTS
# ATTACK
# DEFENSE
# MAGIC ATTACK (Specialized attack)
# # Vampire
# MAGIC DEFENSE (Specialized Defense)
# # Thorns
# Speed - 1/Speed time
# Evasion -
# Accuracy
# Critical
# Luck


class Backpack:
    def __init__(self):
        self.items = {
            Rarity.COMMON: {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0},
            Rarity.UNCOMMON: {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0},
            Rarity.RARE: {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
            Rarity.EPIC: {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0},
            Rarity.LEGENDARY: {'1': 0, '2': 0, '3': 0},
            Rarity.MYTHIC: {'1': 0, '2': 0},
            Rarity.DIVINE: {'0': 0}
        }
        self.loot_level = 0

    def merge(self):
        while self.merge_pass([Rarity.DIVINE, 0, 0]):
            pass

    def merge_pass(self, want) -> bool:
        for [part, level, amount] in MERGE_COST[want[0]][want[1]]:
            while self.items[part][str(level)] < amount:
                if part == Rarity.COMMON and level == 0:
                    return False
                # print(f'{"-"*want[2]}Request {part} {level}')
                success = self.merge_pass([part, level, want[2] + 1])
                if not success:
                    return False

        for [part, level, amount] in MERGE_COST[want[0]][want[1]]:
            self.items[part][str(level)] -= amount
        self.items[want[0]][str(want[1])] += 1
        # print(f'{"-"*want[2]}Made {want[0]} {want[1]}')
        return True

    def loot(self, n):
        current_max_roll = MAX_ROLL - RARITY_DROP[min(self.loot_level, 11)][0] - 11111 * max(0, self.loot_level - 11)
        for i in range(n):
            ROLL = randint(1, current_max_roll)
            for [value, item] in RARITY_DROP[::-1]:
                if ROLL <= value - RARITY_DROP[min(self.loot_level, 11)][0] - 11111 * max(0, self.loot_level - 11):
                    continue
                self.items[item[0]][str(item[1])] += 1
                break


def main() -> None:
    B = Backpack()
    while True:
        action = input()
        if action == 'm':
            B.merge()
            pass
        elif action == 'e':
            break
        elif int(action) > 0:
            B.loot(int(action))
