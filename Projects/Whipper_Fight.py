from itertools import product

monsters = [
    [15, 5, 5, 1],
    [20, 8, 7, 1],
    [25, 14, 10, 1],
    [30, 20, 15, 2],
    [35, 18, 16, 5],
    [40, 30, 20, 8],
    [30, 20, 25, 2],
    [40, 25, 25, 3],
    [40, 40, 28, 7],
    [50, 35, 28, 6],
    [60, 70, 60, 10],
    [40, 40, 25, 4],
    [60, 60, 40, 10],
    [60, 70, 35, 15],
    [80, 80, 65, 15],
    [100, 100, 70, 17],
    [5, 10, 10, 50],
    [55, 40, 40, 3],
    [80, 67, 50, 10],
    [80, 80, 60, 10],
    [90, 95, 68, 10],
    [110, 110, 90, 20],
    [130, 110, 90, 10],
    [160, 150, 95, 20],
    [200, 180, 100, 30],
    [100, 80, 50, 1],
    [110, 85, 60, 1],
    [120, 100, 65, 2],
    [110, 90, 50, 1],
    [150, 130, 70, 3],
    [100, 110, 67, 2],
    [120, 80, 115, 2],
    [150, 110, 110, 5],
    [210, 140, 113, 10],
    [250, 150, 115, 10],
    [240, 140, 110, 5],
    [280, 230, 144, 20],
    [260, 240, 180, 35],
    [340, 540, 360, 43],
    [270, 250, 200, 42],
    [280, 220, 210, 35],
    [300, 450, 200, 35],
    [370, 530, 340, 35],
    [300, 550, 350, 50],
    [400, 560, 400, 24],
    [420, 600, 450, 50],
    [500, 580, 420, 35],
    [400, 600, 390, 45],
    [390, 450, 450, 60],
    [420, 640, 520, 60],
    [500, 650, 470, 30],
    [2000, 700, 0, 40],
    [1000, 750, 100, 50],
    [240, 680, 450, 40],
    [300, 400, 350, 70],
    [300, 500, 450, 70],
    [200, 700, 350, 80],
    [100, 900, 250, 90],
    [1, 900, 1, 256],
    [240, 450, 440, 45],
    [650, 700, 560, 60],
    [3000, 850, 0, 1],
    [680, 750, 590, 62],
    [2900, 900, 10, 77],
    [4000, 1000, 150, 40],
    [10, 700, 2000, 1],
    [1000, 900, 500, 67],
    [650, 850, 550, 55],
    [300, 1200, 400, 100],
    [600, 780, 600, 65],
    [600, 1300, 400, 75],
    [2000, 1000, 600, 70],
    [780, 900, 700, 68],
    [1800, 1000, 560, 50],
    [1800, 1200, 650, 55],
    [500, 2000, 500, 120],
    [2000, 1300, 850, 70],
    [3000, 1500, 720, 77],
    [1500, 1200, 850, 100],
    [6000, 1300, 44, 20],
    [1000, 100, 10, 600],
    [2000, 1700, 860, 140],
    [1790, 2500, 450, 1],
    [2800, 1550, 1000, 90],
    [5000, 1800, 100, 30],
    [10, 2000, 1300, 290],
    [4000, 2400, 500, 130],
    [4500, 2600, 400, 160],
    [2600, 2200, 950, 95],
    [1000, 2400, 1000, 150],
    [100, 5000, 1, 100],
    [6000, 1000, 100, 400],
    [5000, 3000, 1300, 140],
    [6000, 2770, 1600, 10],
    [2000, 3400, 1300, 150],
    [1000, 4800, 1300, 150],
    [1, 6000, 3000, 160],
    [4000, 4200, 1200, 140],
    [5000, 5000, 3000, 150],
    [444, 666, 555, 55],
    [500, 400, 250, 4],
    [620, 450, 210, 10],
    [430, 650, 260, 50],
    [1000, 610, 100, 15],
    [680, 675, 240, 15],
    [1200, 770, 380, 30],
    [700, 750, 430, 32],
    [500, 860, 400, 65],
    [1000, 1000, 800, 1000],
    [1800, 1100, 750, 45],
    [1200, 1200, 650, 55],
    [1400, 1450, 680, 600],
    [1200, 800, 700, 600],
    [1500, 1100, 650, 50],
    [1400, 950, 650, 41],
    [1000, 800, 400, 40],
    [1, 400, 1, 200],
    [1, 600, 1, 200],
    [2500, 2500, 600, 100],
    [700, 450, 350, 20],
    [650, 520, 400, 10],
    [800, 550, 100, 600],
    [1500, 620, 400, 41],
    [2000, 650, 10, 54],
    [1000, 1000, 1, 600],
    [1800, 900, 700, 60],
    [2400, 900, 750, 42],
    [2600, 1300, 790, 600],
    [2000, 2100, 900, 1],
]

