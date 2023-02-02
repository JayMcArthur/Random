from enum import Enum
from math import ceil, floor, log2
from random import randrange, random



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


def fight(p1, p2) -> int:
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
        p1.timer += (100 + p1.speed)/100
        p2.timer += (100 + p2.speed)/100
        world_timer += 1
        if p1.timer >= 100:
            # print(f'Player 1 Attacks')
            p1.timer = p1.timer % 100
            if p2.shield > p2.used_shield:
                p2.used_shield += ceil(2*log2(p1.attack))
                # p2.inflicted_poison += p1.poison
                # print(f'- Hit Shield')
            else:
                attack = p1.attack
                attack = max(0, attack - p2.defense)
                # print(f'- Leaches {min(p1.max_hp, p1.health + min(p1.leach, attack)) - p1.health}')
                p1.health = min(p1.max_hp, p1.health + min(p1.leach, attack))
                attack = ceil(attack * (100 - p2.armor)/100)
                p2.health -= attack
                # print(f'- Did {attack} damage')
                p2.inflicted_poison += p1.poison

        if p2.timer >= 100:
            p2.timer = p2.timer % 100
            # print(f'Player 2 Attacks')
            if p1.shield > p1.used_shield:
                p1.used_shield += ceil(2*log2(p2.attack))
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
        print(f'One Win')
        return 1
    print(f'Two Win')
    return 2


def create_player() -> object:
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


def main() -> None:
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
    result = fight(one, fou)
    print(f'Two vs Three')
    result2 = fight(two, thr)
    print(f'Finals')
    if result == 1 and result2 == 1:
        fight(one, two)
    elif result == 1 and result2 == 2:
        fight(one, thr)
    elif result == 2 and result2 == 1:
        fight(fou, two)
    else:
        fight(fou, thr)

    input("Done")

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
