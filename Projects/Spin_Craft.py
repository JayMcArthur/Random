from enum import IntEnum

items = {

}


class SymbolStuff(IntEnum):
    rarity = 0,
    give = 1,
    onDestroy = 2,
    onDestroy_chance = 3,
    spawns = 4,
    spawn_chance = 5,
    consumes = 6,
    consume_give = 7


class Symbol():
    def __init__(self, give, rarity=0, when_destroyed=[], when_destroyed_chance=[], spawns=[], spawn_chance=[], consumes=[], consume_give=[]):
        self.give = give
        self.rarity = rarity
        self.when_destroyed = when_destroyed
        self.when_destroyed_chance = when_destroyed_chance
        self.spawns = spawns
        self.spawn_chance = spawn_chance
        self.consumes = consumes
        self.consume_give = consume_give


symbols = {
    "Banana": Symbol(give=1, when_destroyed=["Peel"], when_destroyed_chance=[1]),
    "Peel": Symbol(give=1),
    "Bear": Symbol(give=1, consumes=["Honey"], consume_give=[50]),

}


# M = 10x Master Scroll, L = 5x Legend Scroll,
# \/v> = 5x Arrow, < = 10x Arrow,
# R = 10x Rouette Wheel, W = 10x Wizard[36],
# Z = Zig or Zag, p = 2x Panda, K = 30x Krull


# 15 * 2^13 = L5.0
# \ ? v ? /
# ? \ v / ?
# > > U < <
# ? / ^ \ ?

# 15 * 10^2 * 5^11 = L10.8
# \ ? v ? /
# ? L L M ?
# > L U L <
# ? L L L ?

# (15 * (10^3)^2 * 5^9 * (2^2)^2) * 5^8 = L20.2
# \ \ v v /
# P L L M L
# > > U J <
# P L L R \

# (15 * (10^4)^2 * 5^8 * (2^2)^2)  * 5^7 = L20.8
# \ \ v v /
# L L L M L
# > > U J <
# P L W R \

# (10 * 100 * (10^4)^2 * 5^7 * (2^2)^2)  * 5^6 = L21.29
# \ \ v v /
# P L L M L
# > Z Z J <
# P L W R \

# (T * 6 * (10^4)^2 * 5^8 * (2^2)^2)  * 5^7 = L22.4
# \ \ v v /
# P L L M L
# > > T J <
# P L W R \

# (10 * 100^2 * (10^4)^2 * 5^6 * (2^2)^2)  * 5^7 = L23.29
# \ \ v v /
# P Z L M L
# > > Z J <
# P Z W R L

# (10 * 100^2 * (10^4)^2 * 5^5 * (2^2)^2 * 30^2)  * 5^6 = L24.8
# \ \ v v /
# P Z K M L
# > > Z J <
# P Z W R L

# Scrolls +1.5
# Everything * 1.15
# Panda *1.2
# Arrows +1.75

# (10 * 1.15^2 * 100^2 * (10^2)^2 * 15^2 * 17.5^2 * (5*1.75)^5 * (2.4^2)^2 * 30^2)  * (5*1.75)^4 * (5*1.5)^2 = L28.6
# \ \ v v /
# P Z K M L
# > > Z J <
# P Z W R L


def main():
    pass