HP = 0
ATK = 1
DEF = 2
SPD = 3
FirstStrike = 4
DoubleStrike = 5
OneStrike = 6

WIN = 0
LOSE = 1
TIE = 2
STALE = 3


def create_lineup(lineup: list) -> list:
    if len(lineup) == 0:

        LEVEL = 50
        STARGAZER = [[300,20],[1600,24],[120,24], 'Stargazer']
        ZODIAC = [[100,0],[1460,30],[0,10], 'Zodiac']
        SHIELD_OF_THOUSAND = [[0,0],[0,0],[1560,50], 'Shield of Thousand']
        BLACK_SWORD_BREATH = [[0,0],[200,35],[350,0], 'Black Sword Breath']
        for A in [STARGAZER, ZODIAC]:
            for D in [SHIELD_OF_THOUSAND, BLACK_SWORD_BREATH]:
                temp = []
                for i in [HP, ATK, DEF]:
                    temp += [A[i][0] + D[i][0] + (A[i][1] + D[i][1]) * LEVEL]
                for s in product(range(2), repeat=3):
                    s = list(map(int, s))
                    given = 1
                    for k in range(6 - max(0, sum(s)-given) + 1):
                        lineup.append(
                            [temp[HP], temp[ATK] + 25 * LEVEL * (6 - max(0, sum(s)-given) - k), temp[DEF] + 25 * LEVEL * k, 1] + s + [A[3], D[3], 6 - max(0, sum(s)-given) - k, k]
                        )
    elif len(lineup[0]) < 7:
        for i in range(len(lineup)):
            lineup[i] += [0, 0, 0]
    return lineup


def main() -> None:
    lineup = create_lineup([])
    record = []
    for i in range(len(lineup)):
        # Win, Lose, Tie, Stale, ID, Rank
        record.append([[], [], [], [], i, 0])

    for id_a, mon_a in enumerate(lineup):
        for id_b, mon_b in enumerate(lineup[id_a + 1::]):
            id_b += id_a + 1
            if id_b == 32 or id_a == 32 or id_b == 37 or id_a == 37:
                pass
            if get_attack(mon_a) <= mon_b[DEF] and mon_a[DEF] >= get_attack(mon_b):
                record[id_a][STALE].append(id_b)
                record[id_b][STALE].append(id_a)
                continue
            elif mon_a[SPD] > mon_b[SPD] or mon_a[FirstStrike] > mon_b[FirstStrike]:
                results = fight(mon_a, mon_b)
            elif mon_a[SPD] < mon_b[SPD] or mon_a[FirstStrike] < mon_b[FirstStrike]:
                results = fight(mon_b, mon_a)[::-1]
            else:
                results = [a + b for a, b in zip(fight(mon_a, mon_b), fight(mon_b, mon_a)[::-1])]

            if results[0] > 0 and results[1] == 0:
                record[id_a][WIN].append(id_b)
                record[id_b][LOSE].append(id_a)
            elif results[0] == 0 and results[1] > 0:
                record[id_a][LOSE].append(id_b)
                record[id_b][WIN].append(id_a)
            else:
                record[id_a][TIE].append(id_b)
                record[id_b][TIE].append(id_a)
        # print("Monster ", id_a, " Complete")
        record[id_a][5] = len(record[id_a][WIN]) * 3 + len(record[id_a][TIE]) + len(record[id_a][STALE])
    record.sort(key=rank_sort)
    s_print(record, lineup)


def fight(attacker: list[int], defender: list[int]) -> list[int]:
    a_HP = attacker[HP]
    a_D = max(0, ((attacker[ATK] * (2**attacker[OneStrike])) - defender[DEF]) * (2**attacker[DoubleStrike]))
    d_HP = defender[HP]
    d_D = max(0, ((defender[ATK] * (2**defender[OneStrike])) - attacker[DEF]) * (2**defender[DoubleStrike]))
    if a_D == 0 and d_D == 0: return [0, 0]
    while True:
        d_HP -= a_D
        if d_HP < 1:
            return [1, 0]
        a_HP -= d_D
        if a_HP < 1:
            return [0, 1]


def get_attack(attacker: list[int]) -> int:
    return attacker[ATK] * (2**attacker[OneStrike])


def rank_sort(e: list[int]) -> int:
    return e[5]


def s_print(records: list, lineup: list) -> None:
    print("Rank #: Player # - [Win, Tie, Lose, Stale] - [FS, DS, OS, Weapon, Shield, STR ^, DEF ^")
    for i in range(len(records)):
        print(f"Rank {records[i][5]}: {records[i][4]} - [{len(records[i][WIN])}, {len(records[i][TIE])}, {len(records[i][LOSE])}, {len(records[i][STALE])}] - {lineup[records[i][4]][4:]}")
